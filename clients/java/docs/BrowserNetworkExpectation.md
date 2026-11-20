

# BrowserNetworkExpectation

Local checks over observed browser traffic, never a second HTTP send. Candidates are not executable checks. Recorded credentials are rejected; current-run bindings are private and optional. Body and headers constrain the request; expectedBody and expectedHeaders constrain the response. Explicit empty response-header objects are checks. Unsupported OpenAPI/schema/attachment assertions are rejected, not processed by Browser.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** |  |  [optional] |
|**policy** | [**PolicyEnum**](#PolicyEnum) | Per-Event policy. IGNORE keeps automatic source capture active without requiring refresh presence. |  [optional] |
|**recordedCallId** | **Integer** |  |  [optional] |
|**recordedUrl** | **String** |  |  [optional] |
|**method** | **String** |  |  [optional] |
|**url** | **String** |  |  [optional] |
|**expectedStatusCode** | **Integer** |  |  [optional] |
|**candidateStatusCode** | **Integer** |  |  [optional] |
|**expectedContentType** | **String** |  |  [optional] |
|**candidateContentType** | **String** |  |  [optional] |
|**expectedHeaders** | **Map&lt;String, String&gt;** |  |  [optional] |
|**candidateHeaders** | **Map&lt;String, String&gt;** |  |  [optional] |
|**excludedHeaderFields** | **List&lt;String&gt;** |  |  [optional] |
|**excludeAllOtherHeaderFields** | **Boolean** |  |  [optional] |
|**body** | **Object** |  |  [optional] |
|**candidateBody** | **Object** |  |  [optional] |
|**expectedBodyPaths** | [**List&lt;BrowserPathExpectation&gt;**](BrowserPathExpectation.md) |  |  [optional] |
|**expectedHeaderPaths** | [**List&lt;BrowserPathExpectation&gt;**](BrowserPathExpectation.md) |  |  [optional] |
|**stream** | [**BrowserStreamMessage**](BrowserStreamMessage.md) |  |  [optional] |
|**candidateBodyPaths** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**excludedBodyFields** | **List&lt;String&gt;** |  |  [optional] |
|**headers** | **Map&lt;String, String&gt;** | Expected request headers; values may use ${runtime.name} from a prior declared current-run response source. |  [optional] |
|**expectedBody** | **Object** | Complete expected response JSON value, including explicit null; absence disables this criterion. Partial or unavailable captured bodies cannot pass. |  [optional] |
|**skipExactBodyCheck** | **Boolean** |  |  [optional] |
|**excludeAllOtherBodyFields** | **Boolean** | Include-only response-object comparison. Array include-only is unsupported in Browser. |  [optional] |
|**occurrence** | **Integer** | Select this request-start occurrence within its Action and method/URL matcher. Required by guided value-transfer relations; old recorded call IDs are not replay identity. |  [optional] |
|**requestBodyPaths** | [**List&lt;BrowserPathExpectation&gt;**](BrowserPathExpectation.md) | Focused outgoing Body checks. A complete runtime placeholder preserves the source JSON type; prefix/suffix text requires a string source. |  [optional] |
|**candidateFields** | [**BrowserNetworkFieldInventory**](BrowserNetworkFieldInventory.md) |  |  [optional] |
|**authTransfer** | [**BrowserAuthTransfer**](BrowserAuthTransfer.md) |  |  [optional] |
|**runtimeBindings** | [**List&lt;BrowserNetworkRuntimeBinding&gt;**](BrowserNetworkRuntimeBinding.md) | Fresh private response sources, active independently of response assertion policy. Never contains a token value. Resume retains the same execution; full Rerun clears it. |  [optional] |



## Enum: PolicyEnum

| Name | Value |
|---- | -----|
| IGNORE | &quot;IGNORE&quot; |
| PRESENCE | &quot;PRESENCE&quot; |
| STRICT | &quot;STRICT&quot; |
