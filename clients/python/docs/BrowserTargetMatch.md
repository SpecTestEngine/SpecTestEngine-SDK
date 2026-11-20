# BrowserTargetMatch

Explicit selector-first role/name policy. Only DRAG accepts a destination identity. Sensitive actions cannot use this policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  |
**name** | **str** |  |
**destination** | [**BrowserTargetIdentity**](BrowserTargetIdentity.md) |  | [optional]

## Example

```python
from spectestengine_sdk.models.browser_target_match import BrowserTargetMatch

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserTargetMatch from a JSON string
browser_target_match_instance = BrowserTargetMatch.from_json(json)
# print the JSON string representation of the object
print(BrowserTargetMatch.to_json())

# convert the object into a dict
browser_target_match_dict = browser_target_match_instance.to_dict()
# create an instance of BrowserTargetMatch from a dict
browser_target_match_from_dict = BrowserTargetMatch.from_dict(browser_target_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
