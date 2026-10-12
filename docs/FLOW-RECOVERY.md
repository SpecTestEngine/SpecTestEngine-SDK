# Flow recovery

Contract: `1.0.0-alpha.7` (preview). These operations require enabled Flow recovery and complete retained authoring evidence. Older runs are not backfilled. Human/customer project-scoped authorization is required; connected-agent delegated recovery is not enabled.

1. Call `reviewFlowRecovery(runId)`. Check `historical.available` and `restoreAvailable`; show the corresponding reason instead of offering an inert action. Review creates nothing.
2. Review the historical Flow and current target/dependency revisions. Page summaries with `listFlowRecoveryDependencies`; load retained definitions lazily with `getFlowRecoveryDependency`, and current safe definitions with `getFlowRecoveryCurrentDependency`.
3. Edit the ordinary Flow draft. Preserve ordered `sourceStepIds` for retained occurrences; use null for an added ordinary reference and retrieve its current revision. Removed steps do not restore unused dependencies. Supply exactly the requested scalar bindings; retain JSON numbers/booleans and fresh values or supported placeholders, not inferred historical secrets.
4. Generate one UUID idempotency key and retain the exact reviewed request in memory. Call `restoreFlowRecoveryDraft` with mode `RESTORE` to update the original Flow and selected original dependencies, preserving IDs. Call `copyFlowRecoveryDraft` with mode `COPY` and a new name to create an independent Flow/dependency set. Both use the same typed draft and revision checks. Neither runs tests or regenerates assertions from responses.
5. Read `getFlowRecoveryOperation`. `COMPLETED` identifies the restored/new Flow. `202` and `OUTCOME_UNKNOWN` are not completion or cancellation.

`previewFlowRecovery`/`createFlowRecovery` retain the existing unedited copy-only API; they do not replace the editable restore/copy distinction.

If a reply is lost or interrupted, read status and explicitly resume with **the same key and identical body**. Do not create a fresh key or fall back to ordinary create. GET readback never resumes writes. Partially restored originals remain updated; partial copies remain retained. There is no automatic rollback or deletion. An intervening ordinary edit rejects stale recovery. After caller restart, resupply the exact intent and fresh bindings; operation summaries do not contain them. Never log/persist credential-bearing requests as diagnostics.

Current company/project/resource, source read, owner update/create and commercial policies are checked independently. A run ID or manifest hash grants no access. Restore changes shared original definitions, so other Flows using those IDs observe them on later execution. Copy leaves originals untouched. Run history and snapshots are immutable. Product UI refreshes linked staging Sentinel snapshots after restore and reports synchronization errors separately; headless consumers must refresh independently maintained monitoring definitions through the ordinary Sentinel API. A later Run uses normal authorization and billing.

Recovery is an API lifecycle, not a new DSL field. Resulting documents use ordinary steps, existing IDs for restore or new IDs for copy, variable placeholders and store/override mappings. Runtime values and private worker plans are not historical authoring sources.

Canonical route and language signatures are generated from OpenAPI. No provider/payment, internal owner-copy, worker-grant or raw artifact-store APIs are exposed by these operations. End-to-end runtime and fault qualification is tracked in the development repository's Flow recovery delivery plan; generated transports alone do not certify server behavior.
