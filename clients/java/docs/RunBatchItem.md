

# RunBatchItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**itemId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**subjectType** | **SnapshotSubjectType** |  |  |
|**subjectId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**subjectKey** | **String** |  |  |
|**subjectName** | **String** |  |  |
|**sourceRunType** | **SnapshotSourceRunType** |  |  |
|**sourceRunId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**status** | **String** |  |  |
|**definitionHash** | **String** |  |  [optional] |
|**behaviorHash** | **String** |  |  [optional] |
|**definitionPayload** | **Object** | A JSON value whose shape depends on the captured test subject and step type. |  [optional] |
|**behaviorPayload** | **Object** | A JSON value whose shape depends on the captured test subject and step type. |  [optional] |
|**recordedAt** | **OffsetDateTime** |  |  |



