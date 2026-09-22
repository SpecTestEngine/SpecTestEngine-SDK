

# RequestNode


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**parentNodeId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  [optional] |
|**orderIndex** | **Integer** |  |  [optional] |
|**request** | [**SavedRequestInput**](SavedRequestInput.md) |  |  [optional] |
|**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FOLDER | &quot;FOLDER&quot; |
| REQUEST | &quot;REQUEST&quot; |



