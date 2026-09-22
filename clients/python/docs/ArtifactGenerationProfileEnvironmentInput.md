# ArtifactGenerationProfileEnvironmentInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_key** | **str** |  |
**resolution_mode** | **str** |  |
**base_url_mode** | [**AtfBaseUrlMode**](AtfBaseUrlMode.md) |  | [optional]
**base_url_variable_name** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.artifact_generation_profile_environment_input import ArtifactGenerationProfileEnvironmentInput

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactGenerationProfileEnvironmentInput from a JSON string
artifact_generation_profile_environment_input_instance = ArtifactGenerationProfileEnvironmentInput.from_json(json)
# print the JSON string representation of the object
print(ArtifactGenerationProfileEnvironmentInput.to_json())

# convert the object into a dict
artifact_generation_profile_environment_input_dict = artifact_generation_profile_environment_input_instance.to_dict()
# create an instance of ArtifactGenerationProfileEnvironmentInput from a dict
artifact_generation_profile_environment_input_from_dict = ArtifactGenerationProfileEnvironmentInput.from_dict(artifact_generation_profile_environment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


