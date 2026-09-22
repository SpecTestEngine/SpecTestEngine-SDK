# SentinelLinkSummaryPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |
**items** | [**List[SentinelLinkSummary]**](SentinelLinkSummary.md) |  |

## Example

```python
from spectestengine_sdk.models.sentinel_link_summary_page import SentinelLinkSummaryPage

# TODO update the JSON string below
json = "{}"
# create an instance of SentinelLinkSummaryPage from a JSON string
sentinel_link_summary_page_instance = SentinelLinkSummaryPage.from_json(json)
# print the JSON string representation of the object
print(SentinelLinkSummaryPage.to_json())

# convert the object into a dict
sentinel_link_summary_page_dict = sentinel_link_summary_page_instance.to_dict()
# create an instance of SentinelLinkSummaryPage from a dict
sentinel_link_summary_page_from_dict = SentinelLinkSummaryPage.from_dict(sentinel_link_summary_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


