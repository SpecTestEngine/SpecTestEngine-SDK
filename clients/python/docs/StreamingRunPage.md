# StreamingRunPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |
**items** | [**List[StreamingRun]**](StreamingRun.md) |  |

## Example

```python
from spectestengine_sdk.models.streaming_run_page import StreamingRunPage

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingRunPage from a JSON string
streaming_run_page_instance = StreamingRunPage.from_json(json)
# print the JSON string representation of the object
print(StreamingRunPage.to_json())

# convert the object into a dict
streaming_run_page_dict = streaming_run_page_instance.to_dict()
# create an instance of StreamingRunPage from a dict
streaming_run_page_from_dict = StreamingRunPage.from_dict(streaming_run_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


