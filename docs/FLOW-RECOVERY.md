# Flow recovery

Contract: `1.0.0-alpha.6` (preview). These additive operations require a server with the Flow recovery feature enabled and complete retained authoring evidence. Older runs are not backfilled. Interactive/customer project-scoped authorization is required; connected-agent delegated recovery is not enabled.

1. Call `previewFlowRecovery(runId)`. Check `available`; show `reason` when evidence or the server feature is unavailable. Preview creates nothing.
2. Review its historical Flow and binding requirements. Page summaries with `listFlowRecoveryDependencies`; load exact retained definitions lazily with `getFlowRecoveryDependency`.
3. Choose a new name and supply exactly the requested scalar bindings. Preserve JSON numbers/booleans; use fresh request values or supported variable placeholders, never inferred historical runtime secrets.
4. Generate one UUID idempotency key for this intent and retain the identical request in memory for a retry. Explicitly call `createFlowRecovery`. It creates a new Flow and independent specification/macro copies, not an overwrite or a test execution.
5. Read `getFlowRecoveryOperation` using the returned operation ID. `COMPLETED` identifies the new Flow. `202` and `OUTCOME_UNKNOWN` are not completion or cancellation.

If a reply is lost or an operation is interrupted, read status and explicitly resume with **the same key and identical body**. Do not create a fresh key or fall back to ordinary create. GET readback never resumes writes. Partially created dependencies are retained and reconciled, not deleted automatically. After restart, fresh bindings must be resupplied by the caller; the operation summary does not contain them. Never log/persist credential-bearing requests as diagnostics.

Current company/project/resource, source read, each owner create and commercial policies are checked independently. A saved run ID or manifest hash does not grant access. Original Flows, specs, macros, run evidence, snapshots and Sentinel/managed bindings remain unchanged. A later Run uses normal authorization and billing.

Recovery is an API lifecycle, not a new field in Flow DSL. Recovered Flow documents use normal steps, new dependency IDs, variable placeholders and store/override mappings. Runtime values and private worker plans are not historical authoring sources.

Canonical route and language signatures are generated from OpenAPI. No provider/payment, internal owner-copy, worker-grant or raw artifact-store APIs are exposed by these operations. End-to-end runtime and fault qualification is tracked in the development repository's Flow recovery delivery plan; generated transports alone do not certify server behavior.
