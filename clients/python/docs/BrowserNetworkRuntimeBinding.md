# BrowserNetworkRuntimeBinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**source** | **str** |  |
**path** | **str** |  |
**scope_origin** | **str** | Optional explicit HTTP(S) origin for later matching calls; no credentials, path, query or fragment. Defaults to the source call origin. | [optional]

## Example

```python
from spectestengine_sdk.models.browser_network_runtime_binding import BrowserNetworkRuntimeBinding

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserNetworkRuntimeBinding from a JSON string
browser_network_runtime_binding_instance = BrowserNetworkRuntimeBinding.from_json(json)
# print the JSON string representation of the object
print(BrowserNetworkRuntimeBinding.to_json())

# convert the object into a dict
browser_network_runtime_binding_dict = browser_network_runtime_binding_instance.to_dict()
# create an instance of BrowserNetworkRuntimeBinding from a dict
browser_network_runtime_binding_from_dict = BrowserNetworkRuntimeBinding.from_dict(browser_network_runtime_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
