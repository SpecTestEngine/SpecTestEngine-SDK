# FlowStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**order_index** | **int** |  |
**flow_name** | **str** |  | [optional]
**step_type** | **str** |  |
**spec_id** | **UUID** |  | [optional]
**spec_type** | [**SpecType**](SpecType.md) |  | [optional]
**spec_name** | **str** |  | [optional]
**ui_macro_id** | **UUID** |  | [optional]
**ui_macro_name** | **str** |  | [optional]
**browser_action_type** | [**BrowserActionType**](BrowserActionType.md) |  | [optional]
**selector** | **str** |  | [optional]
**selector_candidates** | **List[str]** |  | [optional]
**value** | **str** |  | [optional]
**variable_name** | **str** |  | [optional]
**tab_alias** | **str** |  | [optional]
**frame_selector** | **str** |  | [optional]
**pattern** | **str** |  | [optional]
**extraction_hint** | **str** |  | [optional]
**text_source** | **str** |  | [optional]
**expected_page_url** | **str** |  | [optional]
**expected_page_url_policy** | **str** |  | [optional]
**expected_page_title** | **str** |  | [optional]
**expected_page_title_policy** | **str** |  | [optional]
**expected_network_policy** | **str** |  | [optional]
**visual_assertion** | [**BrowserVisualAssertion**](BrowserVisualAssertion.md) |  | [optional]
**expected_network_calls** | [**List[BrowserNetworkExpectation]**](BrowserNetworkExpectation.md) |  | [optional]
**store_values** | **Dict[str, str]** |  | [optional]
**override_values** | **Dict[str, object]** |  | [optional]

## Example

```python
from spectestengine_sdk.models.flow_step import FlowStep

# TODO update the JSON string below
json = "{}"
# create an instance of FlowStep from a JSON string
flow_step_instance = FlowStep.from_json(json)
# print the JSON string representation of the object
print(FlowStep.to_json())

# convert the object into a dict
flow_step_dict = flow_step_instance.to_dict()
# create an instance of FlowStep from a dict
flow_step_from_dict = FlowStep.from_dict(flow_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
