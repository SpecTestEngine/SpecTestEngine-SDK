# PageMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |

## Example

```python
from spectestengine_sdk.models.page_metadata import PageMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PageMetadata from a JSON string
page_metadata_instance = PageMetadata.from_json(json)
# print the JSON string representation of the object
print(PageMetadata.to_json())

# convert the object into a dict
page_metadata_dict = page_metadata_instance.to_dict()
# create an instance of PageMetadata from a dict
page_metadata_from_dict = PageMetadata.from_dict(page_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
