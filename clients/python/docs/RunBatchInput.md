# RunBatchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**description** | **str** |  | [optional]
**environment** | **str** |  |
**sprint** | **str** |  | [optional]
**backend_commit** | **str** |  | [optional]
**frontend_commit** | **str** |  | [optional]
**branch_name** | **str** |  | [optional]
**triggered_by** | **str** |  | [optional]
**trigger_type** | **str** |  | [optional]
**notes** | **str** |  | [optional]
**spec_run_ids** | **List[UUID]** |  | [optional]
**ui_macro_run_ids** | **List[UUID]** |  | [optional]
**flow_run_ids** | **List[UUID]** |  | [optional]

## Example

```python
from spectestengine_sdk.models.run_batch_input import RunBatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of RunBatchInput from a JSON string
run_batch_input_instance = RunBatchInput.from_json(json)
# print the JSON string representation of the object
print(RunBatchInput.to_json())

# convert the object into a dict
run_batch_input_dict = run_batch_input_instance.to_dict()
# create an instance of RunBatchInput from a dict
run_batch_input_from_dict = RunBatchInput.from_dict(run_batch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


