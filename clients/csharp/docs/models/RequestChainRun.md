# SpecTestEngine.Sdk.Model.RequestChainRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WorkspaceId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**RequestNodeId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**FlowName** | **string** |  |
**OverallTestFlowStatus** | **string** |  |
**Steps** | **List&lt;Dictionary&lt;string, Object&gt;&gt;** |  |
**Context** | **Dictionary&lt;string, Object&gt;** | Values explicitly captured during this run. Workflow/global input values and secret sources are not echoed here. |
**StartedAt** | **DateTimeOffset** |  |
**FinishedAt** | **DateTimeOffset** |  |
**Description** | **string** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

