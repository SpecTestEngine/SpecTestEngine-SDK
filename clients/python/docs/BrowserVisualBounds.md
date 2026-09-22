# BrowserVisualBounds

Normalized capture rectangle in page coordinates for REGION scope. Excluded regions are relative to the resulting cropped canvas, not to these page coordinates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_ratio** | **float** |  | [optional]
**top_ratio** | **float** |  | [optional]
**width_ratio** | **float** |  | [optional]
**height_ratio** | **float** |  | [optional]

## Example

```python
from spectestengine_sdk.models.browser_visual_bounds import BrowserVisualBounds

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserVisualBounds from a JSON string
browser_visual_bounds_instance = BrowserVisualBounds.from_json(json)
# print the JSON string representation of the object
print(BrowserVisualBounds.to_json())

# convert the object into a dict
browser_visual_bounds_dict = browser_visual_bounds_instance.to_dict()
# create an instance of BrowserVisualBounds from a dict
browser_visual_bounds_from_dict = BrowserVisualBounds.from_dict(browser_visual_bounds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


