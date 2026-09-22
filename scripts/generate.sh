#!/usr/bin/env sh
set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
TARGET=${1:-all}

generate_target() {
  target=$1
  output="$ROOT_DIR/clients/$target"
  rm -rf "$output"
  mkdir -p "$output"
  "$ROOT_DIR/scripts/openapi-generator.sh" generate \
    -c "/workspace/generator/config/$target.yaml" \
    --skip-validate-spec
  python3 "$ROOT_DIR/scripts/postprocess-generated.py" "$target" "$output"
}

"$ROOT_DIR/scripts/validate.sh"

case "$TARGET" in
  all)
    generate_target java
    generate_target typescript
    generate_target python
    generate_target csharp
    generate_target go
    ;;
  java|typescript|python|csharp|go)
    generate_target "$TARGET"
    ;;
  *)
    printf '%s\n' "Unknown target '$TARGET'. Use all, java, typescript, python, csharp, or go." >&2
    exit 2
    ;;
esac
