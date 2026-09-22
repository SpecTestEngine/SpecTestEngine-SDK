# DocumentVisualAssertionPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  |
**width** | **int** |  |
**height** | **int** |  |
**masked_sha256** | **str** |  |

## Example

```python
from spectestengine_sdk.models.document_visual_assertion_page import DocumentVisualAssertionPage

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVisualAssertionPage from a JSON string
document_visual_assertion_page_instance = DocumentVisualAssertionPage.from_json(json)
# print the JSON string representation of the object
print(DocumentVisualAssertionPage.to_json())

# convert the object into a dict
document_visual_assertion_page_dict = document_visual_assertion_page_instance.to_dict()
# create an instance of DocumentVisualAssertionPage from a dict
document_visual_assertion_page_from_dict = DocumentVisualAssertionPage.from_dict(document_visual_assertion_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


