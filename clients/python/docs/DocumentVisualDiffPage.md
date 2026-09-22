# DocumentVisualDiffPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  |
**actual_artifact_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**expected_artifact_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**diff_artifact_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**width** | **int** |  |
**height** | **int** |  |

## Example

```python
from spectestengine_sdk.models.document_visual_diff_page import DocumentVisualDiffPage

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVisualDiffPage from a JSON string
document_visual_diff_page_instance = DocumentVisualDiffPage.from_json(json)
# print the JSON string representation of the object
print(DocumentVisualDiffPage.to_json())

# convert the object into a dict
document_visual_diff_page_dict = document_visual_diff_page_instance.to_dict()
# create an instance of DocumentVisualDiffPage from a dict
document_visual_diff_page_from_dict = DocumentVisualDiffPage.from_dict(document_visual_diff_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


