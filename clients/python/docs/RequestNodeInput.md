# RequestNodeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**type** | **str** |  |
**parent_node_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**order_index** | **int** |  | [optional]
**request** | [**SavedRequestInput**](SavedRequestInput.md) |  | [optional]

## Example

```python
from spectestengine_sdk.models.request_node_input import RequestNodeInput

# TODO update the JSON string below
json = "{}"
# create an instance of RequestNodeInput from a JSON string
request_node_input_instance = RequestNodeInput.from_json(json)
# print the JSON string representation of the object
print(RequestNodeInput.to_json())

# convert the object into a dict
request_node_input_dict = request_node_input_instance.to_dict()
# create an instance of RequestNodeInput from a dict
request_node_input_from_dict = RequestNodeInput.from_dict(request_node_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
