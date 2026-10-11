# FlowRunPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |
**items** | [**List[FlowRunSummary]**](FlowRunSummary.md) |  |

## Example

```python
from spectestengine_sdk.models.flow_run_page import FlowRunPage

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRunPage from a JSON string
flow_run_page_instance = FlowRunPage.from_json(json)
# print the JSON string representation of the object
print(FlowRunPage.to_json())

# convert the object into a dict
flow_run_page_dict = flow_run_page_instance.to_dict()
# create an instance of FlowRunPage from a dict
flow_run_page_from_dict = FlowRunPage.from_dict(flow_run_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
