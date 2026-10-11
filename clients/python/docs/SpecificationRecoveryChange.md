# SpecificationRecoveryChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  |
**before** | **object** |  | [optional]
**after** | **object** |  | [optional]
**status** | **str** |  |

## Example

```python
from spectestengine_sdk.models.specification_recovery_change import SpecificationRecoveryChange

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationRecoveryChange from a JSON string
specification_recovery_change_instance = SpecificationRecoveryChange.from_json(json)
# print the JSON string representation of the object
print(SpecificationRecoveryChange.to_json())

# convert the object into a dict
specification_recovery_change_dict = specification_recovery_change_instance.to_dict()
# create an instance of SpecificationRecoveryChange from a dict
specification_recovery_change_from_dict = SpecificationRecoveryChange.from_dict(specification_recovery_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
