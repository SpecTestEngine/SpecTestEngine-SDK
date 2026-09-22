# FlowRunSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**flow_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**flow_name** | **str** |  |
**overall_test_flow_status** | **str** |  |
**started_at** | **datetime** |  |
**finished_at** | **datetime** |  |

## Example

```python
from spectestengine_sdk.models.flow_run_summary import FlowRunSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRunSummary from a JSON string
flow_run_summary_instance = FlowRunSummary.from_json(json)
# print the JSON string representation of the object
print(FlowRunSummary.to_json())

# convert the object into a dict
flow_run_summary_dict = flow_run_summary_instance.to_dict()
# create an instance of FlowRunSummary from a dict
flow_run_summary_from_dict = FlowRunSummary.from_dict(flow_run_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


