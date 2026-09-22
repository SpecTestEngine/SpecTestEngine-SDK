# CompiledSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | [**ContentFormat**](ContentFormat.md) |  | [default to ContentFormat.JSON]
**raw_spec** | **str** |  |
**compiled_spec** | **Dict[str, object]** |  |

## Example

```python
from spectestengine_sdk.models.compiled_specification import CompiledSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of CompiledSpecification from a JSON string
compiled_specification_instance = CompiledSpecification.from_json(json)
# print the JSON string representation of the object
print(CompiledSpecification.to_json())

# convert the object into a dict
compiled_specification_dict = compiled_specification_instance.to_dict()
# create an instance of CompiledSpecification from a dict
compiled_specification_from_dict = CompiledSpecification.from_dict(compiled_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


