# SnapshotItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_flow_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**source_batch_item_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
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
**created_at** | **datetime** |  |

## Example

```python
from spectestengine_sdk.models.snapshot_item import SnapshotItem

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotItem from a JSON string
snapshot_item_instance = SnapshotItem.from_json(json)
# print the JSON string representation of the object
print(SnapshotItem.to_json())

# convert the object into a dict
snapshot_item_dict = snapshot_item_instance.to_dict()
# create an instance of SnapshotItem from a dict
snapshot_item_from_dict = SnapshotItem.from_dict(snapshot_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


