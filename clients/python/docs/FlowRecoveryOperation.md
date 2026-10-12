# FlowRecoveryOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **UUID** |  |
**state** | **str** |  |
**mode** | **str** |  | [optional]
**flow_id** | **UUID** |  | [optional]
**failure_code** | **str** |  | [optional]
**idempotency_key** | **UUID** |  |
**name** | **str** |  |
**description** | **str** |  | [optional]
**manifest_hash** | **str** |  |
**copied_dependencies** | **int** |  |
**total_dependencies** | **int** |  |

## Example

```python
from spectestengine_sdk.models.flow_recovery_operation import FlowRecoveryOperation

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRecoveryOperation from a JSON string
flow_recovery_operation_instance = FlowRecoveryOperation.from_json(json)
# print the JSON string representation of the object
print(FlowRecoveryOperation.to_json())

# convert the object into a dict
flow_recovery_operation_dict = flow_recovery_operation_instance.to_dict()
# create an instance of FlowRecoveryOperation from a dict
flow_recovery_operation_from_dict = FlowRecoveryOperation.from_dict(flow_recovery_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
