# DocumentAssetReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**file_name** | **str** |  |
**content_type** | **str** |  |
**size_bytes** | **int** |  |
**sha256** | **str** |  |
**object_key** | **str** |  |
**field_name** | **str** |  |
**content_id** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.document_asset_reference import DocumentAssetReference

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAssetReference from a JSON string
document_asset_reference_instance = DocumentAssetReference.from_json(json)
# print the JSON string representation of the object
print(DocumentAssetReference.to_json())

# convert the object into a dict
document_asset_reference_dict = document_asset_reference_instance.to_dict()
# create an instance of DocumentAssetReference from a dict
document_asset_reference_from_dict = DocumentAssetReference.from_dict(document_asset_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
