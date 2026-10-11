

# SentinelCheckInput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**sourceName** | **String** |  |  [optional] |
|**environment** | **String** | Immutable environment scope for the check and its runs. |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**specType** | **SpecType** | Required when type is SPEC and prohibited when type is FLOW or URL. |  [optional] |
|**format** | **ContentFormat** |  |  |
|**definition** | **String** |  |  |
|**active** | **Boolean** |  |  [optional] |
|**timeoutMs** | **Long** |  |  [optional] |
|**failureStrategy** | [**FailureStrategyEnum**](#FailureStrategyEnum) |  |  [optional] |
|**maxRetries** | **Integer** |  |  [optional] |
|**retryDelayMinMs** | **Long** |  |  [optional] |
|**retryDelayMaxMs** | **Long** |  |  [optional] |
|**circuitBreakerFailureThreshold** | **Integer** |  |  [optional] |
|**cooldownMs** | **Long** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SPEC | &quot;SPEC&quot; |
| FLOW | &quot;FLOW&quot; |
| URL | &quot;URL&quot; |



## Enum: FailureStrategyEnum

| Name | Value |
|---- | -----|
| FAIL_FAST | &quot;FAIL_FAST&quot; |
| CONTINUE_ON_ERROR | &quot;CONTINUE_ON_ERROR&quot; |
