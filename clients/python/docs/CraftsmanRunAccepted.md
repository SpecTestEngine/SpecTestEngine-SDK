# CraftsmanRunAccepted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**state** | [**CraftsmanRunState**](CraftsmanRunState.md) |  |

## Example

```python
from spectestengine_sdk.models.craftsman_run_accepted import CraftsmanRunAccepted

# TODO update the JSON string below
json = "{}"
# create an instance of CraftsmanRunAccepted from a JSON string
craftsman_run_accepted_instance = CraftsmanRunAccepted.from_json(json)
# print the JSON string representation of the object
print(CraftsmanRunAccepted.to_json())

# convert the object into a dict
craftsman_run_accepted_dict = craftsman_run_accepted_instance.to_dict()
# create an instance of CraftsmanRunAccepted from a dict
craftsman_run_accepted_from_dict = CraftsmanRunAccepted.from_dict(craftsman_run_accepted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
