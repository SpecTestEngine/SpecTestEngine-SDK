# RequestWorkspacePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |
**items** | [**List[RequestWorkspace]**](RequestWorkspace.md) |  |

## Example

```python
from spectestengine_sdk.models.request_workspace_page import RequestWorkspacePage

# TODO update the JSON string below
json = "{}"
# create an instance of RequestWorkspacePage from a JSON string
request_workspace_page_instance = RequestWorkspacePage.from_json(json)
# print the JSON string representation of the object
print(RequestWorkspacePage.to_json())

# convert the object into a dict
request_workspace_page_dict = request_workspace_page_instance.to_dict()
# create an instance of RequestWorkspacePage from a dict
request_workspace_page_from_dict = RequestWorkspacePage.from_dict(request_workspace_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
