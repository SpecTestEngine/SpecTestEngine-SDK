# FragmentPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |
**items** | [**List[Fragment]**](Fragment.md) |  |

## Example

```python
from spectestengine_sdk.models.fragment_page import FragmentPage

# TODO update the JSON string below
json = "{}"
# create an instance of FragmentPage from a JSON string
fragment_page_instance = FragmentPage.from_json(json)
# print the JSON string representation of the object
print(FragmentPage.to_json())

# convert the object into a dict
fragment_page_dict = fragment_page_instance.to_dict()
# create an instance of FragmentPage from a dict
fragment_page_from_dict = FragmentPage.from_dict(fragment_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
