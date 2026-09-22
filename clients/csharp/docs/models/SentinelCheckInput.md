# SpecTestEngine.Sdk.Model.SentinelCheckInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**VarEnvironment** | **string** | Immutable environment scope for the check and its runs. |
**Type** | **string** |  |
**Format** | **ContentFormat** |  |
**Definition** | **string** |  |
**Description** | **string** |  | [optional]
**SourceName** | **string** |  | [optional]
**SpecType** | **SpecType** | Required when type is SPEC and prohibited when type is FLOW or URL. | [optional]
**Active** | **bool** |  | [optional] [default to true]
**TimeoutMs** | **long** |  | [optional] [default to 10000]
**FailureStrategy** | **string** |  | [optional] [default to FailureStrategyEnum.FAILFAST]
**MaxRetries** | **int** |  | [optional] [default to 3]
**RetryDelayMinMs** | **long** |  | [optional] [default to 5000]
**RetryDelayMaxMs** | **long** |  | [optional] [default to 10000]
**CircuitBreakerFailureThreshold** | **int** |  | [optional] [default to 5]
**CooldownMs** | **long** |  | [optional] [default to 300000]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

