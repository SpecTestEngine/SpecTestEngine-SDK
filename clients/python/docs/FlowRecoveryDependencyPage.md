# FlowRecoveryDependencyPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FlowRecoveryDependency]**](FlowRecoveryDependency.md) |  |
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |

## Example

```python
from spectestengine_sdk.models.flow_recovery_dependency_page import FlowRecoveryDependencyPage

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRecoveryDependencyPage from a JSON string
flow_recovery_dependency_page_instance = FlowRecoveryDependencyPage.from_json(json)
# print the JSON string representation of the object
print(FlowRecoveryDependencyPage.to_json())

# convert the object into a dict
flow_recovery_dependency_page_dict = flow_recovery_dependency_page_instance.to_dict()
# create an instance of FlowRecoveryDependencyPage from a dict
flow_recovery_dependency_page_from_dict = FlowRecoveryDependencyPage.from_dict(flow_recovery_dependency_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
