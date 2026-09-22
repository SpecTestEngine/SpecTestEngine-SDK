# FragmentDraftInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional]
**type** | [**FragmentType**](FragmentType.md) |  |
**content** | **Dict[str, object]** |  |

## Example

```python
from spectestengine_sdk.models.fragment_draft_input import FragmentDraftInput

# TODO update the JSON string below
json = "{}"
# create an instance of FragmentDraftInput from a JSON string
fragment_draft_input_instance = FragmentDraftInput.from_json(json)
# print the JSON string representation of the object
print(FragmentDraftInput.to_json())

# convert the object into a dict
fragment_draft_input_dict = fragment_draft_input_instance.to_dict()
# create an instance of FragmentDraftInput from a dict
fragment_draft_input_from_dict = FragmentDraftInput.from_dict(fragment_draft_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


