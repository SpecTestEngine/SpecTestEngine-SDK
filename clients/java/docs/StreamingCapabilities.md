

# StreamingCapabilities


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**engine** | [**EngineEnum**](#EngineEnum) |  |  |
|**storage** | **String** |  |  |
|**formats** | [**List&lt;FormatsEnum&gt;**](#List&lt;FormatsEnum&gt;) |  |  |
|**transports** | **List&lt;StreamingTransport&gt;** |  |  |
|**schemes** | **Map&lt;String, List&lt;String&gt;&gt;** |  |  |
|**codecs** | **List&lt;String&gt;** |  |  |
|**actions** | **List&lt;String&gt;** |  |  |
|**eventAssertionFields** | **List&lt;String&gt;** |  |  |
|**limits** | [**StreamingLimits**](StreamingLimits.md) |  |  |



## Enum: EngineEnum

| Name | Value |
|---- | -----|
| STREAMING | &quot;STREAMING&quot; |



## Enum: List&lt;FormatsEnum&gt;

| Name | Value |
|---- | -----|
| JSON | &quot;JSON&quot; |
| YAML | &quot;YAML&quot; |



