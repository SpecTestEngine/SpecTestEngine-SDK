# BrowserVisualAssertion

Persisted visual definition. Revisions are server-owned; baseline bytes are fetched separately through retained artifact references.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  |
**name** | **str** |  | [optional]
**scope_type** | [**BrowserVisualScopeType**](BrowserVisualScopeType.md) |  | [optional]
**compare_mode** | [**BrowserVisualCompareMode**](BrowserVisualCompareMode.md) |  | [optional]
**stop_policy** | [**BrowserVisualStopPolicy**](BrowserVisualStopPolicy.md) |  | [optional]
**baseline_artifact_id** | **UUID** |  | [optional]
**baseline_revision_id** | **UUID** |  | [optional]
**assertion_revision** | **int** |  |
**max_diff_pixels** | **int** |  | [optional]
**max_diff_pixel_ratio** | **float** |  | [optional]
**color_threshold** | **float** |  | [optional]
**move_tolerance_px** | **float** |  | [optional]
**bounds** | [**BrowserVisualBounds**](BrowserVisualBounds.md) |  | [optional]
**excluded_regions** | [**List[BrowserVisualExcludedRegion]**](BrowserVisualExcludedRegion.md) |  |

## Example

```python
from spectestengine_sdk.models.browser_visual_assertion import BrowserVisualAssertion

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserVisualAssertion from a JSON string
browser_visual_assertion_instance = BrowserVisualAssertion.from_json(json)
# print the JSON string representation of the object
print(BrowserVisualAssertion.to_json())

# convert the object into a dict
browser_visual_assertion_dict = browser_visual_assertion_instance.to_dict()
# create an instance of BrowserVisualAssertion from a dict
browser_visual_assertion_from_dict = BrowserVisualAssertion.from_dict(browser_visual_assertion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


