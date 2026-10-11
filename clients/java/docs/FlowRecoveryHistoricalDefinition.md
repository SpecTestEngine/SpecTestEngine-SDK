

# FlowRecoveryHistoricalDefinition

Read-only historical Flow, not the live Flow. Creation timestamps are not evidence of the original authoring time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**flowId** | **UUID** |  |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**globalVariableFallbacks** | **Map&lt;String, String&gt;** |  |  [optional] |
|**browserStartUrl** | **String** |  |  [optional] |
|**browserViewportWidth** | **Integer** |  |  [optional] |
|**browserViewportHeight** | **Integer** |  |  [optional] |
|**browserViewportPreset** | **String** |  |  [optional] |
|**steps** | [**List&lt;FlowStep&gt;**](FlowStep.md) |  |  |
