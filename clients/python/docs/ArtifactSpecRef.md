# ArtifactSpecRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**spec_type** | **str** | Selects the owning engine used to resolve this specification. Streaming specifications are not currently representable by the HTTP ATF runtime and must fail through the compatibility policy. |

## Example

```python
from spectestengine_sdk.models.artifact_spec_ref import ArtifactSpecRef

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactSpecRef from a JSON string
artifact_spec_ref_instance = ArtifactSpecRef.from_json(json)
# print the JSON string representation of the object
print(ArtifactSpecRef.to_json())

# convert the object into a dict
artifact_spec_ref_dict = artifact_spec_ref_instance.to_dict()
# create an instance of ArtifactSpecRef from a dict
artifact_spec_ref_from_dict = ArtifactSpecRef.from_dict(artifact_spec_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


