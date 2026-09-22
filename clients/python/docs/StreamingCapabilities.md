# StreamingCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | **str** |  |
**storage** | **str** |  |
**formats** | **List[str]** |  |
**transports** | [**List[StreamingTransport]**](StreamingTransport.md) |  |
**schemes** | **Dict[str, List[str]]** |  |
**codecs** | **List[str]** |  |
**actions** | **List[str]** |  |
**event_assertion_fields** | **List[str]** |  |
**limits** | [**StreamingLimits**](StreamingLimits.md) |  |

## Example

```python
from spectestengine_sdk.models.streaming_capabilities import StreamingCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingCapabilities from a JSON string
streaming_capabilities_instance = StreamingCapabilities.from_json(json)
# print the JSON string representation of the object
print(StreamingCapabilities.to_json())

# convert the object into a dict
streaming_capabilities_dict = streaming_capabilities_instance.to_dict()
# create an instance of StreamingCapabilities from a dict
streaming_capabilities_from_dict = StreamingCapabilities.from_dict(streaming_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


