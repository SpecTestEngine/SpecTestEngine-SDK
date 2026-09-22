

# BrowserVisualComparison

Immutable visual comparison generation. Baseline promotion creates a new baseline revision; it never deletes evidence referenced by older comparisons or snapshots.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comparisonId** | **UUID** |  |  |
|**status** | **BrowserVisualComparisonStatus** |  |  |
|**decisionStatus** | **BrowserVisualDecisionStatus** |  |  |
|**scopeType** | **BrowserVisualScopeType** |  |  |
|**compareMode** | **BrowserVisualCompareMode** |  |  |
|**stopPolicy** | **BrowserVisualStopPolicy** |  |  |
|**baselineArtifactId** | **UUID** |  |  [optional] |
|**actualArtifactId** | **UUID** |  |  [optional] |
|**diffArtifactId** | **UUID** |  |  [optional] |
|**diffPixels** | **Long** |  |  [optional] |
|**diffPixelRatio** | **Double** |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**changedDetails** | **List&lt;String&gt;** |  |  [optional] |
|**changedRegions** | [**List&lt;BrowserVisualDiffRegion&gt;**](BrowserVisualDiffRegion.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  |
|**reviewedAt** | **OffsetDateTime** |  |  [optional] |
|**assertionRevision** | **Long** |  |  |
|**baselineRevisionId** | **UUID** |  |  [optional] |
|**appliedBaselineRevisionId** | **UUID** |  |  [optional] |
|**generationNumber** | **Integer** |  |  |
|**sourceComparisonId** | **UUID** |  |  [optional] |
|**rootComparisonId** | **UUID** |  |  |
|**excludedRegions** | [**List&lt;BrowserVisualExcludedRegion&gt;**](BrowserVisualExcludedRegion.md) |  |  |
|**changedExcludedRegionIndexes** | **Set&lt;Integer&gt;** |  |  |
|**reviewCapabilities** | [**BrowserVisualReviewCapabilities**](BrowserVisualReviewCapabilities.md) |  |  |



