# FragmentSummaryCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rest** | **int** |  |
**soap** | **int** |  |
**graphql** | **int** |  |
**streaming** | **int** |  |

## Example

```python
from spectestengine_sdk.models.fragment_summary_counts import FragmentSummaryCounts

# TODO update the JSON string below
json = "{}"
# create an instance of FragmentSummaryCounts from a JSON string
fragment_summary_counts_instance = FragmentSummaryCounts.from_json(json)
# print the JSON string representation of the object
print(FragmentSummaryCounts.to_json())

# convert the object into a dict
fragment_summary_counts_dict = fragment_summary_counts_instance.to_dict()
# create an instance of FragmentSummaryCounts from a dict
fragment_summary_counts_from_dict = FragmentSummaryCounts.from_dict(fragment_summary_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
