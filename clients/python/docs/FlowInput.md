# FlowInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**description** | **str** |  | [optional]
**steps** | [**List[FlowStepInput]**](FlowStepInput.md) |  |
**global_variable_fallbacks** | **Dict[str, str]** |  | [optional]
**browser_session** | [**BrowserSessionInput**](BrowserSessionInput.md) |  | [optional]

## Example

```python
from spectestengine_sdk.models.flow_input import FlowInput

# TODO update the JSON string below
json = "{}"
# create an instance of FlowInput from a JSON string
flow_input_instance = FlowInput.from_json(json)
# print the JSON string representation of the object
print(FlowInput.to_json())

# convert the object into a dict
flow_input_dict = flow_input_instance.to_dict()
# create an instance of FlowInput from a dict
flow_input_from_dict = FlowInput.from_dict(flow_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
