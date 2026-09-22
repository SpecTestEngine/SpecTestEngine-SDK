# AtfValidationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **str** |  |
**export_mode** | **str** |  |
**build_tool** | **str** |  |
**validation_passed** | **bool** |  |
**suggested_command** | **str** |  |
**steps** | [**List[AtfValidationStep]**](AtfValidationStep.md) |  |

## Example

```python
from spectestengine_sdk.models.atf_validation_result import AtfValidationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AtfValidationResult from a JSON string
atf_validation_result_instance = AtfValidationResult.from_json(json)
# print the JSON string representation of the object
print(AtfValidationResult.to_json())

# convert the object into a dict
atf_validation_result_dict = atf_validation_result_instance.to_dict()
# create an instance of AtfValidationResult from a dict
atf_validation_result_from_dict = AtfValidationResult.from_dict(atf_validation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


