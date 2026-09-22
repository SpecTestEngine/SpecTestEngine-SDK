# FragmentAssembly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec_type** | [**SpecType**](SpecType.md) |  |
**streaming_transport** | [**StreamingTransport**](StreamingTransport.md) |  | [optional]
**fragment_ids** | **List[UUID]** |  |

## Example

```python
from spectestengine_sdk.models.fragment_assembly import FragmentAssembly

# TODO update the JSON string below
json = "{}"
# create an instance of FragmentAssembly from a JSON string
fragment_assembly_instance = FragmentAssembly.from_json(json)
# print the JSON string representation of the object
print(FragmentAssembly.to_json())

# convert the object into a dict
fragment_assembly_dict = fragment_assembly_instance.to_dict()
# create an instance of FragmentAssembly from a dict
fragment_assembly_from_dict = FragmentAssembly.from_dict(fragment_assembly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


