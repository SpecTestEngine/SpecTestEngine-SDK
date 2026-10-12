# FlowRecoveryReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**historical** | [**FlowRecoveryPreview**](FlowRecoveryPreview.md) |  |
**target_revision** | **int** |  |
**target_name** | **str** |  | [optional]
**target_description** | **str** |  | [optional]
**dependency_revisions** | **Dict[str, int]** |  |
**occurrences** | [**List[FlowRecoveryOccurrence]**](FlowRecoveryOccurrence.md) |  |
**restore_available** | **bool** |  |
**restore_reason** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.flow_recovery_review import FlowRecoveryReview

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRecoveryReview from a JSON string
flow_recovery_review_instance = FlowRecoveryReview.from_json(json)
# print the JSON string representation of the object
print(FlowRecoveryReview.to_json())

# convert the object into a dict
flow_recovery_review_dict = flow_recovery_review_instance.to_dict()
# create an instance of FlowRecoveryReview from a dict
flow_recovery_review_from_dict = FlowRecoveryReview.from_dict(flow_recovery_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
