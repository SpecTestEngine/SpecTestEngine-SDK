# FlowRecoveryOccurrence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_step_id** | **UUID** |  |
**order_index** | **int** |  |
**dependency_key** | **str** |  | [optional]
**role** | **str** |  |

## Example

```python
from spectestengine_sdk.models.flow_recovery_occurrence import FlowRecoveryOccurrence

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRecoveryOccurrence from a JSON string
flow_recovery_occurrence_instance = FlowRecoveryOccurrence.from_json(json)
# print the JSON string representation of the object
print(FlowRecoveryOccurrence.to_json())

# convert the object into a dict
flow_recovery_occurrence_dict = flow_recovery_occurrence_instance.to_dict()
# create an instance of FlowRecoveryOccurrence from a dict
flow_recovery_occurrence_from_dict = FlowRecoveryOccurrence.from_dict(flow_recovery_occurrence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
