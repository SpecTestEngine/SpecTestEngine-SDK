# BrowserMacroInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**description** | **str** |  | [optional]
**start_url** | **str** |  |
**viewport_width** | **int** |  | [optional]
**viewport_height** | **int** |  | [optional]
**steps** | [**List[BrowserMacroStepInput]**](BrowserMacroStepInput.md) |  |

## Example

```python
from spectestengine_sdk.models.browser_macro_input import BrowserMacroInput

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserMacroInput from a JSON string
browser_macro_input_instance = BrowserMacroInput.from_json(json)
# print the JSON string representation of the object
print(BrowserMacroInput.to_json())

# convert the object into a dict
browser_macro_input_dict = browser_macro_input_instance.to_dict()
# create an instance of BrowserMacroInput from a dict
browser_macro_input_from_dict = BrowserMacroInput.from_dict(browser_macro_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
