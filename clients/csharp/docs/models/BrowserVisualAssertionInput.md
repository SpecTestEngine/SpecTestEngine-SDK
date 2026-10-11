# SpecTestEngine.Sdk.Model.BrowserVisualAssertionInput
Saved visual assertion. The existing Java comparator and thresholds are unchanged. Baseline images are raw captures, never WebRTC video frames. Omitted exclusions mean an empty list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | **bool** |  | [optional]
**Name** | **string** |  | [optional]
**ScopeType** | **BrowserVisualScopeType** |  | [optional]
**CompareMode** | **BrowserVisualCompareMode** |  | [optional]
**StopPolicy** | **BrowserVisualStopPolicy** |  | [optional]
**MaxDiffPixels** | **long** |  | [optional]
**MaxDiffPixelRatio** | **double** |  | [optional]
**ColorThreshold** | **double** |  | [optional]
**MoveTolerancePx** | **double** |  | [optional]
**Bounds** | [**BrowserVisualBounds**](BrowserVisualBounds.md) |  | [optional]
**ExcludedRegions** | [**List&lt;BrowserVisualExcludedRegion&gt;**](BrowserVisualExcludedRegion.md) |  | [optional]
**BaselineScreenshotBase64** | **byte[]** | Raw baseline capture supplied during authoring; omitted from saved definition reads. | [optional]
**BaselineSemanticJson** | **string** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
