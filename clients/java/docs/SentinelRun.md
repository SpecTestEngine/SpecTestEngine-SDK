

# SentinelRun


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**executionId** | **String** |  |  |
|**environment** | **String** | Environment captured when the run was queued. |  |
|**checkId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**checkName** | **String** |  |  |
|**checkType** | [**CheckTypeEnum**](#CheckTypeEnum) |  |  |
|**definitionHash** | **String** |  |  |
|**behaviorHash** | **String** | Assertion-relevant behavior fingerprint of the completed run; null while unavailable. |  [optional] |
|**region** | **String** |  |  |
|**triggerType** | **String** |  |  |
|**status** | **RunStatus** |  |  |
|**errorType** | **String** |  |  [optional] |
|**finalStatusCode** | **Integer** |  |  [optional] |
|**latencyMs** | **Long** |  |  [optional] |
|**responseSizeBytes** | **Long** |  |  [optional] |
|**errorMessage** | **String** |  |  [optional] |
|**resultLog** | **String** |  |  [optional] |
|**queuedAt** | **OffsetDateTime** |  |  |
|**startedAt** | **OffsetDateTime** |  |  [optional] |
|**finishedAt** | **OffsetDateTime** |  |  [optional] |
|**attempts** | **List&lt;Map&lt;String, Object&gt;&gt;** |  |  [optional] |
|**baseline** | [**SentinelRunBaseline**](SentinelRunBaseline.md) |  |  [optional] |



## Enum: CheckTypeEnum

| Name | Value |
|---- | -----|
| SPEC | &quot;SPEC&quot; |
| FLOW | &quot;FLOW&quot; |
| URL | &quot;URL&quot; |



