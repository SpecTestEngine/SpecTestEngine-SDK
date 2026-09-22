

# Specification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**specType** | **SpecType** |  |  |
|**method** | [**MethodEnum**](#MethodEnum) | HTTP method from a REST specification request. |  [optional] |
|**url** | **String** | Request URL from a REST specification. |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  |
|**lastRunAt** | **OffsetDateTime** |  |  [optional] |
|**lastRunStatus** | **String** |  |  [optional] |
|**stableKey** | **String** |  |  [optional] |
|**format** | **ContentFormat** |  |  |
|**rawSpec** | **String** |  |  |
|**spec** | **Map&lt;String, Object&gt;** |  |  |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PUT | &quot;PUT&quot; |
| PATCH | &quot;PATCH&quot; |
| DELETE | &quot;DELETE&quot; |
| HEAD | &quot;HEAD&quot; |



