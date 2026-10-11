# RunBatch


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
**batch_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**items** | [**List[RunBatchItem]**](RunBatchItem.md) |  |
**created_at** | **datetime** |  |
**finished_at** | **datetime** |  | [optional]

## Example

```python
from spectestengine_sdk.models.run_batch import RunBatch

# TODO update the JSON string below
json = "{}"
# create an instance of RunBatch from a JSON string
run_batch_instance = RunBatch.from_json(json)
# print the JSON string representation of the object
print(RunBatch.to_json())

# convert the object into a dict
run_batch_dict = run_batch_instance.to_dict()
# create an instance of RunBatch from a dict
run_batch_from_dict = RunBatch.from_dict(run_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
