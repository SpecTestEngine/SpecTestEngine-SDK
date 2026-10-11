# DocumentVisualExcludedRegion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  |
**x_ratio** | **float** |  |
**y_ratio** | **float** |  |
**width_ratio** | **float** |  |
**height_ratio** | **float** |  |
**reason** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.document_visual_excluded_region import DocumentVisualExcludedRegion

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVisualExcludedRegion from a JSON string
document_visual_excluded_region_instance = DocumentVisualExcludedRegion.from_json(json)
# print the JSON string representation of the object
print(DocumentVisualExcludedRegion.to_json())

# convert the object into a dict
document_visual_excluded_region_dict = document_visual_excluded_region_instance.to_dict()
# create an instance of DocumentVisualExcludedRegion from a dict
document_visual_excluded_region_from_dict = DocumentVisualExcludedRegion.from_dict(document_visual_excluded_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
