# DocumentVisualDiffBaselinePreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visual_diff_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**source_type** | **str** |  |
**source_run_id** | **str** |  | [optional]
**source_step_id** | **str** |  | [optional]
**attachment_id** | **str** |  |
**expected_attachment_hash** | **str** |  |
**expected_attachment_fingerprint** | **str** | Serialized deterministic fingerprint for a new specification revision. | [optional]
**mode** | **str** |  |
**proposed_assertion** | [**DocumentAttachmentAssertionBaseline**](DocumentAttachmentAssertionBaseline.md) |  |
**confirmed** | **bool** |  |
**status** | **str** |  |
**message** | **str** |  |

## Example

```python
from spectestengine_sdk.models.document_visual_diff_baseline_preview import DocumentVisualDiffBaselinePreview

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVisualDiffBaselinePreview from a JSON string
document_visual_diff_baseline_preview_instance = DocumentVisualDiffBaselinePreview.from_json(json)
# print the JSON string representation of the object
print(DocumentVisualDiffBaselinePreview.to_json())

# convert the object into a dict
document_visual_diff_baseline_preview_dict = document_visual_diff_baseline_preview_instance.to_dict()
# create an instance of DocumentVisualDiffBaselinePreview from a dict
document_visual_diff_baseline_preview_from_dict = DocumentVisualDiffBaselinePreview.from_dict(document_visual_diff_baseline_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


