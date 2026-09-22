# DocumentVisualDiff


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visual_diff_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**viewer_url** | **str** |  |
**source_type** | **str** |  |
**source_run_id** | **str** |  | [optional]
**source_step_id** | **str** |  | [optional]
**attachment_id** | **str** |  |
**actual_content_type** | **str** |  |
**actual_sha256** | **str** |  |
**expected_sha256** | **str** |  | [optional]
**status** | [**DocumentVisualDiffStatus**](DocumentVisualDiffStatus.md) |  |
**decision** | [**DocumentVisualDiffDecision**](DocumentVisualDiffDecision.md) |  |
**actual_page_count** | **int** |  |
**created_at** | **datetime** |  |
**expires_at** | **datetime** |  |
**actual_available** | **bool** |  |
**expected_upload_required** | **bool** |  |
**regenerate_available** | **bool** |  |
**generations** | [**List[DocumentVisualDiffGeneration]**](DocumentVisualDiffGeneration.md) |  |
**current_generation** | [**DocumentVisualDiffGeneration**](DocumentVisualDiffGeneration.md) |  | [optional]

## Example

```python
from spectestengine_sdk.models.document_visual_diff import DocumentVisualDiff

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVisualDiff from a JSON string
document_visual_diff_instance = DocumentVisualDiff.from_json(json)
# print the JSON string representation of the object
print(DocumentVisualDiff.to_json())

# convert the object into a dict
document_visual_diff_dict = document_visual_diff_instance.to_dict()
# create an instance of DocumentVisualDiff from a dict
document_visual_diff_from_dict = DocumentVisualDiff.from_dict(document_visual_diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


