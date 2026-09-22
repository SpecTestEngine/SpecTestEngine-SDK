# SnapshotInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**description** | **str** |  | [optional]
**sprint** | **str** |  |
**source_batch_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**parent_snapshot_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**selection_policy** | [**SnapshotSelectionPolicy**](SnapshotSelectionPolicy.md) |  | [optional]
**batch_item_ids** | **List[UUID]** |  | [optional]
**environment** | **str** |  |
**branch_name** | **str** |  | [optional]
**backend_commit** | **str** |  | [optional]
**frontend_commit** | **str** |  | [optional]
**created_by** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.snapshot_input import SnapshotInput

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotInput from a JSON string
snapshot_input_instance = SnapshotInput.from_json(json)
# print the JSON string representation of the object
print(SnapshotInput.to_json())

# convert the object into a dict
snapshot_input_dict = snapshot_input_instance.to_dict()
# create an instance of SnapshotInput from a dict
snapshot_input_from_dict = SnapshotInput.from_dict(snapshot_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


