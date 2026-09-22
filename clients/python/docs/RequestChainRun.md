# RequestChainRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**request_node_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**flow_name** | **str** |  |
**description** | **str** |  | [optional]
**overall_test_flow_status** | **str** |  |
**steps** | **List[Dict[str, object]]** |  |
**context** | **Dict[str, object]** | Values explicitly captured during this run. Workflow/global input values and secret sources are not echoed here. |
**started_at** | **datetime** |  |
**finished_at** | **datetime** |  |

## Example

```python
from spectestengine_sdk.models.request_chain_run import RequestChainRun

# TODO update the JSON string below
json = "{}"
# create an instance of RequestChainRun from a JSON string
request_chain_run_instance = RequestChainRun.from_json(json)
# print the JSON string representation of the object
print(RequestChainRun.to_json())

# convert the object into a dict
request_chain_run_dict = request_chain_run_instance.to_dict()
# create an instance of RequestChainRun from a dict
request_chain_run_from_dict = RequestChainRun.from_dict(request_chain_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


