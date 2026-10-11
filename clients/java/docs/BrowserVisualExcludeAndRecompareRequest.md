

# BrowserVisualExcludeAndRecompareRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionId** | **UUID** | Client-generated idempotency key for this review command. |  |
|**expectedAssertionRevision** | **Long** | Current assertion revision. A stale value is rejected with HTTP 409. |  |
|**excludedRegions** | [**List&lt;BrowserVisualExcludedRegion&gt;**](BrowserVisualExcludedRegion.md) | Complete normalized exclusion set for the next assertion revision. Overlaps are valid; rectangles crossing right or bottom edges are clamped to the comparison canvas. |  |
