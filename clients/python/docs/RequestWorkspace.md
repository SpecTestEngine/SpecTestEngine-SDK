# RequestWorkspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**description** | **str** |  | [optional]
**variables** | **Dict[str, str]** |  | [optional]
**global_variable_fallbacks** | **Dict[str, str]** |  | [optional]
**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**nodes** | [**List[RequestNode]**](RequestNode.md) |  |
**created_at** | **datetime** |  |
**updated_at** | **datetime** |  |

## Example

```python
from spectestengine_sdk.models.request_workspace import RequestWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of RequestWorkspace from a JSON string
request_workspace_instance = RequestWorkspace.from_json(json)
# print the JSON string representation of the object
print(RequestWorkspace.to_json())

# convert the object into a dict
request_workspace_dict = request_workspace_instance.to_dict()
# create an instance of RequestWorkspace from a dict
request_workspace_from_dict = RequestWorkspace.from_dict(request_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
