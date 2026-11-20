# RESTSpecificationsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**captureRestSpecificationAttachmentVisualDiff**](RESTSpecificationsApi.md#capturerestspecificationattachmentvisualdiff) | **POST** /test/rest-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed REST attachment assertion |
| [**createRestSpecification**](RESTSpecificationsApi.md#createrestspecification) | **POST** /test/rest-spec/create | Create a REST specification |
| [**deleteRestSpecification**](RESTSpecificationsApi.md#deleterestspecification) | **DELETE** /test/rest-spec/by-id | Delete a REST specification |
| [**getRestPreparation**](RESTSpecificationsApi.md#getrestpreparation) | **GET** /test/rest-spec/preparations/by-ref/{ref} | Read eligible REST Prepare request metadata by stable key |
| [**getRestSpecification**](RESTSpecificationsApi.md#getrestspecification) | **GET** /test/rest-spec/by-id | Get a REST specification |
| [**getRestSpecificationRun**](RESTSpecificationsApi.md#getrestspecificationrun) | **GET** /test/rest-spec/run/history/by-run-id/{runId} | Get saved REST run evidence |
| [**listRestPreparations**](RESTSpecificationsApi.md#listrestpreparations) | **GET** /test/rest-spec/preparations | List eligible Prepare requests and output declarations |
| [**listRestSpecificationRuns**](RESTSpecificationsApi.md#listrestspecificationruns) | **GET** /test/rest-spec/run/page/by-spec-id/{specId} | List saved REST runs |
| [**listRestSpecifications**](RESTSpecificationsApi.md#listrestspecifications) | **GET** /test/rest-spec/page | List REST specifications |
| [**previewRestSpecificationRecovery**](RESTSpecificationsApi.md#previewrestspecificationrecovery) | **POST** /test/rest-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a REST specification version |
| [**restoreRestSpecificationFromRun**](RESTSpecificationsApi.md#restorerestspecificationfromrun) | **PUT** /test/rest-spec/recovery/{specId}/from-run/{runId}/restore | Restore a REST specification version |
| [**runRestSpecification**](RESTSpecificationsApi.md#runrestspecification) | **POST** /test/rest-spec/run/by-id | Run a saved REST specification |
| [**testRestSpecificationRecoveryVersion**](RESTSpecificationsApi.md#testrestspecificationrecoveryversion) | **POST** /test/rest-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous REST specification version |
| [**updateRestSpecification**](RESTSpecificationsApi.md#updaterestspecification) | **PUT** /test/rest-spec/by-id | Replace a REST specification definition |



## captureRestSpecificationAttachmentVisualDiff

> SpecificationRun captureRestSpecificationAttachmentVisualDiff(specId, documentVisualDiffCaptureRunRequest)

Create a visual diff from a failed REST attachment assertion

Explicitly reruns the saved REST specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status; no visual-diff fallback changes the test result.

### Example

```ts
import {
  Configuration,
  RESTSpecificationsApi,
} from '@spectestengine/sdk';
import type { CaptureRestSpecificationAttachmentVisualDiffRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RESTSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // DocumentVisualDiffCaptureRunRequest
    documentVisualDiffCaptureRunRequest: ...,
  } satisfies CaptureRestSpecificationAttachmentVisualDiffRequest;

  try {
    const data = await api.captureRestSpecificationAttachmentVisualDiff(body);
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
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |
| **documentVisualDiffCaptureRunRequest** | [DocumentVisualDiffCaptureRunRequest](DocumentVisualDiffCaptureRunRequest.md) |  | |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete failed run evidence containing the temporary visual diff link. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createRestSpecification

> Specification createRestSpecification(specName, body, description, idempotencyKey)

Create a REST specification

### Example

```ts
import {
  Configuration,
  RESTSpecificationsApi,
} from '@spectestengine/sdk';
import type { CreateRestSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RESTSpecificationsApi(config);

  const body = {
    // string | User-facing specification name within the active project.
    specName: specName_example,
    // string
    body: body_example,
    // string | Optional user-facing description stored with the asset. (optional)
    description: description_example,
    // string | A caller-generated UUID retained for safe write retries where supported. (optional)
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CreateRestSpecificationRequest;

  try {
    const data = await api.createRestSpecification(body);
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
| **specName** | `string` | User-facing specification name within the active project. | [Defaults to `undefined`] |
| **body** | `string` |  | |
| **description** | `string` | Optional user-facing description stored with the asset. | [Optional] [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A caller-generated UUID retained for safe write retries where supported. | [Optional] [Defaults to `undefined`] |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored REST specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteRestSpecification

> Specification deleteRestSpecification(specId)

Delete a REST specification

### Example

```ts
import {
  Configuration,
  RESTSpecificationsApi,
} from '@spectestengine/sdk';
import type { DeleteRestSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RESTSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteRestSpecificationRequest;

  try {
    const data = await api.deleteRestSpecification(body);
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
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted REST specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getRestPreparation

> PreparationSummary getRestPreparation(ref)

Read eligible REST Prepare request metadata by stable key

Same-company current-read metadata only; no definition or runtime values. Missing, unmarked or inaccessible sources cannot be selected.

### Example

```ts
import {
  Configuration,
  RESTSpecificationsApi,
} from '@spectestengine/sdk';
import type { GetRestPreparationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RESTSpecificationsApi(config);

  const body = {
    // string
    ref: ref_example,
  } satisfies GetRestPreparationRequest;

  try {
    const data = await api.getRestPreparation(body);
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
| **ref** | `string` |  | [Defaults to `undefined`] |

### Return type

[**PreparationSummary**](PreparationSummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The eligible source and its declared output variables. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getRestSpecification

> Specification getRestSpecification(specId)

Get a REST specification

### Example

```ts
import {
  Configuration,
  RESTSpecificationsApi,
} from '@spectestengine/sdk';
import type { GetRestSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RESTSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetRestSpecificationRequest;

  try {
    const data = await api.getRestSpecification(body);
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
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested REST specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getRestSpecificationRun

> SpecificationRun getRestSpecificationRun(runId)

Get saved REST run evidence

### Example

```ts
import {
  Configuration,
  RESTSpecificationsApi,
} from '@spectestengine/sdk';
import type { GetRestSpecificationRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RESTSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetRestSpecificationRunRequest;

  try {
    const data = await api.getRestSpecificationRun(body);
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
| **runId** | `string` | UUIDv7 identifier of the stored run evidence. | [Defaults to `undefined`] |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete saved run evidence. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listRestPreparations

> PreparationPage listRestPreparations(page, size, search)

List eligible Prepare requests and output declarations

Same-company paginated metadata only. Values and full specification definitions are never included. The selected protocol and stableKey are used as preparation.protocol and preparation.ref in the consumer DSL. Any native protocol can prepare any other protocol.

### Example

```ts
import {
  Configuration,
  RESTSpecificationsApi,
} from '@spectestengine/sdk';
import type { ListRestPreparationsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RESTSpecificationsApi(config);

  const body = {
    // number | Zero-based page index. (optional)
    page: 56,
    // number (optional)
    size: 56,
    // string | Case-insensitive server-side search within the active project. (optional)
    search: search_example,
  } satisfies ListRestPreparationsRequest;

  try {
    const data = await api.listRestPreparations(body);
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
| **page** | `number` | Zero-based page index. | [Optional] [Defaults to `0`] |
| **size** | `number` |  | [Optional] [Defaults to `20`] |
| **search** | `string` | Case-insensitive server-side search within the active project. | [Optional] [Defaults to `undefined`] |

### Return type

[**PreparationPage**](PreparationPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of eligible REST preparation sources. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listRestSpecificationRuns

> SpecificationRunPage listRestSpecificationRuns(specId, page, size)

List saved REST runs

### Example

```ts
import {
  Configuration,
  RESTSpecificationsApi,
} from '@spectestengine/sdk';
import type { ListRestSpecificationRunsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RESTSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
  } satisfies ListRestSpecificationRunsRequest;

  try {
    const data = await api.listRestSpecificationRuns(body);
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
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |
| **page** | `number` | Zero-based page index. | [Optional] [Defaults to `0`] |
| **size** | `number` | Maximum number of results returned in one page. | [Optional] [Defaults to `20`] |

### Return type

[**SpecificationRunPage**](SpecificationRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of run summaries. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listRestSpecifications

> SpecificationPage listRestSpecifications(page, size, search)

List REST specifications

### Example

```ts
import {
  Configuration,
  RESTSpecificationsApi,
} from '@spectestengine/sdk';
import type { ListRestSpecificationsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RESTSpecificationsApi(config);

  const body = {
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
    // string | Case-insensitive server-side search within the active project. (optional)
    search: search_example,
  } satisfies ListRestSpecificationsRequest;

  try {
    const data = await api.listRestSpecifications(body);
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
| **page** | `number` | Zero-based page index. | [Optional] [Defaults to `0`] |
| **size** | `number` | Maximum number of results returned in one page. | [Optional] [Defaults to `20`] |
| **search** | `string` | Case-insensitive server-side search within the active project. | [Optional] [Defaults to `undefined`] |

### Return type

[**SpecificationPage**](SpecificationPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of REST specifications. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## previewRestSpecificationRecovery

> SpecificationRecoveryPreview previewRestSpecificationRecovery(specId, runId)

Preview restoring a REST specification version

Compares the current specification with the exact DSL snapshot retained by a completed PASS or FAIL run. No expectations are regenerated.

### Example

```ts
import {
  Configuration,
  RESTSpecificationsApi,
} from '@spectestengine/sdk';
import type { PreviewRestSpecificationRecoveryRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RESTSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies PreviewRestSpecificationRecoveryRequest;

  try {
    const data = await api.previewRestSpecificationRecovery(body);
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
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |
| **runId** | `string` | UUIDv7 identifier of the stored run evidence. | [Defaults to `undefined`] |

### Return type

[**SpecificationRecoveryPreview**](SpecificationRecoveryPreview.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Definition-only recovery preview. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## restoreRestSpecificationFromRun

> Specification restoreRestSpecificationFromRun(specId, runId)

Restore a REST specification version

Replaces only the current DSL content with the exact snapshot retained by a completed PASS or FAIL run. The specification id, name, description, and stable identity are preserved.

### Example

```ts
import {
  Configuration,
  RESTSpecificationsApi,
} from '@spectestengine/sdk';
import type { RestoreRestSpecificationFromRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RESTSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies RestoreRestSpecificationFromRunRequest;

  try {
    const data = await api.restoreRestSpecificationFromRun(body);
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
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |
| **runId** | `string` | UUIDv7 identifier of the stored run evidence. | [Defaults to `undefined`] |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Restored specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## runRestSpecification

> SpecificationRun runRestSpecification(specId)

Run a saved REST specification

Starts and completes one synchronous specification execution.

### Example

```ts
import {
  Configuration,
  RESTSpecificationsApi,
} from '@spectestengine/sdk';
import type { RunRestSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RESTSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies RunRestSpecificationRequest;

  try {
    const data = await api.runRestSpecification(body);
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
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete run evidence. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## testRestSpecificationRecoveryVersion

> SpecificationRun testRestSpecificationRecoveryVersion(specId, runId)

Test a previous REST specification version

Executes the exact DSL snapshot retained by the selected completed PASS or FAIL run against the current API without changing the saved specification.

### Example

```ts
import {
  Configuration,
  RESTSpecificationsApi,
} from '@spectestengine/sdk';
import type { TestRestSpecificationRecoveryVersionRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RESTSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies TestRestSpecificationRecoveryVersionRequest;

  try {
    const data = await api.testRestSpecificationRecoveryVersion(body);
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
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |
| **runId** | `string` | UUIDv7 identifier of the stored run evidence. | [Defaults to `undefined`] |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete test-run evidence for the selected version. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateRestSpecification

> Specification updateRestSpecification(specId, body, description)

Replace a REST specification definition

### Example

```ts
import {
  Configuration,
  RESTSpecificationsApi,
} from '@spectestengine/sdk';
import type { UpdateRestSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RESTSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    body: body_example,
    // string | Optional user-facing description stored with the asset. (optional)
    description: description_example,
  } satisfies UpdateRestSpecificationRequest;

  try {
    const data = await api.updateRestSpecification(body);
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
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |
| **body** | `string` |  | |
| **description** | `string` | Optional user-facing description stored with the asset. | [Optional] [Defaults to `undefined`] |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated REST specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
