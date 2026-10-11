# BrowserVisualExcludeAndRecompareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **UUID** | Client-generated idempotency key for this review command. |
**expected_assertion_revision** | **int** | Current assertion revision. A stale value is rejected with HTTP 409. |
**excluded_regions** | [**List[BrowserVisualExcludedRegion]**](BrowserVisualExcludedRegion.md) | Complete normalized exclusion set for the next assertion revision. Overlaps are valid; rectangles crossing right or bottom edges are clamped to the comparison canvas. |

## Example

```python
from spectestengine_sdk.models.browser_visual_exclude_and_recompare_request import BrowserVisualExcludeAndRecompareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserVisualExcludeAndRecompareRequest from a JSON string
browser_visual_exclude_and_recompare_request_instance = BrowserVisualExcludeAndRecompareRequest.from_json(json)
# print the JSON string representation of the object
print(BrowserVisualExcludeAndRecompareRequest.to_json())

# convert the object into a dict
browser_visual_exclude_and_recompare_request_dict = browser_visual_exclude_and_recompare_request_instance.to_dict()
# create an instance of BrowserVisualExcludeAndRecompareRequest from a dict
browser_visual_exclude_and_recompare_request_from_dict = BrowserVisualExcludeAndRecompareRequest.from_dict(browser_visual_exclude_and_recompare_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
