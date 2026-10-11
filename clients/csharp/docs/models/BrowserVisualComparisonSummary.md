# SpecTestEngine.Sdk.Model.BrowserVisualComparisonSummary
Immutable visual evidence embedded in a Flow run or Snapshot behavior payload. Empty diagnostic/exclusion lists may be omitted. Fetch the comparison detail lazily for review capabilities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ComparisonId** | **Guid** |  | [optional]
**Status** | **BrowserVisualComparisonStatus** |  | [optional]
**DecisionStatus** | **BrowserVisualDecisionStatus** |  | [optional]
**ScopeType** | **BrowserVisualScopeType** |  | [optional]
**CompareMode** | **BrowserVisualCompareMode** |  | [optional]
**StopPolicy** | **BrowserVisualStopPolicy** |  | [optional]
**BaselineArtifactId** | **Guid** |  | [optional]
**ActualArtifactId** | **Guid** |  | [optional]
**DiffArtifactId** | **Guid** |  | [optional]
**DiffPixels** | **long** |  | [optional]
**DiffPixelRatio** | **double** |  | [optional]
**Message** | **string** |  | [optional]
**ChangedDetails** | **List&lt;string&gt;** |  | [optional]
**ChangedRegions** | [**List&lt;BrowserVisualDiffRegion&gt;**](BrowserVisualDiffRegion.md) |  | [optional]
**AssertionRevision** | **long** |  | [optional]
**BaselineRevisionId** | **Guid** |  | [optional]
**GenerationNumber** | **int** |  | [optional]
**SourceComparisonId** | **Guid** |  | [optional]
**RootComparisonId** | **Guid** |  | [optional]
**ExcludedRegions** | [**List&lt;BrowserVisualExcludedRegion&gt;**](BrowserVisualExcludedRegion.md) |  | [optional]
**ChangedExcludedRegionIndexes** | **List&lt;int&gt;** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
