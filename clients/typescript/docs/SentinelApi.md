# SentinelApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSentinelCheck**](SentinelApi.md#createsentinelcheck) | **POST** /sentinel/checks | Create a Sentinel check |
| [**deleteSentinelCheck**](SentinelApi.md#deletesentinelcheck) | **DELETE** /sentinel/checks/{checkId} | Delete a Sentinel check |
| [**enqueueSentinelRun**](SentinelApi.md#enqueuesentinelrun) | **POST** /sentinel/checks/{checkId}/run | Queue a Sentinel run |
| [**getSentinelCheck**](SentinelApi.md#getsentinelcheck) | **GET** /sentinel/checks/{checkId} | Get a Sentinel check |
| [**getSentinelDashboardSummary**](SentinelApi.md#getsentineldashboardsummary) | **GET** /sentinel/dashboard/summary | Get Sentinel dashboard summary |
| [**getSentinelRun**](SentinelApi.md#getsentinelrun) | **GET** /sentinel/runs/{runId} | Get Sentinel run evidence |
| [**listLatestSentinelRuns**](SentinelApi.md#listlatestsentinelruns) | **GET** /sentinel/runs | List latest Sentinel runs |
| [**listSentinelChecks**](SentinelApi.md#listsentinelchecks) | **GET** /sentinel/checks/page | List Sentinel checks |
| [**listSentinelDashboardIncidents**](SentinelApi.md#listsentineldashboardincidents) | **GET** /sentinel/dashboard/incidents | List recent Sentinel incidents |
| [**listSentinelLinkedAssets**](SentinelApi.md#listsentinellinkedassets) | **GET** /sentinel/checks/spec-links/page | List compact Sentinel links for one Automation asset type |
| [**listSentinelRuns**](SentinelApi.md#listsentinelruns) | **GET** /sentinel/runs/page | List Sentinel runs |
| [**sampleSentinelRuns**](SentinelApi.md#samplesentinelruns) | **GET** /sentinel/runs/sample | Sample Sentinel runs |
| [**updateSentinelCheck**](SentinelApi.md#updatesentinelcheck) | **PUT** /sentinel/checks/{checkId} | Replace a Sentinel check configuration |



## createSentinelCheck

> SentinelCheck createSentinelCheck(sentinelCheckInput, idempotencyKey)

Create a Sentinel check

### Example

```ts
import {
  Configuration,
  SentinelApi,
} from '@spectestengine/sdk';
import type { CreateSentinelCheckRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SentinelApi(config);

  const body = {
    // SentinelCheckInput
    sentinelCheckInput: ...,
    // string | A caller-generated UUID retained for safe write retries where supported. (optional)
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CreateSentinelCheckRequest;

  try {
    const data = await api.createSentinelCheck(body);
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
| **sentinelCheckInput** | [SentinelCheckInput](SentinelCheckInput.md) |  | |
| **idempotencyKey** | `string` | A caller-generated UUID retained for safe write retries where supported. | [Optional] [Defaults to `undefined`] |

### Return type

[**SentinelCheck**](SentinelCheck.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created check. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteSentinelCheck

> deleteSentinelCheck(checkId)

Delete a Sentinel check

### Example

```ts
import {
  Configuration,
  SentinelApi,
} from '@spectestengine/sdk';
import type { DeleteSentinelCheckRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SentinelApi(config);

  const body = {
    // string | UUIDv7 identifier of the Sentinel check.
    checkId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteSentinelCheckRequest;

  try {
    const data = await api.deleteSentinelCheck(body);
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
| **checkId** | `string` | UUIDv7 identifier of the Sentinel check. | [Defaults to `undefined`] |

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
| **204** | Check deleted. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## enqueueSentinelRun

> RunEnqueueResponse enqueueSentinelRun(checkId, idempotencyKey, region)

Queue a Sentinel run

### Example

```ts
import {
  Configuration,
  SentinelApi,
} from '@spectestengine/sdk';
import type { EnqueueSentinelRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SentinelApi(config);

  const body = {
    // string | UUIDv7 identifier of the Sentinel check.
    checkId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A caller-generated UUID retained for safe write retries where supported. (optional)
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string (optional)
    region: region_example,
  } satisfies EnqueueSentinelRunRequest;

  try {
    const data = await api.enqueueSentinelRun(body);
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
| **checkId** | `string` | UUIDv7 identifier of the Sentinel check. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A caller-generated UUID retained for safe write retries where supported. | [Optional] [Defaults to `undefined`] |
| **region** | `string` |  | [Optional] [Defaults to `&#39;local&#39;`] |

### Return type

[**RunEnqueueResponse**](RunEnqueueResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Queue acknowledgement and execution id. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getSentinelCheck

> SentinelCheck getSentinelCheck(checkId)

Get a Sentinel check

### Example

```ts
import {
  Configuration,
  SentinelApi,
} from '@spectestengine/sdk';
import type { GetSentinelCheckRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SentinelApi(config);

  const body = {
    // string | UUIDv7 identifier of the Sentinel check.
    checkId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetSentinelCheckRequest;

  try {
    const data = await api.getSentinelCheck(body);
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
| **checkId** | `string` | UUIDv7 identifier of the Sentinel check. | [Defaults to `undefined`] |

### Return type

[**SentinelCheck**](SentinelCheck.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested check. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getSentinelDashboardSummary

> SentinelDashboardSummary getSentinelDashboardSummary(environment)

Get Sentinel dashboard summary

### Example

```ts
import {
  Configuration,
  SentinelApi,
} from '@spectestengine/sdk';
import type { GetSentinelDashboardSummaryRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SentinelApi(config);

  const body = {
    // string | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
    environment: environment_example,
  } satisfies GetSentinelDashboardSummaryRequest;

  try {
    const data = await api.getSentinelDashboardSummary(body);
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
| **environment** | `string` | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. | [Defaults to `undefined`] |

### Return type

[**SentinelDashboardSummary**](SentinelDashboardSummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Environment-scoped Sentinel dashboard counters and latency summary. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getSentinelRun

> SentinelRun getSentinelRun(runId)

Get Sentinel run evidence

### Example

```ts
import {
  Configuration,
  SentinelApi,
} from '@spectestengine/sdk';
import type { GetSentinelRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SentinelApi(config);

  const body = {
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetSentinelRunRequest;

  try {
    const data = await api.getSentinelRun(body);
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

[**SentinelRun**](SentinelRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Run, retry attempts, response preview, and baseline evidence. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listLatestSentinelRuns

> Array&lt;SentinelRun&gt; listLatestSentinelRuns(environment, size)

List latest Sentinel runs

### Example

```ts
import {
  Configuration,
  SentinelApi,
} from '@spectestengine/sdk';
import type { ListLatestSentinelRunsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SentinelApi(config);

  const body = {
    // string | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
    environment: environment_example,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
  } satisfies ListLatestSentinelRunsRequest;

  try {
    const data = await api.listLatestSentinelRuns(body);
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
| **environment** | `string` | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. | [Defaults to `undefined`] |
| **size** | `number` | Maximum number of results returned in one page. | [Optional] [Defaults to `20`] |

### Return type

[**Array&lt;SentinelRun&gt;**](SentinelRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The latest Sentinel runs for the selected environment. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listSentinelChecks

> SentinelCheckPage listSentinelChecks(environment, page, size, search)

List Sentinel checks

### Example

```ts
import {
  Configuration,
  SentinelApi,
} from '@spectestengine/sdk';
import type { ListSentinelChecksRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SentinelApi(config);

  const body = {
    // string | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
    environment: environment_example,
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
    // string | Case-insensitive server-side search within the active project. (optional)
    search: search_example,
  } satisfies ListSentinelChecksRequest;

  try {
    const data = await api.listSentinelChecks(body);
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
| **environment** | `string` | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. | [Defaults to `undefined`] |
| **page** | `number` | Zero-based page index. | [Optional] [Defaults to `0`] |
| **size** | `number` | Maximum number of results returned in one page. | [Optional] [Defaults to `20`] |
| **search** | `string` | Case-insensitive server-side search within the active project. | [Optional] [Defaults to `undefined`] |

### Return type

[**SentinelCheckPage**](SentinelCheckPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of Sentinel checks. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listSentinelDashboardIncidents

> Array&lt;SentinelIncident&gt; listSentinelDashboardIncidents(environment)

List recent Sentinel incidents

### Example

```ts
import {
  Configuration,
  SentinelApi,
} from '@spectestengine/sdk';
import type { ListSentinelDashboardIncidentsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SentinelApi(config);

  const body = {
    // string | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
    environment: environment_example,
  } satisfies ListSentinelDashboardIncidentsRequest;

  try {
    const data = await api.listSentinelDashboardIncidents(body);
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
| **environment** | `string` | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. | [Defaults to `undefined`] |

### Return type

[**Array&lt;SentinelIncident&gt;**](SentinelIncident.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recent incidents for the selected Sentinel environment. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listSentinelLinkedAssets

> SentinelLinkSummaryPage listSentinelLinkedAssets(environment, checkType, page, size)

List compact Sentinel links for one Automation asset type

### Example

```ts
import {
  Configuration,
  SentinelApi,
} from '@spectestengine/sdk';
import type { ListSentinelLinkedAssetsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SentinelApi(config);

  const body = {
    // string | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
    environment: environment_example,
    // SentinelLinkedAssetCheckType | Exact Automation asset type whose Sentinel links should be returned.
    checkType: ...,
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
  } satisfies ListSentinelLinkedAssetsRequest;

  try {
    const data = await api.listSentinelLinkedAssets(body);
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
| **environment** | `string` | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. | [Defaults to `undefined`] |
| **checkType** | `SentinelLinkedAssetCheckType` | Exact Automation asset type whose Sentinel links should be returned. | [Defaults to `undefined`] [Enum: REST, SOAP, GRAPHQL, STREAMING, FLOW] |
| **page** | `number` | Zero-based page index. | [Optional] [Defaults to `0`] |
| **size** | `number` | Maximum number of results returned in one page. | [Optional] [Defaults to `20`] |

### Return type

[**SentinelLinkSummaryPage**](SentinelLinkSummaryPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of normalized asset names and their Sentinel link counts. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listSentinelRuns

> SentinelRunPage listSentinelRuns(environment, page, size, checkId, status, sortBy, sortDirection)

List Sentinel runs

### Example

```ts
import {
  Configuration,
  SentinelApi,
} from '@spectestengine/sdk';
import type { ListSentinelRunsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SentinelApi(config);

  const body = {
    // string | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
    environment: environment_example,
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
    // string (optional)
    checkId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // RunStatusCode (optional)
    status: ...,
    // string (optional)
    sortBy: sortBy_example,
    // 'asc' | 'desc' (optional)
    sortDirection: sortDirection_example,
  } satisfies ListSentinelRunsRequest;

  try {
    const data = await api.listSentinelRuns(body);
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
| **environment** | `string` | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. | [Defaults to `undefined`] |
| **page** | `number` | Zero-based page index. | [Optional] [Defaults to `0`] |
| **size** | `number` | Maximum number of results returned in one page. | [Optional] [Defaults to `20`] |
| **checkId** | `string` |  | [Optional] [Defaults to `undefined`] |
| **status** | `RunStatusCode` |  | [Optional] [Defaults to `undefined`] [Enum: QUEUED, RUNNING, PASS, RECOVERED, FAIL, ERROR, SKIPPED] |
| **sortBy** | `string` |  | [Optional] [Defaults to `&#39;queuedAt&#39;`] |
| **sortDirection** | `asc`, `desc` |  | [Optional] [Defaults to `&#39;desc&#39;`] [Enum: asc, desc] |

### Return type

[**SentinelRunPage**](SentinelRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of Sentinel runs. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## sampleSentinelRuns

> Array&lt;SentinelRun&gt; sampleSentinelRuns(environment, days, size)

Sample Sentinel runs

### Example

```ts
import {
  Configuration,
  SentinelApi,
} from '@spectestengine/sdk';
import type { SampleSentinelRunsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SentinelApi(config);

  const body = {
    // string | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
    environment: environment_example,
    // number (optional)
    days: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
  } satisfies SampleSentinelRunsRequest;

  try {
    const data = await api.sampleSentinelRuns(body);
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
| **environment** | `string` | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. | [Defaults to `undefined`] |
| **days** | `number` |  | [Optional] [Defaults to `30`] |
| **size** | `number` | Maximum number of results returned in one page. | [Optional] [Defaults to `20`] |

### Return type

[**Array&lt;SentinelRun&gt;**](SentinelRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A bounded sample of Sentinel runs for the selected environment. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateSentinelCheck

> SentinelCheck updateSentinelCheck(checkId, sentinelCheckInput)

Replace a Sentinel check configuration

### Example

```ts
import {
  Configuration,
  SentinelApi,
} from '@spectestengine/sdk';
import type { UpdateSentinelCheckRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SentinelApi(config);

  const body = {
    // string | UUIDv7 identifier of the Sentinel check.
    checkId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // SentinelCheckInput
    sentinelCheckInput: ...,
  } satisfies UpdateSentinelCheckRequest;

  try {
    const data = await api.updateSentinelCheck(body);
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
| **checkId** | `string` | UUIDv7 identifier of the Sentinel check. | [Defaults to `undefined`] |
| **sentinelCheckInput** | [SentinelCheckInput](SentinelCheckInput.md) |  | |

### Return type

[**SentinelCheck**](SentinelCheck.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated check. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
