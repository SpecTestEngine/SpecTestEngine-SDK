

# BrowserAuthSource


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**source** | [**SourceEnum**](#SourceEnum) |  |  |
|**path** | **String** |  |  |
|**scopeOrigin** | **URI** | Exact HTTP(S) origin without credentials, path, query or fragment. |  |
|**updateFrom** | [**BrowserAuthGuard**](BrowserAuthGuard.md) |  |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| RESPONSE_BODY | &quot;RESPONSE_BODY&quot; |
| RESPONSE_HEADER | &quot;RESPONSE_HEADER&quot; |
| RESPONSE_COOKIE | &quot;RESPONSE_COOKIE&quot; |
