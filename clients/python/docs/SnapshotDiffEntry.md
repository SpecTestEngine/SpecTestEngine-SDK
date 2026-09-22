# SnapshotDiffEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_type** | [**SnapshotSubjectType**](SnapshotSubjectType.md) |  |
**subject_key** | **str** |  |
**subject_name** | **str** |  |
**change_type** | [**SnapshotDiffChangeType**](SnapshotDiffChangeType.md) |  |
**left_status** | **str** |  | [optional]
**right_status** | **str** |  | [optional]
**left_definition_hash** | **str** |  | [optional]
**right_definition_hash** | **str** |  | [optional]
**left_behavior_hash** | **str** |  | [optional]
**right_behavior_hash** | **str** |  | [optional]
**details** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.snapshot_diff_entry import SnapshotDiffEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotDiffEntry from a JSON string
snapshot_diff_entry_instance = SnapshotDiffEntry.from_json(json)
# print the JSON string representation of the object
print(SnapshotDiffEntry.to_json())

# convert the object into a dict
snapshot_diff_entry_dict = snapshot_diff_entry_instance.to_dict()
# create an instance of SnapshotDiffEntry from a dict
snapshot_diff_entry_from_dict = SnapshotDiffEntry.from_dict(snapshot_diff_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


