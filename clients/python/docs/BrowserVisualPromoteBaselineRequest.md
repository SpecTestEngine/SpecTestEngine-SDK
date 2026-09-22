# BrowserVisualPromoteBaselineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **UUID** | Client-generated idempotency key for this review command. |
**expected_assertion_revision** | **int** | Current assertion revision. A stale value is rejected with HTTP 409. |

## Example

```python
from spectestengine_sdk.models.browser_visual_promote_baseline_request import BrowserVisualPromoteBaselineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserVisualPromoteBaselineRequest from a JSON string
browser_visual_promote_baseline_request_instance = BrowserVisualPromoteBaselineRequest.from_json(json)
# print the JSON string representation of the object
print(BrowserVisualPromoteBaselineRequest.to_json())

# convert the object into a dict
browser_visual_promote_baseline_request_dict = browser_visual_promote_baseline_request_instance.to_dict()
# create an instance of BrowserVisualPromoteBaselineRequest from a dict
browser_visual_promote_baseline_request_from_dict = BrowserVisualPromoteBaselineRequest.from_dict(browser_visual_promote_baseline_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


