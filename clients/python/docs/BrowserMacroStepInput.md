# BrowserMacroStepInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_index** | **int** |  | [optional]
**action_type** | [**BrowserActionType**](BrowserActionType.md) |  |
**selector** | **str** |  | [optional]
**target_match** | [**BrowserTargetMatch**](BrowserTargetMatch.md) |  | [optional]
**selector_candidates** | **List[str]** |  | [optional]
**value** | **str** | Action value or explicit variable template. EXTRACT_TEXT captures a fresh value on every run; a later FILL uses that variable, never a recorded OTP sample. | [optional]
**sensitive** | **bool** | Explicit sensitive-action marker. Persist variable references, not secret literal values. | [optional]
**timeout_ms** | **int** |  | [optional] [default to 20000]
**tab_alias** | **str** |  | [optional]
**frame_selector** | **str** |  | [optional]
**variable_name** | **str** |  | [optional]
**pattern** | **str** |  | [optional]
**extraction_hint** | **str** |  | [optional]
**text_source** | **str** |  | [optional]
**expected_page_url** | **str** |  | [optional]
**expected_page_url_policy** | **str** |  | [optional]
**expected_page_title** | **str** |  | [optional]
**expected_page_title_policy** | **str** |  | [optional]
**expected_network_policy** | **str** |  | [optional]
**expected_network_calls** | [**List[BrowserNetworkExpectation]**](BrowserNetworkExpectation.md) |  | [optional]
**visual_assertion** | [**BrowserVisualAssertionInput**](BrowserVisualAssertionInput.md) |  | [optional]
**page_id** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.browser_macro_step_input import BrowserMacroStepInput

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserMacroStepInput from a JSON string
browser_macro_step_input_instance = BrowserMacroStepInput.from_json(json)
# print the JSON string representation of the object
print(BrowserMacroStepInput.to_json())

# convert the object into a dict
browser_macro_step_input_dict = browser_macro_step_input_instance.to_dict()
# create an instance of BrowserMacroStepInput from a dict
browser_macro_step_input_from_dict = BrowserMacroStepInput.from_dict(browser_macro_step_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
