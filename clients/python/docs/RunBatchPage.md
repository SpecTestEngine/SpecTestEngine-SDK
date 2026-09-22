# RunBatchPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |
**items** | [**List[RunBatch]**](RunBatch.md) |  |

## Example

```python
from spectestengine_sdk.models.run_batch_page import RunBatchPage

# TODO update the JSON string below
json = "{}"
# create an instance of RunBatchPage from a JSON string
run_batch_page_instance = RunBatchPage.from_json(json)
# print the JSON string representation of the object
print(RunBatchPage.to_json())

# convert the object into a dict
run_batch_page_dict = run_batch_page_instance.to_dict()
# create an instance of RunBatchPage from a dict
run_batch_page_from_dict = RunBatchPage.from_dict(run_batch_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


