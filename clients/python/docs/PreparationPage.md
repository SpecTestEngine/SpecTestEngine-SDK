# PreparationPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PreparationSummary]**](PreparationSummary.md) |  |
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |

## Example

```python
from spectestengine_sdk.models.preparation_page import PreparationPage

# TODO update the JSON string below
json = "{}"
# create an instance of PreparationPage from a JSON string
preparation_page_instance = PreparationPage.from_json(json)
# print the JSON string representation of the object
print(PreparationPage.to_json())

# convert the object into a dict
preparation_page_dict = preparation_page_instance.to_dict()
# create an instance of PreparationPage from a dict
preparation_page_from_dict = PreparationPage.from_dict(preparation_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
