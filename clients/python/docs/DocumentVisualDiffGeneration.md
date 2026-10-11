# DocumentVisualDiffGeneration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generation_id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**generation_number** | **int** |  |
**expected_sha256** | **str** |  |
**color_threshold** | **float** |  |
**total_pages** | **int** |  |
**changed_pages** | **int** |  |
**diff_pixels** | **int** |  |
**diff_pixel_ratio** | **float** |  |
**created_at** | **datetime** |  |
**expires_at** | **datetime** |  |
**excluded_regions** | [**List[DocumentVisualExcludedRegion]**](DocumentVisualExcludedRegion.md) | Immutable normalized masks used by this generation. |
**changed_excluded_region_indexes** | **List[int]** | Indexes into excludedRegions whose masked area contained a real change in this immutable generation. |
**pages** | [**List[DocumentVisualDiffPage]**](DocumentVisualDiffPage.md) |  |

## Example

```python
from spectestengine_sdk.models.document_visual_diff_generation import DocumentVisualDiffGeneration

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVisualDiffGeneration from a JSON string
document_visual_diff_generation_instance = DocumentVisualDiffGeneration.from_json(json)
# print the JSON string representation of the object
print(DocumentVisualDiffGeneration.to_json())

# convert the object into a dict
document_visual_diff_generation_dict = document_visual_diff_generation_instance.to_dict()
# create an instance of DocumentVisualDiffGeneration from a dict
document_visual_diff_generation_from_dict = DocumentVisualDiffGeneration.from_dict(document_visual_diff_generation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
