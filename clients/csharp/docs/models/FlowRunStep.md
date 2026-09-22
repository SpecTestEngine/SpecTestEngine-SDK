# SpecTestEngine.Sdk.Model.FlowRunStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StepId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**OrderIndex** | **int** |  |
**StepType** | **string** |  |
**StepStatus** | **string** |  |
**SpecName** | **string** |  | [optional]
**UiMacroId** | **Guid** |  | [optional]
**UiMacroName** | **string** |  | [optional]
**UiMacroRunId** | **Guid** |  | [optional]
**BrowserActionType** | **BrowserActionType** |  | [optional]
**Selector** | **string** |  | [optional]
**Value** | **string** |  | [optional]
**VariableName** | **string** |  | [optional]
**BrowserPageUrl** | **string** |  | [optional]
**BrowserPageTitle** | **string** |  | [optional]
**BrowserFailureCode** | **string** |  | [optional]
**BrowserFailureMessage** | **string** |  | [optional]
**VisualComparison** | [**BrowserVisualComparisonSummary**](BrowserVisualComparisonSummary.md) |  | [optional]
**UiMacroFailureCode** | **string** |  | [optional]
**UiMacroFailureMessage** | **string** |  | [optional]
**TestStepRun** | **Dictionary&lt;string, Object&gt;** | Engine-native specification result; Browser steps do not fabricate an API result. | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

