# SentinelDashboardSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_checks** | **int** |  |
**active_checks** | **int** |  |
**active_incidents** | **int** |  |
**runs24h** | **int** |  |
**failed_runs24h** | **int** |  |
**uptime24h** | **float** |  |
**average_latency24h** | **float** |  | [optional]

## Example

```python
from spectestengine_sdk.models.sentinel_dashboard_summary import SentinelDashboardSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SentinelDashboardSummary from a JSON string
sentinel_dashboard_summary_instance = SentinelDashboardSummary.from_json(json)
# print the JSON string representation of the object
print(SentinelDashboardSummary.to_json())

# convert the object into a dict
sentinel_dashboard_summary_dict = sentinel_dashboard_summary_instance.to_dict()
# create an instance of SentinelDashboardSummary from a dict
sentinel_dashboard_summary_from_dict = SentinelDashboardSummary.from_dict(sentinel_dashboard_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
