# SpecTestEngine.Sdk.Model.StreamingRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SpecName** | **string** |  |
**SpecType** | **string** |  |
**Format** | **string** |  |
**Transport** | **StreamingTransport** |  |
**DefinitionHash** | **string** |  |
**State** | **StreamingRunState** |  |
**EventCount** | **long** |  |
**ByteCount** | **long** |  |
**AssertionPassCount** | **int** |  |
**AssertionFailCount** | **int** |  |
**CreatedAt** | **DateTimeOffset** |  |
**SpecId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**SpecStableKey** | **string** |  | [optional]
**Outcome** | **StreamingRunOutcome** |  | [optional]
**TerminationReason** | **string** |  | [optional]
**EvidenceSummary** | **Dictionary&lt;string, Object&gt;** |  | [optional]
**ErrorMessage** | **string** |  | [optional]
**StartedAt** | **DateTimeOffset** |  | [optional]
**FinishedAt** | **DateTimeOffset** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
