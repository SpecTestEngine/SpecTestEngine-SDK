# BrowserAuthTransfer

Metadata only. Initial sources are Action-bound; renewal sources are run-bound and require an exact current-run private input. No token values or public initial-variable seeds are accepted. Resolve Recorder ambiguity before saving.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | [**List[BrowserAuthSource]**](BrowserAuthSource.md) |  | [optional]
**authorization_variable** | **str** |  | [optional]
**candidates** | **List[object]** |  | [optional]
**optional_refresh** | **bool** |  | [optional] [default to False]
**choice_id** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.browser_auth_transfer import BrowserAuthTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserAuthTransfer from a JSON string
browser_auth_transfer_instance = BrowserAuthTransfer.from_json(json)
# print the JSON string representation of the object
print(BrowserAuthTransfer.to_json())

# convert the object into a dict
browser_auth_transfer_dict = browser_auth_transfer_instance.to_dict()
# create an instance of BrowserAuthTransfer from a dict
browser_auth_transfer_from_dict = BrowserAuthTransfer.from_dict(browser_auth_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
