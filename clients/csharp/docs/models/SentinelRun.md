# SpecTestEngine.Sdk.Model.SentinelRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**ExecutionId** | **string** |  |
**VarEnvironment** | **string** | Environment captured when the run was queued. |
**CheckId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**CheckName** | **string** |  |
**CheckType** | **string** |  |
**DefinitionHash** | **string** |  |
**Region** | **string** |  |
**TriggerType** | **string** |  |
**Status** | **RunStatus** |  |
**QueuedAt** | **DateTimeOffset** |  |
**BehaviorHash** | **string** | Assertion-relevant behavior fingerprint of the completed run; null while unavailable. | [optional]
**ErrorType** | **string** |  | [optional]
**FinalStatusCode** | **int** |  | [optional]
**LatencyMs** | **long** |  | [optional]
**ResponseSizeBytes** | **long** |  | [optional]
**ErrorMessage** | **string** |  | [optional]
**ResultLog** | **string** |  | [optional]
**StartedAt** | **DateTimeOffset** |  | [optional]
**FinishedAt** | **DateTimeOffset** |  | [optional]
**Attempts** | **List&lt;Dictionary&lt;string, Object&gt;&gt;** |  | [optional]
**Baseline** | [**SentinelRunBaseline**](SentinelRunBaseline.md) |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
