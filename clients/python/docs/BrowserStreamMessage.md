# BrowserStreamMessage

Observed stream message metadata. SSE only supports INBOUND. This never sends another request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport** | **str** |  |
**direction** | **str** |  |
**event_name** | **str** |  | [optional]
**binary** | **bool** |  | [optional] [default to False]
**failed** | **bool** |  | [optional] [default to False]

## Example

```python
from spectestengine_sdk.models.browser_stream_message import BrowserStreamMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserStreamMessage from a JSON string
browser_stream_message_instance = BrowserStreamMessage.from_json(json)
# print the JSON string representation of the object
print(BrowserStreamMessage.to_json())

# convert the object into a dict
browser_stream_message_dict = browser_stream_message_instance.to_dict()
# create an instance of BrowserStreamMessage from a dict
browser_stream_message_from_dict = BrowserStreamMessage.from_dict(browser_stream_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
