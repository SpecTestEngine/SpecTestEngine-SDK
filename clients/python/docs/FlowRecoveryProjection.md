# FlowRecoveryProjection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition_json** | **str** | Safe authoring JSON only; no runtime values or worker grants. | [optional]
**bindings** | [**List[FlowRecoveryBinding]**](FlowRecoveryBinding.md) |  |
**unavailable_reason** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.flow_recovery_projection import FlowRecoveryProjection

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRecoveryProjection from a JSON string
flow_recovery_projection_instance = FlowRecoveryProjection.from_json(json)
# print the JSON string representation of the object
print(FlowRecoveryProjection.to_json())

# convert the object into a dict
flow_recovery_projection_dict = flow_recovery_projection_instance.to_dict()
# create an instance of FlowRecoveryProjection from a dict
flow_recovery_projection_from_dict = FlowRecoveryProjection.from_dict(flow_recovery_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
