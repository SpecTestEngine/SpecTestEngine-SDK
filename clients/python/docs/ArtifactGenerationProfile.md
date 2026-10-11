# ArtifactGenerationProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**revision** | **int** |  |
**name** | **str** |  |
**description** | **str** |  | [optional]
**artifact_type** | **str** |  |
**selection** | [**ArtifactSelection**](ArtifactSelection.md) |  |
**atf** | [**AtfProjectConfig**](AtfProjectConfig.md) |  |
**environments** | [**List[ArtifactGenerationProfileEnvironment]**](ArtifactGenerationProfileEnvironment.md) |  |
**created_at** | **datetime** |  |
**updated_at** | **datetime** |  |

## Example

```python
from spectestengine_sdk.models.artifact_generation_profile import ArtifactGenerationProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactGenerationProfile from a JSON string
artifact_generation_profile_instance = ArtifactGenerationProfile.from_json(json)
# print the JSON string representation of the object
print(ArtifactGenerationProfile.to_json())

# convert the object into a dict
artifact_generation_profile_dict = artifact_generation_profile_instance.to_dict()
# create an instance of ArtifactGenerationProfile from a dict
artifact_generation_profile_from_dict = ArtifactGenerationProfile.from_dict(artifact_generation_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
