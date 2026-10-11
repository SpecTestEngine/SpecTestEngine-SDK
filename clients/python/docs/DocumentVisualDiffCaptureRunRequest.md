# DocumentVisualDiffCaptureRunRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_id** | **str** | Attachment assertion identifier from the failed saved run, for example response.body. |

## Example

```python
from spectestengine_sdk.models.document_visual_diff_capture_run_request import DocumentVisualDiffCaptureRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVisualDiffCaptureRunRequest from a JSON string
document_visual_diff_capture_run_request_instance = DocumentVisualDiffCaptureRunRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentVisualDiffCaptureRunRequest.to_json())

# convert the object into a dict
document_visual_diff_capture_run_request_dict = document_visual_diff_capture_run_request_instance.to_dict()
# create an instance of DocumentVisualDiffCaptureRunRequest from a dict
document_visual_diff_capture_run_request_from_dict = DocumentVisualDiffCaptureRunRequest.from_dict(document_visual_diff_capture_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
