

# Flow

Saved Flow read model. Browser action fields are flattened on each step; create/update use FlowInput with nested browserAction instead.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**flowId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**globalVariableFallbacks** | **Map&lt;String, String&gt;** |  |  [optional] |
|**browserStartUrl** | **String** |  |  [optional] |
|**browserViewportWidth** | **Integer** |  |  [optional] |
|**browserViewportHeight** | **Integer** |  |  [optional] |
|**browserViewportPreset** | [**BrowserViewportPresetEnum**](#BrowserViewportPresetEnum) |  |  [optional] |
|**steps** | [**List&lt;FlowStep&gt;**](FlowStep.md) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |



## Enum: BrowserViewportPresetEnum

| Name | Value |
|---- | -----|
| MOBILE | &quot;MOBILE&quot; |
| TABLET | &quot;TABLET&quot; |
| DESKTOP | &quot;DESKTOP&quot; |
| CUSTOM | &quot;CUSTOM&quot; |
