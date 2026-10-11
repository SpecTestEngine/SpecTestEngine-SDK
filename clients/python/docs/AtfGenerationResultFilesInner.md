# AtfGenerationResultFilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  |
**content** | **str** |  |
**binary** | **bool** |  | [optional] [default to False]

## Example

```python
from spectestengine_sdk.models.atf_generation_result_files_inner import AtfGenerationResultFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AtfGenerationResultFilesInner from a JSON string
atf_generation_result_files_inner_instance = AtfGenerationResultFilesInner.from_json(json)
# print the JSON string representation of the object
print(AtfGenerationResultFilesInner.to_json())

# convert the object into a dict
atf_generation_result_files_inner_dict = atf_generation_result_files_inner_instance.to_dict()
# create an instance of AtfGenerationResultFilesInner from a dict
atf_generation_result_files_inner_from_dict = AtfGenerationResultFilesInner.from_dict(atf_generation_result_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
