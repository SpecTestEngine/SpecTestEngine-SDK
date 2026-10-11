# ArtifactSelection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specs** | [**List[ArtifactSpecRef]**](ArtifactSpecRef.md) |  |
**flow_ids** | **List[UUID]** |  |
**ui_macro_ids** | **List[UUID]** |  |

## Example

```python
from spectestengine_sdk.models.artifact_selection import ArtifactSelection

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactSelection from a JSON string
artifact_selection_instance = ArtifactSelection.from_json(json)
# print the JSON string representation of the object
print(ArtifactSelection.to_json())

# convert the object into a dict
artifact_selection_dict = artifact_selection_instance.to_dict()
# create an instance of ArtifactSelection from a dict
artifact_selection_from_dict = ArtifactSelection.from_dict(artifact_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
