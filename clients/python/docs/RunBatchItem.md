# RunBatchItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**subject_type** | [**SnapshotSubjectType**](SnapshotSubjectType.md) |  |
**subject_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**subject_key** | **str** |  |
**subject_name** | **str** |  |
**source_run_type** | [**SnapshotSourceRunType**](SnapshotSourceRunType.md) |  |
**source_run_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**status** | **str** |  |
**definition_hash** | **str** |  | [optional]
**behavior_hash** | **str** |  | [optional]
**definition_payload** | **object** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**behavior_payload** | **object** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**recorded_at** | **datetime** |  |

## Example

```python
from spectestengine_sdk.models.run_batch_item import RunBatchItem

# TODO update the JSON string below
json = "{}"
# create an instance of RunBatchItem from a JSON string
run_batch_item_instance = RunBatchItem.from_json(json)
# print the JSON string representation of the object
print(RunBatchItem.to_json())

# convert the object into a dict
run_batch_item_dict = run_batch_item_instance.to_dict()
# create an instance of RunBatchItem from a dict
run_batch_item_from_dict = RunBatchItem.from_dict(run_batch_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


