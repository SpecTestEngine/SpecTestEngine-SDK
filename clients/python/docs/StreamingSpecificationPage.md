# StreamingSpecificationPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |
**items** | [**List[StreamingSpecificationSummary]**](StreamingSpecificationSummary.md) |  |

## Example

```python
from spectestengine_sdk.models.streaming_specification_page import StreamingSpecificationPage

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingSpecificationPage from a JSON string
streaming_specification_page_instance = StreamingSpecificationPage.from_json(json)
# print the JSON string representation of the object
print(StreamingSpecificationPage.to_json())

# convert the object into a dict
streaming_specification_page_dict = streaming_specification_page_instance.to_dict()
# create an instance of StreamingSpecificationPage from a dict
streaming_specification_page_from_dict = StreamingSpecificationPage.from_dict(streaming_specification_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
