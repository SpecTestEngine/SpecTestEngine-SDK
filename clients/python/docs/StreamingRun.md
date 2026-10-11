# StreamingRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**spec_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**spec_name** | **str** |  |
**spec_stable_key** | **str** |  | [optional]
**spec_type** | **str** |  |
**format** | **str** |  |
**transport** | [**StreamingTransport**](StreamingTransport.md) |  |
**definition_hash** | **str** |  |
**state** | [**StreamingRunState**](StreamingRunState.md) |  |
**outcome** | [**StreamingRunOutcome**](StreamingRunOutcome.md) |  | [optional]
**termination_reason** | **str** |  | [optional]
**event_count** | **int** |  |
**byte_count** | **int** |  |
**assertion_pass_count** | **int** |  |
**assertion_fail_count** | **int** |  |
**evidence_summary** | **Dict[str, object]** |  | [optional]
**error_message** | **str** |  | [optional]
**created_at** | **datetime** |  |
**started_at** | **datetime** |  | [optional]
**finished_at** | **datetime** |  | [optional]

## Example

```python
from spectestengine_sdk.models.streaming_run import StreamingRun

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingRun from a JSON string
streaming_run_instance = StreamingRun.from_json(json)
# print the JSON string representation of the object
print(StreamingRun.to_json())

# convert the object into a dict
streaming_run_dict = streaming_run_instance.to_dict()
# create an instance of StreamingRun from a dict
streaming_run_from_dict = StreamingRun.from_dict(streaming_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
