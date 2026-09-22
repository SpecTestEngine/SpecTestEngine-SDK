# FragmentInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**description** | **str** |  | [optional]
**spec_type** | [**SpecType**](SpecType.md) |  |
**streaming_transport** | [**StreamingTransport**](StreamingTransport.md) |  | [optional]
**type** | [**FragmentType**](FragmentType.md) |  |
**content** | **Dict[str, object]** |  |

## Example

```python
from spectestengine_sdk.models.fragment_input import FragmentInput

# TODO update the JSON string below
json = "{}"
# create an instance of FragmentInput from a JSON string
fragment_input_instance = FragmentInput.from_json(json)
# print the JSON string representation of the object
print(FragmentInput.to_json())

# convert the object into a dict
fragment_input_dict = fragment_input_instance.to_dict()
# create an instance of FragmentInput from a dict
fragment_input_from_dict = FragmentInput.from_dict(fragment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


