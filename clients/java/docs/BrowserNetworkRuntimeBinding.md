

# BrowserNetworkRuntimeBinding


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**source** | [**SourceEnum**](#SourceEnum) |  |  |
|**path** | **String** |  |  |
|**scopeOrigin** | **String** | Optional explicit HTTP(S) origin for later matching calls; no credentials, path, query or fragment. Defaults to the source call origin. |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| RESPONSE_BODY | &quot;RESPONSE_BODY&quot; |
| RESPONSE_HEADER | &quot;RESPONSE_HEADER&quot; |
