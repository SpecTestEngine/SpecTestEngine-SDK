# DocumentVisualDiffsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDocumentVisualDiff**](DocumentVisualDiffsApi.md#getdocumentvisualdiff) | **GET** /browser/visual/document-diffs/{visualDiffId} | Get a visual document diff |
| [**getDocumentVisualDiffArtifact**](DocumentVisualDiffsApi.md#getdocumentvisualdiffartifact) | **GET** /browser/visual/document-diffs/{visualDiffId}/artifacts/{artifactId} | Download a rendered visual diff page |
| [**prepareDocumentVisualDiffBaseline**](DocumentVisualDiffsApi.md#preparedocumentvisualdiffbaseline) | **POST** /browser/visual/document-diffs/{visualDiffId}/baseline | Preview or create an attachment baseline update draft |
| [**regenerateDocumentVisualDiff**](DocumentVisualDiffsApi.md#regeneratedocumentvisualdiff) | **POST** /browser/visual/document-diffs/{visualDiffId}/regenerate | Regenerate a visual document diff |
| [**uploadDocumentVisualDiffExpected**](DocumentVisualDiffsApi.md#uploaddocumentvisualdiffexpected) | **POST** /browser/visual/document-diffs/{visualDiffId}/expected | Upload a reference document and create a diff generation |



## getDocumentVisualDiff

> DocumentVisualDiff getDocumentVisualDiff(visualDiffId)

Get a visual document diff

Returns the protected viewer URL, TTL, immutable generations, and page-level artifact references.

### Example

```ts
import {
  Configuration,
  DocumentVisualDiffsApi,
} from '@spectestengine/sdk';
import type { GetDocumentVisualDiffRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DocumentVisualDiffsApi(config);

  const body = {
    // string | UUIDv7 identifier of an organization-scoped visual document diff session.
    visualDiffId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetDocumentVisualDiffRequest;

  try {
    const data = await api.getDocumentVisualDiff(body);
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
| **visualDiffId** | `string` | UUIDv7 identifier of an organization-scoped visual document diff session. | [Defaults to `undefined`] |

### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Visual diff metadata scoped to the token company and active project. |  -  |
| **410** | Derived visual artifacts expired; source run metadata remains available. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getDocumentVisualDiffArtifact

> Blob getDocumentVisualDiffArtifact(visualDiffId, artifactId)

Download a rendered visual diff page

### Example

```ts
import {
  Configuration,
  DocumentVisualDiffsApi,
} from '@spectestengine/sdk';
import type { GetDocumentVisualDiffArtifactRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DocumentVisualDiffsApi(config);

  const body = {
    // string | UUIDv7 identifier of an organization-scoped visual document diff session.
    visualDiffId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    artifactId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetDocumentVisualDiffArtifactRequest;

  try {
    const data = await api.getDocumentVisualDiffArtifact(body);
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
| **visualDiffId** | `string` | UUIDv7 identifier of an organization-scoped visual document diff session. | [Defaults to `undefined`] |
| **artifactId** | `string` |  | [Defaults to `undefined`] |

### Return type

**Blob**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `image/png`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Decrypted PNG page. The encrypted derivative remains subject to the diagnostic TTL. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## prepareDocumentVisualDiffBaseline

> DocumentVisualDiffBaselinePreview prepareDocumentVisualDiffBaseline(visualDiffId, documentVisualDiffBaselineRequest)

Preview or create an attachment baseline update draft

Never silently overwrites a specification. Send confirm&#x3D;false first, then confirm&#x3D;true only after review.

### Example

```ts
import {
  Configuration,
  DocumentVisualDiffsApi,
} from '@spectestengine/sdk';
import type { PrepareDocumentVisualDiffBaselineRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DocumentVisualDiffsApi(config);

  const body = {
    // string | UUIDv7 identifier of an organization-scoped visual document diff session.
    visualDiffId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // DocumentVisualDiffBaselineRequest
    documentVisualDiffBaselineRequest: ...,
  } satisfies PrepareDocumentVisualDiffBaselineRequest;

  try {
    const data = await api.prepareDocumentVisualDiffBaseline(body);
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
| **visualDiffId** | `string` | UUIDv7 identifier of an organization-scoped visual document diff session. | [Defaults to `undefined`] |
| **documentVisualDiffBaselineRequest** | [DocumentVisualDiffBaselineRequest](DocumentVisualDiffBaselineRequest.md) |  | |

### Return type

[**DocumentVisualDiffBaselinePreview**](DocumentVisualDiffBaselinePreview.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Baseline hash/fingerprint preview or confirmed update draft. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## regenerateDocumentVisualDiff

> DocumentVisualDiff regenerateDocumentVisualDiff(visualDiffId, documentVisualDiffRegenerateRequest)

Regenerate a visual document diff

Creates an immutable generation from the existing rendered pages with new comparison settings and normalized visual exclusion regions.

### Example

```ts
import {
  Configuration,
  DocumentVisualDiffsApi,
} from '@spectestengine/sdk';
import type { RegenerateDocumentVisualDiffRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DocumentVisualDiffsApi(config);

  const body = {
    // string | UUIDv7 identifier of an organization-scoped visual document diff session.
    visualDiffId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // DocumentVisualDiffRegenerateRequest (optional)
    documentVisualDiffRegenerateRequest: ...,
  } satisfies RegenerateDocumentVisualDiffRequest;

  try {
    const data = await api.regenerateDocumentVisualDiff(body);
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
| **visualDiffId** | `string` | UUIDv7 identifier of an organization-scoped visual document diff session. | [Defaults to `undefined`] |
| **documentVisualDiffRegenerateRequest** | [DocumentVisualDiffRegenerateRequest](DocumentVisualDiffRegenerateRequest.md) |  | [Optional] |

### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Visual diff with a new current generation. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## uploadDocumentVisualDiffExpected

> DocumentVisualDiff uploadDocumentVisualDiffExpected(visualDiffId, expected, colorThreshold)

Upload a reference document and create a diff generation

The uploaded PDF or image is rendered in memory and discarded. Only encrypted page images and diff metadata remain until TTL expiry.

### Example

```ts
import {
  Configuration,
  DocumentVisualDiffsApi,
} from '@spectestengine/sdk';
import type { UploadDocumentVisualDiffExpectedRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DocumentVisualDiffsApi(config);

  const body = {
    // string | UUIDv7 identifier of an organization-scoped visual document diff session.
    visualDiffId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Blob
    expected: BINARY_DATA_HERE,
    // number (optional)
    colorThreshold: 1.2,
  } satisfies UploadDocumentVisualDiffExpectedRequest;

  try {
    const data = await api.uploadDocumentVisualDiffExpected(body);
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
| **visualDiffId** | `string` | UUIDv7 identifier of an organization-scoped visual document diff session. | [Defaults to `undefined`] |
| **expected** | `Blob` |  | [Defaults to `undefined`] |
| **colorThreshold** | `number` |  | [Optional] [Defaults to `24`] |

### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The visual diff with a new current generation. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

