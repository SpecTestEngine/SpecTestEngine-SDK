# Contributing

## Contract-first workflow

1. Confirm the requested operation belongs in the public API rather than an internal service API.
2. Update `openapi/spectestengine-public-v1.yaml` with stable names, constraints, examples, and error behavior.
3. Run `make validate`.
4. Run `make generate` from a clean working tree.
5. Build all generated clients with `make verify`.
6. Review the generated diff for accidental renames, nullable changes, or widened authentication.
7. Describe compatibility and migration impact in the pull request.

Generated files are not edited manually. A generated defect is fixed in the canonical contract,
the language config, or a reviewed custom template.

## Public contract boundary

Do not expose internal engine-to-engine routes, owner ids, actor ids, storage credentials, session
cookies, or implementation-specific DTOs. Public operations must work through the production
gateway with a project-scoped bearer token.

Use a thin handwritten façade for polling, SSE, WebSocket, browser playback, or attachment
lifecycle helpers when plain generated transport code is not enough. A façade must depend on the
generated layer and include its own tests.

## Compatibility review

Treat these changes as breaking unless proved otherwise:

- removing or renaming an operation, field, enum value, or security scheme;
- changing a required field to a different type;
- making an optional request field required;
- changing identifier or pagination semantics;
- changing success status codes or media types;
- weakening error-code guarantees or retry behavior.

Additive optional fields and new operations are normally compatible, but every supported language
must still compile after regeneration.
