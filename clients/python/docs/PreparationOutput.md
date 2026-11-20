# PreparationOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | JSON Pointer into the native response surface (REST body, GraphQL envelope, namespace-local SOAP projection, or Streaming events) |
**type** | **str** |  | [optional]
**required** | **bool** |  | [default to True]

## Example

```python
from spectestengine_sdk.models.preparation_output import PreparationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of PreparationOutput from a JSON string
preparation_output_instance = PreparationOutput.from_json(json)
# print the JSON string representation of the object
print(PreparationOutput.to_json())

# convert the object into a dict
preparation_output_dict = preparation_output_instance.to_dict()
# create an instance of PreparationOutput from a dict
preparation_output_from_dict = PreparationOutput.from_dict(preparation_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
