# StreamingTranscriptPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**events** | **List[Dict[str, object]]** |  |
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**complete** | **bool** |  |

## Example

```python
from spectestengine_sdk.models.streaming_transcript_page import StreamingTranscriptPage

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingTranscriptPage from a JSON string
streaming_transcript_page_instance = StreamingTranscriptPage.from_json(json)
# print the JSON string representation of the object
print(StreamingTranscriptPage.to_json())

# convert the object into a dict
streaming_transcript_page_dict = streaming_transcript_page_instance.to_dict()
# create an instance of StreamingTranscriptPage from a dict
streaming_transcript_page_from_dict = StreamingTranscriptPage.from_dict(streaming_transcript_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
