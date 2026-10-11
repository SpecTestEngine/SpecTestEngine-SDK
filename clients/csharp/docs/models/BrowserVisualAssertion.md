# SpecTestEngine.Sdk.Model.BrowserVisualAssertion
Persisted visual definition. Revisions are server-owned; baseline bytes are fetched separately through retained artifact references.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | **bool** |  |
**AssertionRevision** | **long** |  |
**ExcludedRegions** | [**List&lt;BrowserVisualExcludedRegion&gt;**](BrowserVisualExcludedRegion.md) |  |
**Name** | **string** |  | [optional]
**ScopeType** | **BrowserVisualScopeType** |  | [optional]
**CompareMode** | **BrowserVisualCompareMode** |  | [optional]
**StopPolicy** | **BrowserVisualStopPolicy** |  | [optional]
**BaselineArtifactId** | **Guid** |  | [optional]
**BaselineRevisionId** | **Guid** |  | [optional]
**MaxDiffPixels** | **long** |  | [optional]
**MaxDiffPixelRatio** | **double** |  | [optional]
**ColorThreshold** | **double** |  | [optional]
**MoveTolerancePx** | **double** |  | [optional]
**Bounds** | [**BrowserVisualBounds**](BrowserVisualBounds.md) |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
