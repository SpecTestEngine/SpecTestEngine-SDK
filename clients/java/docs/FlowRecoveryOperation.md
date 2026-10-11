

# FlowRecoveryOperation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operationId** | **UUID** |  |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**flowId** | **UUID** |  |  [optional] |
|**failureCode** | **String** |  |  [optional] |
|**idempotencyKey** | **UUID** |  |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**manifestHash** | **String** |  |  |
|**copiedDependencies** | **Integer** |  |  |
|**totalDependencies** | **Integer** |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PREPARING | &quot;PREPARING&quot; |
| CREATING_DEPENDENCIES | &quot;CREATING_DEPENDENCIES&quot; |
| OUTCOME_UNKNOWN | &quot;OUTCOME_UNKNOWN&quot; |
| COMPLETED | &quot;COMPLETED&quot; |
