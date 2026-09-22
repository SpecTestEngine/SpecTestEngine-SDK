# FlowsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**captureFlowStepAttachmentVisualDiff**](FlowsApi.md#captureflowstepattachmentvisualdiff) | **POST** /test/flow/run/by-id/{flowId}/visual-diff-captures | Create a visual diff from a failed flow-step attachment assertion |
| [**createFlow**](FlowsApi.md#createflow) | **POST** /test/flow/create | Create a test flow |
| [**deleteFlow**](FlowsApi.md#deleteflow) | **DELETE** /test/flow/by-id | Delete a test flow |
| [**getFlow**](FlowsApi.md#getflow) | **GET** /test/flow/by-id/{flowId} | Get a test flow |
| [**getFlowRun**](FlowsApi.md#getflowrun) | **GET** /test/flow/run/saved/{runId} | Get a saved flow run |
| [**listFlowRuns**](FlowsApi.md#listflowruns) | **GET** /test/flow/run/by-flow-id/{flowId}/page | List saved runs for a flow |
| [**listFlows**](FlowsApi.md#listflows) | **GET** /test/flow/page | List test flows |
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

