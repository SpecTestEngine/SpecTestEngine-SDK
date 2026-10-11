

# BrowserVisualAssertionInput

Saved visual assertion. The existing Java comparator and thresholds are unchanged. Baseline images are raw captures, never WebRTC video frames. Omitted exclusions mean an empty list.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**scopeType** | **BrowserVisualScopeType** |  |  [optional] |
|**compareMode** | **BrowserVisualCompareMode** |  |  [optional] |
|**stopPolicy** | **BrowserVisualStopPolicy** |  |  [optional] |
|**maxDiffPixels** | **Long** |  |  [optional] |
|**maxDiffPixelRatio** | **Double** |  |  [optional] |
|**colorThreshold** | **Double** |  |  [optional] |
|**moveTolerancePx** | **Double** |  |  [optional] |
|**bounds** | [**BrowserVisualBounds**](BrowserVisualBounds.md) |  |  [optional] |
|**excludedRegions** | [**List&lt;BrowserVisualExcludedRegion&gt;**](BrowserVisualExcludedRegion.md) |  |  [optional] |
|**baselineScreenshotBase64** | **byte[]** | Raw baseline capture supplied during authoring; omitted from saved definition reads. |  [optional] |
|**baselineSemanticJson** | **String** |  |  [optional] |
