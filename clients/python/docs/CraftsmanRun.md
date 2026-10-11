# CraftsmanRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**workspace_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**node_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**state** | [**CraftsmanRunState**](CraftsmanRunState.md) |  |
**result** | [**RequestChainRun**](RequestChainRun.md) |  | [optional]
**transcript** | **object** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**error_message** | **str** |  | [optional]
**created_at** | **datetime** |  |
**started_at** | **datetime** |  | [optional]
**finished_at** | **datetime** |  | [optional]

## Example

```python
from spectestengine_sdk.models.craftsman_run import CraftsmanRun

# TODO update the JSON string below
json = "{}"
# create an instance of CraftsmanRun from a JSON string
craftsman_run_instance = CraftsmanRun.from_json(json)
# print the JSON string representation of the object
print(CraftsmanRun.to_json())

# convert the object into a dict
craftsman_run_dict = craftsman_run_instance.to_dict()
# create an instance of CraftsmanRun from a dict
craftsman_run_from_dict = CraftsmanRun.from_dict(craftsman_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
