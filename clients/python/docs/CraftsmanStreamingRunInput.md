# CraftsmanStreamingRunInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional]
**streaming_spec** | [**StreamingDefinition**](StreamingDefinition.md) |  |

## Example

```python
from spectestengine_sdk.models.craftsman_streaming_run_input import CraftsmanStreamingRunInput

# TODO update the JSON string below
json = "{}"
# create an instance of CraftsmanStreamingRunInput from a JSON string
craftsman_streaming_run_input_instance = CraftsmanStreamingRunInput.from_json(json)
# print the JSON string representation of the object
print(CraftsmanStreamingRunInput.to_json())

# convert the object into a dict
craftsman_streaming_run_input_dict = craftsman_streaming_run_input_instance.to_dict()
# create an instance of CraftsmanStreamingRunInput from a dict
craftsman_streaming_run_input_from_dict = CraftsmanStreamingRunInput.from_dict(craftsman_streaming_run_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
