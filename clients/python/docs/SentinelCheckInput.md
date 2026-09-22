# SentinelCheckInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**description** | **str** |  | [optional]
**source_name** | **str** |  | [optional]
**environment** | **str** | Immutable environment scope for the check and its runs. |
**type** | **str** |  |
**spec_type** | [**SpecType**](SpecType.md) | Required when type is SPEC and prohibited when type is FLOW or URL. | [optional]
**format** | [**ContentFormat**](ContentFormat.md) |  | [default to ContentFormat.JSON]
**definition** | **str** |  |
**active** | **bool** |  | [optional] [default to True]
**timeout_ms** | **int** |  | [optional] [default to 10000]
**failure_strategy** | **str** |  | [optional] [default to 'FAIL_FAST']
**max_retries** | **int** |  | [optional] [default to 3]
**retry_delay_min_ms** | **int** |  | [optional] [default to 5000]
**retry_delay_max_ms** | **int** |  | [optional] [default to 10000]
**circuit_breaker_failure_threshold** | **int** |  | [optional] [default to 5]
**cooldown_ms** | **int** |  | [optional] [default to 300000]

## Example

```python
from spectestengine_sdk.models.sentinel_check_input import SentinelCheckInput

# TODO update the JSON string below
json = "{}"
# create an instance of SentinelCheckInput from a JSON string
sentinel_check_input_instance = SentinelCheckInput.from_json(json)
# print the JSON string representation of the object
print(SentinelCheckInput.to_json())

# convert the object into a dict
sentinel_check_input_dict = sentinel_check_input_instance.to_dict()
# create an instance of SentinelCheckInput from a dict
sentinel_check_input_from_dict = SentinelCheckInput.from_dict(sentinel_check_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


