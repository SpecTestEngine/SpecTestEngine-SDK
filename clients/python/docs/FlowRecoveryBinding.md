# FlowRecoveryBinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  |
**label** | **str** |  | [optional]
**path** | **str** | JSON Pointer in the safe authoring definition. |
**value_type** | **str** |  |

## Example

```python
from spectestengine_sdk.models.flow_recovery_binding import FlowRecoveryBinding

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRecoveryBinding from a JSON string
flow_recovery_binding_instance = FlowRecoveryBinding.from_json(json)
# print the JSON string representation of the object
print(FlowRecoveryBinding.to_json())

# convert the object into a dict
flow_recovery_binding_dict = flow_recovery_binding_instance.to_dict()
# create an instance of FlowRecoveryBinding from a dict
flow_recovery_binding_from_dict = FlowRecoveryBinding.from_dict(flow_recovery_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
