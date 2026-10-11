# DocumentAttachmentAssertionBaseline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  |
**expected_attachment_hash** | **str** |  |
**visual_assertion** | [**DocumentVisualAssertion**](DocumentVisualAssertion.md) |  | [optional]

## Example

```python
from spectestengine_sdk.models.document_attachment_assertion_baseline import DocumentAttachmentAssertionBaseline

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAttachmentAssertionBaseline from a JSON string
document_attachment_assertion_baseline_instance = DocumentAttachmentAssertionBaseline.from_json(json)
# print the JSON string representation of the object
print(DocumentAttachmentAssertionBaseline.to_json())

# convert the object into a dict
document_attachment_assertion_baseline_dict = document_attachment_assertion_baseline_instance.to_dict()
# create an instance of DocumentAttachmentAssertionBaseline from a dict
document_attachment_assertion_baseline_from_dict = DocumentAttachmentAssertionBaseline.from_dict(document_attachment_assertion_baseline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
