# FlowRecoveryDependency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  |
**kind** | **str** |  |
**source_name** | **str** |  |
**format** | **str** |  |
**definition_hash** | **str** |  |
**roles** | **List[str]** |  |
**binding_count** | **int** |  |

## Example

```python
from spectestengine_sdk.models.flow_recovery_dependency import FlowRecoveryDependency

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRecoveryDependency from a JSON string
flow_recovery_dependency_instance = FlowRecoveryDependency.from_json(json)
# print the JSON string representation of the object
print(FlowRecoveryDependency.to_json())

# convert the object into a dict
flow_recovery_dependency_dict = flow_recovery_dependency_instance.to_dict()
# create an instance of FlowRecoveryDependency from a dict
flow_recovery_dependency_from_dict = FlowRecoveryDependency.from_dict(flow_recovery_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
