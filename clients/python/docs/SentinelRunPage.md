# SentinelRunPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |
**items** | [**List[SentinelRun]**](SentinelRun.md) |  |

## Example

```python
from spectestengine_sdk.models.sentinel_run_page import SentinelRunPage

# TODO update the JSON string below
json = "{}"
# create an instance of SentinelRunPage from a JSON string
sentinel_run_page_instance = SentinelRunPage.from_json(json)
# print the JSON string representation of the object
print(SentinelRunPage.to_json())

# convert the object into a dict
sentinel_run_page_dict = sentinel_run_page_instance.to_dict()
# create an instance of SentinelRunPage from a dict
sentinel_run_page_from_dict = SentinelRunPage.from_dict(sentinel_run_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


