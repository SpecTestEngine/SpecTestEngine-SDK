# AtfGenerationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **str** |  |
**target_framework** | **str** |  |
**export_mode** | **str** |  |
**build_tool** | **str** |  |
**manifest** | **Dict[str, object]** |  |
**files** | [**List[AtfGenerationResultFilesInner]**](AtfGenerationResultFilesInner.md) |  |
**notes** | **List[Dict[str, object]]** |  |

## Example

```python
from spectestengine_sdk.models.atf_generation_result import AtfGenerationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AtfGenerationResult from a JSON string
atf_generation_result_instance = AtfGenerationResult.from_json(json)
# print the JSON string representation of the object
print(AtfGenerationResult.to_json())

# convert the object into a dict
atf_generation_result_dict = atf_generation_result_instance.to_dict()
# create an instance of AtfGenerationResult from a dict
atf_generation_result_from_dict = AtfGenerationResult.from_dict(atf_generation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
