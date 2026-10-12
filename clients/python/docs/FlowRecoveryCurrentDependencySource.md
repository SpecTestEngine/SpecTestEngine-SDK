# FlowRecoveryCurrentDependencySource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **UUID** |  |
**revision** | **int** |  |
**name** | **str** |  |
**format** | **str** |  |
**definition** | [**FlowRecoveryProjection**](FlowRecoveryProjection.md) |  | [optional]

## Example

```python
from spectestengine_sdk.models.flow_recovery_current_dependency_source import FlowRecoveryCurrentDependencySource

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRecoveryCurrentDependencySource from a JSON string
flow_recovery_current_dependency_source_instance = FlowRecoveryCurrentDependencySource.from_json(json)
# print the JSON string representation of the object
print(FlowRecoveryCurrentDependencySource.to_json())

# convert the object into a dict
flow_recovery_current_dependency_source_dict = flow_recovery_current_dependency_source_instance.to_dict()
# create an instance of FlowRecoveryCurrentDependencySource from a dict
flow_recovery_current_dependency_source_from_dict = FlowRecoveryCurrentDependencySource.from_dict(flow_recovery_current_dependency_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
