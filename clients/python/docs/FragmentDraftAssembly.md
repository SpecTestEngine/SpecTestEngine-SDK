# FragmentDraftAssembly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec_type** | [**SpecType**](SpecType.md) |  |
**streaming_transport** | [**StreamingTransport**](StreamingTransport.md) |  | [optional]
**fragments** | [**List[FragmentDraftInput]**](FragmentDraftInput.md) |  |

## Example

```python
from spectestengine_sdk.models.fragment_draft_assembly import FragmentDraftAssembly

# TODO update the JSON string below
json = "{}"
# create an instance of FragmentDraftAssembly from a JSON string
fragment_draft_assembly_instance = FragmentDraftAssembly.from_json(json)
# print the JSON string representation of the object
print(FragmentDraftAssembly.to_json())

# convert the object into a dict
fragment_draft_assembly_dict = fragment_draft_assembly_instance.to_dict()
# create an instance of FragmentDraftAssembly from a dict
fragment_draft_assembly_from_dict = FragmentDraftAssembly.from_dict(fragment_draft_assembly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
