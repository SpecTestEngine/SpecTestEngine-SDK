

# FlowRecoveryInput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**manifestHash** | **String** |  |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**bindings** | **Map&lt;String, Object&gt;** | Exactly the binding keys requested by preview. Values must be scalar strings, numbers or booleans with their declared type, or variable placeholders; nested objects and null are rejected. Total encoded bindings at most 4 MiB. Values are not retained in the operation journal. |  |
