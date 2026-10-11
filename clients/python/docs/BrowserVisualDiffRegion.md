# BrowserVisualDiffRegion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **int** |  |
**y** | **int** |  |
**width** | **int** |  |
**height** | **int** |  |
**diff_pixels** | **int** |  |
**left_ratio** | **float** |  |
**top_ratio** | **float** |  |
**width_ratio** | **float** |  |
**height_ratio** | **float** |  |

## Example

```python
from spectestengine_sdk.models.browser_visual_diff_region import BrowserVisualDiffRegion

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserVisualDiffRegion from a JSON string
browser_visual_diff_region_instance = BrowserVisualDiffRegion.from_json(json)
# print the JSON string representation of the object
print(BrowserVisualDiffRegion.to_json())

# convert the object into a dict
browser_visual_diff_region_dict = browser_visual_diff_region_instance.to_dict()
# create an instance of BrowserVisualDiffRegion from a dict
browser_visual_diff_region_from_dict = BrowserVisualDiffRegion.from_dict(browser_visual_diff_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
