# BrowserAuthSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**source** | **str** |  |
**path** | **str** |  |
**scope_origin** | **str** | Exact HTTP(S) origin without credentials, path, query or fragment. |
**update_from** | [**BrowserAuthGuard**](BrowserAuthGuard.md) |  | [optional]

## Example

```python
from spectestengine_sdk.models.browser_auth_source import BrowserAuthSource

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserAuthSource from a JSON string
browser_auth_source_instance = BrowserAuthSource.from_json(json)
# print the JSON string representation of the object
print(BrowserAuthSource.to_json())

# convert the object into a dict
browser_auth_source_dict = browser_auth_source_instance.to_dict()
# create an instance of BrowserAuthSource from a dict
browser_auth_source_from_dict = BrowserAuthSource.from_dict(browser_auth_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
