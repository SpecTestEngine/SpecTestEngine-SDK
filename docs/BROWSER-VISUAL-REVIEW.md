# Browser Flow authoring and visual review

Contract: `1.0.0-alpha.5`. The canonical OpenAPI is authoritative for all five generated clients.
Browser execution remains a server operation; SDK clients do not install Chromium or run a second
execution engine. The SDK exposes the curated Flow and visual-review APIs, not live Recorder
signaling, TURN credentials, queues, worker registry, storage grants or pod management.

## Author a Browser Flow

`FlowInput.browserSession.url` is the initial URL. An inline Browser action uses the nested
`browserAction` input. Saved Flow reads instead expose flattened fields on `FlowStep`, including
`browserActionType` and the server-owned visual revisions. Do not submit a saved read model as an
update request without mapping it to the input model.

```json
{
  "name": "Checkout summary",
  "browserSession": {
    "url": "https://shop.example.com/cart",
    "viewportWidth": 1440,
    "viewportHeight": 900
  },
  "steps": [{
    "stepType": "BROWSER_ACTION",
    "orderIndex": 0,
    "browserAction": {
      "actionType": "CLICK",
      "orderIndex": 0,
      "selector": "[data-testid='checkout']",
      "selectorCandidates": ["[data-testid='checkout']"],
      "timeoutMs": 20000,
      "expectedPageTitle": "Checkout",
      "expectedPageTitlePolicy": "EXACT",
      "expectedNetworkPolicy": "PRESENCE",
      "expectedNetworkCalls": [{
        "enabled": true,
        "method": "POST",
        "url": "https://shop.example.com/api/cart/validate",
        "expectedStatusCode": 200
      }],
      "visualAssertion": {
        "enabled": true,
        "scopeType": "REGION",
        "compareMode": "LAYOUT",
        "stopPolicy": "CONTINUE_AND_REVIEW",
        "bounds": {
          "leftRatio": 0.55, "topRatio": 0.18,
          "widthRatio": 0.4, "heightRatio": 0.68
        },
        "excludedRegions": [{
          "xRatio": 0.04, "yRatio": 0.82,
          "widthRatio": 0.48, "heightRatio": 0.12,
          "reason": "Generated order number"
        }]
      }
    }
  }]
}
```

Without an existing or supplied raw baseline capture, the first visual check can return
`BASELINE_MISSING`; this is not a silently accepted baseline. Review its Current capture explicitly.

`PAGE` exclusions use the page image. `ELEMENT` exclusions use the selected element image.
`REGION` bounds select the page crop, while exclusions use coordinates local to that crop.
Coordinates are finite ratios in `[0, 1]`, with positive width and height. Rectangles crossing the
right/bottom edge are clipped without moving their origin; empty clipped areas are rejected.
Overlaps are valid, at most 250 regions are accepted, and an optional reason is trimmed and limited
to 300 characters. An empty list means no exclusions. Masks affect the existing pixel, SSIM,
changed-region and scoped semantic checks; URL, title and network assertions remain independent.

## Selectors, tabs and copied variables

The saved candidate chain is tried in order and must resolve one visible element. Replay does not
guess a replacement ID or choose an arbitrary ambiguous element. Keep `tabAlias`, `frameSelector`,
and macro `pageId` when mapping recorded actions. A missing target is an execution failure, not a
visual difference that an exclusion can hide.

Copy/paste between pages is represented by `EXTRACT_TEXT` followed by a variable-backed `FILL`.
The extraction runs again on every execution, so a mailbox OTP is never reused from the recording
sample. Use explicit variable references for sensitive action values; do not log values, clipboard
samples, tokens or artifact bytes. Network body/path values retain their JSON types.

## Review an immutable comparison

Read the comparison ID from `FlowRunStep.visualComparison`, then call `getBrowserVisualComparison`.
The run summary preserves the baseline revision, assertion revision, generation and parent/root
comparison IDs. Fetch details and PNG artifacts only when needed; do not put binaries in list
queries. Action capabilities are server-authoritative.

| UI decision | Generated operation | Request |
| --- | --- | --- |
| Use current as new baseline | `useCurrentBrowserVisualAsNewBaseline` | `actionId`, `expectedAssertionRevision` |
| Exclude area and recompare | `excludeBrowserVisualAreaAndRecompare` | `actionId`, `expectedAssertionRevision`, complete `excludedRegions` |
| Keep as regression | `keepBrowserVisualAsRegression` | `actionId`, `expectedAssertionRevision` |

Use one UUID `actionId` for one logical request. If transport fails, retry that exact body and ID;
do not create another logical action. A changed payload is a new user decision. HTTP 409 means the
definition or action conflicts: reload instead of blindly retrying against the latest revision.
HTTP 401/403 requires renewed authorization, not a fabricated successful result.

Promotion changes the active baseline definition and returns the applied baseline revision.
Historical comparisons retain their original Expected and Current references. Exclusion review
creates a linked generation from the same raw captures, without running the browser again. A change
outside the exclusions still fails. Keep as regression records a decision without changing any
baseline, threshold or exclusion. For Flow-owned assertions, success requires the authoritative
Flow definition update; an owner/backend failure must not be treated as applied.

## Retention and cancellation

Evidence is not permanent for every run. Identical captures share content-addressed storage;
successful unchanged comparisons can reference retained identical evidence. Review captures remain
available only within configured retention, and unreferenced expired blobs are garbage-collected.
Promoted captures are retained while active or historical baseline references exist. Missing PNG
content or `EVIDENCE_EXPIRED` means the SDK should preserve the available metadata and disable
evidence-dependent review, not silently run the test again.

An action timeout is bounded at 120000 ms (default 20000 ms). Cancelling a local HTTP request or a
workflow-helper poll does not itself cancel server-side browser work. Use only a server cancel
operation explicitly exposed by the chosen public workflow; worker cancellation/lease endpoints
are internal and are not SDK APIs. Watching or viewing retained evidence does not execute a test.
