# ArtifactGenerationProfileInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **int** | Omit when creating. Send the last returned revision when updating. | [optional]
**name** | **str** |  |
**description** | **str** |  | [optional]
**artifact_type** | **str** |  |
**selection** | [**ArtifactSelection**](ArtifactSelection.md) |  |
**atf** | [**AtfProjectConfig**](AtfProjectConfig.md) |  |
**environments** | [**List[ArtifactGenerationProfileEnvironmentInput]**](ArtifactGenerationProfileEnvironmentInput.md) |  |

## Example

```python
from spectestengine_sdk.models.artifact_generation_profile_input import ArtifactGenerationProfileInput

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactGenerationProfileInput from a JSON string
artifact_generation_profile_input_instance = ArtifactGenerationProfileInput.from_json(json)
# print the JSON string representation of the object
print(ArtifactGenerationProfileInput.to_json())

# convert the object into a dict
artifact_generation_profile_input_dict = artifact_generation_profile_input_instance.to_dict()
# create an instance of ArtifactGenerationProfileInput from a dict
artifact_generation_profile_input_from_dict = ArtifactGenerationProfileInput.from_dict(artifact_generation_profile_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


