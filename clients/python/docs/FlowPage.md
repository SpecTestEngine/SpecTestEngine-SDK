# FlowPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |
**items** | [**List[FlowSummary]**](FlowSummary.md) |  |

## Example

```python
from spectestengine_sdk.models.flow_page import FlowPage

# TODO update the JSON string below
json = "{}"
# create an instance of FlowPage from a JSON string
flow_page_instance = FlowPage.from_json(json)
# print the JSON string representation of the object
print(FlowPage.to_json())

# convert the object into a dict
flow_page_dict = flow_page_instance.to_dict()
# create an instance of FlowPage from a dict
flow_page_from_dict = FlowPage.from_dict(flow_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
