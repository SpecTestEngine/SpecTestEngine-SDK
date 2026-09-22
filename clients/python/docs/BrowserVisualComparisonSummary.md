# BrowserVisualComparisonSummary

Immutable visual evidence embedded in a Flow run or Snapshot behavior payload. Empty diagnostic/exclusion lists may be omitted. Fetch the comparison detail lazily for review capabilities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_id** | **UUID** |  | [optional]
**status** | [**BrowserVisualComparisonStatus**](BrowserVisualComparisonStatus.md) |  | [optional]
**decision_status** | [**BrowserVisualDecisionStatus**](BrowserVisualDecisionStatus.md) |  | [optional]
**scope_type** | [**BrowserVisualScopeType**](BrowserVisualScopeType.md) |  | [optional]
**compare_mode** | [**BrowserVisualCompareMode**](BrowserVisualCompareMode.md) |  | [optional]
**stop_policy** | [**BrowserVisualStopPolicy**](BrowserVisualStopPolicy.md) |  | [optional]
**baseline_artifact_id** | **UUID** |  | [optional]
**actual_artifact_id** | **UUID** |  | [optional]
**diff_artifact_id** | **UUID** |  | [optional]
**diff_pixels** | **int** |  | [optional]
**diff_pixel_ratio** | **float** |  | [optional]
**message** | **str** |  | [optional]
**changed_details** | **List[str]** |  | [optional]
**changed_regions** | [**List[BrowserVisualDiffRegion]**](BrowserVisualDiffRegion.md) |  | [optional]
**assertion_revision** | **int** |  | [optional]
**baseline_revision_id** | **UUID** |  | [optional]
**generation_number** | **int** |  | [optional]
**source_comparison_id** | **UUID** |  | [optional]
**root_comparison_id** | **UUID** |  | [optional]
**excluded_regions** | [**List[BrowserVisualExcludedRegion]**](BrowserVisualExcludedRegion.md) |  | [optional]
**changed_excluded_region_indexes** | **List[int]** |  | [optional]

## Example

```python
from spectestengine_sdk.models.browser_visual_comparison_summary import BrowserVisualComparisonSummary

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserVisualComparisonSummary from a JSON string
browser_visual_comparison_summary_instance = BrowserVisualComparisonSummary.from_json(json)
# print the JSON string representation of the object
print(BrowserVisualComparisonSummary.to_json())

# convert the object into a dict
browser_visual_comparison_summary_dict = browser_visual_comparison_summary_instance.to_dict()
# create an instance of BrowserVisualComparisonSummary from a dict
browser_visual_comparison_summary_from_dict = BrowserVisualComparisonSummary.from_dict(browser_visual_comparison_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


