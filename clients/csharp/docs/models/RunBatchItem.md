# SpecTestEngine.Sdk.Model.RunBatchItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ItemId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SubjectType** | **SnapshotSubjectType** |  |
**SubjectId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SubjectKey** | **string** |  |
**SubjectName** | **string** |  |
**SourceRunType** | **SnapshotSourceRunType** |  |
**SourceRunId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Status** | **string** |  |
**RecordedAt** | **DateTimeOffset** |  |
**DefinitionHash** | **string** |  | [optional]
**BehaviorHash** | **string** |  | [optional]
**DefinitionPayload** | **Object** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**BehaviorPayload** | **Object** | A JSON value whose shape depends on the captured test subject and step type. | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

