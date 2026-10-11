# SpecificationRecoveryPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**spec_name** | **str** |  |
**spec_type** | [**SpecType**](SpecType.md) |  |
**current_spec** | **Dict[str, object]** |  |
**recovered_spec** | **Dict[str, object]** |  |
**current_raw_spec** | **str** |  |
**recovered_raw_spec** | **str** |  |
**source_run_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**source_run_status** | **str** | Completed passing or assertion-failing status as retained by the owning engine. |
**changes** | [**List[SpecificationRecoveryChange]**](SpecificationRecoveryChange.md) |  |

## Example

```python
from spectestengine_sdk.models.specification_recovery_preview import SpecificationRecoveryPreview

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationRecoveryPreview from a JSON string
specification_recovery_preview_instance = SpecificationRecoveryPreview.from_json(json)
# print the JSON string representation of the object
print(SpecificationRecoveryPreview.to_json())

# convert the object into a dict
specification_recovery_preview_dict = specification_recovery_preview_instance.to_dict()
# create an instance of SpecificationRecoveryPreview from a dict
specification_recovery_preview_from_dict = SpecificationRecoveryPreview.from_dict(specification_recovery_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
