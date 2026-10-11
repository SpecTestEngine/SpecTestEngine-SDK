# ArtifactGenerationProfileEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_key** | **str** |  |
**resolution_mode** | **str** |  |
**base_url_mode** | [**AtfBaseUrlMode**](AtfBaseUrlMode.md) |  | [optional]
**base_url_variable_name** | **str** |  | [optional]
**snapshot_bundle_hash** | **str** |  | [optional]
**snapshot_at** | **datetime** |  | [optional]
**cached_bundle_hash** | **str** |  | [optional]
**cached_at** | **datetime** |  | [optional]

## Example

```python
from spectestengine_sdk.models.artifact_generation_profile_environment import ArtifactGenerationProfileEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactGenerationProfileEnvironment from a JSON string
artifact_generation_profile_environment_instance = ArtifactGenerationProfileEnvironment.from_json(json)
# print the JSON string representation of the object
print(ArtifactGenerationProfileEnvironment.to_json())

# convert the object into a dict
artifact_generation_profile_environment_dict = artifact_generation_profile_environment_instance.to_dict()
# create an instance of ArtifactGenerationProfileEnvironment from a dict
artifact_generation_profile_environment_from_dict = ArtifactGenerationProfileEnvironment.from_dict(artifact_generation_profile_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
