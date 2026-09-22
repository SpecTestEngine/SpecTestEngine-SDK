# SnapshotsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**compareSnapshotStep**](SnapshotsApi.md#comparesnapshotstep) | **POST** /test/snapshot/diff/step | Compare snapshot step payloads |
| [**compareSnapshotToRunBatch**](SnapshotsApi.md#comparesnapshottorunbatch) | **GET** /test/snapshot/diff/snapshot/{snapshotId}/batch/{batchId} | Compare a snapshot with a run batch |
| [**compareSnapshots**](SnapshotsApi.md#comparesnapshots) | **GET** /test/snapshot/diff/snapshot/{leftSnapshotId}/snapshot/{rightSnapshotId} | Compare two snapshots |
| [**createSnapshot**](SnapshotsApi.md#createsnapshot) | **POST** /test/snapshot/create | Create a snapshot baseline |
| [**getSnapshot**](SnapshotsApi.md#getsnapshot) | **GET** /test/snapshot/by-id/{snapshotId} | Get a snapshot |
| [**listSnapshots**](SnapshotsApi.md#listsnapshots) | **GET** /test/snapshot/page | List snapshots |



## compareSnapshotStep

> SnapshotStepDiff compareSnapshotStep(snapshotStepDiffInput)

Compare snapshot step payloads

Produce a field-level definition and behavior diff for one API, UI macro, or browser-action step.

### Example

```ts
import {
  Configuration,
  SnapshotsApi,
} from '@spectestengine/sdk';
import type { CompareSnapshotStepRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SnapshotsApi(config);

  const body = {
    // SnapshotStepDiffInput
    snapshotStepDiffInput: ...,
  } satisfies CompareSnapshotStepRequest;

  try {
    const data = await api.compareSnapshotStep(body);
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
| **snapshotStepDiffInput** | [SnapshotStepDiffInput](SnapshotStepDiffInput.md) |  | |

### Return type

[**SnapshotStepDiff**](SnapshotStepDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A grouped, field-level step comparison suitable for a review UI. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## compareSnapshotToRunBatch

> SnapshotDiff compareSnapshotToRunBatch(snapshotId, batchId)

Compare a snapshot with a run batch

Compare a saved baseline with fresh run-batch evidence before promoting a new snapshot.

### Example

```ts
import {
  Configuration,
  SnapshotsApi,
} from '@spectestengine/sdk';
import type { CompareSnapshotToRunBatchRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SnapshotsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved snapshot baseline.
    snapshotId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | UUIDv7 identifier of the saved run batch.
    batchId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CompareSnapshotToRunBatchRequest;

  try {
    const data = await api.compareSnapshotToRunBatch(body);
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
| **snapshotId** | `string` | UUIDv7 identifier of the saved snapshot baseline. | [Defaults to `undefined`] |
| **batchId** | `string` | UUIDv7 identifier of the saved run batch. | [Defaults to `undefined`] |

### Return type

[**SnapshotDiff**](SnapshotDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The classified baseline-to-batch comparison. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## compareSnapshots

> SnapshotDiff compareSnapshots(leftSnapshotId, rightSnapshotId)

Compare two snapshots

Compare two saved baselines and classify new, removed, regressed, improved, and stable subjects.

### Example

```ts
import {
  Configuration,
  SnapshotsApi,
} from '@spectestengine/sdk';
import type { CompareSnapshotsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SnapshotsApi(config);

  const body = {
    // string | UUIDv7 identifier of the baseline side of the comparison.
    leftSnapshotId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | UUIDv7 identifier of the candidate side of the comparison.
    rightSnapshotId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CompareSnapshotsRequest;

  try {
    const data = await api.compareSnapshots(body);
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
| **leftSnapshotId** | `string` | UUIDv7 identifier of the baseline side of the comparison. | [Defaults to `undefined`] |
| **rightSnapshotId** | `string` | UUIDv7 identifier of the candidate side of the comparison. | [Defaults to `undefined`] |

### Return type

[**SnapshotDiff**](SnapshotDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The classified snapshot comparison. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createSnapshot

> Snapshot createSnapshot(snapshotInput, idempotencyKey)

Create a snapshot baseline

Promote all or a selected subset of one run batch into a versioned baseline for later regression comparison.

### Example

```ts
import {
  Configuration,
  SnapshotsApi,
} from '@spectestengine/sdk';
import type { CreateSnapshotRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SnapshotsApi(config);

  const body = {
    // SnapshotInput
    snapshotInput: ...,
    // string | A caller-generated UUID retained for safe write retries where supported. (optional)
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CreateSnapshotRequest;

  try {
    const data = await api.createSnapshot(body);
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
| **snapshotInput** | [SnapshotInput](SnapshotInput.md) |  | |
| **idempotencyKey** | `string` | A caller-generated UUID retained for safe write retries where supported. | [Optional] [Defaults to `undefined`] |

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created snapshot baseline. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getSnapshot

> Snapshot getSnapshot(snapshotId)

Get a snapshot

### Example

```ts
import {
  Configuration,
  SnapshotsApi,
} from '@spectestengine/sdk';
import type { GetSnapshotRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SnapshotsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved snapshot baseline.
    snapshotId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetSnapshotRequest;

  try {
    const data = await api.getSnapshot(body);
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
| **snapshotId** | `string` | UUIDv7 identifier of the saved snapshot baseline. | [Defaults to `undefined`] |

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested snapshot and its baseline evidence. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listSnapshots

> SnapshotPage listSnapshots(page, size, search)

List snapshots

### Example

```ts
import {
  Configuration,
  SnapshotsApi,
} from '@spectestengine/sdk';
import type { ListSnapshotsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SnapshotsApi(config);

  const body = {
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
    // string | Case-insensitive server-side search within the active project. (optional)
    search: search_example,
  } satisfies ListSnapshotsRequest;

  try {
    const data = await api.listSnapshots(body);
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

[**SnapshotPage**](SnapshotPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of snapshot baselines in the active project. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

