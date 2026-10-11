# SnapshotStepDiff


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_type** | [**SnapshotStepType**](SnapshotStepType.md) |  |
**overview** | **List[str]** |  |
**definition** | [**SnapshotStepDiffSection**](SnapshotStepDiffSection.md) |  |
**behavior** | [**SnapshotStepDiffSection**](SnapshotStepDiffSection.md) |  |

## Example

```python
from spectestengine_sdk.models.snapshot_step_diff import SnapshotStepDiff

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotStepDiff from a JSON string
snapshot_step_diff_instance = SnapshotStepDiff.from_json(json)
# print the JSON string representation of the object
print(SnapshotStepDiff.to_json())

# convert the object into a dict
snapshot_step_diff_dict = snapshot_step_diff_instance.to_dict()
# create an instance of SnapshotStepDiff from a dict
snapshot_step_diff_from_dict = SnapshotStepDiff.from_dict(snapshot_step_diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
