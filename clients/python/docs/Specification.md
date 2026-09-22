# Specification


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
**stable_key** | **str** |  | [optional]
**format** | [**ContentFormat**](ContentFormat.md) |  | [default to ContentFormat.JSON]
**raw_spec** | **str** |  |
**spec** | **Dict[str, object]** |  |

## Example

```python
from spectestengine_sdk.models.specification import Specification

# TODO update the JSON string below
json = "{}"
# create an instance of Specification from a JSON string
specification_instance = Specification.from_json(json)
# print the JSON string representation of the object
print(Specification.to_json())

# convert the object into a dict
specification_dict = specification_instance.to_dict()
# create an instance of Specification from a dict
specification_from_dict = Specification.from_dict(specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


