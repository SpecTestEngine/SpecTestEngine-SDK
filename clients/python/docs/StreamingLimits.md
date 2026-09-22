# StreamingLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_duration** | **str** |  |
**max_idle_timeout** | **str** |  |
**max_events** | **int** |  |
**max_bytes** | **int** |  |
**max_event_bytes** | **int** |  |
**max_concurrent_runs_per_company** | **int** |  |

## Example

```python
from spectestengine_sdk.models.streaming_limits import StreamingLimits

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingLimits from a JSON string
streaming_limits_instance = StreamingLimits.from_json(json)
# print the JSON string representation of the object
print(StreamingLimits.to_json())

# convert the object into a dict
streaming_limits_dict = streaming_limits_instance.to_dict()
# create an instance of StreamingLimits from a dict
streaming_limits_from_dict = StreamingLimits.from_dict(streaming_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


