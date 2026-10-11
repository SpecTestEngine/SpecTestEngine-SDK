# OpenApiGenerationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_api_url** | **str** |  | [optional]
**generated_specs_count** | **int** |  |
**generated_specs** | **List[Dict[str, object]]** |  |
**include_negative_tests** | **bool** |  |
**generate_flow_scenarios** | **bool** |  |
**generated_flow_scenarios_count** | **int** |  | [optional]
**generated_flow_scenarios** | [**List[FlowInput]**](FlowInput.md) |  | [optional]
**coverage** | **Dict[str, object]** |  | [optional]

## Example

```python
from spectestengine_sdk.models.open_api_generation_result import OpenApiGenerationResult

# TODO update the JSON string below
json = "{}"
# create an instance of OpenApiGenerationResult from a JSON string
open_api_generation_result_instance = OpenApiGenerationResult.from_json(json)
# print the JSON string representation of the object
print(OpenApiGenerationResult.to_json())

# convert the object into a dict
open_api_generation_result_dict = open_api_generation_result_instance.to_dict()
# create an instance of OpenApiGenerationResult from a dict
open_api_generation_result_from_dict = OpenApiGenerationResult.from_dict(open_api_generation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
