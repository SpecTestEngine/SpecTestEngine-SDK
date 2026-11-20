# BrowserAuthGuard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable** | **str** |  |
**source** | **str** |  |
**path** | **str** |  |
**prefix** | **str** |  |

## Example

```python
from spectestengine_sdk.models.browser_auth_guard import BrowserAuthGuard

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserAuthGuard from a JSON string
browser_auth_guard_instance = BrowserAuthGuard.from_json(json)
# print the JSON string representation of the object
print(BrowserAuthGuard.to_json())

# convert the object into a dict
browser_auth_guard_dict = browser_auth_guard_instance.to_dict()
# create an instance of BrowserAuthGuard from a dict
browser_auth_guard_from_dict = BrowserAuthGuard.from_dict(browser_auth_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
