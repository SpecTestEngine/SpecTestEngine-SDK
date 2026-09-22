

# FlowStep


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stepId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**orderIndex** | **Integer** |  |  |
|**flowName** | **String** |  |  [optional] |
|**stepType** | [**StepTypeEnum**](#StepTypeEnum) |  |  |
|**specId** | **UUID** |  |  [optional] |
|**specType** | **SpecType** |  |  [optional] |
|**specName** | **String** |  |  [optional] |
|**uiMacroId** | **UUID** |  |  [optional] |
|**uiMacroName** | **String** |  |  [optional] |
|**browserActionType** | **BrowserActionType** |  |  [optional] |
|**selector** | **String** |  |  [optional] |
|**selectorCandidates** | **List&lt;String&gt;** |  |  [optional] |
|**value** | **String** |  |  [optional] |
|**variableName** | **String** |  |  [optional] |
|**tabAlias** | **String** |  |  [optional] |
|**frameSelector** | **String** |  |  [optional] |
|**pattern** | **String** |  |  [optional] |
|**extractionHint** | **String** |  |  [optional] |
|**textSource** | [**TextSourceEnum**](#TextSourceEnum) |  |  [optional] |
|**expectedPageUrl** | **String** |  |  [optional] |
|**expectedPageUrlPolicy** | [**ExpectedPageUrlPolicyEnum**](#ExpectedPageUrlPolicyEnum) |  |  [optional] |
|**expectedPageTitle** | **String** |  |  [optional] |
|**expectedPageTitlePolicy** | [**ExpectedPageTitlePolicyEnum**](#ExpectedPageTitlePolicyEnum) |  |  [optional] |
|**expectedNetworkPolicy** | [**ExpectedNetworkPolicyEnum**](#ExpectedNetworkPolicyEnum) |  |  [optional] |
|**visualAssertion** | [**BrowserVisualAssertion**](BrowserVisualAssertion.md) |  |  [optional] |
|**expectedNetworkCalls** | [**List&lt;BrowserNetworkExpectation&gt;**](BrowserNetworkExpectation.md) |  |  [optional] |
|**storeValues** | **Map&lt;String, String&gt;** |  |  [optional] |
|**overrideValues** | **Map&lt;String, Object&gt;** |  |  [optional] |



## Enum: StepTypeEnum

| Name | Value |
|---- | -----|
| API_SPEC | &quot;API_SPEC&quot; |
| UI_MACRO | &quot;UI_MACRO&quot; |
| BROWSER_ACTION | &quot;BROWSER_ACTION&quot; |



## Enum: TextSourceEnum

| Name | Value |
|---- | -----|
| ELEMENT_TEXT | &quot;ELEMENT_TEXT&quot; |
| TEXT_BLOCK | &quot;TEXT_BLOCK&quot; |



## Enum: ExpectedPageUrlPolicyEnum

| Name | Value |
|---- | -----|
| IGNORE | &quot;IGNORE&quot; |
| CORE | &quot;CORE&quot; |
| EXACT | &quot;EXACT&quot; |



## Enum: ExpectedPageTitlePolicyEnum

| Name | Value |
|---- | -----|
| IGNORE | &quot;IGNORE&quot; |
| EXACT | &quot;EXACT&quot; |
| CONTAINS | &quot;CONTAINS&quot; |



## Enum: ExpectedNetworkPolicyEnum

| Name | Value |
|---- | -----|
| IGNORE | &quot;IGNORE&quot; |
| PRESENCE | &quot;PRESENCE&quot; |
| STRICT | &quot;STRICT&quot; |



