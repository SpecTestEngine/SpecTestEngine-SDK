# SpecTestEngine.Sdk.Model.BrowserActionInput
One persisted semantic Browser action. Replay tries only the saved selector candidates in order; missing or ambiguous targets fail explicitly. No selector or visual-change guessing is performed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ActionType** | **BrowserActionType** |  |
**OrderIndex** | **int** |  | [optional]
**Selector** | **string** |  | [optional]
**SelectorCandidates** | **List&lt;string&gt;** |  | [optional]
**Value** | **string** | Action value or explicit variable template. EXTRACT_TEXT captures a fresh value on every run; a later FILL uses that variable, never a recorded OTP sample. | [optional]
**Sensitive** | **bool** | Explicit sensitive-action marker. Persist variable references, not secret literal values. | [optional]
**TimeoutMs** | **long** |  | [optional] [default to 20000]
**TabAlias** | **string** |  | [optional]
**FrameSelector** | **string** |  | [optional]
**VariableName** | **string** |  | [optional]
**Pattern** | **string** |  | [optional]
**ExtractionHint** | **string** |  | [optional]
**TextSource** | **string** |  | [optional]
**ExpectedPageUrl** | **string** |  | [optional]
**ExpectedPageUrlPolicy** | **string** |  | [optional]
**ExpectedPageTitle** | **string** |  | [optional]
**ExpectedPageTitlePolicy** | **string** |  | [optional]
**ExpectedNetworkPolicy** | **string** |  | [optional]
**ExpectedNetworkCalls** | [**List&lt;BrowserNetworkExpectation&gt;**](BrowserNetworkExpectation.md) |  | [optional]
**VisualAssertion** | [**BrowserVisualAssertionInput**](BrowserVisualAssertionInput.md) |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
