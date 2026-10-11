# StreamingDefinitionStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport** | [**StreamingTransport**](StreamingTransport.md) |  |
**endpoint** | **str** |  |
**connection** | **Dict[str, object]** |  | [optional]
**steps** | **List[Dict[str, object]]** |  | [optional]

## Example

```python
from spectestengine_sdk.models.streaming_definition_stream import StreamingDefinitionStream

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingDefinitionStream from a JSON string
streaming_definition_stream_instance = StreamingDefinitionStream.from_json(json)
# print the JSON string representation of the object
print(StreamingDefinitionStream.to_json())

# convert the object into a dict
streaming_definition_stream_dict = streaming_definition_stream_instance.to_dict()
# create an instance of StreamingDefinitionStream from a dict
streaming_definition_stream_from_dict = StreamingDefinitionStream.from_dict(streaming_definition_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
