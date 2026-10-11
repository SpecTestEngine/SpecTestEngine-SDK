# BrowserVisualReviewCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_current_as_new_baseline** | [**BrowserVisualReviewCapability**](BrowserVisualReviewCapability.md) |  |
**exclude_area_and_recompare** | [**BrowserVisualReviewCapability**](BrowserVisualReviewCapability.md) |  |
**keep_as_regression** | [**BrowserVisualReviewCapability**](BrowserVisualReviewCapability.md) |  |

## Example

```python
from spectestengine_sdk.models.browser_visual_review_capabilities import BrowserVisualReviewCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserVisualReviewCapabilities from a JSON string
browser_visual_review_capabilities_instance = BrowserVisualReviewCapabilities.from_json(json)
# print the JSON string representation of the object
print(BrowserVisualReviewCapabilities.to_json())

# convert the object into a dict
browser_visual_review_capabilities_dict = browser_visual_review_capabilities_instance.to_dict()
# create an instance of BrowserVisualReviewCapabilities from a dict
browser_visual_review_capabilities_from_dict = BrowserVisualReviewCapabilities.from_dict(browser_visual_review_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
