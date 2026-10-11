# BrowserVisualReviewsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**excludeBrowserVisualAreaAndRecompare**](BrowserVisualReviewsApi.md#excludebrowservisualareaandrecompare) | **POST** /browser/visual/comparisons/{comparisonId}/exclude-and-recompare | Exclude area and recompare |
| [**getBrowserVisualArtifactContent**](BrowserVisualReviewsApi.md#getbrowservisualartifactcontent) | **GET** /browser/visual/artifacts/{artifactId}/content | Download Browser visual evidence |
| [**getBrowserVisualComparison**](BrowserVisualReviewsApi.md#getbrowservisualcomparison) | **GET** /browser/visual/comparisons/{comparisonId} | Get a Browser visual comparison |
| [**keepBrowserVisualAsRegression**](BrowserVisualReviewsApi.md#keepbrowservisualasregression) | **POST** /browser/visual/comparisons/{comparisonId}/keep-as-regression | Keep as regression |
| [**useCurrentBrowserVisualAsNewBaseline**](BrowserVisualReviewsApi.md#usecurrentbrowservisualasnewbaseline) | **POST** /browser/visual/comparisons/{comparisonId}/use-current-as-new-baseline | Use current as new baseline |



## excludeBrowserVisualAreaAndRecompare

> BrowserVisualComparison excludeBrowserVisualAreaAndRecompare(comparisonId, browserVisualExcludeAndRecompareRequest)

Exclude area and recompare

Saves normalized exclusion masks in a new assertion revision and creates a child comparison generation with the existing Browser comparator.

### Example

```ts
import {
  Configuration,
  BrowserVisualReviewsApi,
} from '@spectestengine/sdk';
import type { ExcludeBrowserVisualAreaAndRecompareRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new BrowserVisualReviewsApi(config);

  const body = {
    // string | Identifier of an immutable Browser visual comparison generation.
    comparisonId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // BrowserVisualExcludeAndRecompareRequest
    browserVisualExcludeAndRecompareRequest: ...,
  } satisfies ExcludeBrowserVisualAreaAndRecompareRequest;

  try {
    const data = await api.excludeBrowserVisualAreaAndRecompare(body);
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
| **comparisonId** | `string` | Identifier of an immutable Browser visual comparison generation. | [Defaults to `undefined`] |
| **browserVisualExcludeAndRecompareRequest** | [BrowserVisualExcludeAndRecompareRequest](BrowserVisualExcludeAndRecompareRequest.md) |  | |

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New comparison generation linked to the source and root comparisons. |  -  |
| **409** | The expected assertion revision is stale or the action id conflicts with another command. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getBrowserVisualArtifactContent

> Blob getBrowserVisualArtifactContent(artifactId)

Download Browser visual evidence

Returns a retained PNG baseline, current, or diff artifact after company and project authorization.

### Example

```ts
import {
  Configuration,
  BrowserVisualReviewsApi,
} from '@spectestengine/sdk';
import type { GetBrowserVisualArtifactContentRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new BrowserVisualReviewsApi(config);

  const body = {
    // string
    artifactId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetBrowserVisualArtifactContentRequest;

  try {
    const data = await api.getBrowserVisualArtifactContent(body);
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
| **200** | PNG visual evidence subject to the configured artifact retention policy. |  -  |
| **410** | The artifact expired; comparison metadata and lineage remain available. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getBrowserVisualComparison

> BrowserVisualComparison getBrowserVisualComparison(comparisonId)

Get a Browser visual comparison

Returns one immutable comparison generation, its evidence lineage, normalized exclusions, and currently available review actions.

### Example

```ts
import {
  Configuration,
  BrowserVisualReviewsApi,
} from '@spectestengine/sdk';
import type { GetBrowserVisualComparisonRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new BrowserVisualReviewsApi(config);

  const body = {
    // string | Identifier of an immutable Browser visual comparison generation.
    comparisonId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetBrowserVisualComparisonRequest;

  try {
    const data = await api.getBrowserVisualComparison(body);
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
| **comparisonId** | `string` | Identifier of an immutable Browser visual comparison generation. | [Defaults to `undefined`] |

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Browser visual comparison scoped to the token company and active project. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## keepBrowserVisualAsRegression

> BrowserVisualComparison keepBrowserVisualAsRegression(comparisonId, browserVisualKeepRegressionRequest)

Keep as regression

Confirms the mismatch as a regression without changing the active baseline or assertion exclusions.

### Example

```ts
import {
  Configuration,
  BrowserVisualReviewsApi,
} from '@spectestengine/sdk';
import type { KeepBrowserVisualAsRegressionRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new BrowserVisualReviewsApi(config);

  const body = {
    // string | Identifier of an immutable Browser visual comparison generation.
    comparisonId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // BrowserVisualKeepRegressionRequest
    browserVisualKeepRegressionRequest: ...,
  } satisfies KeepBrowserVisualAsRegressionRequest;

  try {
    const data = await api.keepBrowserVisualAsRegression(body);
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
| **comparisonId** | `string` | Identifier of an immutable Browser visual comparison generation. | [Defaults to `undefined`] |
| **browserVisualKeepRegressionRequest** | [BrowserVisualKeepRegressionRequest](BrowserVisualKeepRegressionRequest.md) |  | |

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comparison marked as a confirmed regression. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## useCurrentBrowserVisualAsNewBaseline

> BrowserVisualComparison useCurrentBrowserVisualAsNewBaseline(comparisonId, browserVisualPromoteBaselineRequest)

Use current as new baseline

Creates and activates a new immutable baseline revision. Historical comparison and baseline evidence remains addressable by Snapshot Timeline.

### Example

```ts
import {
  Configuration,
  BrowserVisualReviewsApi,
} from '@spectestengine/sdk';
import type { UseCurrentBrowserVisualAsNewBaselineRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new BrowserVisualReviewsApi(config);

  const body = {
    // string | Identifier of an immutable Browser visual comparison generation.
    comparisonId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // BrowserVisualPromoteBaselineRequest
    browserVisualPromoteBaselineRequest: ...,
  } satisfies UseCurrentBrowserVisualAsNewBaselineRequest;

  try {
    const data = await api.useCurrentBrowserVisualAsNewBaseline(body);
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
| **comparisonId** | `string` | Identifier of an immutable Browser visual comparison generation. | [Defaults to `undefined`] |
| **browserVisualPromoteBaselineRequest** | [BrowserVisualPromoteBaselineRequest](BrowserVisualPromoteBaselineRequest.md) |  | |

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reviewed comparison with the applied baseline revision. |  -  |
| **409** | The expected assertion revision is stale or the action id conflicts with another command. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
