# SpecificationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**name** | **str** |  |
**description** | **str** |  | [optional]
**spec_type** | [**SpecType**](SpecType.md) |  |
**method** | **str** | HTTP method from a REST specification request. | [optional]
**url** | **str** | Request URL from a REST specification. | [optional]
**updated_at** | **datetime** |  | [optional]
**created_at** | **datetime** |  |
**last_run_at** | **datetime** |  | [optional]
**last_run_status** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.specification_summary import SpecificationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationSummary from a JSON string
specification_summary_instance = SpecificationSummary.from_json(json)
# print the JSON string representation of the object
print(SpecificationSummary.to_json())

# convert the object into a dict
specification_summary_dict = specification_summary_instance.to_dict()
# create an instance of SpecificationSummary from a dict
specification_summary_from_dict = SpecificationSummary.from_dict(specification_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


