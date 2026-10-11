# SpecTestEngine.Sdk.Api.GenerationApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CreateArtifactGenerationProfile**](GenerationApi.md#createartifactgenerationprofile) | **POST** /artifact-profiles | Create a CI export profile |
| [**DeleteArtifactGenerationProfile**](GenerationApi.md#deleteartifactgenerationprofile) | **DELETE** /artifact-profiles/{profileId} | Delete a CI export profile |
| [**DownloadArtifactGenerationProfileArchive**](GenerationApi.md#downloadartifactgenerationprofilearchive) | **POST** /artifact-profiles/{profileId}/environments/{environmentKey}/atf/archive | Validate and download a CI profile archive |
| [**DownloadAtfProject**](GenerationApi.md#downloadatfproject) | **POST** /atf/generate/download | Download a generated ATF project |
| [**GenerateFromOpenApiContent**](GenerationApi.md#generatefromopenapicontent) | **POST** /openapi/generate-from-content | Generate specifications and flows from OpenAPI content |
| [**GenerateSpecification**](GenerationApi.md#generatespecification) | **POST** /spec/generate | Generate an executable specification from concrete request evidence |
| [**GetArtifactGenerationProfile**](GenerationApi.md#getartifactgenerationprofile) | **GET** /artifact-profiles/{profileId} | Get a CI export profile |
| [**GetAtfProjectValidationResult**](GenerationApi.md#getatfprojectvalidationresult) | **GET** /atf/generate/validate/result/{validationId} | Get ATF validation status or result |
| [**ListArtifactGenerationProfiles**](GenerationApi.md#listartifactgenerationprofiles) | **GET** /artifact-profiles | List CI export profiles |
| [**ObserveAtfProjectValidation**](GenerationApi.md#observeatfprojectvalidation) | **GET** /atf/generate/validate/events/{validationId} | Observe ATF validation progress |
| [**PreviewAtfProject**](GenerationApi.md#previewatfproject) | **POST** /atf/generate/preview | Generate an ATF project preview |
| [**RefreshArtifactGenerationProfileBundle**](GenerationApi.md#refreshartifactgenerationprofilebundle) | **POST** /artifact-profiles/{profileId}/environments/{environmentKey}/bundle/refresh | Capture or refresh an environment baseline |
| [**StartAtfProjectValidation**](GenerationApi.md#startatfprojectvalidation) | **POST** /atf/generate/validate/start | Start asynchronous ATF compile validation |
| [**UpdateArtifactGenerationProfile**](GenerationApi.md#updateartifactgenerationprofile) | **PUT** /artifact-profiles/{profileId} | Update a CI export profile |
| [**ValidateAtfProject**](GenerationApi.md#validateatfproject) | **POST** /atf/generate/validate | Validate that an ATF project compiles |

<a id="createartifactgenerationprofile"></a>
# **CreateArtifactGenerationProfile**
> ArtifactGenerationProfile CreateArtifactGenerationProfile (ArtifactGenerationProfileInput artifactGenerationProfileInput, Guid idempotencyKey = null)

Create a CI export profile


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **artifactGenerationProfileInput** | [**ArtifactGenerationProfileInput**](ArtifactGenerationProfileInput.md) |  |  |
| **idempotencyKey** | **Guid** | A caller-generated UUID retained for safe write retries where supported. | [optional]  |

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored CI export profile. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="deleteartifactgenerationprofile"></a>
# **DeleteArtifactGenerationProfile**
> void DeleteArtifactGenerationProfile (Guid profileId)

Delete a CI export profile


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **profileId** | **Guid** | UUIDv7 identifier of a CI export profile. |  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The profile was deleted. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="downloadartifactgenerationprofilearchive"></a>
# **DownloadArtifactGenerationProfileArchive**
> System.IO.Stream DownloadArtifactGenerationProfileArchive (Guid profileId, string environmentKey)

Validate and download a CI profile archive

Resolves the environment policy, enforces drift rules, then returns an archive only after the generated project passes compile validation.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **profileId** | **Guid** | UUIDv7 identifier of a CI export profile. |  |
| **environmentKey** | **string** | Stable profile environment key such as test, staging, or production. |  |

### Return type

**System.IO.Stream**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A compile-validated ATF project archive. |  * Content-Disposition -  <br>  |
| **422** | The generated project did not pass readiness validation; no archive was returned. |  -  |
| **429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="downloadatfproject"></a>
# **DownloadAtfProject**
> System.IO.Stream DownloadAtfProject (AtfGenerationInput atfGenerationInput)

Download a generated ATF project


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **atfGenerationInput** | [**AtfGenerationInput**](AtfGenerationInput.md) |  |  |

### Return type

**System.IO.Stream**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A portable ATF project archive. |  * Content-Disposition -  <br>  |
| **422** | The generated project did not pass readiness validation; no archive was returned. |  -  |
| **429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="generatefromopenapicontent"></a>
# **GenerateFromOpenApiContent**
> OpenApiGenerationResult GenerateFromOpenApiContent (ContentFormat contentFormat, string body, bool includeNegativeTests = null, bool generateFlowScenarios = null, string generationStrategy = null, string negativeTestGenerationMode = null)

Generate specifications and flows from OpenAPI content


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **contentFormat** | **ContentFormat** |  |  |
| **body** | **string** |  |  |
| **includeNegativeTests** | **bool** |  | [optional] [default to false] |
| **generateFlowScenarios** | **bool** |  | [optional] [default to false] |
| **generationStrategy** | **string** |  | [optional] [default to SCHEMA_BASED] |
| **negativeTestGenerationMode** | **string** |  | [optional] [default to EXTENDED] |

### Return type

[**OpenApiGenerationResult**](OpenApiGenerationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated specification drafts, flow drafts, and operation coverage. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="generatespecification"></a>
# **GenerateSpecification**
> List&lt;SpecGenerationResult&gt; GenerateSpecification (Dictionary<string, Object> requestBody, string mode = null, ContentFormat format = null, List<string> specGenerationTypes = null)

Generate an executable specification from concrete request evidence

Generates a REST, SOAP, GraphQL, or Streaming specification. Streaming input may contain observedEvidence from a completed Craftsman session; generation derives expectations from that transcript and never opens a second connection. Workflow placeholders must be materialized before this endpoint is called.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **requestBody** | [**Dictionary&lt;string, Object&gt;**](Object.md) |  |  |
| **mode** | **string** |  | [optional] [default to FULL] |
| **format** | **ContentFormat** |  | [optional]  |
| **specGenerationTypes** | [**List&lt;string&gt;**](string.md) | Comma-separated generation variants. Streaming currently accepts POSITIVE only. | [optional]  |

### Return type

[**List&lt;SpecGenerationResult&gt;**](SpecGenerationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated executable specification variants. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getartifactgenerationprofile"></a>
# **GetArtifactGenerationProfile**
> ArtifactGenerationProfile GetArtifactGenerationProfile (Guid profileId)

Get a CI export profile


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **profileId** | **Guid** | UUIDv7 identifier of a CI export profile. |  |

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested profile. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getatfprojectvalidationresult"></a>
# **GetAtfProjectValidationResult**
> AtfValidationResult GetAtfProjectValidationResult (string validationId)

Get ATF validation status or result


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **validationId** | **string** | Opaque identifier of a bounded asynchronous ATF validation job. |  |

### Return type

[**AtfValidationResult**](AtfValidationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current or terminal validation result. |  -  |
| **409** | The validation job is still running. Retry with the same identifier. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listartifactgenerationprofiles"></a>
# **ListArtifactGenerationProfiles**
> List&lt;ArtifactGenerationProfile&gt; ListArtifactGenerationProfiles ()

List CI export profiles

Lists reusable export definitions used by CI to resolve an environment-specific source bundle and download a compile-validated ATF archive.


### Parameters
This endpoint does not need any parameter.
### Return type

[**List&lt;ArtifactGenerationProfile&gt;**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CI export profiles in the active project. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="observeatfprojectvalidation"></a>
# **ObserveAtfProjectValidation**
> string ObserveAtfProjectValidation (string validationId)

Observe ATF validation progress


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **validationId** | **string** | Opaque identifier of a bounded asynchronous ATF validation job. |  |

### Return type

**string**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server-sent validation lifecycle events. If the stream is interrupted, fetch the result endpoint with the same identifier. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="previewatfproject"></a>
# **PreviewAtfProject**
> AtfGenerationResult PreviewAtfProject (AtfGenerationInput atfGenerationInput)

Generate an ATF project preview


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **atfGenerationInput** | [**AtfGenerationInput**](AtfGenerationInput.md) |  |  |

### Return type

[**AtfGenerationResult**](AtfGenerationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated files, manifest, and compatibility notes. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="refreshartifactgenerationprofilebundle"></a>
# **RefreshArtifactGenerationProfileBundle**
> ArtifactGenerationProfile RefreshArtifactGenerationProfileBundle (Guid profileId, string environmentKey)

Capture or refresh an environment baseline

Resolves current selected assets and atomically stores the bundle plus its hash for PINNED or FAIL_ON_DRIFT downloads.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **profileId** | **Guid** | UUIDv7 identifier of a CI export profile. |  |
| **environmentKey** | **string** | Stable profile environment key such as test, staging, or production. |  |

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The refreshed profile. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="startatfprojectvalidation"></a>
# **StartAtfProjectValidation**
> AtfValidationStart StartAtfProjectValidation (AtfGenerationInput atfGenerationInput)

Start asynchronous ATF compile validation


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **atfGenerationInput** | [**AtfGenerationInput**](AtfGenerationInput.md) |  |  |

### Return type

[**AtfValidationStart**](AtfValidationStart.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Identifier used to observe the bounded validation job. |  -  |
| **429** | The company or global validation capacity is currently in use. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="updateartifactgenerationprofile"></a>
# **UpdateArtifactGenerationProfile**
> ArtifactGenerationProfile UpdateArtifactGenerationProfile (Guid profileId, ArtifactGenerationProfileInput artifactGenerationProfileInput)

Update a CI export profile

Send the revision returned by the latest read. A stale revision is rejected instead of overwriting a teammate's changes.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **profileId** | **Guid** | UUIDv7 identifier of a CI export profile. |  |
| **artifactGenerationProfileInput** | [**ArtifactGenerationProfileInput**](ArtifactGenerationProfileInput.md) |  |  |

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated profile and its next revision. |  -  |
| **409** | The profile was updated after the supplied revision was read. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="validateatfproject"></a>
# **ValidateAtfProject**
> AtfValidationResult ValidateAtfProject (AtfGenerationInput atfGenerationInput)

Validate that an ATF project compiles

Resolves the selected assets, generates the project, and runs a bounded compile validation without creating an archive.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **atfGenerationInput** | [**AtfGenerationInput**](AtfGenerationInput.md) |  |  |

### Return type

[**AtfValidationResult**](AtfValidationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Structural and compile readiness for the generated project. |  -  |
| **429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
