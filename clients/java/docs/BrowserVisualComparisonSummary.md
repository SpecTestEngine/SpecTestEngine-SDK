

# BrowserVisualComparisonSummary

Immutable visual evidence embedded in a Flow run or Snapshot behavior payload. Empty diagnostic/exclusion lists may be omitted. Fetch the comparison detail lazily for review capabilities.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comparisonId** | **UUID** |  |  [optional] |
|**status** | **BrowserVisualComparisonStatus** |  |  [optional] |
|**decisionStatus** | **BrowserVisualDecisionStatus** |  |  [optional] |
|**scopeType** | **BrowserVisualScopeType** |  |  [optional] |
|**compareMode** | **BrowserVisualCompareMode** |  |  [optional] |
|**stopPolicy** | **BrowserVisualStopPolicy** |  |  [optional] |
|**baselineArtifactId** | **UUID** |  |  [optional] |
|**actualArtifactId** | **UUID** |  |  [optional] |
|**diffArtifactId** | **UUID** |  |  [optional] |
|**diffPixels** | **Long** |  |  [optional] |
|**diffPixelRatio** | **Double** |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**changedDetails** | **List&lt;String&gt;** |  |  [optional] |
|**changedRegions** | [**List&lt;BrowserVisualDiffRegion&gt;**](BrowserVisualDiffRegion.md) |  |  [optional] |
|**assertionRevision** | **Long** |  |  [optional] |
|**baselineRevisionId** | **UUID** |  |  [optional] |
|**generationNumber** | **Integer** |  |  [optional] |
|**sourceComparisonId** | **UUID** |  |  [optional] |
|**rootComparisonId** | **UUID** |  |  [optional] |
|**excludedRegions** | [**List&lt;BrowserVisualExcludedRegion&gt;**](BrowserVisualExcludedRegion.md) |  |  [optional] |
|**changedExcludedRegionIndexes** | **List&lt;Integer&gt;** |  |  [optional] |
