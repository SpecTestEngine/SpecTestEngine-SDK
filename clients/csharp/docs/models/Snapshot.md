# SpecTestEngine.Sdk.Model.Snapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Sprint** | **string** |  |
**SourceBatchId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SelectionPolicy** | **SnapshotSelectionPolicy** |  |
**VarEnvironment** | **string** |  |
**SnapshotId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Status** | **SnapshotStatus** |  |
**Flows** | [**List&lt;SnapshotItem&gt;**](SnapshotItem.md) | Captured specification, UI macro, and flow evidence retained by the snapshot. |
**CreatedAt** | **DateTimeOffset** |  |
**Description** | **string** |  | [optional]
**ParentSnapshotId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**BatchItemIds** | **List&lt;Guid&gt;** |  | [optional]
**BranchName** | **string** |  | [optional]
**BackendCommit** | **string** |  | [optional]
**FrontendCommit** | **string** |  | [optional]
**CreatedBy** | **string** |  | [optional]
**ApprovedAt** | **DateTimeOffset** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

