# AtfProjectConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **str** |  |
**package_name** | **str** |  |
**target_framework** | **str** |  |
**export_mode** | **str** |  |
**build_tool** | **str** |  |
**java_version** | **int** |  |
**base_url_mode** | [**AtfBaseUrlMode**](AtfBaseUrlMode.md) |  |
**base_url_variable_name** | **str** |  | [optional]
**include_support_files** | **bool** |  |
**include_coverage** | **bool** |  |
**ci_provider** | **str** |  |
**unsupported_feature_mode** | **str** |  | [default to 'FAIL']

## Example

```python
from spectestengine_sdk.models.atf_project_config import AtfProjectConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AtfProjectConfig from a JSON string
atf_project_config_instance = AtfProjectConfig.from_json(json)
# print the JSON string representation of the object
print(AtfProjectConfig.to_json())

# convert the object into a dict
atf_project_config_dict = atf_project_config_instance.to_dict()
# create an instance of AtfProjectConfig from a dict
atf_project_config_from_dict = AtfProjectConfig.from_dict(atf_project_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
