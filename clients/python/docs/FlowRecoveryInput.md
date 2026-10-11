# FlowRecoveryInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manifest_hash** | **str** |  |
**name** | **str** |  |
**description** | **str** |  | [optional]
**bindings** | **Dict[str, object]** | Exactly the binding keys requested by preview. Values must be scalar strings, numbers or booleans with their declared type, or variable placeholders; nested objects and null are rejected. Total encoded bindings at most 4 MiB. Values are not retained in the operation journal. |

## Example

```python
from spectestengine_sdk.models.flow_recovery_input import FlowRecoveryInput

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRecoveryInput from a JSON string
flow_recovery_input_instance = FlowRecoveryInput.from_json(json)
# print the JSON string representation of the object
print(FlowRecoveryInput.to_json())

# convert the object into a dict
flow_recovery_input_dict = flow_recovery_input_instance.to_dict()
# create an instance of FlowRecoveryInput from a dict
flow_recovery_input_from_dict = FlowRecoveryInput.from_dict(flow_recovery_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
