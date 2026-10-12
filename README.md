# SpecTestEngine SDK

Typed clients and the canonical public OpenAPI contract for integrating with
[SpecTestEngine](https://ste.software).

> **Preview status:** the source repository and public API contract are available for evaluation.
> The contract is versioned, validated, and usable for local client generation and deterministic
> ZIP downloads, but packages are not yet published to Maven
> Central, npm, PyPI, NuGet, or the public Go module proxy.

## Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Authentication](#authentication)
- [Language Guides](#language-guides)
- [Common Workflows](#common-workflows)
- [Contract Maintenance](#contract-maintenance)
- [Security and Support](#security-and-support)
- [License](#license)

| I want to... | Start here |
|---|---|
| Explore the public API | [`openapi/spectestengine-public-v1.yaml`](openapi/spectestengine-public-v1.yaml) or the [visual SDK reference](https://ste.software/docs/sdk) |
| Generate one typed client | [Generate a client](#generate-a-client) |
| Use an SDK before registry publication | [Self-contained SDK ZIPs](#use-an-sdk-without-a-public-registry) |
| Configure authorization | [Authentication](#authentication) |
| Poll jobs, consume SSE, or stream files | [Workflow helpers](#workflow-helpers) |
| Contribute a contract change | [Contract maintenance](#contract-maintenance) |

## Overview

### What You Can Automate

The current public contract covers 143 operations across the core testing workflow:

See [Flow recovery](docs/FLOW-RECOVERY.md) for historical review, typed editable drafts, same-ID restore, optional copy and safe retry/readback.

| Area | Typical integrations |
|---|---|
| REST, SOAP, GraphQL, and streaming specifications | Create executable contracts, search libraries, run saved specs, inspect run history, and recover the exact DSL content retained by a completed PASS or FAIL run |
| Streaming testing | Validate and execute bounded WebSocket/WSS, SSE, gRPC Streaming, and MQTT DSL, poll asynchronous runs, page redacted semantic transcripts, and cancel active work |
| Fragments | Discover the protocol-aware DSL catalog, filter and store granular blocks, compile saved or inline fragments, and save the result in the matching engine |
| Flows | Compose API and typed browser steps, run one Flow or a batch, review historical recovery and restore the original Flow/dependencies or explicitly create an independent copy |
| Run batches and snapshots | Collect release evidence, promote baselines, and compare definition or behavior drift |
| Craftsman | Manage mixed-protocol request workspaces, queue HTTP or bounded Streaming sessions, poll evidence/transcripts, cancel active work, and reuse request attachments |
| Sentinel | Create checks, queue probes, and retrieve retry and baseline evidence |
| Generation | Generate self-contained REST/SOAP/GraphQL/Streaming specs from concrete Craftsman evidence, generate tests from OpenAPI, and export portable ATF Java projects |
| Visual document diffs | Open a protected review link after a failed attachment assertion, upload the reference document, inspect rendered page changes, regenerate immutable comparisons, and prepare a baseline update draft |

Interactive browser recording, MCP transport, and AI conversations are not pretended to be
ordinary request/response APIs. Streaming test execution itself has an explicit bounded async
lifecycle: queue a WebSocket/WSS, SSE, gRPC Streaming, or MQTT run, poll its returned status URL, page
the already-redacted transcript, and cancel through the returned cancel URL.

### Repository Layout

```text
openapi/
  spectestengine-public-v1.yaml   Canonical public contract
  versions.json                   Allowlisted contract versions and SHA-256 checksums
  versions/                       Immutable contracts available to the ZIP generator
generator/
  version.env                     Pinned OpenAPI Generator version
  config/                         One reviewed config per supported language
scripts/
  validate.sh                     OpenAPI and policy validation
  generate.sh                     Deterministic client generation
  verify.sh                       Validation plus language smoke builds
  package-sdk.py                  Versioned deterministic SDK ZIP builder
clients/
  java/                           Generated Java client
  typescript/                     Generated TypeScript Fetch client
  python/                         Generated Python client
  csharp/                         Generated .NET 10 client
  go/                             Generated Go module
facades/                          Maintained polling, SSE, cancellation, and streaming helpers
artifacts/                        Local self-service ZIP output (not committed)
```

The OpenAPI document is the source of truth. Files under `clients/` are reproducible generated
output. Do not hand-edit generated models or API classes; update the contract or a generator
configuration and regenerate instead.

Fragment models require `specType` and expose SOAP-specific `SOAP_REQUEST`/`SOAP_ASSERTION`,
GraphQL-specific `GRAPHQL_OPERATION`/`GRAPHQL_ASSERTION`, and granular `STREAM_*` values. Streaming
fragment requests additionally carry the selected `streamingTransport`, while catalog entries
declare their compatible transports. Call the generated
`getFragmentCatalog` operation before authoring DSL, and keep every compile request scoped to one
API type. Fragment UUIDv7 values are opaque integration identifiers; applications should present
names and protocol/type labels to users.

Version recovery is definition-only and separate from response-driven regeneration. Call the
protocol-specific recovery preview before restore. The source must be a completed `PASS` or `FAIL`
run, never an execution error. The optional recovery test-run executes that exact historical DSL
against the current API without changing the saved specification. Restore copies the same persisted
DSL into the current saved specification while preserving its id, name, description, and stable
identity. Existing run and snapshot evidence is immutable; future pairwise comparisons observe the
restored definition via the existing definition hash.

## Quick Start

### Prerequisites

- Docker 24 or newer
- Make (optional; every command also has a script equivalent)
- A SpecTestEngine base URL
- A short-lived bearer token issued for a user-delegated session or machine principal

Generation uses the pinned `openapitools/openapi-generator-cli:v7.22.0` image. You do not need a
global Java, Node, Python, or OpenAPI Generator installation just to generate clients.

### Generate a Client

Clone the repository and generate all supported clients:

```bash
git clone https://github.com/SpecTestEngine/SpecTestEngine-SDK.git
cd SpecTestEngine-SDK
make validate
make generate
```

Generate only one language:

```bash
make generate-java
make generate-typescript
make generate-python
make generate-csharp
make generate-go
```

The equivalent script commands are:

```bash
./scripts/validate.sh
./scripts/generate.sh java
./scripts/generate.sh typescript
./scripts/generate.sh python
./scripts/generate.sh csharp
./scripts/generate.sh go
```

Generation removes and recreates the selected `clients/<language>` directory. Handwritten helpers
live under `facades/`; generated API classes and maintained workflow behavior therefore have clear
ownership and can be reviewed independently.

### Use an SDK Without a Public Registry

Maven Central and the other package registries are conveniences, not generator dependencies. You
can use every supported SDK during the package preview in any of these ways:

1. Generate `clients/<language>` locally from the pinned Docker image.
2. Build the generated client and consume its local JAR, editable Python package, NuGet package,
   or Go module.
3. Add the generated source as a Gradle composite build, repository module, or equivalent source
   dependency.
4. Build a self-contained ZIP containing the client, exact contract, metadata, and workflow helpers.

Build one ZIP for the latest contract:

```bash
python3 scripts/package-sdk.py --language java
python3 scripts/package-sdk.py --language csharp
```

Select an immutable contract explicitly:

```bash
python3 scripts/package-sdk.py \
  --language go \
  --contract-version 1.0.0-alpha.6
```

Use `--language all` or `make package` to build all five. Archives and `.sha256` sidecars are written
under `artifacts/<contract-version>/`. The generator rejects unknown languages, unknown versions,
and checksum mismatches; it never silently falls back to the latest contract.

Repository users can also run the **Build one SDK ZIP** GitHub Actions workflow, choose a language,
enter an allowlisted contract version, and download the resulting workflow artifact. This is CI
artifact delivery, not package-registry publication.

### Authentication

SDK calls use an OAuth2/OIDC bearer access token:

```http
Authorization: Bearer <access-token>
```

Use a user-delegated token for an interactive integration acting on behalf of a signed-in person.
Use a machine principal for CI, scheduled automation, or a server-to-server integration. Grant
only the permissions required by the operations you call and keep tokens out of source code,
logs, URLs, and generated artifacts.

Choose the matching OAuth flow:

| Integration | OAuth flow |
|---|---|
| Web, desktop, or mobile app acting for a signed-in user | Authorization Code with PKCE |
| CI, scheduled automation, CLI, or server-to-server integration | Client Credentials |

A SpecTestEngine company administrator registers the integration and approves its scopes. Use the
issuer discovery document to resolve the authorization and token endpoints; do not hardcode
provider-specific paths. The complete public procedure, token request example, expiration rules,
and production checklist are in [`docs/AUTHENTICATION.md`](docs/AUTHENTICATION.md).

The Integration Builder offers only capabilities included in the company's subscription. The
selected integration type determines whether the token is user-delegated or machine-to-machine;
the approved capabilities determine its available scopes. A valid token still cannot use a
feature that is outside the current subscription.

Examples below read credentials from environment variables:

```bash
export STE_BASE_URL="https://app.ste.software"
export STE_ACCESS_TOKEN="<short-lived-access-token>"
```

The token selects the approved company and project context. Public clients must not send internal
`ownerCompanyId` or `actorId` values.

### First Request

Before using a generated client, the same request can be checked with curl:

```bash
curl --fail-with-body \
  --header "Authorization: Bearer ${STE_ACCESS_TOKEN}" \
  --get "${STE_BASE_URL}/test/rest-spec/page" \
  --data-urlencode "page=0" \
  --data-urlencode "size=20" \
  --data-urlencode "search=catalog"
```

The response uses the shared page envelope:

```json
{
  "items": [],
  "page": 0,
  "size": 20,
  "totalElements": 0,
  "totalPages": 0,
  "first": true,
  "last": true
}
```

## Language Guides

Each generated client exposes the same versioned public operations and shared schemas, bearer authentication,
and project-scoped behavior. Choose the language used by the integrating application; do not mix
generated transports from different contract versions in one deployment.

### Java

Generate the Java client, then build it with its generated Gradle wrapper:

```bash
make generate-java
cd clients/java
./gradlew build
```

The preview client uses Java's native HTTP client and Jackson. Configure the generated
`ApiClient` with the base URL and bearer token, then call a tag-specific API class such as
`RestSpecificationsApi` or `SentinelApi`. Exact generated class names are documented under
`clients/java/docs/` after generation.

Java 17 is the minimum generated-client target. Applications running Java 21, 25, or 26 can use
the same artifact.

### TypeScript

```bash
make generate-typescript
cd clients/typescript
npm install
npm run build
```

The TypeScript client uses `fetch`, so it works in modern browsers and Node.js runtimes that
provide the standard Fetch API. Supply the base path and an access-token callback when creating
the generated configuration. Prefer a callback over a fixed token so long-running applications
can refresh credentials without rebuilding the client.

### Python

```bash
make generate-python
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e clients/python
```

Configure `host` and the bearer token through the generated `Configuration` object. Keep one
`ApiClient` open for a related group of calls so its HTTP connection pool can be reused.

### C#

```bash
make generate-csharp
dotnet build clients/csharp/SpecTestEngine.Sdk.sln --configuration Release
```

The C# client targets .NET 10 and uses Generic Host integration, `HttpClient`, nullable reference
types, `System.Text.Json`, `DateTimeOffset`, and cancellation tokens on generated async operations.
Use the generated service registration extensions when dependency injection is available.

### Go

```bash
make generate-go
cd clients/go
go test ./...
```

The generated Go 1.23 module uses `context.Context` for cancellation and request-scoped bearer
tokens. Import it from `github.com/SpecTestEngine/SpecTestEngine-SDK/clients/go`.

## Common Workflows

### Workflow Helpers

Each language has a small module under `facades/<language>` with equivalent semantics:

- polling with a deadline, bounded backoff, progress callbacks, and cancellation;
- SSE parsing with multiline data, event ids, comments, and server retry hints;
- bounded streaming for ATF archives and request attachments;
- callback-based orchestration that composes generated typed operations without duplicating them.

For example, enqueue a Sentinel run with the generated client, then pass `getSentinelRun` as the
poll callback and treat `PASS`, `RECOVERED`, `FAIL`, `ERROR`, and `SKIPPED` as terminal states. The
same helper works for future asynchronous generation jobs because it is transport-neutral.

### Pagination, Search, and Retries

- Page indexes are zero-based.
- `size` is between 1 and 100.
- Search is server-side and project-scoped.
- Read operations marked `x-idempotent: true` can be retried after transient connection failures.
- Do not automatically retry runs or creates unless you supplied an `Idempotency-Key` and the
  endpoint documents support for it.
- Respect `429` and `Retry-After` when rate-limit responses are enabled.
- Sentinel queues runs asynchronously; enqueue first, then retrieve the returned run id.

### Run Batches and Snapshots

Use `RunBatchesApi` to collect completed specification, UI macro, and flow runs into one release
evidence set. A run batch is the candidate data: it records what ran, its status, hashes, and the
captured definition and behavior payloads.

Use `SnapshotsApi` to promote all or selected batch items into a baseline. You can then compare two
snapshots, compare a snapshot with a newer run batch, or request a field-level step diff. The diff
separates definition drift from behavior drift so integrations can distinguish an intentional test
change from a regression in the tested system.

Snapshot payload fields are deliberately represented as JSON values because API specs, browser
macros, and flows capture different evidence shapes. Stable metadata, identifiers, statuses,
selection policies, and diff classifications remain strongly typed.

### Request Attachments

Upload request files once with `uploadDocumentAsset`. The response is an immutable,
content-addressed `DocumentAssetReference` containing a UUIDv7 asset id, SHA-256 hash, content
type, size, object key, and multipart field metadata. Reuse that reference in Craftsman requests,
fragments, specifications, flows, and generated ATF projects instead of uploading duplicate file
bytes.

The SDK never exposes MinIO credentials. Asset access remains project-scoped and is performed by
SpecTestEngine services.

### Visual Document Diff

A PDF or image attachment assertion can persist normalized page masks in
`visualAssertion.excludedRegions`. REST, SOAP, and GraphQL engines always evaluate the exact hash
and structural fingerprint locally first. They call Browser Engine only when that local assertion
fails and at least one visual exclusion region is configured. Ordinary attachment failures never
send a response document to Browser Engine and do not use an automatic visual-diff fallback.

For the first failed attachment, explicitly call the capture operation for the saved REST, SOAP,
or GraphQL specification. For a saved flow, call the flow-step capture operation with its
zero-based `stepOrderIndex`. The server reruns the persisted source and captures only the selected
PDF/image attachment if it still fails. The returned specification or flow run keeps its real
failed status and contains the protected visual-review link. Draft sources are intentionally not
accepted because the diagnostic must be reproducible from a saved source.

When the masked visual assertion also fails, run evidence includes `visualDiffId`,
`visualDiffViewerUrl`, `visualDiffExpiresAt`, and `visualDiffStatus`. Give the protected viewer URL
to the current user, or use `DocumentVisualDiffsApi` to build the same review into an integration.

The reviewer uploads the expected file, compares Expected, Actual, and Changes page views, and can
draw page regions that are intentionally dynamic. Regeneration creates an immutable generation
containing its own threshold and normalized masks. Preview a baseline update in `EXACT` mode to
replace only the file hash, or in `VISUAL_EXCLUSIONS` mode to persist the masks and deterministic
masked page fingerprints. Confirm it only after explicit review. Confirmation creates a draft
proposal and never silently overwrites the source specification.

Source documents are rendered and discarded. The API exposes only hashes, summary metadata, and
encrypted rendered page artifacts until the diagnostic TTL expires. Access remains bound to the
company and active project selected by the bearer token; the viewer URL is protected, not public.

### Browser Visual Review

`BrowserVisualReviewsApi` exposes the review surface for saved Browser comparison evidence. It
does not expose the live Recorder WebRTC transport, execution-worker queues, leases, or storage
credentials. Retrieve an immutable comparison generation, download its retained Baseline,
Current, or Diff PNG artifacts, and inspect the action capabilities returned by the server.

The three explicit outcomes are `useCurrentBrowserVisualAsNewBaseline`,
`excludeBrowserVisualAreaAndRecompare`, and `keepBrowserVisualAsRegression`. Baseline promotion
creates a new immutable baseline revision; it does not delete artifacts referenced by historical
comparisons or Snapshot Timeline. Exclusion review sends the complete normalized region set and
creates a child comparison generation with the existing Browser comparator.

Each exclusion rectangle is relative to the active comparison canvas: the page for `PAGE`, the
captured element for `ELEMENT`, or the crop selected by `REGION` bounds. Masks affect visual
pixel/SSIM/region and scoped semantic comparison, and never hide URL, title, or network assertion failures. Send a new UUID `actionId`
and the current positive `expectedAssertionRevision` for mutating review commands. Replaying the
same action is idempotent; a stale revision is rejected with HTTP 409 instead of overwriting newer
work.

The current contract types Browser actions and inline macros in `FlowInput`, the flattened saved
`FlowStep` read model, and visual lineage in `FlowRunStep`. The saved Flow read model is not
an update request: use `browserSession.url` and nested `browserAction` when authoring. See
[`docs/BROWSER-VISUAL-REVIEW.md`](docs/BROWSER-VISUAL-REVIEW.md) for complete scope, replay, review,
retry, and retention examples. Interactive Recorder transport and worker control remain outside
the public SDK.

### Errors

Non-success responses use the shared `ProblemDetails` envelope:

```json
{
  "timestamp": "2026-07-16T10:15:30Z",
  "status": 422,
  "error": "UNPROCESSABLE_ENTITY",
  "message": "Specification validation failed",
  "path": "/test/rest-spec/create",
  "errorCode": "SPEC_VALIDATION_FAILED",
  "translationKey": "error.spec.validation"
}
```

Handle `errorCode` in automation. Treat `message` as user-facing context rather than a stable
programming contract. Never log bearer tokens, request authorization headers, provider API keys,
or unredacted secret variables when reporting an SDK error.

## Contract Maintenance

### Contract and Release Policy

- `/openapi/spectestengine-public-v1.yaml` is the canonical v1 contract.
- Breaking public changes require a new API/SDK major version.
- Compatible operations and fields produce a minor SDK release.
- Generator, template, or documentation fixes produce a patch release.
- UUID identifiers are opaque strings even though SpecTestEngine currently generates UUIDv7.
- `stable` operations are expected to preserve compatibility; `beta` operations may receive
  additive workflow refinements before package publication.

Every release candidate must validate immutable contract checksums, regenerate from a clean
checkout, compile all five supported clients and helpers, run shared contract fixtures, prove ZIP
determinism, and show no generated diff.

### Verify a Change

```bash
make verify
git diff --exit-code -- clients
```

CI runs the same contract and generation checks. A pull request should include the contract
change, regenerated clients, and a concise compatibility note.

Public registry publication remains an explicit pre-release task. The checklist is maintained in
[`docs/TODO-PACKAGE-PUBLISHING.md`](docs/TODO-PACKAGE-PUBLISHING.md); no registry credentials or
half-configured publishing behavior is present in this repository.

## Security and Support

### Security

Report suspected vulnerabilities privately to `security@ste.software` when that dedicated inbox
is published. Until then, use `support@ste.software` and do not include live credentials or
sensitive customer payloads. General SDK questions can also be sent to `support@ste.software`.

### Support

- Product documentation: <https://ste.software/docs/sdk>
- Website: <https://ste.software>
- Support: <support@ste.software>

## License

This project is licensed under the [Apache License 2.0](LICENSE). The license covers the public
OpenAPI contract, generated clients, maintained workflow helpers, documentation, and repository
tooling included here. SpecTestEngine product names and logos remain subject to the trademark
provision in Section 6 of the license.
