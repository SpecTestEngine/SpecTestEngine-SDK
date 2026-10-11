# FlowRecoveryDependencyDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**FlowRecoveryDependency**](FlowRecoveryDependency.md) |  |
**definition** | [**FlowRecoveryProjection**](FlowRecoveryProjection.md) |  |

## Example

```python
from spectestengine_sdk.models.flow_recovery_dependency_detail import FlowRecoveryDependencyDetail

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRecoveryDependencyDetail from a JSON string
flow_recovery_dependency_detail_instance = FlowRecoveryDependencyDetail.from_json(json)
# print the JSON string representation of the object
print(FlowRecoveryDependencyDetail.to_json())

# convert the object into a dict
flow_recovery_dependency_detail_dict = flow_recovery_dependency_detail_instance.to_dict()
# create an instance of FlowRecoveryDependencyDetail from a dict
flow_recovery_dependency_detail_from_dict = FlowRecoveryDependencyDetail.from_dict(flow_recovery_dependency_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
