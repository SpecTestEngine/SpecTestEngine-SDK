

# BrowserVisualExcludedRegion

Normalized rectangle relative to the active PAGE, ELEMENT, or REGION comparison canvas. Exclusions apply before pixel, SSIM, changed-region and scoped semantic comparison; URL, title, and network checks remain active. Overlaps are valid. Right/bottom overflow is clipped without moving the origin; a rectangle without in-canvas area is rejected.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**xRatio** | **Double** |  |  |
|**yRatio** | **Double** |  |  |
|**widthRatio** | **Double** |  |  |
|**heightRatio** | **Double** |  |  |
|**reason** | **String** |  |  [optional] |
