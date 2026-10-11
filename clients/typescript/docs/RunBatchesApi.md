# RunBatchesApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRunBatch**](RunBatchesApi.md#createrunbatch) | **POST** /test/run-batch/create | Create a run batch |
| [**getRunBatch**](RunBatchesApi.md#getrunbatch) | **GET** /test/run-batch/by-id/{batchId} | Get a run batch |
| [**listRunBatches**](RunBatchesApi.md#listrunbatches) | **GET** /test/run-batch/page | List run batches |



## createRunBatch

> RunBatch createRunBatch(runBatchInput, idempotencyKey)

Create a run batch

Collect completed specification, UI macro, and flow runs into one immutable evidence set that can later become a snapshot baseline.

### Example

```ts
import {
  Configuration,
  RunBatchesApi,
} from '@spectestengine/sdk';
import type { CreateRunBatchRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RunBatchesApi(config);

  const body = {
    // RunBatchInput
    runBatchInput: ...,
    // string | A caller-generated UUID retained for safe write retries where supported. (optional)
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CreateRunBatchRequest;

  try {
    const data = await api.createRunBatch(body);
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
| **runBatchInput** | [RunBatchInput](RunBatchInput.md) |  | |
| **idempotencyKey** | `string` | A caller-generated UUID retained for safe write retries where supported. | [Optional] [Defaults to `undefined`] |

### Return type

[**RunBatch**](RunBatch.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created run batch and its captured evidence items. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getRunBatch

> RunBatch getRunBatch(batchId)

Get a run batch

### Example

```ts
import {
  Configuration,
  RunBatchesApi,
} from '@spectestengine/sdk';
import type { GetRunBatchRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RunBatchesApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved run batch.
    batchId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetRunBatchRequest;

  try {
    const data = await api.getRunBatch(body);
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
| **batchId** | `string` | UUIDv7 identifier of the saved run batch. | [Defaults to `undefined`] |

### Return type

[**RunBatch**](RunBatch.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested run batch with its captured evidence items. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listRunBatches

> RunBatchPage listRunBatches(page, size, search)

List run batches

### Example

```ts
import {
  Configuration,
  RunBatchesApi,
} from '@spectestengine/sdk';
import type { ListRunBatchesRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new RunBatchesApi(config);

  const body = {
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
    // string | Case-insensitive server-side search within the active project. (optional)
    search: search_example,
  } satisfies ListRunBatchesRequest;

  try {
    const data = await api.listRunBatches(body);
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

[**RunBatchPage**](RunBatchPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of run batches in the active project. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
