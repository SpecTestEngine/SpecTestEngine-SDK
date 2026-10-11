# BrowserNetworkExpectation

Approved expectations and recorded candidates are separate. Body/path values remain typed JSON; exclusions affect network validation only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional]
**recorded_call_id** | **int** |  | [optional]
**recorded_url** | **str** |  | [optional]
**method** | **str** |  | [optional]
**url** | **str** |  | [optional]
**expected_status_code** | **int** |  | [optional]
**candidate_status_code** | **int** |  | [optional]
**expected_content_type** | **str** |  | [optional]
**candidate_content_type** | **str** |  | [optional]
**expected_headers** | **Dict[str, str]** |  | [optional]
**candidate_headers** | **Dict[str, str]** |  | [optional]
**excluded_header_fields** | **List[str]** |  | [optional]
**exclude_all_other_header_fields** | **bool** |  | [optional]
**body** | **object** |  | [optional]
**candidate_body** | **object** |  | [optional]
**expected_body_paths** | **List[Dict[str, object]]** |  | [optional]
**candidate_body_paths** | **Dict[str, object]** |  | [optional]
**excluded_body_fields** | **List[str]** |  | [optional]

## Example

```python
from spectestengine_sdk.models.browser_network_expectation import BrowserNetworkExpectation

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserNetworkExpectation from a JSON string
browser_network_expectation_instance = BrowserNetworkExpectation.from_json(json)
# print the JSON string representation of the object
print(BrowserNetworkExpectation.to_json())

# convert the object into a dict
browser_network_expectation_dict = browser_network_expectation_instance.to_dict()
# create an instance of BrowserNetworkExpectation from a dict
browser_network_expectation_from_dict = BrowserNetworkExpectation.from_dict(browser_network_expectation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
