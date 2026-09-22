# FlowDocumentVisualDiffCaptureRunRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_order_index** | **int** | Zero-based order index of the saved API specification step. |
**attachment_id** | **str** | Attachment assertion identifier from that failed step. |

## Example

```python
from spectestengine_sdk.models.flow_document_visual_diff_capture_run_request import FlowDocumentVisualDiffCaptureRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowDocumentVisualDiffCaptureRunRequest from a JSON string
flow_document_visual_diff_capture_run_request_instance = FlowDocumentVisualDiffCaptureRunRequest.from_json(json)
# print the JSON string representation of the object
print(FlowDocumentVisualDiffCaptureRunRequest.to_json())

# convert the object into a dict
flow_document_visual_diff_capture_run_request_dict = flow_document_visual_diff_capture_run_request_instance.to_dict()
# create an instance of FlowDocumentVisualDiffCaptureRunRequest from a dict
flow_document_visual_diff_capture_run_request_from_dict = FlowDocumentVisualDiffCaptureRunRequest.from_dict(flow_document_visual_diff_capture_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


