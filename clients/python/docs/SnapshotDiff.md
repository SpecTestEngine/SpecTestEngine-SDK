# SnapshotDiff


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_snapshot_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**right_snapshot_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**batch_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**entries** | [**List[SnapshotDiffEntry]**](SnapshotDiffEntry.md) |  |
**generated_at** | **datetime** |  |

## Example

```python
from spectestengine_sdk.models.snapshot_diff import SnapshotDiff

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotDiff from a JSON string
snapshot_diff_instance = SnapshotDiff.from_json(json)
# print the JSON string representation of the object
print(SnapshotDiff.to_json())

# convert the object into a dict
snapshot_diff_dict = snapshot_diff_instance.to_dict()
# create an instance of SnapshotDiff from a dict
snapshot_diff_from_dict = SnapshotDiff.from_dict(snapshot_diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
