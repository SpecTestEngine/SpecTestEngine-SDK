# StreamingSpecificationsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelStreamingSpecificationRun**](StreamingSpecificationsApi.md#cancelstreamingspecificationrun) | **POST** /test/streaming-spec/run/history/by-run-id/{runId}/cancel | Cancel an active streaming run |
| [**createStreamingSpecification**](StreamingSpecificationsApi.md#createstreamingspecification) | **POST** /test/streaming-spec/create | Create a streaming specification |
| [**deleteStreamingSpecification**](StreamingSpecificationsApi.md#deletestreamingspecification) | **DELETE** /test/streaming-spec/by-id | Delete a streaming specification |
| [**getStreamingCapabilities**](StreamingSpecificationsApi.md#getstreamingcapabilities) | **GET** /engine/streaming/capabilities | Get streaming engine capabilities and enforced limits |
| [**getStreamingPreparation**](StreamingSpecificationsApi.md#getstreamingpreparation) | **GET** /test/streaming-spec/preparations/by-ref/{ref} | Read eligible STREAMING Prepare request metadata by stable key |
| [**getStreamingSpecification**](StreamingSpecificationsApi.md#getstreamingspecification) | **GET** /test/streaming-spec/by-id | Get a streaming specification |
| [**getStreamingSpecificationRun**](StreamingSpecificationsApi.md#getstreamingspecificationrun) | **GET** /test/streaming-spec/run/history/by-run-id/{runId} | Get streaming run state and bounded semantic evidence |
| [**getStreamingSpecificationRunTranscript**](StreamingSpecificationsApi.md#getstreamingspecificationruntranscript) | **GET** /test/streaming-spec/run/history/by-run-id/{runId}/transcript | Page a bounded streaming run transcript |
| [**listStreamingPreparations**](StreamingSpecificationsApi.md#liststreamingpreparations) | **GET** /test/streaming-spec/preparations | List eligible Prepare requests and output declarations |
| [**listStreamingSpecificationRuns**](StreamingSpecificationsApi.md#liststreamingspecificationruns) | **GET** /test/streaming-spec/run/page/by-spec-id/{specId} | List runs for a saved streaming specification |
| [**listStreamingSpecifications**](StreamingSpecificationsApi.md#liststreamingspecifications) | **GET** /test/streaming-spec/page | List streaming specifications |
| [**previewStreamingSpecificationRecovery**](StreamingSpecificationsApi.md#previewstreamingspecificationrecovery) | **POST** /test/streaming-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a Streaming specification version |
| [**restoreStreamingSpecificationFromRun**](StreamingSpecificationsApi.md#restorestreamingspecificationfromrun) | **PUT** /test/streaming-spec/recovery/{specId}/from-run/{runId}/restore | Restore a Streaming specification version |
| [**runStreamingSpecification**](StreamingSpecificationsApi.md#runstreamingspecification) | **POST** /test/streaming-spec/run/by-id/{specId} | Queue a saved streaming specification run |
| [**runStreamingSpecificationDraft**](StreamingSpecificationsApi.md#runstreamingspecificationdraft) | **POST** /test/streaming-spec/run/draft | Queue a bounded streaming specification draft run |
| [**testStreamingSpecificationRecoveryVersion**](StreamingSpecificationsApi.md#teststreamingspecificationrecoveryversion) | **POST** /test/streaming-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous Streaming specification version |
| [**updateStreamingSpecification**](StreamingSpecificationsApi.md#updatestreamingspecification) | **PUT** /test/streaming-spec/by-id | Replace a streaming specification definition |
| [**validateStreamingSpecificationDraft**](StreamingSpecificationsApi.md#validatestreamingspecificationdraft) | **POST** /test/streaming-spec/validate-draft | Validate and detect the transport of a streaming specification draft |



## cancelStreamingSpecificationRun

> StreamingRun cancelStreamingSpecificationRun(runId)

Cancel an active streaming run

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { CancelStreamingSpecificationRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CancelStreamingSpecificationRunRequest;

  try {
    const data = await api.cancelStreamingSpecificationRun(body);
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

[**StreamingRun**](StreamingRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Cancelled run, or the unchanged result when it was already terminal. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createStreamingSpecification

> StreamingSpecification createStreamingSpecification(specName, body, description, idempotencyKey)

Create a streaming specification

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { CreateStreamingSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string | User-facing specification name within the active project.
    specName: specName_example,
    // string
    body: body_example,
    // string | Optional user-facing description stored with the asset. (optional)
    description: description_example,
    // string | A caller-generated UUID retained for safe write retries where supported. (optional)
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CreateStreamingSpecificationRequest;

  try {
    const data = await api.createStreamingSpecification(body);
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

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The stored streaming specification and detected transport. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteStreamingSpecification

> StreamingSpecification deleteStreamingSpecification(specId)

Delete a streaming specification

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { DeleteStreamingSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteStreamingSpecificationRequest;

  try {
    const data = await api.deleteStreamingSpecification(body);
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

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted streaming specification. Existing run evidence remains detached and readable. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getStreamingCapabilities

> StreamingCapabilities getStreamingCapabilities()

Get streaming engine capabilities and enforced limits

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { GetStreamingCapabilitiesRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  try {
    const data = await api.getStreamingCapabilities();
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

[**StreamingCapabilities**](StreamingCapabilities.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Supported transports, codecs, actions, expected* assertion fields, endpoint schemes, and hard limits. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getStreamingPreparation

> PreparationSummary getStreamingPreparation(ref)

Read eligible STREAMING Prepare request metadata by stable key

Same-company current-read metadata only; no definition or runtime values. Missing, unmarked or inaccessible sources cannot be selected.

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { GetStreamingPreparationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string
    ref: ref_example,
  } satisfies GetStreamingPreparationRequest;

  try {
    const data = await api.getStreamingPreparation(body);
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


## getStreamingSpecification

> StreamingSpecification getStreamingSpecification(specId)

Get a streaming specification

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { GetStreamingSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetStreamingSpecificationRequest;

  try {
    const data = await api.getStreamingSpecification(body);
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

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested streaming specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getStreamingSpecificationRun

> StreamingRun getStreamingSpecificationRun(runId)

Get streaming run state and bounded semantic evidence

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { GetStreamingSpecificationRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetStreamingSpecificationRunRequest;

  try {
    const data = await api.getStreamingSpecificationRun(body);
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

[**StreamingRun**](StreamingRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current or terminal run metadata and evidence summary. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getStreamingSpecificationRunTranscript

> StreamingTranscriptPage getStreamingSpecificationRunTranscript(runId, page, size)

Page a bounded streaming run transcript

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { GetStreamingSpecificationRunTranscriptRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Zero-based page index. (optional)
    page: 56,
    // number (optional)
    size: 56,
  } satisfies GetStreamingSpecificationRunTranscriptRequest;

  try {
    const data = await api.getStreamingSpecificationRunTranscript(body);
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
| **page** | `number` | Zero-based page index. | [Optional] [Defaults to `0`] |
| **size** | `number` |  | [Optional] [Defaults to `100`] |

### Return type

[**StreamingTranscriptPage**](StreamingTranscriptPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One transcript page. Payload exclusions and redactions are already applied. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listStreamingPreparations

> PreparationPage listStreamingPreparations(page, size, search)

List eligible Prepare requests and output declarations

Same-company paginated metadata only. Values and full specification definitions are never included. The selected protocol and stableKey are used as preparation.protocol and preparation.ref in the consumer DSL. Any native protocol can prepare any other protocol.

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { ListStreamingPreparationsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // number | Zero-based page index. (optional)
    page: 56,
    // number (optional)
    size: 56,
    // string | Case-insensitive server-side search within the active project. (optional)
    search: search_example,
  } satisfies ListStreamingPreparationsRequest;

  try {
    const data = await api.listStreamingPreparations(body);
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
| **200** | A page of eligible STREAMING preparation sources. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listStreamingSpecificationRuns

> StreamingRunPage listStreamingSpecificationRuns(specId, page, size)

List runs for a saved streaming specification

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { ListStreamingSpecificationRunsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
  } satisfies ListStreamingSpecificationRunsRequest;

  try {
    const data = await api.listStreamingSpecificationRuns(body);
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

[**StreamingRunPage**](StreamingRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of current and terminal streaming runs. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listStreamingSpecifications

> StreamingSpecificationPage listStreamingSpecifications(page, size, search, transport)

List streaming specifications

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { ListStreamingSpecificationsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
    // string | Case-insensitive server-side search within the active project. (optional)
    search: search_example,
    // StreamingTransport | Filter by streaming transport. (optional)
    transport: ...,
  } satisfies ListStreamingSpecificationsRequest;

  try {
    const data = await api.listStreamingSpecifications(body);
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
| **transport** | `StreamingTransport` | Filter by streaming transport. | [Optional] [Defaults to `undefined`] [Enum: WEBSOCKET, SSE, GRPC, MQTT] |

### Return type

[**StreamingSpecificationPage**](StreamingSpecificationPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of WebSocket/WSS, SSE, gRPC Streaming, and MQTT specifications. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## previewStreamingSpecificationRecovery

> SpecificationRecoveryPreview previewStreamingSpecificationRecovery(specId, runId)

Preview restoring a Streaming specification version

Compares the current specification with the exact DSL snapshot retained by a completed PASS or FAIL run. No expectations are regenerated.

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { PreviewStreamingSpecificationRecoveryRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies PreviewStreamingSpecificationRecoveryRequest;

  try {
    const data = await api.previewStreamingSpecificationRecovery(body);
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


## restoreStreamingSpecificationFromRun

> StreamingSpecification restoreStreamingSpecificationFromRun(specId, runId)

Restore a Streaming specification version

Replaces only the current DSL content with the exact snapshot retained by a completed PASS or FAIL run. The specification id, name, description, and stable identity are preserved.

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { RestoreStreamingSpecificationFromRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies RestoreStreamingSpecificationFromRunRequest;

  try {
    const data = await api.restoreStreamingSpecificationFromRun(body);
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

[**StreamingSpecification**](StreamingSpecification.md)

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


## runStreamingSpecification

> StreamingRunAccepted runStreamingSpecification(specId)

Queue a saved streaming specification run

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { RunStreamingSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies RunStreamingSpecificationRequest;

  try {
    const data = await api.runStreamingSpecification(body);
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

[**StreamingRunAccepted**](StreamingRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Run accepted. Poll the returned status URL until the state is terminal. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## runStreamingSpecificationDraft

> StreamingRunAccepted runStreamingSpecificationDraft(body, specName)

Queue a bounded streaming specification draft run

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { RunStreamingSpecificationDraftRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string
    body: body_example,
    // string (optional)
    specName: specName_example,
  } satisfies RunStreamingSpecificationDraftRequest;

  try {
    const data = await api.runStreamingSpecificationDraft(body);
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
| **body** | `string` |  | |
| **specName** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**StreamingRunAccepted**](StreamingRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Run accepted. Poll statusUrl, page transcriptUrl, or POST cancelUrl. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## testStreamingSpecificationRecoveryVersion

> StreamingRun testStreamingSpecificationRecoveryVersion(specId, runId)

Test a previous Streaming specification version

Executes the exact DSL snapshot retained by the selected completed PASS or FAIL run against the current API without changing the saved specification.

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { TestStreamingSpecificationRecoveryVersionRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies TestStreamingSpecificationRecoveryVersionRequest;

  try {
    const data = await api.testStreamingSpecificationRecoveryVersion(body);
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

[**StreamingRun**](StreamingRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete terminal test-run evidence for the selected version. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateStreamingSpecification

> StreamingSpecification updateStreamingSpecification(specId, body, description)

Replace a streaming specification definition

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { UpdateStreamingSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    body: body_example,
    // string | Optional user-facing description stored with the asset. (optional)
    description: description_example,
  } satisfies UpdateStreamingSpecificationRequest;

  try {
    const data = await api.updateStreamingSpecification(body);
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

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated streaming specification and newly detected transport. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## validateStreamingSpecificationDraft

> StreamingDraftValidation validateStreamingSpecificationDraft(body)

Validate and detect the transport of a streaming specification draft

### Example

```ts
import {
  Configuration,
  StreamingSpecificationsApi,
} from '@spectestengine/sdk';
import type { ValidateStreamingSpecificationDraftRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new StreamingSpecificationsApi(config);

  const body = {
    // string
    body: body_example,
  } satisfies ValidateStreamingSpecificationDraftRequest;

  try {
    const data = await api.validateStreamingSpecificationDraft(body);
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
| **body** | `string` |  | |

### Return type

[**StreamingDraftValidation**](StreamingDraftValidation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid draft with its detected streaming transport. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
