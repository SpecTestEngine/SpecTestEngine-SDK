# SpecTestEngine.Sdk.Model.FlowStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StepId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**OrderIndex** | **int** |  |
**StepType** | **string** |  |
**FlowName** | **string** |  | [optional]
**SpecId** | **Guid** |  | [optional]
**SpecType** | **SpecType** |  | [optional]
**SpecName** | **string** |  | [optional]
**UiMacroId** | **Guid** |  | [optional]
**UiMacroName** | **string** |  | [optional]
**BrowserActionType** | **BrowserActionType** |  | [optional]
**Selector** | **string** |  | [optional]
**TargetMatch** | [**BrowserTargetMatch**](BrowserTargetMatch.md) |  | [optional]
**SelectorCandidates** | **List&lt;string&gt;** |  | [optional]
**Value** | **string** |  | [optional]
**VariableName** | **string** |  | [optional]
**TabAlias** | **string** |  | [optional]
**FrameSelector** | **string** |  | [optional]
**Pattern** | **string** |  | [optional]
**ExtractionHint** | **string** |  | [optional]
**TextSource** | **string** |  | [optional]
**ExpectedPageUrl** | **string** |  | [optional]
**ExpectedPageUrlPolicy** | **string** |  | [optional]
**ExpectedPageTitle** | **string** |  | [optional]
**ExpectedPageTitlePolicy** | **string** |  | [optional]
**ExpectedNetworkPolicy** | **string** |  | [optional]
**VisualAssertion** | [**BrowserVisualAssertion**](BrowserVisualAssertion.md) |  | [optional]
**ExpectedNetworkCalls** | [**List&lt;BrowserNetworkExpectation&gt;**](BrowserNetworkExpectation.md) |  | [optional]
**StoreValues** | **Dictionary&lt;string, string&gt;** |  | [optional]
**OverrideValues** | **Dictionary&lt;string, Object&gt;** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
