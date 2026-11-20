# BrowserTargetIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  |
**name** | **str** |  |

## Example

```python
from spectestengine_sdk.models.browser_target_identity import BrowserTargetIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserTargetIdentity from a JSON string
browser_target_identity_instance = BrowserTargetIdentity.from_json(json)
# print the JSON string representation of the object
print(BrowserTargetIdentity.to_json())

# convert the object into a dict
browser_target_identity_dict = browser_target_identity_instance.to_dict()
# create an instance of BrowserTargetIdentity from a dict
browser_target_identity_from_dict = BrowserTargetIdentity.from_dict(browser_target_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
