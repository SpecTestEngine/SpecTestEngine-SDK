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
        "gradle-9.8.2-bin.zip\ndistributionSha256Sum=21bd5da2de49b642904077f38c0efdc7778e92b3ed0889392dca61b97e389607",
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
    # Gradle 9 no longer supplies the JUnit launcher implicitly. Align the test-only
    # launcher with the already pinned Jupiter 5.10.2 engine; no client runtime change.
    replace(output / "build.gradle",
            '    testRuntimeOnly "org.junit.jupiter:junit-jupiter-engine:$junit_version"',
            '    testRuntimeOnly "org.junit.jupiter:junit-jupiter-engine:$junit_version"\n    testRuntimeOnly "org.junit.platform:junit-platform-launcher:1.10.2"')
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


def restore_engine_status_literals(content: str) -> str:
    # C# generator escapes repeated hyphens for Markdown, including runtime enum
    # literals. Restore only the three exact native wire values, never payload text.
    statuses = {"----------------PASS-------------------", "----------------FAIL-------------------", "---------------ERROR-------------------"}
    return re.sub(r'"([- A-Z]+)"', lambda match: '"' + match[1].replace(" ", "") + '"'
                  if match[1].replace(" ", "") in statuses else match[0], content)


def preserve_optional_csharp_enums(content: str) -> str:
    """An absent optional enum must neither throw nor become a default criterion."""
    pattern = (r'(?m)^ {12}var (\w+) = ([\w.]+)\(([\w.]+Option)\.Value!\.Value\);\n'
               r' {12}writer.WriteString\("([^"]+)", \1\);')
    def guarded(match: re.Match) -> str:
        raw, converter, option, field = match.groups()
        return (f"            if ({option}.IsSet)\n            {{\n"
                f"                if ({option}.Value is {{ }} enumValue)\n                {{\n"
                f"                    var {raw} = {converter}(enumValue);\n"
                f'                    writer.WriteString("{field}", {raw});\n'
                f'                }} else writer.WriteNull("{field}");\n            }}')
    return re.sub(pattern, guarded, content)


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
        updated = preserve_optional_csharp_enums(restore_engine_status_literals(content)).replace(
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


def preserve_json_operand_presence(target: str, output: Path) -> None:
    """Absent body/value operands disable a criterion; explicit JSON null is a value."""
    models = {"BrowserPathExpectation": ("value",),
              "BrowserNetworkExpectation": ("body", "candidateBody", "expectedBody")}
    for model, operands in models.items():
        snake = re.sub(r"(?<!^)(?=[A-Z])", "_", model).lower()
        if target == "typescript":
            path = output / f"src/models/{model}.ts"
            if not path.exists():
                continue  # Explicit older contract versions may lack this schema.
            for field in operands:
                replace(path, f"'{field}': json['{field}'] == null ? undefined : json['{field}'],",
                        f"'{field}': json['{field}'],")
        elif target == "python":
            path = output / f"spectestengine_sdk/models/{snake}.py"
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8")
            updated, count = re.subn(r"        _obj = cls.model_validate\(\{.*?\}\)\n        return _obj",
                                    "        return cls.model_validate(obj)", text, flags=re.DOTALL)
            if count != 1:
                raise RuntimeError(f"Expected one generated from_dict projection in {path}")
            path.write_text(updated, encoding="utf-8")
        elif target == "go":
            path = output / f"model_{snake}.go"
            if not path.exists():
                continue
            presence = []
            for field in operands:
                name = field[0].upper() + field[1:]
                flag = field + "Set"
                replace(path, f'{name} interface{{}} `json:"{field},omitempty"`',
                        f'{name} interface{{}} `json:"{field},omitempty"`\n\t{flag} bool')
                replace(path, f'o.{name} = v', f'o.{name} = v\n\to.{flag} = true')
                replace(path, f'if o.{name} != nil {{', f'if o.{flag} || o.{name} != nil {{')
                replace(path, f'o == nil || IsNil(o.{name})', f'o == nil || (!o.{flag} && IsNil(o.{name}))')
                replace(path, f'o != nil && !IsNil(o.{name})', f'o != nil && (o.{flag} || !IsNil(o.{name}))')
                presence.append(f'\t_, o.{flag} = operandPresence["{field}"]')
            track = '\n\tvar operandPresence map[string]json.RawMessage\n\tif err := json.Unmarshal(data, &operandPresence); err != nil { return err }\n' + '\n'.join(presence)
            marker = f'*o = {model}(var{model})'
            if marker in path.read_text():
                replace(path, marker, marker + track)
            else:
                with path.open("a", encoding="utf-8") as stream:
                    stream.write(f"\nfunc (o *{model}) UnmarshalJSON(data []byte) error {{\n"
                                 f"\ttype plain {model}\n\tvar decoded plain\n"
                                 "\tif err := json.Unmarshal(data, &decoded); err != nil { return err }\n"
                                 f"\t*o = {model}(decoded)" + track + "\n\treturn nil\n}\n")
        elif target == "java":
            path = output / f"src/main/java/software/ste/sdk/generated/model/{model}.java"
            if not path.exists():
                continue
            flags = "\n".join(f"  private boolean {field}Set;" for field in operands)
            replace(path, f'public class {model} {{',
                    f'@com.fasterxml.jackson.databind.annotation.JsonSerialize(using = {model}.OperandSerializer.class)\npublic class {model} {{\n{flags}')
            for field in operands:
                replace(path, f'this.{field} = {field};', f'this.{field} = {field};\n    this.{field}Set = true;')
            # Optional generated collections must stay absent: an injected empty
            # expectedHeaders object is itself an executable Browser criterion.
            text = path.read_text(encoding="utf-8")
            text = re.sub(r"(^  private (?:List<.*>|Map<.*>) \w+) = new (?:ArrayList|HashMap|LinkedHashMap)<>\(\);$",
                          r"\1 = null;", text, flags=re.MULTILINE)
            path.write_text(text, encoding="utf-8")
            properties = re.findall(r'public static final String JSON_PROPERTY_\w+ = "([^"]+)";', path.read_text())
            lines = []
            for field in properties:
                getter = f"rule.get{field[0].upper() + field[1:]}()"
                condition = f"rule.{field}Set || {getter} != null" if field in operands else f"{getter} != null"
                writer = f"writeOperand({getter}, json, provider)" if field in operands else f"provider.defaultSerializeValue({getter}, json)"
                lines.append(f'      if ({condition}) {{ json.writeFieldName("{field}"); {writer}; }}')
            serializer = f"""  public static final class OperandSerializer extends com.fasterxml.jackson.databind.ser.std.StdSerializer<{model}> {{
    public OperandSerializer() {{ super({model}.class); }}
    private static void writeOperand(Object value, com.fasterxml.jackson.core.JsonGenerator json,
        com.fasterxml.jackson.databind.SerializerProvider provider) throws java.io.IOException {{
      if (value instanceof java.util.Map<?, ?> object) {{
        json.writeStartObject();
        for (var entry : object.entrySet()) {{
          json.writeFieldName(String.valueOf(entry.getKey()));
          writeOperand(entry.getValue(), json, provider);
        }}
        json.writeEndObject();
      }} else if (value instanceof Iterable<?> array) {{
        json.writeStartArray();
        for (var item : array) writeOperand(item, json, provider);
        json.writeEndArray();
      }} else provider.defaultSerializeValue(value, json);
    }}
    @Override public void serialize({model} rule, com.fasterxml.jackson.core.JsonGenerator json,
        com.fasterxml.jackson.databind.SerializerProvider provider) throws java.io.IOException {{
      json.writeStartObject();
{chr(10).join(lines)}
      json.writeEndObject();
    }}
  }}

"""
            replace(path, f'  public {model}() {{', serializer + f'  public {model}() {{')


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
    preserve_json_operand_presence(target, output)
    replace_repository_placeholders(output)
    clean_document_visual_generation_docs(output)
    strip_trailing_whitespace(output)


if __name__ == "__main__":
    main()
