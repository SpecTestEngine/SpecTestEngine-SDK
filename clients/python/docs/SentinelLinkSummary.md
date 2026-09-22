# SentinelLinkSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_name** | **str** |  |
**link_count** | **int** |  |

## Example

```python
from spectestengine_sdk.models.sentinel_link_summary import SentinelLinkSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SentinelLinkSummary from a JSON string
sentinel_link_summary_instance = SentinelLinkSummary.from_json(json)
# print the JSON string representation of the object
print(SentinelLinkSummary.to_json())

# convert the object into a dict
sentinel_link_summary_dict = sentinel_link_summary_instance.to_dict()
# create an instance of SentinelLinkSummary from a dict
sentinel_link_summary_from_dict = SentinelLinkSummary.from_dict(sentinel_link_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


