

# CraftsmanRun


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**runId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**workspaceId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  [optional] |
|**nodeId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  [optional] |
|**state** | **CraftsmanRunState** |  |  |
|**result** | [**RequestChainRun**](RequestChainRun.md) |  |  [optional] |
|**transcript** | **Object** | A JSON value whose shape depends on the captured test subject and step type. |  [optional] |
|**errorMessage** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  |
|**startedAt** | **OffsetDateTime** |  |  [optional] |
|**finishedAt** | **OffsetDateTime** |  |  [optional] |



