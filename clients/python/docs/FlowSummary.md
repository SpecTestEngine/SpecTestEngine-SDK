# FlowSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**name** | **str** |  |
**description** | **str** |  | [optional]
**steps** | **List[Dict[str, object]]** |  |
**created_at** | **datetime** |  |
**updated_at** | **datetime** |  |
**last_run_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**previous_run_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**last_run_at** | **datetime** |  | [optional]
**last_run_status** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.flow_summary import FlowSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSummary from a JSON string
flow_summary_instance = FlowSummary.from_json(json)
# print the JSON string representation of the object
print(FlowSummary.to_json())

# convert the object into a dict
flow_summary_dict = flow_summary_instance.to_dict()
# create an instance of FlowSummary from a dict
flow_summary_from_dict = FlowSummary.from_dict(flow_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


