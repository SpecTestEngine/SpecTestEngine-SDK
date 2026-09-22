# RequestNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**type** | **str** |  |
**parent_node_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**order_index** | **int** |  | [optional]
**request** | [**SavedRequestInput**](SavedRequestInput.md) |  | [optional]
**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**created_at** | **datetime** |  |
**updated_at** | **datetime** |  |

## Example

```python
from spectestengine_sdk.models.request_node import RequestNode

# TODO update the JSON string below
json = "{}"
# create an instance of RequestNode from a JSON string
request_node_instance = RequestNode.from_json(json)
# print the JSON string representation of the object
print(RequestNode.to_json())

# convert the object into a dict
request_node_dict = request_node_instance.to_dict()
# create an instance of RequestNode from a dict
request_node_from_dict = RequestNode.from_dict(request_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


