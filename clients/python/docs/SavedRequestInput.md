# SavedRequestInput

HTTP-shaped fields are required for REST/SOAP/GraphQL; streamingSpec is required for STREAMING.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec_type** | **str** |  |
**method** | **str** |  | [optional]
**url** | **str** |  | [optional]
**streaming_spec** | [**StreamingDefinition**](StreamingDefinition.md) |  | [optional]
**headers** | **Dict[str, str]** |  | [optional]
**var_query_params** | **Dict[str, str]** |  | [optional]
**body** | **str** |  | [optional]
**auth** | **Dict[str, object]** |  | [optional]
**request_auth** | **Dict[str, object]** |  | [optional]
**request_attachments** | [**List[DocumentAssetReference]**](DocumentAssetReference.md) |  | [optional]
**prerequisites** | **List[Dict[str, object]]** |  | [optional]

## Example

```python
from spectestengine_sdk.models.saved_request_input import SavedRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of SavedRequestInput from a JSON string
saved_request_input_instance = SavedRequestInput.from_json(json)
# print the JSON string representation of the object
print(SavedRequestInput.to_json())

# convert the object into a dict
saved_request_input_dict = saved_request_input_instance.to_dict()
# create an instance of SavedRequestInput from a dict
saved_request_input_from_dict = SavedRequestInput.from_dict(saved_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


