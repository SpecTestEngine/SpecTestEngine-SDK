# SpecificationRunSummary


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

## Example

```python
from spectestengine_sdk.models.specification_run_summary import SpecificationRunSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationRunSummary from a JSON string
specification_run_summary_instance = SpecificationRunSummary.from_json(json)
# print the JSON string representation of the object
print(SpecificationRunSummary.to_json())

# convert the object into a dict
specification_run_summary_dict = specification_run_summary_instance.to_dict()
# create an instance of SpecificationRunSummary from a dict
specification_run_summary_from_dict = SpecificationRunSummary.from_dict(specification_run_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


