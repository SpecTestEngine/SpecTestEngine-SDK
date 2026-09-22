# FragmentCatalogType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FragmentType**](FragmentType.md) |  |
**allowed_fields** | **List[str]** |  |
**singleton** | **bool** |  |
**editor_mode** | **str** |  |
**compatible_streaming_transports** | [**List[StreamingTransport]**](StreamingTransport.md) |  | [optional]
**starter_template** | **Dict[str, object]** |  |

## Example

```python
from spectestengine_sdk.models.fragment_catalog_type import FragmentCatalogType

# TODO update the JSON string below
json = "{}"
# create an instance of FragmentCatalogType from a JSON string
fragment_catalog_type_instance = FragmentCatalogType.from_json(json)
# print the JSON string representation of the object
print(FragmentCatalogType.to_json())

# convert the object into a dict
fragment_catalog_type_dict = fragment_catalog_type_instance.to_dict()
# create an instance of FragmentCatalogType from a dict
fragment_catalog_type_from_dict = FragmentCatalogType.from_dict(fragment_catalog_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


