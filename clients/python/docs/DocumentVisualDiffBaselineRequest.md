# DocumentVisualDiffBaselineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirm** | **bool** |  | [default to False]
**mode** | **str** |  |

## Example

```python
from spectestengine_sdk.models.document_visual_diff_baseline_request import DocumentVisualDiffBaselineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVisualDiffBaselineRequest from a JSON string
document_visual_diff_baseline_request_instance = DocumentVisualDiffBaselineRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentVisualDiffBaselineRequest.to_json())

# convert the object into a dict
document_visual_diff_baseline_request_dict = document_visual_diff_baseline_request_instance.to_dict()
# create an instance of DocumentVisualDiffBaselineRequest from a dict
document_visual_diff_baseline_request_from_dict = DocumentVisualDiffBaselineRequest.from_dict(document_visual_diff_baseline_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


