# FragmentCatalog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec_type** | [**SpecType**](SpecType.md) |  |
**streaming_transport** | [**StreamingTransport**](StreamingTransport.md) |  | [optional]
**types** | [**List[FragmentCatalogType]**](FragmentCatalogType.md) |  |

## Example

```python
from spectestengine_sdk.models.fragment_catalog import FragmentCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of FragmentCatalog from a JSON string
fragment_catalog_instance = FragmentCatalog.from_json(json)
# print the JSON string representation of the object
print(FragmentCatalog.to_json())

# convert the object into a dict
fragment_catalog_dict = fragment_catalog_instance.to_dict()
# create an instance of FragmentCatalog from a dict
fragment_catalog_from_dict = FragmentCatalog.from_dict(fragment_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
