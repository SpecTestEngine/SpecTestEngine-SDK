#!/usr/bin/env sh
set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
. "$ROOT_DIR/generator/version.env"

if command -v docker >/dev/null 2>&1; then
  exec docker run --rm \
    --user "$(id -u):$(id -g)" \
    -v "$ROOT_DIR:/workspace" \
    "openapitools/openapi-generator-cli:v${OPENAPI_GENERATOR_VERSION}" "$@"
fi

printf '%s\n' "Docker is required to run the pinned OpenAPI Generator ${OPENAPI_GENERATOR_VERSION}." >&2
exit 1
