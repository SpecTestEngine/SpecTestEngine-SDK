# FlowsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**captureFlowStepAttachmentVisualDiff**](FlowsApi.md#captureflowstepattachmentvisualdiff) | **POST** /test/flow/run/by-id/{flowId}/visual-diff-captures | Create a visual diff from a failed flow-step attachment assertion |
| [**copyFlowRecoveryDraft**](FlowsApi.md#copyflowrecoverydraft) | **POST** /test/flow/run/saved/{runId}/recovery/copy | Recover an edited draft as an independent new Flow |
| [**createFlow**](FlowsApi.md#createflow) | **POST** /test/flow/create | Create a test flow |
| [**createFlowRecovery**](FlowsApi.md#createflowrecovery) | **POST** /test/flow/run/saved/{runId}/recovery | Recover a saved run as a new Flow and new dependency copies |
| [**deleteFlow**](FlowsApi.md#deleteflow) | **DELETE** /test/flow/by-id | Delete a test flow |
| [**getFlow**](FlowsApi.md#getflow) | **GET** /test/flow/by-id/{flowId} | Get a test flow |
| [**getFlowRecoveryCurrentDependency**](FlowsApi.md#getflowrecoverycurrentdependency) | **GET** /test/flow/run/saved/{runId}/recovery/current-dependency | Read one current safe Recovery dependency |
| [**getFlowRecoveryDependency**](FlowsApi.md#getflowrecoverydependency) | **GET** /test/flow/run/saved/{runId}/recovery/dependencies/{dependencyKey} | Inspect one retained safe dependency definition |
| [**getFlowRecoveryOperation**](FlowsApi.md#getflowrecoveryoperation) | **GET** /test/flow/run/recovery-operations/{operationId} | Read a Flow recovery outcome without performing writes |
| [**getFlowRun**](FlowsApi.md#getflowrun) | **GET** /test/flow/run/saved/{runId} | Get a saved flow run |
| [**listFlowRecoveryDependencies**](FlowsApi.md#listflowrecoverydependencies) | **GET** /test/flow/run/saved/{runId}/recovery/dependencies | List historical dependency versions for Flow recovery |
| [**listFlowRuns**](FlowsApi.md#listflowruns) | **GET** /test/flow/run/by-flow-id/{flowId}/page | List saved runs for a flow |
| [**listFlows**](FlowsApi.md#listflows) | **GET** /test/flow/page | List test flows |
| [**previewFlowRecovery**](FlowsApi.md#previewflowrecovery) | **GET** /test/flow/run/saved/{runId}/recovery/preview | Preview an independent Flow recovery from a saved run |
| [**restoreFlowRecoveryDraft**](FlowsApi.md#restoreflowrecoverydraft) | **POST** /test/flow/run/saved/{runId}/recovery/restore | Restore an edited historical Flow into the current Flow |
| [**reviewFlowRecovery**](FlowsApi.md#reviewflowrecovery) | **GET** /test/flow/run/saved/{runId}/recovery/review | Review Flow Recovery for restore or independent copy |
| [**runFlow**](FlowsApi.md#runflow) | **POST** /test/flow/run/by-id/{flowId} | Run a saved flow |
| [**runFlowBatch**](FlowsApi.md#runflowbatchoperation) | **POST** /test/flow/run/batch | Run multiple saved flows |
| [**updateFlow**](FlowsApi.md#updateflow) | **PUT** /test/flow/by-id | Replace a test flow |



## captureFlowStepAttachmentVisualDiff

> FlowRun captureFlowStepAttachmentVisualDiff(flowId, flowDocumentVisualDiffCaptureRunRequest)

Create a visual diff from a failed flow-step attachment assertion

Explicitly reruns the saved flow and captures one failed PDF or image response from the selected API step. The flow and attachment assertion retain their real status.

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { CaptureFlowStepAttachmentVisualDiffRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved test flow.
    flowId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // FlowDocumentVisualDiffCaptureRunRequest
    flowDocumentVisualDiffCaptureRunRequest: ...,
  } satisfies CaptureFlowStepAttachmentVisualDiffRequest;

  try {
    const data = await api.captureFlowStepAttachmentVisualDiff(body);
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
| **flowId** | `string` | UUIDv7 identifier of the saved test flow. | [Defaults to `undefined`] |
| **flowDocumentVisualDiffCaptureRunRequest** | [FlowDocumentVisualDiffCaptureRunRequest](FlowDocumentVisualDiffCaptureRunRequest.md) |  | |

### Return type

[**FlowRun**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete flow run evidence containing the temporary visual diff link in the selected step. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## copyFlowRecoveryDraft

> FlowRecoveryOperation copyFlowRecoveryDraft(runId, idempotencyKey, flowRecoveryDraftInput)

Recover an edited draft as an independent new Flow

Creates a new Flow and independent selected dependency copies; originals are unchanged. Requires current owner create authority and a unique Flow name. No ordinary-create fallback or execution. Mode must be COPY. Retain the identical reviewed body and UUID key; GET status never resumes writes.

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { CopyFlowRecoveryDraftRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // FlowRecoveryDraftInput
    flowRecoveryDraftInput: ...,
  } satisfies CopyFlowRecoveryDraftRequest;

  try {
    const data = await api.copyFlowRecoveryDraft(body);
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
| **runId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **flowRecoveryDraftInput** | [FlowRecoveryDraftInput](FlowRecoveryDraftInput.md) |  | |

### Return type

[**FlowRecoveryOperation**](FlowRecoveryOperation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Completed outcome with original Flow ID for RESTORE or new Flow ID for COPY. |  -  |
| **202** | Partial or unconfirmed outcome, not success. Resume only this same request. |  * Location -  <br>  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createFlow

> Flow createFlow(flowInput, format, idempotencyKey)

Create a test flow

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { CreateFlowRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // FlowInput
    flowInput: ...,
    // ContentFormat | Serialization format used for the returned specification source. (optional)
    format: ...,
    // string | A caller-generated UUID retained for safe write retries where supported. (optional)
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CreateFlowRequest;

  try {
    const data = await api.createFlow(body);
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
| **flowInput** | [FlowInput](FlowInput.md) |  | |
| **format** | `ContentFormat` | Serialization format used for the returned specification source. | [Optional] [Defaults to `undefined`] [Enum: JSON, YAML, XML] |
| **idempotencyKey** | `string` | A caller-generated UUID retained for safe write retries where supported. | [Optional] [Defaults to `undefined`] |

### Return type

[**Flow**](Flow.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored flow. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createFlowRecovery

> FlowRecoveryOperation createFlowRecovery(runId, idempotencyKey, flowRecoveryInput)

Recover a saved run as a new Flow and new dependency copies

Explicitly creates independent owned artifacts. Originals, snapshots and scheduled bindings are unchanged; tests are not executed. Requires current Flow create and owning specification/macro create permissions and entitlements. Keep the same key and identical body after an ambiguous response; GET status never resumes writes. Partial copies remain tracked. Agent-delegated grants are not supported.

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { CreateFlowRecoveryRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // FlowRecoveryInput
    flowRecoveryInput: ...,
  } satisfies CreateFlowRecoveryRequest;

  try {
    const data = await api.createFlowRecovery(body);
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
| **runId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **flowRecoveryInput** | [FlowRecoveryInput](FlowRecoveryInput.md) |  | |

### Return type

[**FlowRecoveryOperation**](FlowRecoveryOperation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Confirmed completed operation; retries reuse its result identities. |  -  |
| **202** | Accepted or unconfirmed operation. Read its status; resume only this same intent explicitly. |  * Location -  <br>  |
| **409** | The request failed. |  -  |
| **422** | The request failed. |  -  |
| **429** | The request failed. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteFlow

> deleteFlow(flowId)

Delete a test flow

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { DeleteFlowRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string
    flowId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteFlowRequest;

  try {
    const data = await api.deleteFlow(body);
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
| **flowId** | `string` |  | [Defaults to `undefined`] |

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
| **204** | Flow deleted. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFlow

> Flow getFlow(flowId)

Get a test flow

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { GetFlowRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved test flow.
    flowId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetFlowRequest;

  try {
    const data = await api.getFlow(body);
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
| **flowId** | `string` | UUIDv7 identifier of the saved test flow. | [Defaults to `undefined`] |

### Return type

[**Flow**](Flow.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested flow. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFlowRecoveryCurrentDependency

> FlowRecoveryCurrentDependency getFlowRecoveryCurrentDependency(runId, kind, sourceId, dependencyKey)

Read one current safe Recovery dependency

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { GetFlowRecoveryCurrentDependencyRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // 'REST' | 'SOAP' | 'GRAPHQL' | 'STREAMING' | 'UI_MACRO'
    kind: kind_example,
    // string
    sourceId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Retained key for an existing occurrence; omit for an explicitly added saved reference. (optional)
    dependencyKey: dependencyKey_example,
  } satisfies GetFlowRecoveryCurrentDependencyRequest;

  try {
    const data = await api.getFlowRecoveryCurrentDependency(body);
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
| **runId** | `string` |  | [Defaults to `undefined`] |
| **kind** | `REST`, `SOAP`, `GRAPHQL`, `STREAMING`, `UI_MACRO` |  | [Defaults to `undefined`] [Enum: REST, SOAP, GRAPHQL, STREAMING, UI_MACRO] |
| **sourceId** | `string` |  | [Defaults to `undefined`] |
| **dependencyKey** | `string` | Retained key for an existing occurrence; omit for an explicitly added saved reference. | [Optional] [Defaults to `undefined`] |

### Return type

[**FlowRecoveryCurrentDependency**](FlowRecoveryCurrentDependency.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current authoring projection and revision, with masked literal inputs. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFlowRecoveryDependency

> FlowRecoveryDependencyDetail getFlowRecoveryDependency(runId, dependencyKey)

Inspect one retained safe dependency definition

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { GetFlowRecoveryDependencyRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    dependencyKey: dependencyKey_example,
  } satisfies GetFlowRecoveryDependencyRequest;

  try {
    const data = await api.getFlowRecoveryDependency(body);
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
| **runId** | `string` |  | [Defaults to `undefined`] |
| **dependencyKey** | `string` |  | [Defaults to `undefined`] |

### Return type

[**FlowRecoveryDependencyDetail**](FlowRecoveryDependencyDetail.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Exact historical safe authoring projection, up to 4 MiB, scoped to this manifest. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFlowRecoveryOperation

> FlowRecoveryOperation getFlowRecoveryOperation(operationId)

Read a Flow recovery outcome without performing writes

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { GetFlowRecoveryOperationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string
    operationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetFlowRecoveryOperationRequest;

  try {
    const data = await api.getFlowRecoveryOperation(body);
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
| **operationId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**FlowRecoveryOperation**](FlowRecoveryOperation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current initiating-principal and project-scoped outcome, with no request bindings or raw dependency bodies. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFlowRun

> FlowRun getFlowRun(runId)

Get a saved flow run

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { GetFlowRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetFlowRunRequest;

  try {
    const data = await api.getFlowRun(body);
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
| **runId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**FlowRun**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete persisted flow run evidence. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listFlowRecoveryDependencies

> FlowRecoveryDependencyPage listFlowRecoveryDependencies(runId, page, size)

List historical dependency versions for Flow recovery

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { ListFlowRecoveryDependenciesRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Zero-based page index. (optional)
    page: 56,
    // number (optional)
    size: 56,
  } satisfies ListFlowRecoveryDependenciesRequest;

  try {
    const data = await api.listFlowRecoveryDependencies(body);
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
| **runId** | `string` |  | [Defaults to `undefined`] |
| **page** | `number` | Zero-based page index. | [Optional] [Defaults to `0`] |
| **size** | `number` |  | [Optional] [Defaults to `20`] |

### Return type

[**FlowRecoveryDependencyPage**](FlowRecoveryDependencyPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary-shaped page, without nested DSL, binaries or worker authority. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listFlowRuns

> FlowRunPage listFlowRuns(flowId, page, size)

List saved runs for a flow

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { ListFlowRunsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved test flow.
    flowId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
  } satisfies ListFlowRunsRequest;

  try {
    const data = await api.listFlowRuns(body);
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
| **flowId** | `string` | UUIDv7 identifier of the saved test flow. | [Defaults to `undefined`] |
| **page** | `number` | Zero-based page index. | [Optional] [Defaults to `0`] |
| **size** | `number` | Maximum number of results returned in one page. | [Optional] [Defaults to `20`] |

### Return type

[**FlowRunPage**](FlowRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of lightweight persisted flow run summaries. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listFlows

> FlowPage listFlows(page, size, search)

List test flows

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { ListFlowsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
    // string | Case-insensitive server-side search within the active project. (optional)
    search: search_example,
  } satisfies ListFlowsRequest;

  try {
    const data = await api.listFlows(body);
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

[**FlowPage**](FlowPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of flow summaries. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## previewFlowRecovery

> FlowRecoveryPreview previewFlowRecovery(runId)

Preview an independent Flow recovery from a saved run

Read-only historical authoring preview. Requires current source Flow/project and dependency read access. Legacy or incomplete evidence is explicitly unavailable. Does not execute tests or create artifacts.

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { PreviewFlowRecoveryRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies PreviewFlowRecoveryRequest;

  try {
    const data = await api.previewFlowRecovery(body);
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
| **runId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**FlowRecoveryPreview**](FlowRecoveryPreview.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Eligibility, historical definition, binding requirements and bounded dependency summaries. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## restoreFlowRecoveryDraft

> FlowRecoveryOperation restoreFlowRecoveryDraft(runId, idempotencyKey, flowRecoveryDraftInput)

Restore an edited historical Flow into the current Flow

Updates the original Flow and selected original dependencies. Shared consumers are affected. Requires current resource update authority. Added saved references stay unchanged. Owner-local receipts make the same exact key/body resumable; some originals may already be updated after a partial failure. No automatic rollback or execution. Mode must be RESTORE. Retain the identical reviewed body and UUID key; GET status never resumes writes.

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { RestoreFlowRecoveryDraftRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // FlowRecoveryDraftInput
    flowRecoveryDraftInput: ...,
  } satisfies RestoreFlowRecoveryDraftRequest;

  try {
    const data = await api.restoreFlowRecoveryDraft(body);
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
| **runId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **flowRecoveryDraftInput** | [FlowRecoveryDraftInput](FlowRecoveryDraftInput.md) |  | |

### Return type

[**FlowRecoveryOperation**](FlowRecoveryOperation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Completed outcome with original Flow ID for RESTORE or new Flow ID for COPY. |  -  |
| **202** | Partial or unconfirmed outcome, not success. Resume only this same request. |  * Location -  <br>  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## reviewFlowRecovery

> FlowRecoveryReview reviewFlowRecovery(runId)

Review Flow Recovery for restore or independent copy

Historical authoring, original occurrence mapping and current versions only. Does not write or execute. Current human and resource read authority required.

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { ReviewFlowRecoveryRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies ReviewFlowRecoveryRequest;

  try {
    const data = await api.reviewFlowRecovery(body);
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
| **runId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**FlowRecoveryReview**](FlowRecoveryReview.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Shared review for both recovery intents. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## runFlow

> FlowRun runFlow(flowId, watch)

Run a saved flow

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { RunFlowRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved test flow.
    flowId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // boolean | Create a browser watch token when the flow contains visible browser steps. (optional)
    watch: true,
  } satisfies RunFlowRequest;

  try {
    const data = await api.runFlow(body);
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
| **flowId** | `string` | UUIDv7 identifier of the saved test flow. | [Defaults to `undefined`] |
| **watch** | `boolean` | Create a browser watch token when the flow contains visible browser steps. | [Optional] [Defaults to `false`] |

### Return type

[**FlowRun**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete flow run evidence. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## runFlowBatch

> Array&lt;FlowRun&gt; runFlowBatch(runFlowBatchRequest)

Run multiple saved flows

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { RunFlowBatchOperationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // RunFlowBatchRequest
    runFlowBatchRequest: ...,
  } satisfies RunFlowBatchOperationRequest;

  try {
    const data = await api.runFlowBatch(body);
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
| **runFlowBatchRequest** | [RunFlowBatchRequest](RunFlowBatchRequest.md) |  | |

### Return type

[**Array&lt;FlowRun&gt;**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete evidence for every requested flow. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateFlow

> Flow updateFlow(flowId, flowInput, format)

Replace a test flow

### Example

```ts
import {
  Configuration,
  FlowsApi,
} from '@spectestengine/sdk';
import type { UpdateFlowRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FlowsApi(config);

  const body = {
    // string
    flowId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // FlowInput
    flowInput: ...,
    // ContentFormat | Serialization format used for the returned specification source. (optional)
    format: ...,
  } satisfies UpdateFlowRequest;

  try {
    const data = await api.updateFlow(body);
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
| **flowId** | `string` |  | [Defaults to `undefined`] |
| **flowInput** | [FlowInput](FlowInput.md) |  | |
| **format** | `ContentFormat` | Serialization format used for the returned specification source. | [Optional] [Defaults to `undefined`] [Enum: JSON, YAML, XML] |

### Return type

[**Flow**](Flow.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated flow. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
