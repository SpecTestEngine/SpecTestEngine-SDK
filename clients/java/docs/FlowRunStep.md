

# FlowRunStep


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stepId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**orderIndex** | **Integer** |  |  |
|**stepType** | [**StepTypeEnum**](#StepTypeEnum) |  |  |
|**specName** | **String** |  |  [optional] |
|**uiMacroId** | **UUID** |  |  [optional] |
|**uiMacroName** | **String** |  |  [optional] |
|**uiMacroRunId** | **UUID** |  |  [optional] |
|**browserActionType** | **BrowserActionType** |  |  [optional] |
|**selector** | **String** |  |  [optional] |
|**value** | **String** |  |  [optional] |
|**variableName** | **String** |  |  [optional] |
|**browserPageUrl** | **String** |  |  [optional] |
|**browserPageTitle** | **String** |  |  [optional] |
|**browserFailureCode** | **String** |  |  [optional] |
|**browserFailureMessage** | **String** |  |  [optional] |
|**visualComparison** | [**BrowserVisualComparisonSummary**](BrowserVisualComparisonSummary.md) |  |  [optional] |
|**stepStatus** | **String** |  |  |
|**uiMacroFailureCode** | **String** |  |  [optional] |
|**uiMacroFailureMessage** | **String** |  |  [optional] |
|**testStepRun** | **Map&lt;String, Object&gt;** | Engine-native specification result; Browser steps do not fabricate an API result. |  [optional] |



## Enum: StepTypeEnum

| Name | Value |
|---- | -----|
| API_SPEC | &quot;API_SPEC&quot; |
| UI_MACRO | &quot;UI_MACRO&quot; |
| BROWSER_ACTION | &quot;BROWSER_ACTION&quot; |



