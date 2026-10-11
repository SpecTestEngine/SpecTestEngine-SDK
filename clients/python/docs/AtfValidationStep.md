# AtfValidationStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  |
**label** | **str** |  |
**status** | **str** |  |
**message** | **str** |  |

## Example

```python
from spectestengine_sdk.models.atf_validation_step import AtfValidationStep

# TODO update the JSON string below
json = "{}"
# create an instance of AtfValidationStep from a JSON string
atf_validation_step_instance = AtfValidationStep.from_json(json)
# print the JSON string representation of the object
print(AtfValidationStep.to_json())

# convert the object into a dict
atf_validation_step_dict = atf_validation_step_instance.to_dict()
# create an instance of AtfValidationStep from a dict
atf_validation_step_from_dict = AtfValidationStep.from_dict(atf_validation_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
