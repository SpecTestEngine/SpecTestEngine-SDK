#!/usr/bin/env python3
"""Validate immutable contract entries and the canonical/latest relationship."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    manifest = json.loads((ROOT / "openapi" / "versions.json").read_text(encoding="utf-8"))
    versions = manifest.get("versions", {})
    latest = manifest.get("latest")
    if latest not in versions:
        raise SystemExit("versions.json latest entry is missing")
    for version, entry in versions.items():
        path = (ROOT / entry["contract"]).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            raise SystemExit(f"contract path for {version} is invalid")
        actual = digest(path)
        if actual != entry["sha256"]:
            raise SystemExit(f"contract checksum mismatch for {version}: {actual}")
    canonical = ROOT / "openapi" / "spectestengine-public-v1.yaml"
    latest_contract = ROOT / versions[latest]["contract"]
    if canonical.read_bytes() != latest_contract.read_bytes():
        raise SystemExit("canonical contract must match the latest immutable contract version")
    print(f"contract versions passed: {len(versions)} version(s), latest {latest}")


if __name__ == "__main__":
    main()
