# SentinelCheckPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |
**items** | [**List[SentinelCheck]**](SentinelCheck.md) |  |

## Example

```python
from spectestengine_sdk.models.sentinel_check_page import SentinelCheckPage

# TODO update the JSON string below
json = "{}"
# create an instance of SentinelCheckPage from a JSON string
sentinel_check_page_instance = SentinelCheckPage.from_json(json)
# print the JSON string representation of the object
print(SentinelCheckPage.to_json())

# convert the object into a dict
sentinel_check_page_dict = sentinel_check_page_instance.to_dict()
# create an instance of SentinelCheckPage from a dict
sentinel_check_page_from_dict = SentinelCheckPage.from_dict(sentinel_check_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
