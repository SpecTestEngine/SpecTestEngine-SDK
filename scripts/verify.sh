#!/usr/bin/env sh
set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)

"$ROOT_DIR/scripts/validate.sh"
python3 -m unittest discover -s "$ROOT_DIR/scripts/tests" -p 'test_generated_formatting.py'

if [ -d "$ROOT_DIR/clients/java" ]; then
  (cd "$ROOT_DIR/clients/java" && ./gradlew test)
fi

if [ -f "$ROOT_DIR/clients/typescript/package.json" ]; then
  (cd "$ROOT_DIR/clients/typescript" && npm install --ignore-scripts --package-lock=false && npm run build)
  node --test "$ROOT_DIR/scripts/tests/browser-contract.test.mjs"
  node --test "$ROOT_DIR/scripts/tests/flow-recovery-contract.test.mjs"
fi

if [ -f "$ROOT_DIR/clients/python/pyproject.toml" ]; then
  python3 -m compileall -q "$ROOT_DIR/clients/python/spectestengine_sdk"
fi

if [ -f "$ROOT_DIR/clients/csharp/SpecTestEngine.Sdk.sln" ]; then
  if command -v dotnet >/dev/null 2>&1; then
    dotnet build "$ROOT_DIR/clients/csharp/SpecTestEngine.Sdk.sln" --configuration Release --warnaserror
  else
    docker run --rm \
      -v "$ROOT_DIR:/workspace" \
      -w /workspace \
      mcr.microsoft.com/dotnet/sdk:10.0 \
      dotnet build clients/csharp/SpecTestEngine.Sdk.sln --configuration Release --warnaserror
  fi
fi

if [ -f "$ROOT_DIR/clients/go/go.mod" ]; then
  if command -v go >/dev/null 2>&1; then
    (cd "$ROOT_DIR/clients/go" && go test ./...)
  else
    docker run --rm \
      -v "$ROOT_DIR:/workspace" \
      -w /workspace/clients/go \
      golang:1.23 \
      go test ./...
  fi
fi

mkdir -p "$ROOT_DIR/.sdk-build/java-facade-test"
javac --release 17 \
  -d "$ROOT_DIR/.sdk-build/java-facade-test" \
  "$ROOT_DIR/facades/java/src/main/java/software/ste/sdk/workflows/WorkflowSupport.java" \
  "$ROOT_DIR/facades/java/src/test/java/software/ste/sdk/workflows/WorkflowSupportTest.java"
java -cp "$ROOT_DIR/.sdk-build/java-facade-test" software.ste.sdk.workflows.WorkflowSupportTest

(cd "$ROOT_DIR/facades/typescript" && npm install --ignore-scripts --package-lock=false && npm test)
PYTHONPATH="$ROOT_DIR/facades/python" python3 -m unittest discover -s "$ROOT_DIR/facades/python/tests" -v

if command -v dotnet >/dev/null 2>&1; then
  dotnet run \
    --project "$ROOT_DIR/facades/csharp/tests/SpecTestEngine.Sdk.Workflows.Tests.csproj" \
    --configuration Release
else
  docker run --rm \
    -v "$ROOT_DIR:/workspace" \
    -w /workspace \
    mcr.microsoft.com/dotnet/sdk:10.0 \
    dotnet run \
      --project facades/csharp/tests/SpecTestEngine.Sdk.Workflows.Tests.csproj \
      --configuration Release
fi

if command -v go >/dev/null 2>&1; then
  (cd "$ROOT_DIR/facades/go" && go test ./...)
else
  docker run --rm \
    -v "$ROOT_DIR:/workspace" \
    -w /workspace/facades/go \
    golang:1.23 \
    go test ./...
fi
