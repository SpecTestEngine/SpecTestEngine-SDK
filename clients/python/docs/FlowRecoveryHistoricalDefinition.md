# FlowRecoveryHistoricalDefinition

Read-only historical Flow, not the live Flow. Creation timestamps are not evidence of the original authoring time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **UUID** |  |
**name** | **str** |  |
**description** | **str** |  | [optional]
**global_variable_fallbacks** | **Dict[str, str]** |  | [optional]
**browser_start_url** | **str** |  | [optional]
**browser_viewport_width** | **int** |  | [optional]
**browser_viewport_height** | **int** |  | [optional]
**browser_viewport_preset** | **str** |  | [optional]
**steps** | [**List[FlowStep]**](FlowStep.md) |  |

## Example

```python
from spectestengine_sdk.models.flow_recovery_historical_definition import FlowRecoveryHistoricalDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRecoveryHistoricalDefinition from a JSON string
flow_recovery_historical_definition_instance = FlowRecoveryHistoricalDefinition.from_json(json)
# print the JSON string representation of the object
print(FlowRecoveryHistoricalDefinition.to_json())

# convert the object into a dict
flow_recovery_historical_definition_dict = flow_recovery_historical_definition_instance.to_dict()
# create an instance of FlowRecoveryHistoricalDefinition from a dict
flow_recovery_historical_definition_from_dict = FlowRecoveryHistoricalDefinition.from_dict(flow_recovery_historical_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
