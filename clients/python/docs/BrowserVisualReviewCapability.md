# BrowserVisualReviewCapability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** |  |
**state** | **str** |  |
**disabled_reason** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.browser_visual_review_capability import BrowserVisualReviewCapability

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserVisualReviewCapability from a JSON string
browser_visual_review_capability_instance = BrowserVisualReviewCapability.from_json(json)
# print the JSON string representation of the object
print(BrowserVisualReviewCapability.to_json())

# convert the object into a dict
browser_visual_review_capability_dict = browser_visual_review_capability_instance.to_dict()
# create an instance of BrowserVisualReviewCapability from a dict
browser_visual_review_capability_from_dict = BrowserVisualReviewCapability.from_dict(browser_visual_review_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
