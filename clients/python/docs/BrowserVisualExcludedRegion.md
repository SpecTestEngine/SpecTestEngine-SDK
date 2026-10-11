# BrowserVisualExcludedRegion

Normalized rectangle relative to the active PAGE, ELEMENT, or REGION comparison canvas. Exclusions apply before pixel, SSIM, changed-region and scoped semantic comparison; URL, title, and network checks remain active. Overlaps are valid. Right/bottom overflow is clipped without moving the origin; a rectangle without in-canvas area is rejected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x_ratio** | **float** |  |
**y_ratio** | **float** |  |
**width_ratio** | **float** |  |
**height_ratio** | **float** |  |
**reason** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.browser_visual_excluded_region import BrowserVisualExcludedRegion

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserVisualExcludedRegion from a JSON string
browser_visual_excluded_region_instance = BrowserVisualExcludedRegion.from_json(json)
# print the JSON string representation of the object
print(BrowserVisualExcludedRegion.to_json())

# convert the object into a dict
browser_visual_excluded_region_dict = browser_visual_excluded_region_instance.to_dict()
# create an instance of BrowserVisualExcludedRegion from a dict
browser_visual_excluded_region_from_dict = BrowserVisualExcludedRegion.from_dict(browser_visual_excluded_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
