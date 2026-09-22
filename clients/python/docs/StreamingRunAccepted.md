# StreamingRunAccepted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**state** | [**StreamingRunState**](StreamingRunState.md) |  |
**status_url** | **str** |  |
**transcript_url** | **str** |  |
**cancel_url** | **str** |  |
**created_at** | **datetime** |  |

## Example

```python
from spectestengine_sdk.models.streaming_run_accepted import StreamingRunAccepted

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingRunAccepted from a JSON string
streaming_run_accepted_instance = StreamingRunAccepted.from_json(json)
# print the JSON string representation of the object
print(StreamingRunAccepted.to_json())

# convert the object into a dict
streaming_run_accepted_dict = streaming_run_accepted_instance.to_dict()
# create an instance of StreamingRunAccepted from a dict
streaming_run_accepted_from_dict = StreamingRunAccepted.from_dict(streaming_run_accepted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


