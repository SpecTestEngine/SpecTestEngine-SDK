# RequestWorkspaceInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**description** | **str** |  | [optional]
**variables** | **Dict[str, str]** |  | [optional]
**global_variable_fallbacks** | **Dict[str, str]** |  | [optional]

## Example

```python
from spectestengine_sdk.models.request_workspace_input import RequestWorkspaceInput

# TODO update the JSON string below
json = "{}"
# create an instance of RequestWorkspaceInput from a JSON string
request_workspace_input_instance = RequestWorkspaceInput.from_json(json)
# print the JSON string representation of the object
print(RequestWorkspaceInput.to_json())

# convert the object into a dict
request_workspace_input_dict = request_workspace_input_instance.to_dict()
# create an instance of RequestWorkspaceInput from a dict
request_workspace_input_from_dict = RequestWorkspaceInput.from_dict(request_workspace_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


