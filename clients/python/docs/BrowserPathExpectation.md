# BrowserPathExpectation

Exactly one of value or pattern is required. Values retain JSON types, including explicit null. Pattern is a whole-string glob with at most 32 stars; only a star or backslash can be escaped. Runtime templates are not accepted in patterns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  |
**value** | **object** | Exact JSON value, including null. Absence selects pattern matching instead. | [optional]
**pattern** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.browser_path_expectation import BrowserPathExpectation

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserPathExpectation from a JSON string
browser_path_expectation_instance = BrowserPathExpectation.from_json(json)
# print the JSON string representation of the object
print(BrowserPathExpectation.to_json())

# convert the object into a dict
browser_path_expectation_dict = browser_path_expectation_instance.to_dict()
# create an instance of BrowserPathExpectation from a dict
browser_path_expectation_from_dict = BrowserPathExpectation.from_dict(browser_path_expectation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
