# SnapshotPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  |
**size** | **int** |  |
**total_elements** | **int** |  |
**total_pages** | **int** |  |
**first** | **bool** |  |
**last** | **bool** |  |
**items** | [**List[Snapshot]**](Snapshot.md) |  |

## Example

```python
from spectestengine_sdk.models.snapshot_page import SnapshotPage

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotPage from a JSON string
snapshot_page_instance = SnapshotPage.from_json(json)
# print the JSON string representation of the object
print(SnapshotPage.to_json())

# convert the object into a dict
snapshot_page_dict = snapshot_page_instance.to_dict()
# create an instance of SnapshotPage from a dict
snapshot_page_from_dict = SnapshotPage.from_dict(snapshot_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
