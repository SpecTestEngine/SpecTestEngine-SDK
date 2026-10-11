# SpecificationRunPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |
**items** | [**List[SpecificationRunSummary]**](SpecificationRunSummary.md) |  |

## Example

```python
from spectestengine_sdk.models.specification_run_page import SpecificationRunPage

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationRunPage from a JSON string
specification_run_page_instance = SpecificationRunPage.from_json(json)
# print the JSON string representation of the object
print(SpecificationRunPage.to_json())

# convert the object into a dict
specification_run_page_dict = specification_run_page_instance.to_dict()
# create an instance of SpecificationRunPage from a dict
specification_run_page_from_dict = SpecificationRunPage.from_dict(specification_run_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
