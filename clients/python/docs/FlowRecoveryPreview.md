# FlowRecoveryPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **UUID** |  |
**available** | **bool** |  |
**reason** | **str** |  | [optional]
**manifest_version** | **int** |  |
**manifest_hash** | **str** |  | [optional]
**suggested_name** | **str** |  | [optional]
**flow** | [**FlowRecoveryHistoricalDefinition**](FlowRecoveryHistoricalDefinition.md) |  | [optional]
**step_count** | **int** |  |
**copy_count** | **int** |  |
**bindings** | [**List[FlowRecoveryBinding]**](FlowRecoveryBinding.md) |  |
**dependencies** | [**FlowRecoveryDependencyPage**](FlowRecoveryDependencyPage.md) |  |
**active_operation** | [**FlowRecoveryOperation**](FlowRecoveryOperation.md) |  | [optional]

## Example

```python
from spectestengine_sdk.models.flow_recovery_preview import FlowRecoveryPreview

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRecoveryPreview from a JSON string
flow_recovery_preview_instance = FlowRecoveryPreview.from_json(json)
# print the JSON string representation of the object
print(FlowRecoveryPreview.to_json())

# convert the object into a dict
flow_recovery_preview_dict = flow_recovery_preview_instance.to_dict()
# create an instance of FlowRecoveryPreview from a dict
flow_recovery_preview_from_dict = FlowRecoveryPreview.from_dict(flow_recovery_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
