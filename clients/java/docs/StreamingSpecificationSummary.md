

# StreamingSpecificationSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**specType** | [**SpecTypeEnum**](#SpecTypeEnum) |  |  |
|**transport** | **StreamingTransport** |  |  |
|**endpoint** | **String** | Streaming endpoint URI |  |
|**codec** | [**CodecEnum**](#CodecEnum) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**lastRunAt** | **OffsetDateTime** |  |  [optional] |
|**lastRunStatus** | **String** |  |  [optional] |



## Enum: SpecTypeEnum

| Name | Value |
|---- | -----|
| STREAMING | &quot;STREAMING&quot; |



## Enum: CodecEnum

| Name | Value |
|---- | -----|
| JSON | &quot;JSON&quot; |
| TEXT | &quot;TEXT&quot; |
| XML | &quot;XML&quot; |
| BINARY | &quot;BINARY&quot; |
| PROTOBUF_JSON | &quot;PROTOBUF_JSON&quot; |
