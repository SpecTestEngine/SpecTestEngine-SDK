# AtfGenerationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **str** |  |
**package_name** | **str** |  |
**target_framework** | **str** |  | [optional]
**export_mode** | **str** |  | [optional]
**build_tool** | **str** |  | [optional]
**java_version** | **int** |  | [optional]
**base_url_mode** | [**AtfBaseUrlMode**](AtfBaseUrlMode.md) |  | [optional]
**base_url_variable_name** | **str** |  | [optional]
**specs** | [**List[ArtifactSpecRef]**](ArtifactSpecRef.md) |  | [optional]
**flow_ids** | **List[UUID]** |  | [optional]
**ui_macro_ids** | **List[UUID]** |  | [optional]
**include_support_files** | **bool** |  | [optional]
**include_coverage** | **bool** |  | [optional]
**ci_provider** | **str** |  | [optional]
**unsupported_feature_mode** | **str** | FAIL is recommended for CI because unsupported flow steps must not silently disappear from an export. | [optional] [default to 'FAIL']

## Example

```python
from spectestengine_sdk.models.atf_generation_input import AtfGenerationInput

# TODO update the JSON string below
json = "{}"
# create an instance of AtfGenerationInput from a JSON string
atf_generation_input_instance = AtfGenerationInput.from_json(json)
# print the JSON string representation of the object
print(AtfGenerationInput.to_json())

# convert the object into a dict
atf_generation_input_dict = atf_generation_input_instance.to_dict()
# create an instance of AtfGenerationInput from a dict
atf_generation_input_from_dict = AtfGenerationInput.from_dict(atf_generation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


