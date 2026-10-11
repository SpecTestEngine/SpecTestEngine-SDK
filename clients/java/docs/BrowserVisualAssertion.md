

# BrowserVisualAssertion

Persisted visual definition. Revisions are server-owned; baseline bytes are fetched separately through retained artifact references.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** |  |  |
|**name** | **String** |  |  [optional] |
|**scopeType** | **BrowserVisualScopeType** |  |  [optional] |
|**compareMode** | **BrowserVisualCompareMode** |  |  [optional] |
|**stopPolicy** | **BrowserVisualStopPolicy** |  |  [optional] |
|**baselineArtifactId** | **UUID** |  |  [optional] |
|**baselineRevisionId** | **UUID** |  |  [optional] |
|**assertionRevision** | **Long** |  |  |
|**maxDiffPixels** | **Long** |  |  [optional] |
|**maxDiffPixelRatio** | **Double** |  |  [optional] |
|**colorThreshold** | **Double** |  |  [optional] |
|**moveTolerancePx** | **Double** |  |  [optional] |
|**bounds** | [**BrowserVisualBounds**](BrowserVisualBounds.md) |  |  [optional] |
|**excludedRegions** | [**List&lt;BrowserVisualExcludedRegion&gt;**](BrowserVisualExcludedRegion.md) |  |  |
