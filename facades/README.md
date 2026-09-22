# Workflow helpers

These small, handwritten modules complement the generated clients without duplicating their API
surface. Each language provides the same transport-level building blocks:

- cancellable polling with timeout and bounded backoff;
- SSE parsing with multiline `data`, event ids, and retry hints;
- bounded streaming for generated archives and request attachments;
- callback-based composition, so generated typed API calls remain the source of HTTP behavior.

The helpers intentionally do not invent endpoints that are absent from the public OpenAPI
contract. Pass a generated SDK operation as the polling or orchestration callback. This keeps the
workflow layer stable when an operation class is renamed by a generator update.
