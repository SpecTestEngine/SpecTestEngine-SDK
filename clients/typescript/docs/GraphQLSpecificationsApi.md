# GraphQLSpecificationsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**captureGraphqlSpecificationAttachmentVisualDiff**](GraphQLSpecificationsApi.md#capturegraphqlspecificationattachmentvisualdiff) | **POST** /test/graphql-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed GraphQL attachment assertion |
| [**createGraphqlSpecification**](GraphQLSpecificationsApi.md#creategraphqlspecification) | **POST** /test/graphql-spec/create | Create a GraphQL specification |
| [**deleteGraphqlSpecification**](GraphQLSpecificationsApi.md#deletegraphqlspecification) | **DELETE** /test/graphql-spec/by-id | Delete a GraphQL specification |
| [**getGraphqlSpecification**](GraphQLSpecificationsApi.md#getgraphqlspecification) | **GET** /test/graphql-spec/by-id | Get a GraphQL specification |
| [**getGraphqlSpecificationRun**](GraphQLSpecificationsApi.md#getgraphqlspecificationrun) | **GET** /test/graphql-spec/run/history/by-run-id/{runId} | Get saved GraphQL run evidence |
| [**listGraphqlSpecificationRuns**](GraphQLSpecificationsApi.md#listgraphqlspecificationruns) | **GET** /test/graphql-spec/run/page/by-spec-id/{specId} | List saved GraphQL runs |
| [**listGraphqlSpecifications**](GraphQLSpecificationsApi.md#listgraphqlspecifications) | **GET** /test/graphql-spec/page | List GraphQL specifications |
| [**previewGraphqlSpecificationRecovery**](GraphQLSpecificationsApi.md#previewgraphqlspecificationrecovery) | **POST** /test/graphql-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a GraphQL specification version |
| [**restoreGraphqlSpecificationFromRun**](GraphQLSpecificationsApi.md#restoregraphqlspecificationfromrun) | **PUT** /test/graphql-spec/recovery/{specId}/from-run/{runId}/restore | Restore a GraphQL specification version |
| [**runGraphqlSpecification**](GraphQLSpecificationsApi.md#rungraphqlspecification) | **POST** /test/graphql-spec/run/by-id | Run a saved GraphQL specification |
| [**testGraphqlSpecificationRecoveryVersion**](GraphQLSpecificationsApi.md#testgraphqlspecificationrecoveryversion) | **POST** /test/graphql-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous GraphQL specification version |
| [**updateGraphqlSpecification**](GraphQLSpecificationsApi.md#updategraphqlspecification) | **PUT** /test/graphql-spec/by-id | Replace a GraphQL specification definition |



## captureGraphqlSpecificationAttachmentVisualDiff

> SpecificationRun captureGraphqlSpecificationAttachmentVisualDiff(specId, documentVisualDiffCaptureRunRequest)

Create a visual diff from a failed GraphQL attachment assertion

Explicitly reruns the saved GraphQL specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status.

### Example

```ts
import {
  Configuration,
  GraphQLSpecificationsApi,
} from '@spectestengine/sdk';
import type { CaptureGraphqlSpecificationAttachmentVisualDiffRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GraphQLSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // DocumentVisualDiffCaptureRunRequest
    documentVisualDiffCaptureRunRequest: ...,
  } satisfies CaptureGraphqlSpecificationAttachmentVisualDiffRequest;

  try {
    const data = await api.captureGraphqlSpecificationAttachmentVisualDiff(body);
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


## createGraphqlSpecification

> Specification createGraphqlSpecification(specName, body, description, idempotencyKey)

Create a GraphQL specification

### Example

```ts
import {
  Configuration,
  GraphQLSpecificationsApi,
} from '@spectestengine/sdk';
import type { CreateGraphqlSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GraphQLSpecificationsApi(config);

  const body = {
    // string | User-facing specification name within the active project.
    specName: specName_example,
    // string
    body: body_example,
    // string | Optional user-facing description stored with the asset. (optional)
    description: description_example,
    // string | A caller-generated UUID retained for safe write retries where supported. (optional)
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CreateGraphqlSpecificationRequest;

  try {
    const data = await api.createGraphqlSpecification(body);
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
| **200** | The stored GraphQL specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteGraphqlSpecification

> Specification deleteGraphqlSpecification(specId)

Delete a GraphQL specification

### Example

```ts
import {
  Configuration,
  GraphQLSpecificationsApi,
} from '@spectestengine/sdk';
import type { DeleteGraphqlSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GraphQLSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteGraphqlSpecificationRequest;

  try {
    const data = await api.deleteGraphqlSpecification(body);
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
| **200** | The deleted GraphQL specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getGraphqlSpecification

> Specification getGraphqlSpecification(specId)

Get a GraphQL specification

### Example

```ts
import {
  Configuration,
  GraphQLSpecificationsApi,
} from '@spectestengine/sdk';
import type { GetGraphqlSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GraphQLSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetGraphqlSpecificationRequest;

  try {
    const data = await api.getGraphqlSpecification(body);
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
| **200** | The requested GraphQL specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getGraphqlSpecificationRun

> SpecificationRun getGraphqlSpecificationRun(runId)

Get saved GraphQL run evidence

### Example

```ts
import {
  Configuration,
  GraphQLSpecificationsApi,
} from '@spectestengine/sdk';
import type { GetGraphqlSpecificationRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GraphQLSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetGraphqlSpecificationRunRequest;

  try {
    const data = await api.getGraphqlSpecificationRun(body);
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


## listGraphqlSpecificationRuns

> SpecificationRunPage listGraphqlSpecificationRuns(specId, page, size)

List saved GraphQL runs

### Example

```ts
import {
  Configuration,
  GraphQLSpecificationsApi,
} from '@spectestengine/sdk';
import type { ListGraphqlSpecificationRunsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GraphQLSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
  } satisfies ListGraphqlSpecificationRunsRequest;

  try {
    const data = await api.listGraphqlSpecificationRuns(body);
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


## listGraphqlSpecifications

> SpecificationPage listGraphqlSpecifications(page, size, search)

List GraphQL specifications

### Example

```ts
import {
  Configuration,
  GraphQLSpecificationsApi,
} from '@spectestengine/sdk';
import type { ListGraphqlSpecificationsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GraphQLSpecificationsApi(config);

  const body = {
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
    // string | Case-insensitive server-side search within the active project. (optional)
    search: search_example,
  } satisfies ListGraphqlSpecificationsRequest;

  try {
    const data = await api.listGraphqlSpecifications(body);
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
| **200** | A page of GraphQL specifications. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## previewGraphqlSpecificationRecovery

> SpecificationRecoveryPreview previewGraphqlSpecificationRecovery(specId, runId)

Preview restoring a GraphQL specification version

Compares the current specification with the exact DSL snapshot retained by a completed PASS or FAIL run. No expectations are regenerated.

### Example

```ts
import {
  Configuration,
  GraphQLSpecificationsApi,
} from '@spectestengine/sdk';
import type { PreviewGraphqlSpecificationRecoveryRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GraphQLSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies PreviewGraphqlSpecificationRecoveryRequest;

  try {
    const data = await api.previewGraphqlSpecificationRecovery(body);
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


## restoreGraphqlSpecificationFromRun

> Specification restoreGraphqlSpecificationFromRun(specId, runId)

Restore a GraphQL specification version

Replaces only the current DSL content with the exact snapshot retained by a completed PASS or FAIL run. The specification id, name, description, and stable identity are preserved.

### Example

```ts
import {
  Configuration,
  GraphQLSpecificationsApi,
} from '@spectestengine/sdk';
import type { RestoreGraphqlSpecificationFromRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GraphQLSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies RestoreGraphqlSpecificationFromRunRequest;

  try {
    const data = await api.restoreGraphqlSpecificationFromRun(body);
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


## runGraphqlSpecification

> SpecificationRun runGraphqlSpecification(specId)

Run a saved GraphQL specification

### Example

```ts
import {
  Configuration,
  GraphQLSpecificationsApi,
} from '@spectestengine/sdk';
import type { RunGraphqlSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GraphQLSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies RunGraphqlSpecificationRequest;

  try {
    const data = await api.runGraphqlSpecification(body);
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


## testGraphqlSpecificationRecoveryVersion

> SpecificationRun testGraphqlSpecificationRecoveryVersion(specId, runId)

Test a previous GraphQL specification version

Executes the exact DSL snapshot retained by the selected completed PASS or FAIL run against the current API without changing the saved specification.

### Example

```ts
import {
  Configuration,
  GraphQLSpecificationsApi,
} from '@spectestengine/sdk';
import type { TestGraphqlSpecificationRecoveryVersionRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GraphQLSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies TestGraphqlSpecificationRecoveryVersionRequest;

  try {
    const data = await api.testGraphqlSpecificationRecoveryVersion(body);
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


## updateGraphqlSpecification

> Specification updateGraphqlSpecification(specId, body, description)

Replace a GraphQL specification definition

### Example

```ts
import {
  Configuration,
  GraphQLSpecificationsApi,
} from '@spectestengine/sdk';
import type { UpdateGraphqlSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GraphQLSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    body: body_example,
    // string | Optional user-facing description stored with the asset. (optional)
    description: description_example,
  } satisfies UpdateGraphqlSpecificationRequest;

  try {
    const data = await api.updateGraphqlSpecification(body);
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
| **200** | The updated GraphQL specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
