# BrowserVisualComparison

Immutable visual comparison generation. Baseline promotion creates a new baseline revision; it never deletes evidence referenced by older comparisons or snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_id** | **UUID** |  |
**status** | [**BrowserVisualComparisonStatus**](BrowserVisualComparisonStatus.md) |  |
**decision_status** | [**BrowserVisualDecisionStatus**](BrowserVisualDecisionStatus.md) |  |
**scope_type** | [**BrowserVisualScopeType**](BrowserVisualScopeType.md) |  |
**compare_mode** | [**BrowserVisualCompareMode**](BrowserVisualCompareMode.md) |  |
**stop_policy** | [**BrowserVisualStopPolicy**](BrowserVisualStopPolicy.md) |  |
**baseline_artifact_id** | **UUID** |  | [optional]
**actual_artifact_id** | **UUID** |  | [optional]
**diff_artifact_id** | **UUID** |  | [optional]
**diff_pixels** | **int** |  | [optional]
**diff_pixel_ratio** | **float** |  | [optional]
**message** | **str** |  | [optional]
**changed_details** | **List[str]** |  | [optional]
**changed_regions** | [**List[BrowserVisualDiffRegion]**](BrowserVisualDiffRegion.md) |  | [optional]
**created_at** | **datetime** |  |
**reviewed_at** | **datetime** |  | [optional]
**assertion_revision** | **int** |  |
**baseline_revision_id** | **UUID** |  | [optional]
**applied_baseline_revision_id** | **UUID** |  | [optional]
**generation_number** | **int** |  |
**source_comparison_id** | **UUID** |  | [optional]
**root_comparison_id** | **UUID** |  |
**excluded_regions** | [**List[BrowserVisualExcludedRegion]**](BrowserVisualExcludedRegion.md) |  |
**changed_excluded_region_indexes** | **List[int]** |  |
**review_capabilities** | [**BrowserVisualReviewCapabilities**](BrowserVisualReviewCapabilities.md) |  |

## Example

```python
from spectestengine_sdk.models.browser_visual_comparison import BrowserVisualComparison

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserVisualComparison from a JSON string
browser_visual_comparison_instance = BrowserVisualComparison.from_json(json)
# print the JSON string representation of the object
print(BrowserVisualComparison.to_json())

# convert the object into a dict
browser_visual_comparison_dict = browser_visual_comparison_instance.to_dict()
# create an instance of BrowserVisualComparison from a dict
browser_visual_comparison_from_dict = BrowserVisualComparison.from_dict(browser_visual_comparison_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
