# FlowStepInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_type** | **str** |  |
**order_index** | **int** |  |
**spec_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**spec_type** | [**SpecType**](SpecType.md) |  | [optional]
**spec_name** | **str** |  | [optional]
**ui_macro_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**ui_macro** | [**BrowserMacroInput**](BrowserMacroInput.md) |  | [optional]
**browser_action** | [**BrowserActionInput**](BrowserActionInput.md) |  | [optional]
**store_values** | **Dict[str, str]** |  | [optional]
**override_values** | **Dict[str, object]** |  | [optional]

## Example

```python
from spectestengine_sdk.models.flow_step_input import FlowStepInput

# TODO update the JSON string below
json = "{}"
# create an instance of FlowStepInput from a JSON string
flow_step_input_instance = FlowStepInput.from_json(json)
# print the JSON string representation of the object
print(FlowStepInput.to_json())

# convert the object into a dict
flow_step_input_dict = flow_step_input_instance.to_dict()
# create an instance of FlowStepInput from a dict
flow_step_input_from_dict = FlowStepInput.from_dict(flow_step_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


