# SpecTestEngine.Sdk.Model.FlowRecoveryHistoricalDefinition
Read-only historical Flow, not the live Flow. Creation timestamps are not evidence of the original authoring time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FlowId** | **Guid** |  |
**Name** | **string** |  |
**Steps** | [**List&lt;FlowStep&gt;**](FlowStep.md) |  |
**Description** | **string** |  | [optional]
**GlobalVariableFallbacks** | **Dictionary&lt;string, string&gt;** |  | [optional]
**BrowserStartUrl** | **string** |  | [optional]
**BrowserViewportWidth** | **int** |  | [optional]
**BrowserViewportHeight** | **int** |  | [optional]
**BrowserViewportPreset** | **string** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
