# SpecTestEngine.Sdk.Model.RunBatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**VarEnvironment** | **string** |  |
**BatchId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Items** | [**List&lt;RunBatchItem&gt;**](RunBatchItem.md) |  |
**CreatedAt** | **DateTimeOffset** |  |
**Description** | **string** |  | [optional]
**Sprint** | **string** |  | [optional]
**BackendCommit** | **string** |  | [optional]
**FrontendCommit** | **string** |  | [optional]
**BranchName** | **string** |  | [optional]
**TriggeredBy** | **string** |  | [optional]
**TriggerType** | **string** |  | [optional]
**Notes** | **string** |  | [optional]
**SpecRunIds** | **List&lt;Guid&gt;** |  | [optional]
**UiMacroRunIds** | **List&lt;Guid&gt;** |  | [optional]
**FlowRunIds** | **List&lt;Guid&gt;** |  | [optional]
**FinishedAt** | **DateTimeOffset** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
