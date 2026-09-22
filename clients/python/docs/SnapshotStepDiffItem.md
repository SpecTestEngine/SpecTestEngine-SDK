# SnapshotStepDiffItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  |
**label** | **str** |  |
**left_value** | **object** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**right_value** | **object** | A JSON value whose shape depends on the captured test subject and step type. | [optional]

## Example

```python
from spectestengine_sdk.models.snapshot_step_diff_item import SnapshotStepDiffItem

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotStepDiffItem from a JSON string
snapshot_step_diff_item_instance = SnapshotStepDiffItem.from_json(json)
# print the JSON string representation of the object
print(SnapshotStepDiffItem.to_json())

# convert the object into a dict
snapshot_step_diff_item_dict = snapshot_step_diff_item_instance.to_dict()
# create an instance of SnapshotStepDiffItem from a dict
snapshot_step_diff_item_from_dict = SnapshotStepDiffItem.from_dict(snapshot_step_diff_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


