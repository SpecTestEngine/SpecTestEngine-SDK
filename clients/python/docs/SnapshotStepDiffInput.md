# SnapshotStepDiffInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_type** | [**SnapshotStepType**](SnapshotStepType.md) |  |
**left_definition_payload** | **object** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**right_definition_payload** | **object** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**left_behavior_payload** | **object** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**right_behavior_payload** | **object** | A JSON value whose shape depends on the captured test subject and step type. | [optional]

## Example

```python
from spectestengine_sdk.models.snapshot_step_diff_input import SnapshotStepDiffInput

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotStepDiffInput from a JSON string
snapshot_step_diff_input_instance = SnapshotStepDiffInput.from_json(json)
# print the JSON string representation of the object
print(SnapshotStepDiffInput.to_json())

# convert the object into a dict
snapshot_step_diff_input_dict = snapshot_step_diff_input_instance.to_dict()
# create an instance of SnapshotStepDiffInput from a dict
snapshot_step_diff_input_from_dict = SnapshotStepDiffInput.from_dict(snapshot_step_diff_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


