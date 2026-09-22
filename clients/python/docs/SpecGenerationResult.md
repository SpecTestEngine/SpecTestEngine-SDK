# SpecGenerationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec_generation_type** | **str** |  |
**generated_spec** | **Dict[str, object]** | Complete executable REST, SOAP, GraphQL, or Streaming specification DSL. |

## Example

```python
from spectestengine_sdk.models.spec_generation_result import SpecGenerationResult

# TODO update the JSON string below
json = "{}"
# create an instance of SpecGenerationResult from a JSON string
spec_generation_result_instance = SpecGenerationResult.from_json(json)
# print the JSON string representation of the object
print(SpecGenerationResult.to_json())

# convert the object into a dict
spec_generation_result_dict = spec_generation_result_instance.to_dict()
# create an instance of SpecGenerationResult from a dict
spec_generation_result_from_dict = SpecGenerationResult.from_dict(spec_generation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


