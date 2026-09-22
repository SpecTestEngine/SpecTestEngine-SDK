# SpecTestEngine.Sdk.Model.BrowserVisualExcludedRegion
Normalized rectangle relative to the active PAGE, ELEMENT, or REGION comparison canvas. Exclusions apply before pixel, SSIM, changed-region and scoped semantic comparison; URL, title, and network checks remain active. Overlaps are valid. Right/bottom overflow is clipped without moving the origin; a rectangle without in-canvas area is rejected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**XRatio** | **double** |  |
**YRatio** | **double** |  |
**WidthRatio** | **double** |  |
**HeightRatio** | **double** |  |
**Reason** | **string** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

