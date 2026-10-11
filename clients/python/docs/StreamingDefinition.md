# StreamingDefinition

Executable SpecTestEngine-like bounded Streaming DSL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stream** | [**StreamingDefinitionStream**](StreamingDefinitionStream.md) |  |
**expected_connection** | **Dict[str, object]** |  | [optional]
**expected_stream** | **Dict[str, object]** |  | [optional]
**expected_termination** | **Dict[str, object]** |  | [optional]
**exclusions** | **List[str]** |  | [optional]
**redactions** | **List[str]** |  | [optional]
**observation_only** | **bool** |  | [optional] [default to False]

## Example

```python
from spectestengine_sdk.models.streaming_definition import StreamingDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingDefinition from a JSON string
streaming_definition_instance = StreamingDefinition.from_json(json)
# print the JSON string representation of the object
print(StreamingDefinition.to_json())

# convert the object into a dict
streaming_definition_dict = streaming_definition_instance.to_dict()
# create an instance of StreamingDefinition from a dict
streaming_definition_from_dict = StreamingDefinition.from_dict(streaming_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
