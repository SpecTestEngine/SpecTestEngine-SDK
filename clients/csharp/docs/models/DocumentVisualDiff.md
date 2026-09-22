# SpecTestEngine.Sdk.Model.DocumentVisualDiff

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**VisualDiffId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**ViewerUrl** | **string** |  |
**SourceType** | **string** |  |
**AttachmentId** | **string** |  |
**ActualContentType** | **string** |  |
**ActualSha256** | **string** |  |
**Status** | **DocumentVisualDiffStatus** |  |
**Decision** | **DocumentVisualDiffDecision** |  |
**ActualPageCount** | **int** |  |
**CreatedAt** | **DateTimeOffset** |  |
**ExpiresAt** | **DateTimeOffset** |  |
**ActualAvailable** | **bool** |  |
**ExpectedUploadRequired** | **bool** |  |
**RegenerateAvailable** | **bool** |  |
**Generations** | [**List&lt;DocumentVisualDiffGeneration&gt;**](DocumentVisualDiffGeneration.md) |  |
**SourceRunId** | **string** |  | [optional]
**SourceStepId** | **string** |  | [optional]
**ExpectedSha256** | **string** |  | [optional]
**CurrentGeneration** | [**DocumentVisualDiffGeneration**](DocumentVisualDiffGeneration.md) |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

