# SpecTestEngine.Sdk.Model.BrowserNetworkExpectation
Local checks over observed browser traffic, never a second HTTP send. Candidates are not executable checks. Recorded credentials are rejected; current-run bindings are private and optional. Body and headers constrain the request; expectedBody and expectedHeaders constrain the response. Explicit empty response-header objects are checks. Unsupported OpenAPI/schema/attachment assertions are rejected, not processed by Browser.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | **bool** |  | [optional]
**Policy** | **string** | Per-Event policy. IGNORE keeps automatic source capture active without requiring refresh presence. | [optional]
**RecordedCallId** | **int** |  | [optional]
**RecordedUrl** | **string** |  | [optional]
**Method** | **string** |  | [optional]
**Url** | **string** |  | [optional]
**ExpectedStatusCode** | **int** |  | [optional]
**CandidateStatusCode** | **int** |  | [optional]
**ExpectedContentType** | **string** |  | [optional]
**CandidateContentType** | **string** |  | [optional]
**ExpectedHeaders** | **Dictionary&lt;string, string&gt;** |  | [optional]
**CandidateHeaders** | **Dictionary&lt;string, string&gt;** |  | [optional]
**ExcludedHeaderFields** | **List&lt;string&gt;** |  | [optional]
**ExcludeAllOtherHeaderFields** | **bool** |  | [optional]
**Body** | **Object** |  | [optional]
**CandidateBody** | **Object** |  | [optional]
**ExpectedBodyPaths** | [**List&lt;BrowserPathExpectation&gt;**](BrowserPathExpectation.md) |  | [optional]
**ExpectedHeaderPaths** | [**List&lt;BrowserPathExpectation&gt;**](BrowserPathExpectation.md) |  | [optional]
**Stream** | [**BrowserStreamMessage**](BrowserStreamMessage.md) |  | [optional]
**CandidateBodyPaths** | **Dictionary&lt;string, Object&gt;** |  | [optional]
**ExcludedBodyFields** | **List&lt;string&gt;** |  | [optional]
**Headers** | **Dictionary&lt;string, string&gt;** | Expected request headers; values may use ${runtime.name} from a prior declared current-run response source. | [optional]
**ExpectedBody** | **Object** | Complete expected response JSON value, including explicit null; absence disables this criterion. Partial or unavailable captured bodies cannot pass. | [optional]
**SkipExactBodyCheck** | **bool** |  | [optional]
**ExcludeAllOtherBodyFields** | **bool** | Include-only response-object comparison. Array include-only is unsupported in Browser. | [optional]
**Occurrence** | **int** | Select this request-start occurrence within its Action and method/URL matcher. Required by guided value-transfer relations; old recorded call IDs are not replay identity. | [optional]
**RequestBodyPaths** | [**List&lt;BrowserPathExpectation&gt;**](BrowserPathExpectation.md) | Focused outgoing Body checks. A complete runtime placeholder preserves the source JSON type; prefix/suffix text requires a string source. | [optional]
**CandidateFields** | [**BrowserNetworkFieldInventory**](BrowserNetworkFieldInventory.md) |  | [optional]
**AuthTransfer** | [**BrowserAuthTransfer**](BrowserAuthTransfer.md) |  | [optional]
**RuntimeBindings** | [**List&lt;BrowserNetworkRuntimeBinding&gt;**](BrowserNetworkRuntimeBinding.md) | Fresh private response sources, active independently of response assertion policy. Never contains a token value. Resume retains the same execution; full Rerun clears it. | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
