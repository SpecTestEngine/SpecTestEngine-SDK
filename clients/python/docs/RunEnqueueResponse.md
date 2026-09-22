# RunEnqueueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**execution_id** | **str** |  |
**queued** | **bool** |  |
**message** | **str** |  |

## Example

```python
from spectestengine_sdk.models.run_enqueue_response import RunEnqueueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RunEnqueueResponse from a JSON string
run_enqueue_response_instance = RunEnqueueResponse.from_json(json)
# print the JSON string representation of the object
print(RunEnqueueResponse.to_json())

# convert the object into a dict
run_enqueue_response_dict = run_enqueue_response_instance.to_dict()
# create an instance of RunEnqueueResponse from a dict
run_enqueue_response_from_dict = RunEnqueueResponse.from_dict(run_enqueue_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


