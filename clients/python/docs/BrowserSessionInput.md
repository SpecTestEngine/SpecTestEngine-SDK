# BrowserSessionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional]
**viewport_width** | **int** |  | [optional]
**viewport_height** | **int** |  | [optional]
**viewport_preset** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.browser_session_input import BrowserSessionInput

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserSessionInput from a JSON string
browser_session_input_instance = BrowserSessionInput.from_json(json)
# print the JSON string representation of the object
print(BrowserSessionInput.to_json())

# convert the object into a dict
browser_session_input_dict = browser_session_input_instance.to_dict()
# create an instance of BrowserSessionInput from a dict
browser_session_input_from_dict = BrowserSessionInput.from_dict(browser_session_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
