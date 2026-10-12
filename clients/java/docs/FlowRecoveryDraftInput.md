

# FlowRecoveryDraftInput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**manifestHash** | **String** |  |  |
|**mode** | [**ModeEnum**](#ModeEnum) |  |  |
|**draft** | **Map&lt;String, Object&gt;** | Ordinary Flow create/update authoring shape, up to 16 MiB. Preserve retained visual references for owner validation. |  |
|**expectedFlowRevision** | **Long** |  |  |
|**sourceStepIds** | **List&lt;UUID&gt;** | One original occurrence UUID per ordered draft step, or null for an added step. Identity does not grant authority. |  |
|**dependencyRevisions** | **Map&lt;String, Long&gt;** |  |  |
|**bindings** | **Map&lt;String, Object&gt;** | Exactly required selected bindings. Preserve scalar types; never invent old literal inputs. Not retained in the journal. |  |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| RESTORE | &quot;RESTORE&quot; |
| COPY | &quot;COPY&quot; |
