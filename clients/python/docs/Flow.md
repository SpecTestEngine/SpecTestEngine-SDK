# Flow

Saved Flow read model. Browser action fields are flattened on each step; create/update use FlowInput with nested browserAction instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**name** | **str** |  |
**description** | **str** |  | [optional]
**global_variable_fallbacks** | **Dict[str, str]** |  | [optional]
**browser_start_url** | **str** |  | [optional]
**browser_viewport_width** | **int** |  | [optional]
**browser_viewport_height** | **int** |  | [optional]
**browser_viewport_preset** | **str** |  | [optional]
**steps** | [**List[FlowStep]**](FlowStep.md) |  |
**created_at** | **datetime** |  |

## Example

```python
from spectestengine_sdk.models.flow import Flow

# TODO update the JSON string below
json = "{}"
# create an instance of Flow from a JSON string
flow_instance = Flow.from_json(json)
# print the JSON string representation of the object
print(Flow.to_json())

# convert the object into a dict
flow_dict = flow_instance.to_dict()
# create an instance of Flow from a dict
flow_from_dict = Flow.from_dict(flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


