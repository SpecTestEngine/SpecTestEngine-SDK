# SentinelRunBaseline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**status** | [**RunStatus**](RunStatus.md) |  |
**label** | **str** |  |
**definition_hash** | **str** |  |
**behavior_hash** | **str** | Assertion-relevant fingerprint; raw transport payloads and explicitly excluded evidence do not affect it. | [optional]
**response_headers_json** | **str** |  | [optional]
**response_body_preview** | **str** |  | [optional]
**result_log** | **str** |  | [optional]
**error_message** | **str** |  | [optional]
**finished_at** | **datetime** |  | [optional]

## Example

```python
from spectestengine_sdk.models.sentinel_run_baseline import SentinelRunBaseline

# TODO update the JSON string below
json = "{}"
# create an instance of SentinelRunBaseline from a JSON string
sentinel_run_baseline_instance = SentinelRunBaseline.from_json(json)
# print the JSON string representation of the object
print(SentinelRunBaseline.to_json())

# convert the object into a dict
sentinel_run_baseline_dict = sentinel_run_baseline_instance.to_dict()
# create an instance of SentinelRunBaseline from a dict
sentinel_run_baseline_from_dict = SentinelRunBaseline.from_dict(sentinel_run_baseline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
