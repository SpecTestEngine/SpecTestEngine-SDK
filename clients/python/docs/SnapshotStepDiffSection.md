# SnapshotStepDiffSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added** | [**List[SnapshotStepDiffGroup]**](SnapshotStepDiffGroup.md) |  |
**removed** | [**List[SnapshotStepDiffGroup]**](SnapshotStepDiffGroup.md) |  |
**changed** | [**List[SnapshotStepDiffGroup]**](SnapshotStepDiffGroup.md) |  |

## Example

```python
from spectestengine_sdk.models.snapshot_step_diff_section import SnapshotStepDiffSection

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotStepDiffSection from a JSON string
snapshot_step_diff_section_instance = SnapshotStepDiffSection.from_json(json)
# print the JSON string representation of the object
print(SnapshotStepDiffSection.to_json())

# convert the object into a dict
snapshot_step_diff_section_dict = snapshot_step_diff_section_instance.to_dict()
# create an instance of SnapshotStepDiffSection from a dict
snapshot_step_diff_section_from_dict = SnapshotStepDiffSection.from_dict(snapshot_step_diff_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
