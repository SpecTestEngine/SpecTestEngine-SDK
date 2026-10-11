# SpecificationRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**spec_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**spec_name** | **str** |  |
**spec_stable_key** | **str** |  | [optional]
**spec_type** | [**SpecType**](SpecType.md) |  |
**overall_test_status** | **str** |  |
**started_at** | **datetime** |  |
**finished_at** | **datetime** |  |
**spec_definition_hash** | **str** |  | [optional]
**format** | [**ContentFormat**](ContentFormat.md) |  | [optional] [default to ContentFormat.JSON]
**test_result_log** | **Dict[str, object]** |  |
**raw_spec** | **str** |  |

## Example

```python
from spectestengine_sdk.models.specification_run import SpecificationRun

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationRun from a JSON string
specification_run_instance = SpecificationRun.from_json(json)
# print the JSON string representation of the object
print(SpecificationRun.to_json())

# convert the object into a dict
specification_run_dict = specification_run_instance.to_dict()
# create an instance of SpecificationRun from a dict
specification_run_from_dict = SpecificationRun.from_dict(specification_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
