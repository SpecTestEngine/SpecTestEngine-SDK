# FlowRunStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**order_index** | **int** |  |
**step_type** | **str** |  |
**spec_name** | **str** |  | [optional]
**ui_macro_id** | **UUID** |  | [optional]
**ui_macro_name** | **str** |  | [optional]
**ui_macro_run_id** | **UUID** |  | [optional]
**browser_action_type** | [**BrowserActionType**](BrowserActionType.md) |  | [optional]
**selector** | **str** |  | [optional]
**value** | **str** |  | [optional]
**variable_name** | **str** |  | [optional]
**browser_page_url** | **str** |  | [optional]
**browser_page_title** | **str** |  | [optional]
**browser_failure_code** | **str** |  | [optional]
**browser_failure_message** | **str** |  | [optional]
**visual_comparison** | [**BrowserVisualComparisonSummary**](BrowserVisualComparisonSummary.md) |  | [optional]
**step_status** | **str** |  |
**ui_macro_failure_code** | **str** |  | [optional]
**ui_macro_failure_message** | **str** |  | [optional]
**test_step_run** | **Dict[str, object]** | Engine-native specification result; Browser steps do not fabricate an API result. | [optional]

## Example

```python
from spectestengine_sdk.models.flow_run_step import FlowRunStep

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRunStep from a JSON string
flow_run_step_instance = FlowRunStep.from_json(json)
# print the JSON string representation of the object
print(FlowRunStep.to_json())

# convert the object into a dict
flow_run_step_dict = flow_run_step_instance.to_dict()
# create an instance of FlowRunStep from a dict
flow_run_step_from_dict = FlowRunStep.from_dict(flow_run_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


