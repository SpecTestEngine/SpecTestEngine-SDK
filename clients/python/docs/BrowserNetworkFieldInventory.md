# BrowserNetworkFieldInventory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_headers** | **List[str]** |  |
**request_body** | [**List[BrowserNetworkField]**](BrowserNetworkField.md) |  |
**response_body** | [**List[BrowserNetworkField]**](BrowserNetworkField.md) |  |
**request_headers_complete** | **bool** |  |
**request_body_complete** | **bool** |  |
**response_body_complete** | **bool** |  |

## Example

```python
from spectestengine_sdk.models.browser_network_field_inventory import BrowserNetworkFieldInventory

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserNetworkFieldInventory from a JSON string
browser_network_field_inventory_instance = BrowserNetworkFieldInventory.from_json(json)
# print the JSON string representation of the object
print(BrowserNetworkFieldInventory.to_json())

# convert the object into a dict
browser_network_field_inventory_dict = browser_network_field_inventory_instance.to_dict()
# create an instance of BrowserNetworkFieldInventory from a dict
browser_network_field_inventory_from_dict = BrowserNetworkFieldInventory.from_dict(browser_network_field_inventory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
