# FlowRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**flow_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**flow_name** | **str** |  |
**description** | **str** |  | [optional]
**overall_test_flow_status** | **str** |  |
**steps** | [**List[FlowRunStep]**](FlowRunStep.md) |  |
**started_at** | **datetime** |  |
**finished_at** | **datetime** |  |

## Example

```python
from spectestengine_sdk.models.flow_run import FlowRun

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRun from a JSON string
flow_run_instance = FlowRun.from_json(json)
# print the JSON string representation of the object
print(FlowRun.to_json())

# convert the object into a dict
flow_run_dict = flow_run_instance.to_dict()
# create an instance of FlowRun from a dict
flow_run_from_dict = FlowRun.from_dict(flow_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
