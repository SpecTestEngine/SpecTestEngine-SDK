# SentinelIncident


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**environment** | **str** |  |
**check_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**check_name** | **str** |  |
**fingerprint** | **str** |  |
**status** | **str** |  |
**consecutive_failures** | **int** |  |
**last_run_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**summary** | **str** |  | [optional]
**started_at** | **datetime** |  | [optional]
**resolved_at** | **datetime** |  | [optional]

## Example

```python
from spectestengine_sdk.models.sentinel_incident import SentinelIncident

# TODO update the JSON string below
json = "{}"
# create an instance of SentinelIncident from a JSON string
sentinel_incident_instance = SentinelIncident.from_json(json)
# print the JSON string representation of the object
print(SentinelIncident.to_json())

# convert the object into a dict
sentinel_incident_dict = sentinel_incident_instance.to_dict()
# create an instance of SentinelIncident from a dict
sentinel_incident_from_dict = SentinelIncident.from_dict(sentinel_incident_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


