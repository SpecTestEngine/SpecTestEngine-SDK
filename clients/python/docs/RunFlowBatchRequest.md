# RunFlowBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_ids** | **List[UUID]** |  |

## Example

```python
from spectestengine_sdk.models.run_flow_batch_request import RunFlowBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunFlowBatchRequest from a JSON string
run_flow_batch_request_instance = RunFlowBatchRequest.from_json(json)
# print the JSON string representation of the object
print(RunFlowBatchRequest.to_json())

# convert the object into a dict
run_flow_batch_request_dict = run_flow_batch_request_instance.to_dict()
# create an instance of RunFlowBatchRequest from a dict
run_flow_batch_request_from_dict = RunFlowBatchRequest.from_dict(run_flow_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


