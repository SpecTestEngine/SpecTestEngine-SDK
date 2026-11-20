

# BrowserStreamMessage

Observed stream message metadata. SSE only supports INBOUND. This never sends another request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**transport** | [**TransportEnum**](#TransportEnum) |  |  |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  |
|**eventName** | **String** |  |  [optional] |
|**binary** | **Boolean** |  |  [optional] |
|**failed** | **Boolean** |  |  [optional] |



## Enum: TransportEnum

| Name | Value |
|---- | -----|
| WEBSOCKET | &quot;WEBSOCKET&quot; |
| SSE | &quot;SSE&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INBOUND | &quot;INBOUND&quot; |
| OUTBOUND | &quot;OUTBOUND&quot; |
