#!/usr/bin/env python3
"""Apply small, reviewed packaging fixes not exposed by OpenAPI Generator options."""

import os
from pathlib import Path
import re
import sys


def replace(path: Path, old: str, new: str) -> None:
    content = path.read_text(encoding="utf-8")
    if old not in content:
        raise RuntimeError(f"Expected generated marker was not found in {path}: {old!r}")
    path.write_text(content.replace(old, new), encoding="utf-8")


def postprocess_java(output: Path) -> None:
    replace(
        output / "build.gradle",
        "sourceCompatibility = JavaVersion.VERSION_11\ntargetCompatibility = JavaVersion.VERSION_11",
        "java {\n    sourceCompatibility = JavaVersion.VERSION_17\n    targetCompatibility = JavaVersion.VERSION_17\n    withJavadocJar()\n    withSourcesJar()\n}",
    )
    replace(output / "pom.xml", "<version>11</version>", "<version>17</version>")
    replace(
        output / "pom.xml",
        "<maven.compiler.source>11</maven.compiler.source>",
        "<maven.compiler.source>17</maven.compiler.source>",
    )
    replace(
        output / "pom.xml",
        "<maven.compiler.target>11</maven.compiler.target>",
        "<maven.compiler.target>17</maven.compiler.target>",
    )
    replace(output / "README.md", "1. Java 11+", "1. Java 17+")
    replace(
        output / "gradle/wrapper/gradle-wrapper.properties",
        "gradle-8.7-bin.zip",
        "gradle-9.6.0-bin.zip",
    )
    replace(
        output / "build.gradle",
        "   main = System.getProperty('mainClass')",
        "   mainClass = System.getProperty('mainClass')",
    )
    replace(
        output / "build.gradle",
        """task sourcesJar(type: Jar, dependsOn: classes) {
    archiveClassifier = 'sources'
    from sourceSets.main.allSource
}

task javadocJar(type: Jar, dependsOn: javadoc) {
    archiveClassifier = 'javadoc'
    from javadoc.destinationDir
}

artifacts {
    archives sourcesJar
    archives javadocJar
}


""",
        "",
    )
    replace(output / "build.gradle", "    enforceCheck false", "    enforceCheck = false")
    gradlew = output / "gradlew"
    os.chmod(gradlew, gradlew.stat().st_mode | 0o111)


def postprocess_python(output: Path) -> None:
    replace(output / "README.md", "Python 3.10+", "Python 3.11+")
    replace(output / "pyproject.toml", 'requires-python = ">=3.9"', 'requires-python = ">=3.11"')
    replace(output / "setup.py", 'PYTHON_REQUIRES = ">= 3.10"', 'PYTHON_REQUIRES = ">= 3.11"')
    replace(output / "setup.py", '    url="",', '    url="https://github.com/SpecTestEngine/SpecTestEngine-SDK",')


def postprocess_typescript(output: Path) -> None:
    replace(output / "package.json", '"author": "OpenAPI-Generator"', '"author": "SpecTestEngine"')
    replace(output / ".gitignore", "dist\n", "dist\npackage-lock.json\n")


def postprocess_csharp(output: Path) -> None:
    replace(
        output / "README.md",
        "See the project's [REAMDE](src/SpecTestEngine.Sdk/README.md)",
        "See the project's [README](src/SpecTestEngine.Sdk/README.md)",
    )
    # OpenAPI Generator emits one trailing space when an optional response type
    # is absent from this XML documentation line. Keep this reviewed cleanup
    # deliberately narrow so unrelated generated formatting remains untouched.
    for path in output.rglob("*.cs"):
        content = path.read_text(encoding="utf-8")
        updated = content.replace(
            "    /// An interface for responses of type \n",
            "    /// An interface for responses of type\n",
        )
        if updated != content:
            path.write_text(updated, encoding="utf-8")


def postprocess_go(output: Path) -> None:
    old_modules = (
        "github.com/GIT_USER_ID/GIT_REPO_ID/spectestengine",
        "github.com/SpecTestEngine/SpecTestEngine-SDK/spectestengine",
    )
    new_module = "github.com/SpecTestEngine/SpecTestEngine-SDK/clients/go"
    for path in output.rglob("*"):
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = content
        for old_module in old_modules:
            updated = updated.replace(old_module, new_module)
        if updated != content:
            path.write_text(updated, encoding="utf-8")


def replace_repository_placeholders(output: Path) -> None:
    for path in output.rglob("*"):
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = content.replace("GIT_USER_ID", "SpecTestEngine").replace(
            "GIT_REPO_ID", "SpecTestEngine-SDK"
        )
        if updated != content:
            path.write_text(updated, encoding="utf-8")


def clean_document_visual_generation_docs(output: Path) -> None:
    """Keep the newly generated table row free of target-specific trailing whitespace."""
    marker = (
        "Indexes into excludedRegions whose masked area contained a real change "
        "in this immutable generation. | \n"
    )
    replacement = marker[:-2] + "\n"
    for path in output.rglob("DocumentVisualDiffGeneration.md"):
        content = path.read_text(encoding="utf-8")
        updated = content.replace(marker, replacement)
        if updated != content:
            path.write_text(updated, encoding="utf-8")


def normalize_generated_whitespace(content: str) -> str:
    updated = re.sub(r"[ \t]+(?=\r?$)", "", content, flags=re.MULTILINE)
    return re.sub(r"(?:\r?\n){2,}\Z", "\n", updated)


def strip_trailing_whitespace(output: Path) -> None:
    """Normalize generator whitespace so output is identical across local and CI runs."""
    for path in output.rglob("*"):
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = normalize_generated_whitespace(content)
        if updated != content:
            path.write_text(updated, encoding="utf-8")


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: postprocess-generated.py <target> <output-directory>")

    target = sys.argv[1]
    output = Path(sys.argv[2]).resolve()
    if target == "java":
        postprocess_java(output)
    elif target == "python":
        postprocess_python(output)
    elif target == "typescript":
        postprocess_typescript(output)
    elif target == "csharp":
        postprocess_csharp(output)
    elif target == "go":
        postprocess_go(output)
    replace_repository_placeholders(output)
    clean_document_visual_generation_docs(output)
    strip_trailing_whitespace(output)


if __name__ == "__main__":
    main()
