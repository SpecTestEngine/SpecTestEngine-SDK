#!/usr/bin/env python3
"""Build deterministic, self-contained SDK archives from an allowlisted contract version."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import stat
import subprocess
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "openapi" / "versions.json"
LANGUAGES = ("java", "typescript", "python", "csharp", "go")
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)
EXCLUDED_PARTS = {
    ".gradle",
    ".openapi-generator",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", choices=("all", *LANGUAGES), default="all")
    parser.add_argument("--contract-version", help="Version from openapi/versions.json; defaults to latest")
    parser.add_argument("--output", type=Path, help="Archive directory; defaults to artifacts/<version>")
    return parser.parse_args()


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_contract(version: str, entry: dict) -> Path:
    contract = (ROOT / entry["contract"]).resolve()
    if not contract.is_relative_to(ROOT) or not contract.is_file():
        raise SystemExit(f"Contract for {version!r} is missing or outside the repository")
    actual = sha256(contract)
    if actual != entry["sha256"]:
        raise SystemExit(
            f"Contract checksum mismatch for {version}: expected {entry['sha256']}, found {actual}"
        )
    return contract


def relative_workspace_path(path: Path) -> str:
    return "/workspace/" + path.resolve().relative_to(ROOT).as_posix()


def generate_client(language: str, contract: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    generated = subprocess.run(
        [
            str(ROOT / "scripts" / "openapi-generator.sh"),
            "generate",
            "-c",
            f"/workspace/generator/config/{language}.yaml",
            "-i",
            relative_workspace_path(contract),
            "-o",
            relative_workspace_path(destination),
            "--skip-validate-spec",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if generated.returncode != 0:
        raise SystemExit(generated.stdout + generated.stderr)
    subprocess.run(
        [
            "python3",
            str(ROOT / "scripts" / "postprocess-generated.py"),
            language,
            str(destination),
        ],
        cwd=ROOT,
        check=True,
    )


def should_include(path: Path) -> bool:
    return not any(part in EXCLUDED_PARTS or part.endswith(".egg-info") for part in path.parts)


def copy_tree(source: Path, destination: Path) -> None:
    for path in sorted(source.rglob("*")):
        relative = path.relative_to(source)
        if not should_include(relative):
            continue
        target = destination / relative
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif path.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
            target.chmod(path.stat().st_mode & 0o777)


def archive_readme(language: str, version: str) -> str:
    commands = {
        "java": "cd client && ./gradlew build",
        "typescript": "cd client && npm install && npm run build",
        "python": "python3 -m venv .venv && . .venv/bin/activate && python -m pip install -e client",
        "csharp": "dotnet build client/SpecTestEngine.Sdk.sln",
        "go": "cd client && go test ./...",
    }
    return f"""# SpecTestEngine SDK for {language}

Contract version: `{version}`

This archive contains a generated typed client, the exact OpenAPI contract used to generate it,
and maintained workflow helpers. It does not require Maven Central, npm, PyPI, NuGet, or another
public package registry.

## Build locally

```bash
{commands[language]}
```

Use the generated client directly as a source/module dependency, build a local package, or publish
it to your organization's private registry. The `workflows/` directory contains polling, SSE,
cancellation, and bounded streaming helpers that complement the generated HTTP operations.

Authenticate with a short-lived OAuth2/OIDC bearer token. Never place live tokens in source code,
logs, archive metadata, or generated configuration files.
"""


def write_deterministic_zip(source: Path, archive: Path) -> None:
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as target:
        for path in sorted(item for item in source.rglob("*") if item.is_file()):
            relative = path.relative_to(source.parent).as_posix()
            info = zipfile.ZipInfo(relative, FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            mode = 0o755 if path.stat().st_mode & stat.S_IXUSR else 0o644
            info.external_attr = (stat.S_IFREG | mode) << 16
            target.writestr(info, path.read_bytes())


def package_language(language: str, version: str, entry: dict, contract: Path, output: Path) -> Path:
    with tempfile.TemporaryDirectory(prefix="sdk-package-", dir=ROOT / ".sdk-build") as temporary:
        working = Path(temporary)
        package_root = working / f"spectestengine-sdk-{language}-{version}"
        client = package_root / "client"
        generate_client(language, contract, client)
        copy_tree(ROOT / "facades" / language, package_root / "workflows")
        (package_root / "openapi").mkdir(parents=True, exist_ok=True)
        shutil.copyfile(contract, package_root / "openapi" / "spectestengine-public.yaml")
        (package_root / "README.md").write_text(archive_readme(language, version), encoding="utf-8")
        metadata = {
            "contractSha256": entry["sha256"],
            "contractStatus": entry["status"],
            "contractVersion": version,
            "generator": "openapi-generator",
            "generatorVersion": generator_version(),
            "language": language,
            "registryPublication": "TODO",
        }
        (package_root / "SDK-METADATA.json").write_text(
            json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        archive = output / f"spectestengine-sdk-{language}-{version}.zip"
        write_deterministic_zip(package_root, archive)
    checksum = sha256(archive)
    archive.with_suffix(archive.suffix + ".sha256").write_text(
        f"{checksum}  {archive.name}\n", encoding="utf-8"
    )
    return archive


def generator_version() -> str:
    for line in (ROOT / "generator" / "version.env").read_text(encoding="utf-8").splitlines():
        if line.startswith("OPENAPI_GENERATOR_VERSION="):
            return line.split("=", 1)[1]
    raise SystemExit("OPENAPI_GENERATOR_VERSION is missing")


def main() -> None:
    args = parse_args()
    manifest = load_manifest()
    version = args.contract_version or manifest["latest"]
    entry = manifest["versions"].get(version)
    if entry is None:
        available = ", ".join(sorted(manifest["versions"]))
        raise SystemExit(f"Unknown contract version {version!r}. Available versions: {available}")
    contract = verify_contract(version, entry)
    output = (args.output or ROOT / "artifacts" / version).resolve()
    output.mkdir(parents=True, exist_ok=True)
    (ROOT / ".sdk-build").mkdir(exist_ok=True)
    languages = LANGUAGES if args.language == "all" else (args.language,)
    for language in languages:
        archive = package_language(language, version, entry, contract, output)
        print(f"{language}: {archive} ({sha256(archive)})")


if __name__ == "__main__":
    main()
