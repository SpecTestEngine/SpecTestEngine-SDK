# GenerationApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createArtifactGenerationProfile**](GenerationApi.md#createartifactgenerationprofile) | **POST** /artifact-profiles | Create a CI export profile |
| [**deleteArtifactGenerationProfile**](GenerationApi.md#deleteartifactgenerationprofile) | **DELETE** /artifact-profiles/{profileId} | Delete a CI export profile |
| [**downloadArtifactGenerationProfileArchive**](GenerationApi.md#downloadartifactgenerationprofilearchive) | **POST** /artifact-profiles/{profileId}/environments/{environmentKey}/atf/archive | Validate and download a CI profile archive |
| [**downloadAtfProject**](GenerationApi.md#downloadatfproject) | **POST** /atf/generate/download | Download a generated ATF project |
| [**generateFromOpenApiContent**](GenerationApi.md#generatefromopenapicontent) | **POST** /openapi/generate-from-content | Generate specifications and flows from OpenAPI content |
| [**generateSpecification**](GenerationApi.md#generatespecification) | **POST** /spec/generate | Generate an executable specification from concrete request evidence |
| [**getArtifactGenerationProfile**](GenerationApi.md#getartifactgenerationprofile) | **GET** /artifact-profiles/{profileId} | Get a CI export profile |
| [**getAtfProjectValidationResult**](GenerationApi.md#getatfprojectvalidationresult) | **GET** /atf/generate/validate/result/{validationId} | Get ATF validation status or result |
| [**listArtifactGenerationProfiles**](GenerationApi.md#listartifactgenerationprofiles) | **GET** /artifact-profiles | List CI export profiles |
| [**observeAtfProjectValidation**](GenerationApi.md#observeatfprojectvalidation) | **GET** /atf/generate/validate/events/{validationId} | Observe ATF validation progress |
| [**previewAtfProject**](GenerationApi.md#previewatfproject) | **POST** /atf/generate/preview | Generate an ATF project preview |
| [**refreshArtifactGenerationProfileBundle**](GenerationApi.md#refreshartifactgenerationprofilebundle) | **POST** /artifact-profiles/{profileId}/environments/{environmentKey}/bundle/refresh | Capture or refresh an environment baseline |
| [**startAtfProjectValidation**](GenerationApi.md#startatfprojectvalidation) | **POST** /atf/generate/validate/start | Start asynchronous ATF compile validation |
| [**updateArtifactGenerationProfile**](GenerationApi.md#updateartifactgenerationprofile) | **PUT** /artifact-profiles/{profileId} | Update a CI export profile |
| [**validateAtfProject**](GenerationApi.md#validateatfproject) | **POST** /atf/generate/validate | Validate that an ATF project compiles |



## createArtifactGenerationProfile

> ArtifactGenerationProfile createArtifactGenerationProfile(artifactGenerationProfileInput, idempotencyKey)

Create a CI export profile

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { CreateArtifactGenerationProfileRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  const body = {
    // ArtifactGenerationProfileInput
    artifactGenerationProfileInput: ...,
    // string | A caller-generated UUID retained for safe write retries where supported. (optional)
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CreateArtifactGenerationProfileRequest;

  try {
    const data = await api.createArtifactGenerationProfile(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artifactGenerationProfileInput** | [ArtifactGenerationProfileInput](ArtifactGenerationProfileInput.md) |  | |
| **idempotencyKey** | `string` | A caller-generated UUID retained for safe write retries where supported. | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored CI export profile. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteArtifactGenerationProfile

> deleteArtifactGenerationProfile(profileId)

Delete a CI export profile

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { DeleteArtifactGenerationProfileRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  const body = {
    // string | UUIDv7 identifier of a CI export profile.
    profileId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteArtifactGenerationProfileRequest;

  try {
    const data = await api.deleteArtifactGenerationProfile(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **profileId** | `string` | UUIDv7 identifier of a CI export profile. | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The profile was deleted. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## downloadArtifactGenerationProfileArchive

> Blob downloadArtifactGenerationProfileArchive(profileId, environmentKey)

Validate and download a CI profile archive

Resolves the environment policy, enforces drift rules, then returns an archive only after the generated project passes compile validation.

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { DownloadArtifactGenerationProfileArchiveRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  const body = {
    // string | UUIDv7 identifier of a CI export profile.
    profileId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Stable profile environment key such as test, staging, or production.
    environmentKey: environmentKey_example,
  } satisfies DownloadArtifactGenerationProfileArchiveRequest;

  try {
    const data = await api.downloadArtifactGenerationProfileArchive(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **profileId** | `string` | UUIDv7 identifier of a CI export profile. | [Defaults to `undefined`] |
| **environmentKey** | `string` | Stable profile environment key such as test, staging, or production. | [Defaults to `undefined`] |

### Return type

**Blob**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/octet-stream`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A compile-validated ATF project archive. |  * Content-Disposition -  <br>  |
| **422** | The generated project did not pass readiness validation; no archive was returned. |  -  |
| **429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## downloadAtfProject

> Blob downloadAtfProject(atfGenerationInput)

Download a generated ATF project

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { DownloadAtfProjectRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  const body = {
    // AtfGenerationInput
    atfGenerationInput: ...,
  } satisfies DownloadAtfProjectRequest;

  try {
    const data = await api.downloadAtfProject(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **atfGenerationInput** | [AtfGenerationInput](AtfGenerationInput.md) |  | |

### Return type

**Blob**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/octet-stream`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A portable ATF project archive. |  * Content-Disposition -  <br>  |
| **422** | The generated project did not pass readiness validation; no archive was returned. |  -  |
| **429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## generateFromOpenApiContent

> OpenApiGenerationResult generateFromOpenApiContent(contentFormat, body, includeNegativeTests, generateFlowScenarios, generationStrategy, negativeTestGenerationMode)

Generate specifications and flows from OpenAPI content

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { GenerateFromOpenApiContentRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  const body = {
    // ContentFormat
    contentFormat: ...,
    // string
    body: body_example,
    // boolean (optional)
    includeNegativeTests: true,
    // boolean (optional)
    generateFlowScenarios: true,
    // 'SCHEMA_BASED' | 'LIVE_API_CALL' | 'HYBRID' (optional)
    generationStrategy: generationStrategy_example,
    // 'STRICT' | 'EXTENDED' (optional)
    negativeTestGenerationMode: negativeTestGenerationMode_example,
  } satisfies GenerateFromOpenApiContentRequest;

  try {
    const data = await api.generateFromOpenApiContent(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **contentFormat** | `ContentFormat` |  | [Defaults to `undefined`] [Enum: JSON, YAML, XML] |
| **body** | `string` |  | |
| **includeNegativeTests** | `boolean` |  | [Optional] [Defaults to `false`] |
| **generateFlowScenarios** | `boolean` |  | [Optional] [Defaults to `false`] |
| **generationStrategy** | `SCHEMA_BASED`, `LIVE_API_CALL`, `HYBRID` |  | [Optional] [Defaults to `&#39;SCHEMA_BASED&#39;`] [Enum: SCHEMA_BASED, LIVE_API_CALL, HYBRID] |
| **negativeTestGenerationMode** | `STRICT`, `EXTENDED` |  | [Optional] [Defaults to `&#39;EXTENDED&#39;`] [Enum: STRICT, EXTENDED] |

### Return type

[**OpenApiGenerationResult**](OpenApiGenerationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `text/plain`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated specification drafts, flow drafts, and operation coverage. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## generateSpecification

> Array&lt;SpecGenerationResult&gt; generateSpecification(requestBody, mode, format, specGenerationTypes)

Generate an executable specification from concrete request evidence

Generates a REST, SOAP, GraphQL, or Streaming specification. Streaming input may contain observedEvidence from a completed Craftsman session; generation derives expectations from that transcript and never opens a second connection. Workflow placeholders must be materialized before this endpoint is called.

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { GenerateSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  const body = {
    // { [key: string]: any; }
    requestBody: Object,
    // 'FULL' | 'PATHS' | 'HYBRID' (optional)
    mode: mode_example,
    // ContentFormat (optional)
    format: ...,
    // Array<'POSITIVE' | 'NEGATIVE' | 'DUPLICATE'> | Comma-separated generation variants. Streaming currently accepts POSITIVE only. (optional)
    specGenerationTypes: ...,
  } satisfies GenerateSpecificationRequest;

  try {
    const data = await api.generateSpecification(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **requestBody** | `{ [key: string]: any; }` |  | |
| **mode** | `FULL`, `PATHS`, `HYBRID` |  | [Optional] [Defaults to `&#39;FULL&#39;`] [Enum: FULL, PATHS, HYBRID] |
| **format** | `ContentFormat` |  | [Optional] [Defaults to `undefined`] [Enum: JSON, YAML, XML] |
| **specGenerationTypes** | `POSITIVE`, `NEGATIVE`, `DUPLICATE` | Comma-separated generation variants. Streaming currently accepts POSITIVE only. | [Optional] [Enum: POSITIVE, NEGATIVE, DUPLICATE] |

### Return type

[**Array&lt;SpecGenerationResult&gt;**](SpecGenerationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated executable specification variants. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getArtifactGenerationProfile

> ArtifactGenerationProfile getArtifactGenerationProfile(profileId)

Get a CI export profile

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { GetArtifactGenerationProfileRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  const body = {
    // string | UUIDv7 identifier of a CI export profile.
    profileId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetArtifactGenerationProfileRequest;

  try {
    const data = await api.getArtifactGenerationProfile(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **profileId** | `string` | UUIDv7 identifier of a CI export profile. | [Defaults to `undefined`] |

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested profile. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getAtfProjectValidationResult

> AtfValidationResult getAtfProjectValidationResult(validationId)

Get ATF validation status or result

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { GetAtfProjectValidationResultRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  const body = {
    // string | Opaque identifier of a bounded asynchronous ATF validation job.
    validationId: validationId_example,
  } satisfies GetAtfProjectValidationResultRequest;

  try {
    const data = await api.getAtfProjectValidationResult(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **validationId** | `string` | Opaque identifier of a bounded asynchronous ATF validation job. | [Defaults to `undefined`] |

### Return type

[**AtfValidationResult**](AtfValidationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current or terminal validation result. |  -  |
| **409** | The validation job is still running. Retry with the same identifier. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listArtifactGenerationProfiles

> Array&lt;ArtifactGenerationProfile&gt; listArtifactGenerationProfiles()

List CI export profiles

Lists reusable export definitions used by CI to resolve an environment-specific source bundle and download a compile-validated ATF archive.

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { ListArtifactGenerationProfilesRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  try {
    const data = await api.listArtifactGenerationProfiles();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Array&lt;ArtifactGenerationProfile&gt;**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CI export profiles in the active project. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## observeAtfProjectValidation

> string observeAtfProjectValidation(validationId)

Observe ATF validation progress

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { ObserveAtfProjectValidationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  const body = {
    // string | Opaque identifier of a bounded asynchronous ATF validation job.
    validationId: validationId_example,
  } satisfies ObserveAtfProjectValidationRequest;

  try {
    const data = await api.observeAtfProjectValidation(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **validationId** | `string` | Opaque identifier of a bounded asynchronous ATF validation job. | [Defaults to `undefined`] |

### Return type

**string**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/event-stream`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server-sent validation lifecycle events. If the stream is interrupted, fetch the result endpoint with the same identifier. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## previewAtfProject

> AtfGenerationResult previewAtfProject(atfGenerationInput)

Generate an ATF project preview

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { PreviewAtfProjectRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  const body = {
    // AtfGenerationInput
    atfGenerationInput: ...,
  } satisfies PreviewAtfProjectRequest;

  try {
    const data = await api.previewAtfProject(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **atfGenerationInput** | [AtfGenerationInput](AtfGenerationInput.md) |  | |

### Return type

[**AtfGenerationResult**](AtfGenerationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated files, manifest, and compatibility notes. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## refreshArtifactGenerationProfileBundle

> ArtifactGenerationProfile refreshArtifactGenerationProfileBundle(profileId, environmentKey)

Capture or refresh an environment baseline

Resolves current selected assets and atomically stores the bundle plus its hash for PINNED or FAIL_ON_DRIFT downloads.

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { RefreshArtifactGenerationProfileBundleRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  const body = {
    // string | UUIDv7 identifier of a CI export profile.
    profileId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Stable profile environment key such as test, staging, or production.
    environmentKey: environmentKey_example,
  } satisfies RefreshArtifactGenerationProfileBundleRequest;

  try {
    const data = await api.refreshArtifactGenerationProfileBundle(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **profileId** | `string` | UUIDv7 identifier of a CI export profile. | [Defaults to `undefined`] |
| **environmentKey** | `string` | Stable profile environment key such as test, staging, or production. | [Defaults to `undefined`] |

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The refreshed profile. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## startAtfProjectValidation

> AtfValidationStart startAtfProjectValidation(atfGenerationInput)

Start asynchronous ATF compile validation

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { StartAtfProjectValidationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  const body = {
    // AtfGenerationInput
    atfGenerationInput: ...,
  } satisfies StartAtfProjectValidationRequest;

  try {
    const data = await api.startAtfProjectValidation(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **atfGenerationInput** | [AtfGenerationInput](AtfGenerationInput.md) |  | |

### Return type

[**AtfValidationStart**](AtfValidationStart.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Identifier used to observe the bounded validation job. |  -  |
| **429** | The company or global validation capacity is currently in use. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateArtifactGenerationProfile

> ArtifactGenerationProfile updateArtifactGenerationProfile(profileId, artifactGenerationProfileInput)

Update a CI export profile

Send the revision returned by the latest read. A stale revision is rejected instead of overwriting a teammate\&#39;s changes.

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { UpdateArtifactGenerationProfileRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  const body = {
    // string | UUIDv7 identifier of a CI export profile.
    profileId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // ArtifactGenerationProfileInput
    artifactGenerationProfileInput: ...,
  } satisfies UpdateArtifactGenerationProfileRequest;

  try {
    const data = await api.updateArtifactGenerationProfile(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **profileId** | `string` | UUIDv7 identifier of a CI export profile. | [Defaults to `undefined`] |
| **artifactGenerationProfileInput** | [ArtifactGenerationProfileInput](ArtifactGenerationProfileInput.md) |  | |

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated profile and its next revision. |  -  |
| **409** | The profile was updated after the supplied revision was read. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## validateAtfProject

> AtfValidationResult validateAtfProject(atfGenerationInput)

Validate that an ATF project compiles

Resolves the selected assets, generates the project, and runs a bounded compile validation without creating an archive.

### Example

```ts
import {
  Configuration,
  GenerationApi,
} from '@spectestengine/sdk';
import type { ValidateAtfProjectRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GenerationApi(config);

  const body = {
    // AtfGenerationInput
    atfGenerationInput: ...,
  } satisfies ValidateAtfProjectRequest;

  try {
    const data = await api.validateAtfProject(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **atfGenerationInput** | [AtfGenerationInput](AtfGenerationInput.md) |  | |

### Return type

[**AtfValidationResult**](AtfValidationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Structural and compile readiness for the generated project. |  -  |
| **429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

