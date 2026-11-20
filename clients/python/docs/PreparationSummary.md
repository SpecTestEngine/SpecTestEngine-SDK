# PreparationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  |
**stable_key** | **str** |  |
**name** | **str** |  |
**protocol** | **str** |  |
**outputs** | [**Dict[str, PreparationOutput]**](PreparationOutput.md) |  |

## Example

```python
from spectestengine_sdk.models.preparation_summary import PreparationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PreparationSummary from a JSON string
preparation_summary_instance = PreparationSummary.from_json(json)
# print the JSON string representation of the object
print(PreparationSummary.to_json())

# convert the object into a dict
preparation_summary_dict = preparation_summary_instance.to_dict()
# create an instance of PreparationSummary from a dict
preparation_summary_from_dict = PreparationSummary.from_dict(preparation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
