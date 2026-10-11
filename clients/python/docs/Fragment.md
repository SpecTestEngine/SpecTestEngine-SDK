# Fragment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**description** | **str** |  | [optional]
**spec_type** | [**SpecType**](SpecType.md) |  |
**streaming_transport** | [**StreamingTransport**](StreamingTransport.md) |  | [optional]
**type** | [**FragmentType**](FragmentType.md) |  |
**content** | **Dict[str, object]** |  |
**fragment_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**created_at** | **datetime** |  |

## Example

```python
from spectestengine_sdk.models.fragment import Fragment

# TODO update the JSON string below
json = "{}"
# create an instance of Fragment from a JSON string
fragment_instance = Fragment.from_json(json)
# print the JSON string representation of the object
print(Fragment.to_json())

# convert the object into a dict
fragment_dict = fragment_instance.to_dict()
# create an instance of Fragment from a dict
fragment_from_dict = Fragment.from_dict(fragment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
