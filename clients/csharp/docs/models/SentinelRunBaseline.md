# SpecTestEngine.Sdk.Model.SentinelRunBaseline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Status** | **RunStatus** |  |
**Label** | **string** |  |
**DefinitionHash** | **string** |  |
**BehaviorHash** | **string** | Assertion-relevant fingerprint; raw transport payloads and explicitly excluded evidence do not affect it. | [optional]
**ResponseHeadersJson** | **string** |  | [optional]
**ResponseBodyPreview** | **string** |  | [optional]
**ResultLog** | **string** |  | [optional]
**ErrorMessage** | **string** |  | [optional]
**FinishedAt** | **DateTimeOffset** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
