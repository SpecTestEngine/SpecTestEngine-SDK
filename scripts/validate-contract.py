#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"contract validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("expected the path to the canonical OpenAPI document")

    contract = Path(sys.argv[1]).read_text(encoding="utf-8")
    paths = contract.split("\npaths:", 1)[1].split("\ncomponents:", 1)[0]
    operation_ids = re.findall(r"^ {6}operationId:\s*([A-Za-z][A-Za-z0-9]*)\s*$", paths, re.MULTILINE)
    if not operation_ids:
        fail("no operationId values were found")
    duplicates = sorted({value for value in operation_ids if operation_ids.count(value) > 1})
    if duplicates:
        fail(f"duplicate operationId values: {', '.join(duplicates)}")

    required_fragments = (
        "openapi: 3.0.3",
        "BearerAuth:",
        "ProblemDetails:",
        "x-sdk-stability:",
        "x-idempotent:",
    )
    for fragment in required_fragments:
        if fragment not in contract:
            fail(f"missing required contract marker: {fragment}")

    print(f"contract validation passed: {len(operation_ids)} operations")


if __name__ == "__main__":
    main()
