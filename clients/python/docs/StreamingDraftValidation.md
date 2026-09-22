# StreamingDraftValidation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** |  |
**spec_type** | **str** |  |
**transport** | [**StreamingTransport**](StreamingTransport.md) |  |

## Example

```python
from spectestengine_sdk.models.streaming_draft_validation import StreamingDraftValidation

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingDraftValidation from a JSON string
streaming_draft_validation_instance = StreamingDraftValidation.from_json(json)
# print the JSON string representation of the object
print(StreamingDraftValidation.to_json())

# convert the object into a dict
streaming_draft_validation_dict = streaming_draft_validation_instance.to_dict()
# create an instance of StreamingDraftValidation from a dict
streaming_draft_validation_from_dict = StreamingDraftValidation.from_dict(streaming_draft_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


