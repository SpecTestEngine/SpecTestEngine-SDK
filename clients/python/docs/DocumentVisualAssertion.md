# DocumentVisualAssertion

Persistent masked-render assertion. Protocol engines contact Browser Engine only when excludedRegions is non-empty and the local attachment hash or fingerprint failed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  |
**algorithm** | **str** |  |
**render_profile** | **str** |  |
**pages** | [**List[DocumentVisualAssertionPage]**](DocumentVisualAssertionPage.md) |  |
**excluded_regions** | [**List[DocumentVisualExcludedRegion]**](DocumentVisualExcludedRegion.md) |  |

## Example

```python
from spectestengine_sdk.models.document_visual_assertion import DocumentVisualAssertion

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVisualAssertion from a JSON string
document_visual_assertion_instance = DocumentVisualAssertion.from_json(json)
# print the JSON string representation of the object
print(DocumentVisualAssertion.to_json())

# convert the object into a dict
document_visual_assertion_dict = document_visual_assertion_instance.to_dict()
# create an instance of DocumentVisualAssertion from a dict
document_visual_assertion_from_dict = DocumentVisualAssertion.from_dict(document_visual_assertion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


