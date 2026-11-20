# BrowserNetworkExpectation

Local checks over observed browser traffic, never a second HTTP send. Candidates are not executable checks. Recorded credentials are rejected; current-run bindings are private and optional. Body and headers constrain the request; expectedBody and expectedHeaders constrain the response. Explicit empty response-header objects are checks. Unsupported OpenAPI/schema/attachment assertions are rejected, not processed by Browser.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional]
**policy** | **str** | Per-Event policy. IGNORE keeps automatic source capture active without requiring refresh presence. | [optional]
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
**expected_body_paths** | [**List[BrowserPathExpectation]**](BrowserPathExpectation.md) |  | [optional]
**expected_header_paths** | [**List[BrowserPathExpectation]**](BrowserPathExpectation.md) |  | [optional]
**stream** | [**BrowserStreamMessage**](BrowserStreamMessage.md) |  | [optional]
**candidate_body_paths** | **Dict[str, object]** |  | [optional]
**excluded_body_fields** | **List[str]** |  | [optional]
**headers** | **Dict[str, str]** | Expected request headers; values may use ${runtime.name} from a prior declared current-run response source. | [optional]
**expected_body** | **object** | Complete expected response JSON value, including explicit null; absence disables this criterion. Partial or unavailable captured bodies cannot pass. | [optional]
**skip_exact_body_check** | **bool** |  | [optional]
**exclude_all_other_body_fields** | **bool** | Include-only response-object comparison. Array include-only is unsupported in Browser. | [optional]
**occurrence** | **int** | Select this request-start occurrence within its Action and method/URL matcher. Required by guided value-transfer relations; old recorded call IDs are not replay identity. | [optional]
**request_body_paths** | [**List[BrowserPathExpectation]**](BrowserPathExpectation.md) | Focused outgoing Body checks. A complete runtime placeholder preserves the source JSON type; prefix/suffix text requires a string source. | [optional]
**candidate_fields** | [**BrowserNetworkFieldInventory**](BrowserNetworkFieldInventory.md) |  | [optional]
**auth_transfer** | [**BrowserAuthTransfer**](BrowserAuthTransfer.md) |  | [optional]
**runtime_bindings** | [**List[BrowserNetworkRuntimeBinding]**](BrowserNetworkRuntimeBinding.md) | Fresh private response sources, active independently of response assertion policy. Never contains a token value. Resume retains the same execution; full Rerun clears it. | [optional]

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
