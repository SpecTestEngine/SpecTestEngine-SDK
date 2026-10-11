

# StreamingRun


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**specId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  [optional] |
|**specName** | **String** |  |  |
|**specStableKey** | **String** |  |  [optional] |
|**specType** | [**SpecTypeEnum**](#SpecTypeEnum) |  |  |
|**format** | [**FormatEnum**](#FormatEnum) |  |  |
|**transport** | **StreamingTransport** |  |  |
|**definitionHash** | **String** |  |  |
|**state** | **StreamingRunState** |  |  |
|**outcome** | **StreamingRunOutcome** |  |  [optional] |
|**terminationReason** | **String** |  |  [optional] |
|**eventCount** | **Long** |  |  |
|**byteCount** | **Long** |  |  |
|**assertionPassCount** | **Integer** |  |  |
|**assertionFailCount** | **Integer** |  |  |
|**evidenceSummary** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**errorMessage** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  |
|**startedAt** | **OffsetDateTime** |  |  [optional] |
|**finishedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: SpecTypeEnum

| Name | Value |
|---- | -----|
| STREAMING | &quot;STREAMING&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| JSON | &quot;JSON&quot; |
| YAML | &quot;YAML&quot; |
