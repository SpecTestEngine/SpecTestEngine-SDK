# Snapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**description** | **str** |  | [optional]
**sprint** | **str** |  |
**source_batch_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**parent_snapshot_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**selection_policy** | [**SnapshotSelectionPolicy**](SnapshotSelectionPolicy.md) |  |
**batch_item_ids** | **List[UUID]** |  | [optional]
**environment** | **str** |  |
**branch_name** | **str** |  | [optional]
**backend_commit** | **str** |  | [optional]
**frontend_commit** | **str** |  | [optional]
**created_by** | **str** |  | [optional]
**snapshot_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**status** | [**SnapshotStatus**](SnapshotStatus.md) |  |
**flows** | [**List[SnapshotItem]**](SnapshotItem.md) | Captured specification, UI macro, and flow evidence retained by the snapshot. |
**created_at** | **datetime** |  |
**approved_at** | **datetime** |  | [optional]

## Example

```python
from spectestengine_sdk.models.snapshot import Snapshot

# TODO update the JSON string below
json = "{}"
# create an instance of Snapshot from a JSON string
snapshot_instance = Snapshot.from_json(json)
# print the JSON string representation of the object
print(Snapshot.to_json())

# convert the object into a dict
snapshot_dict = snapshot_instance.to_dict()
# create an instance of Snapshot from a dict
snapshot_from_dict = Snapshot.from_dict(snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


