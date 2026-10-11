

# FlowStepInput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stepType** | [**StepTypeEnum**](#StepTypeEnum) |  |  |
|**orderIndex** | **Integer** |  |  |
|**specId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  [optional] |
|**specType** | **SpecType** |  |  [optional] |
|**specName** | **String** |  |  [optional] |
|**uiMacroId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  [optional] |
|**uiMacro** | [**BrowserMacroInput**](BrowserMacroInput.md) |  |  [optional] |
|**browserAction** | [**BrowserActionInput**](BrowserActionInput.md) |  |  [optional] |
|**storeValues** | **Map&lt;String, String&gt;** |  |  [optional] |
|**overrideValues** | **Map&lt;String, Object&gt;** |  |  [optional] |



## Enum: StepTypeEnum

| Name | Value |
|---- | -----|
| API_SPEC | &quot;API_SPEC&quot; |
| UI_MACRO | &quot;UI_MACRO&quot; |
| BROWSER_ACTION | &quot;BROWSER_ACTION&quot; |
