# CraftsmanApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelCraftsmanRun**](CraftsmanApi.md#cancelcraftsmanrun) | **POST** /sentinel/request-workspaces/runs/{runId}/cancel | Cancel a queued or active Craftsman run |
| [**createRequestNode**](CraftsmanApi.md#createrequestnode) | **POST** /sentinel/request-workspaces/{workspaceId}/nodes | Add a folder or saved request |
| [**createRequestWorkspace**](CraftsmanApi.md#createrequestworkspace) | **POST** /sentinel/request-workspaces | Create a request workspace |
| [**deleteRequestNode**](CraftsmanApi.md#deleterequestnode) | **DELETE** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId} | Delete a folder or saved request |
| [**deleteRequestWorkspace**](CraftsmanApi.md#deleterequestworkspace) | **DELETE** /sentinel/request-workspaces/{workspaceId} | Delete a request workspace |
| [**getCraftsmanRun**](CraftsmanApi.md#getcraftsmanrun) | **GET** /sentinel/request-workspaces/runs/{runId} | Get Craftsman run lifecycle and evidence |
| [**getCraftsmanRunTranscript**](CraftsmanApi.md#getcraftsmanruntranscript) | **GET** /sentinel/request-workspaces/runs/{runId}/transcript | Get a Craftsman Streaming semantic transcript |
| [**getDocumentAsset**](CraftsmanApi.md#getdocumentasset) | **GET** /sentinel/document-assets/{assetId} | Resolve request attachment metadata |
| [**getRequestWorkspace**](CraftsmanApi.md#getrequestworkspace) | **GET** /sentinel/request-workspaces/{workspaceId} | Get a request workspace |
| [**listRequestWorkspaces**](CraftsmanApi.md#listrequestworkspaces) | **GET** /sentinel/request-workspaces/page | List request workspaces |
| [**queueCraftsmanStreamingRun**](CraftsmanApi.md#queuecraftsmanstreamingrun) | **POST** /sentinel/request-workspaces/runs/streaming | Queue a standalone bounded Streaming session |
| [**queueCraftsmanWorkflowRun**](CraftsmanApi.md#queuecraftsmanworkflowrun) | **POST** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId}/runs | Queue a saved request or mixed-protocol Workflow run |
| [**updateRequestNode**](CraftsmanApi.md#updaterequestnode) | **PUT** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId} | Update a folder or saved request |
| [**updateRequestWorkspace**](CraftsmanApi.md#updaterequestworkspace) | **PUT** /sentinel/request-workspaces/{workspaceId} | Replace request workspace metadata and variables |
| [**uploadDocumentAsset**](CraftsmanApi.md#uploaddocumentasset) | **POST** /sentinel/document-assets | Upload a reusable request attachment |



## cancelCraftsmanRun

> CraftsmanRun cancelCraftsmanRun(runId)

Cancel a queued or active Craftsman run

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { CancelCraftsmanRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CancelCraftsmanRunRequest;

  try {
    const data = await api.cancelCraftsmanRun(body);
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

[**CraftsmanRun**](CraftsmanRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated lifecycle after cooperative cancellation was requested. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createRequestNode

> RequestNode createRequestNode(workspaceId, requestNodeInput, idempotencyKey)

Add a folder or saved request

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { CreateRequestNodeRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // string | UUIDv7 identifier of the Craftsman request workspace.
    workspaceId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // RequestNodeInput
    requestNodeInput: ...,
    // string | A caller-generated UUID retained for safe write retries where supported. (optional)
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CreateRequestNodeRequest;

  try {
    const data = await api.createRequestNode(body);
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
| **workspaceId** | `string` | UUIDv7 identifier of the Craftsman request workspace. | [Defaults to `undefined`] |
| **requestNodeInput** | [RequestNodeInput](RequestNodeInput.md) |  | |
| **idempotencyKey** | `string` | A caller-generated UUID retained for safe write retries where supported. | [Optional] [Defaults to `undefined`] |

### Return type

[**RequestNode**](RequestNode.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created workspace node. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createRequestWorkspace

> RequestWorkspace createRequestWorkspace(requestWorkspaceInput, idempotencyKey)

Create a request workspace

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { CreateRequestWorkspaceRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // RequestWorkspaceInput
    requestWorkspaceInput: ...,
    // string | A caller-generated UUID retained for safe write retries where supported. (optional)
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CreateRequestWorkspaceRequest;

  try {
    const data = await api.createRequestWorkspace(body);
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
| **requestWorkspaceInput** | [RequestWorkspaceInput](RequestWorkspaceInput.md) |  | |
| **idempotencyKey** | `string` | A caller-generated UUID retained for safe write retries where supported. | [Optional] [Defaults to `undefined`] |

### Return type

[**RequestWorkspace**](RequestWorkspace.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created workspace. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteRequestNode

> deleteRequestNode(workspaceId, nodeId)

Delete a folder or saved request

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { DeleteRequestNodeRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // string | UUIDv7 identifier of the Craftsman request workspace.
    workspaceId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    nodeId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteRequestNodeRequest;

  try {
    const data = await api.deleteRequestNode(body);
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
| **workspaceId** | `string` | UUIDv7 identifier of the Craftsman request workspace. | [Defaults to `undefined`] |
| **nodeId** | `string` |  | [Defaults to `undefined`] |

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
| **204** | Workspace node deleted. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteRequestWorkspace

> deleteRequestWorkspace(workspaceId)

Delete a request workspace

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { DeleteRequestWorkspaceRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // string | UUIDv7 identifier of the Craftsman request workspace.
    workspaceId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteRequestWorkspaceRequest;

  try {
    const data = await api.deleteRequestWorkspace(body);
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
| **workspaceId** | `string` | UUIDv7 identifier of the Craftsman request workspace. | [Defaults to `undefined`] |

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
| **204** | Workspace deleted. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getCraftsmanRun

> CraftsmanRun getCraftsmanRun(runId)

Get Craftsman run lifecycle and evidence

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { GetCraftsmanRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetCraftsmanRunRequest;

  try {
    const data = await api.getCraftsmanRun(body);
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

[**CraftsmanRun**](CraftsmanRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current lifecycle and terminal result when available. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getCraftsmanRunTranscript

> any getCraftsmanRunTranscript(runId)

Get a Craftsman Streaming semantic transcript

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { GetCraftsmanRunTranscriptRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetCraftsmanRunTranscriptRequest;

  try {
    const data = await api.getCraftsmanRunTranscript(body);
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

**any**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bounded semantic event transcript captured by Sentinel. Use the completed run result for connection, assertion, and termination evidence required by Generate Spec. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getDocumentAsset

> DocumentAssetReference getDocumentAsset(assetId, fieldName, contentId)

Resolve request attachment metadata

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { GetDocumentAssetRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // string
    assetId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string (optional)
    fieldName: fieldName_example,
    // string (optional)
    contentId: contentId_example,
  } satisfies GetDocumentAssetRequest;

  try {
    const data = await api.getDocumentAsset(body);
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
| **assetId** | `string` |  | [Defaults to `undefined`] |
| **fieldName** | `string` |  | [Optional] [Defaults to `&#39;file&#39;`] |
| **contentId** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DocumentAssetReference**](DocumentAssetReference.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attachment metadata suitable for reuse in a saved request or specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getRequestWorkspace

> RequestWorkspace getRequestWorkspace(workspaceId)

Get a request workspace

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { GetRequestWorkspaceRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // string | UUIDv7 identifier of the Craftsman request workspace.
    workspaceId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetRequestWorkspaceRequest;

  try {
    const data = await api.getRequestWorkspace(body);
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
| **workspaceId** | `string` | UUIDv7 identifier of the Craftsman request workspace. | [Defaults to `undefined`] |

### Return type

[**RequestWorkspace**](RequestWorkspace.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The complete workspace tree. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listRequestWorkspaces

> RequestWorkspacePage listRequestWorkspaces(page, size, search)

List request workspaces

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { ListRequestWorkspacesRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
    // string | Case-insensitive server-side search within the active project. (optional)
    search: search_example,
  } satisfies ListRequestWorkspacesRequest;

  try {
    const data = await api.listRequestWorkspaces(body);
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

[**RequestWorkspacePage**](RequestWorkspacePage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of request workspaces. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## queueCraftsmanStreamingRun

> CraftsmanRunAccepted queueCraftsmanStreamingRun(craftsmanStreamingRunInput)

Queue a standalone bounded Streaming session

Standalone sessions require concrete values and do not inherit Workflow variables.

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { QueueCraftsmanStreamingRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // CraftsmanStreamingRunInput
    craftsmanStreamingRunInput: ...,
  } satisfies QueueCraftsmanStreamingRunRequest;

  try {
    const data = await api.queueCraftsmanStreamingRun(body);
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
| **craftsmanStreamingRunInput** | [CraftsmanStreamingRunInput](CraftsmanStreamingRunInput.md) |  | |

### Return type

[**CraftsmanRunAccepted**](CraftsmanRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The bounded session was accepted. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## queueCraftsmanWorkflowRun

> CraftsmanRunAccepted queueCraftsmanWorkflowRun(workspaceId, nodeId, requestChainRunInput)

Queue a saved request or mixed-protocol Workflow run

Supports REST, SOAP, GraphQL, WebSocket/WSS, SSE, gRPC Streaming, and MQTT nodes. Poll the returned run id.

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { QueueCraftsmanWorkflowRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // string | UUIDv7 identifier of the Craftsman request workspace.
    workspaceId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    nodeId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // RequestChainRunInput (optional)
    requestChainRunInput: ...,
  } satisfies QueueCraftsmanWorkflowRunRequest;

  try {
    const data = await api.queueCraftsmanWorkflowRun(body);
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
| **workspaceId** | `string` | UUIDv7 identifier of the Craftsman request workspace. | [Defaults to `undefined`] |
| **nodeId** | `string` |  | [Defaults to `undefined`] |
| **requestChainRunInput** | [RequestChainRunInput](RequestChainRunInput.md) |  | [Optional] |

### Return type

[**CraftsmanRunAccepted**](CraftsmanRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The bounded Craftsman run was accepted. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateRequestNode

> RequestNode updateRequestNode(workspaceId, nodeId, requestNodeInput)

Update a folder or saved request

Replaces the selected node definition. STREAMING requests use streamingSpec and do not accept HTTP request fields.

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { UpdateRequestNodeRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // string | UUIDv7 identifier of the Craftsman request workspace.
    workspaceId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    nodeId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // RequestNodeInput
    requestNodeInput: ...,
  } satisfies UpdateRequestNodeRequest;

  try {
    const data = await api.updateRequestNode(body);
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
| **workspaceId** | `string` | UUIDv7 identifier of the Craftsman request workspace. | [Defaults to `undefined`] |
| **nodeId** | `string` |  | [Defaults to `undefined`] |
| **requestNodeInput** | [RequestNodeInput](RequestNodeInput.md) |  | |

### Return type

[**RequestNode**](RequestNode.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated workspace node. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateRequestWorkspace

> RequestWorkspace updateRequestWorkspace(workspaceId, requestWorkspaceInput)

Replace request workspace metadata and variables

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { UpdateRequestWorkspaceRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // string | UUIDv7 identifier of the Craftsman request workspace.
    workspaceId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // RequestWorkspaceInput
    requestWorkspaceInput: ...,
  } satisfies UpdateRequestWorkspaceRequest;

  try {
    const data = await api.updateRequestWorkspace(body);
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
| **workspaceId** | `string` | UUIDv7 identifier of the Craftsman request workspace. | [Defaults to `undefined`] |
| **requestWorkspaceInput** | [RequestWorkspaceInput](RequestWorkspaceInput.md) |  | |

### Return type

[**RequestWorkspace**](RequestWorkspace.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated workspace. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## uploadDocumentAsset

> DocumentAssetReference uploadDocumentAsset(file, fieldName, contentId)

Upload a reusable request attachment

### Example

```ts
import {
  Configuration,
  CraftsmanApi,
} from '@spectestengine/sdk';
import type { UploadDocumentAssetRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CraftsmanApi(config);

  const body = {
    // Blob
    file: BINARY_DATA_HERE,
    // string (optional)
    fieldName: fieldName_example,
    // string (optional)
    contentId: contentId_example,
  } satisfies UploadDocumentAssetRequest;

  try {
    const data = await api.uploadDocumentAsset(body);
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
| **file** | `Blob` |  | [Defaults to `undefined`] |
| **fieldName** | `string` |  | [Optional] [Defaults to `&#39;file&#39;`] |
| **contentId** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DocumentAssetReference**](DocumentAssetReference.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Immutable content-addressed attachment reference. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
