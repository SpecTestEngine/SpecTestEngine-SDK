# SpecTestEngine.Sdk.Model.BrowserVisualExcludeAndRecompareRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ActionId** | **Guid** | Client-generated idempotency key for this review command. |
**ExpectedAssertionRevision** | **long** | Current assertion revision. A stale value is rejected with HTTP 409. |
**ExcludedRegions** | [**List&lt;BrowserVisualExcludedRegion&gt;**](BrowserVisualExcludedRegion.md) | Complete normalized exclusion set for the next assertion revision. Overlaps are valid; rectangles crossing right or bottom edges are clamped to the comparison canvas. |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

