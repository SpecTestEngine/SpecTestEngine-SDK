# SentinelRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**execution_id** | **str** |  |
**environment** | **str** | Environment captured when the run was queued. |
**check_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**check_name** | **str** |  |
**check_type** | **str** |  |
**definition_hash** | **str** |  |
**behavior_hash** | **str** | Assertion-relevant behavior fingerprint of the completed run; null while unavailable. | [optional]
**region** | **str** |  |
**trigger_type** | **str** |  |
**status** | [**RunStatus**](RunStatus.md) |  |
**error_type** | **str** |  | [optional]
**final_status_code** | **int** |  | [optional]
**latency_ms** | **int** |  | [optional]
**response_size_bytes** | **int** |  | [optional]
**error_message** | **str** |  | [optional]
**result_log** | **str** |  | [optional]
**queued_at** | **datetime** |  |
**started_at** | **datetime** |  | [optional]
**finished_at** | **datetime** |  | [optional]
**attempts** | **List[Dict[str, object]]** |  | [optional]
**baseline** | [**SentinelRunBaseline**](SentinelRunBaseline.md) |  | [optional]

## Example

```python
from spectestengine_sdk.models.sentinel_run import SentinelRun

# TODO update the JSON string below
json = "{}"
# create an instance of SentinelRun from a JSON string
sentinel_run_instance = SentinelRun.from_json(json)
# print the JSON string representation of the object
print(SentinelRun.to_json())

# convert the object into a dict
sentinel_run_dict = sentinel_run_instance.to_dict()
# create an instance of SentinelRun from a dict
sentinel_run_from_dict = SentinelRun.from_dict(sentinel_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
