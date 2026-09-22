#!/usr/bin/env sh
set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)

"$ROOT_DIR/scripts/openapi-generator.sh" validate \
  -i /workspace/openapi/spectestengine-public-v1.yaml \
  --recommend

python3 "$ROOT_DIR/scripts/validate-contract.py" \
  "$ROOT_DIR/openapi/spectestengine-public-v1.yaml"

python3 "$ROOT_DIR/scripts/validate-versions.py"
