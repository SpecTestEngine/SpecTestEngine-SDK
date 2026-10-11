# SpecTestEngine.Sdk.Model.DocumentVisualDiffGeneration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**GenerationId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**GenerationNumber** | **int** |  |
**ExpectedSha256** | **string** |  |
**ColorThreshold** | **double** |  |
**TotalPages** | **int** |  |
**ChangedPages** | **int** |  |
**DiffPixels** | **long** |  |
**DiffPixelRatio** | **double** |  |
**CreatedAt** | **DateTimeOffset** |  |
**ExpiresAt** | **DateTimeOffset** |  |
**ExcludedRegions** | [**List&lt;DocumentVisualExcludedRegion&gt;**](DocumentVisualExcludedRegion.md) | Immutable normalized masks used by this generation. |
**ChangedExcludedRegionIndexes** | **List&lt;int&gt;** | Indexes into excludedRegions whose masked area contained a real change in this immutable generation. |
**Pages** | [**List&lt;DocumentVisualDiffPage&gt;**](DocumentVisualDiffPage.md) |  |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
