# SpecTestEngine.Sdk.Model.BrowserVisualComparison
Immutable visual comparison generation. Baseline promotion creates a new baseline revision; it never deletes evidence referenced by older comparisons or snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ComparisonId** | **Guid** |  |
**Status** | **BrowserVisualComparisonStatus** |  |
**DecisionStatus** | **BrowserVisualDecisionStatus** |  |
**ScopeType** | **BrowserVisualScopeType** |  |
**CompareMode** | **BrowserVisualCompareMode** |  |
**StopPolicy** | **BrowserVisualStopPolicy** |  |
**CreatedAt** | **DateTimeOffset** |  |
**AssertionRevision** | **long** |  |
**GenerationNumber** | **int** |  |
**RootComparisonId** | **Guid** |  |
**ExcludedRegions** | [**List&lt;BrowserVisualExcludedRegion&gt;**](BrowserVisualExcludedRegion.md) |  |
**ChangedExcludedRegionIndexes** | **List&lt;int&gt;** |  |
**ReviewCapabilities** | [**BrowserVisualReviewCapabilities**](BrowserVisualReviewCapabilities.md) |  |
**BaselineArtifactId** | **Guid** |  | [optional]
**ActualArtifactId** | **Guid** |  | [optional]
**DiffArtifactId** | **Guid** |  | [optional]
**DiffPixels** | **long** |  | [optional]
**DiffPixelRatio** | **double** |  | [optional]
**Message** | **string** |  | [optional]
**ChangedDetails** | **List&lt;string&gt;** |  | [optional]
**ChangedRegions** | [**List&lt;BrowserVisualDiffRegion&gt;**](BrowserVisualDiffRegion.md) |  | [optional]
**ReviewedAt** | **DateTimeOffset** |  | [optional]
**BaselineRevisionId** | **Guid** |  | [optional]
**AppliedBaselineRevisionId** | **Guid** |  | [optional]
**SourceComparisonId** | **Guid** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
