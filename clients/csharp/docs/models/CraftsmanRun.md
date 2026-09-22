# SpecTestEngine.Sdk.Model.CraftsmanRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RunId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**State** | **CraftsmanRunState** |  |
**CreatedAt** | **DateTimeOffset** |  |
**WorkspaceId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**NodeId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**Result** | [**RequestChainRun**](RequestChainRun.md) |  | [optional]
**Transcript** | **Object** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**ErrorMessage** | **string** |  | [optional]
**StartedAt** | **DateTimeOffset** |  | [optional]
**FinishedAt** | **DateTimeOffset** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

