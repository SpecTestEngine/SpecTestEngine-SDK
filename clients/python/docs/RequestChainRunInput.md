# RequestChainRunInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**override_values** | **Dict[str, object]** |  | [optional]
**global_variables** | **Dict[str, str]** |  | [optional]
**global_variable_fallbacks** | **Dict[str, str]** |  | [optional]
**draft_request** | [**SavedRequestInput**](SavedRequestInput.md) |  | [optional]

## Example

```python
from spectestengine_sdk.models.request_chain_run_input import RequestChainRunInput

# TODO update the JSON string below
json = "{}"
# create an instance of RequestChainRunInput from a JSON string
request_chain_run_input_instance = RequestChainRunInput.from_json(json)
# print the JSON string representation of the object
print(RequestChainRunInput.to_json())

# convert the object into a dict
request_chain_run_input_dict = request_chain_run_input_instance.to_dict()
# create an instance of RequestChainRunInput from a dict
request_chain_run_input_from_dict = RequestChainRunInput.from_dict(request_chain_run_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
