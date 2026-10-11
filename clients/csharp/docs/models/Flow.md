# SpecTestEngine.Sdk.Model.Flow
Saved Flow read model. Browser action fields are flattened on each step; create/update use FlowInput with nested browserAction instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FlowId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Name** | **string** |  |
**Steps** | [**List&lt;FlowStep&gt;**](FlowStep.md) |  |
**CreatedAt** | **DateTimeOffset** |  |
**Description** | **string** |  | [optional]
**GlobalVariableFallbacks** | **Dictionary&lt;string, string&gt;** |  | [optional]
**BrowserStartUrl** | **string** |  | [optional]
**BrowserViewportWidth** | **int** |  | [optional]
**BrowserViewportHeight** | **int** |  | [optional]
**BrowserViewportPreset** | **string** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
