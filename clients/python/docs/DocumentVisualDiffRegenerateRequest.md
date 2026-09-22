# DocumentVisualDiffRegenerateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color_threshold** | **float** |  | [optional] [default to 24]
**excluded_regions** | [**List[DocumentVisualExcludedRegion]**](DocumentVisualExcludedRegion.md) |  | [optional]

## Example

```python
from spectestengine_sdk.models.document_visual_diff_regenerate_request import DocumentVisualDiffRegenerateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVisualDiffRegenerateRequest from a JSON string
document_visual_diff_regenerate_request_instance = DocumentVisualDiffRegenerateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentVisualDiffRegenerateRequest.to_json())

# convert the object into a dict
document_visual_diff_regenerate_request_dict = document_visual_diff_regenerate_request_instance.to_dict()
# create an instance of DocumentVisualDiffRegenerateRequest from a dict
document_visual_diff_regenerate_request_from_dict = DocumentVisualDiffRegenerateRequest.from_dict(document_visual_diff_regenerate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


