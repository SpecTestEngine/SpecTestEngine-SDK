# BrowserVisualAssertionInput

Saved visual assertion. The existing Java comparator and thresholds are unchanged. Baseline images are raw captures, never WebRTC video frames. Omitted exclusions mean an empty list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional]
**name** | **str** |  | [optional]
**scope_type** | [**BrowserVisualScopeType**](BrowserVisualScopeType.md) |  | [optional]
**compare_mode** | [**BrowserVisualCompareMode**](BrowserVisualCompareMode.md) |  | [optional]
**stop_policy** | [**BrowserVisualStopPolicy**](BrowserVisualStopPolicy.md) |  | [optional]
**max_diff_pixels** | **int** |  | [optional]
**max_diff_pixel_ratio** | **float** |  | [optional]
**color_threshold** | **float** |  | [optional]
**move_tolerance_px** | **float** |  | [optional]
**bounds** | [**BrowserVisualBounds**](BrowserVisualBounds.md) |  | [optional]
**excluded_regions** | [**List[BrowserVisualExcludedRegion]**](BrowserVisualExcludedRegion.md) |  | [optional]
**baseline_screenshot_base64** | **bytes** | Raw baseline capture supplied during authoring; omitted from saved definition reads. | [optional]
**baseline_semantic_json** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.browser_visual_assertion_input import BrowserVisualAssertionInput

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserVisualAssertionInput from a JSON string
browser_visual_assertion_input_instance = BrowserVisualAssertionInput.from_json(json)
# print the JSON string representation of the object
print(BrowserVisualAssertionInput.to_json())

# convert the object into a dict
browser_visual_assertion_input_dict = browser_visual_assertion_input_instance.to_dict()
# create an instance of BrowserVisualAssertionInput from a dict
browser_visual_assertion_input_from_dict = BrowserVisualAssertionInput.from_dict(browser_visual_assertion_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


