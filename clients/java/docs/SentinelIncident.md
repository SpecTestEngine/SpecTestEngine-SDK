

# SentinelIncident


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**environment** | **String** |  |  |
|**checkId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**checkName** | **String** |  |  |
|**fingerprint** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**consecutiveFailures** | **Integer** |  |  |
|**lastRunId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  [optional] |
|**summary** | **String** |  |  [optional] |
|**startedAt** | **OffsetDateTime** |  |  [optional] |
|**resolvedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;OPEN&quot; |
| RESOLVED | &quot;RESOLVED&quot; |



