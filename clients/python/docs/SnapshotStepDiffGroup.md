# SnapshotStepDiffGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_key** | **str** |  |
**group_label** | **str** |  |
**items** | [**List[SnapshotStepDiffItem]**](SnapshotStepDiffItem.md) |  |

## Example

```python
from spectestengine_sdk.models.snapshot_step_diff_group import SnapshotStepDiffGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotStepDiffGroup from a JSON string
snapshot_step_diff_group_instance = SnapshotStepDiffGroup.from_json(json)
# print the JSON string representation of the object
print(SnapshotStepDiffGroup.to_json())

# convert the object into a dict
snapshot_step_diff_group_dict = snapshot_step_diff_group_instance.to_dict()
# create an instance of SnapshotStepDiffGroup from a dict
snapshot_step_diff_group_from_dict = SnapshotStepDiffGroup.from_dict(snapshot_step_diff_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


