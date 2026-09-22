

# BrowserActionInput

One persisted semantic Browser action. Replay tries only the saved selector candidates in order; missing or ambiguous targets fail explicitly. No selector or visual-change guessing is performed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**orderIndex** | **Integer** |  |  [optional] |
|**actionType** | **BrowserActionType** |  |  |
|**selector** | **String** |  |  [optional] |
|**selectorCandidates** | **List&lt;String&gt;** |  |  [optional] |
|**value** | **String** | Action value or explicit variable template. EXTRACT_TEXT captures a fresh value on every run; a later FILL uses that variable, never a recorded OTP sample. |  [optional] |
|**sensitive** | **Boolean** | Explicit sensitive-action marker. Persist variable references, not secret literal values. |  [optional] |
|**timeoutMs** | **Long** |  |  [optional] |
|**tabAlias** | **String** |  |  [optional] |
|**frameSelector** | **String** |  |  [optional] |
|**variableName** | **String** |  |  [optional] |
|**pattern** | **String** |  |  [optional] |
|**extractionHint** | **String** |  |  [optional] |
|**textSource** | [**TextSourceEnum**](#TextSourceEnum) |  |  [optional] |
|**expectedPageUrl** | **String** |  |  [optional] |
|**expectedPageUrlPolicy** | [**ExpectedPageUrlPolicyEnum**](#ExpectedPageUrlPolicyEnum) |  |  [optional] |
|**expectedPageTitle** | **String** |  |  [optional] |
|**expectedPageTitlePolicy** | [**ExpectedPageTitlePolicyEnum**](#ExpectedPageTitlePolicyEnum) |  |  [optional] |
|**expectedNetworkPolicy** | [**ExpectedNetworkPolicyEnum**](#ExpectedNetworkPolicyEnum) |  |  [optional] |
|**expectedNetworkCalls** | [**List&lt;BrowserNetworkExpectation&gt;**](BrowserNetworkExpectation.md) |  |  [optional] |
|**visualAssertion** | [**BrowserVisualAssertionInput**](BrowserVisualAssertionInput.md) |  |  [optional] |



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



