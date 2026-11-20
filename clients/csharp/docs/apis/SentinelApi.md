# SpecTestEngine.Sdk.Api.SentinelApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CreateSentinelCheck**](SentinelApi.md#createsentinelcheck) | **POST** /sentinel/checks | Create a Sentinel check |
| [**DeleteSentinelCheck**](SentinelApi.md#deletesentinelcheck) | **DELETE** /sentinel/checks/{checkId} | Delete a Sentinel check |
| [**EnqueueSentinelRun**](SentinelApi.md#enqueuesentinelrun) | **POST** /sentinel/checks/{checkId}/run | Queue a Sentinel run |
| [**GetSentinelCheck**](SentinelApi.md#getsentinelcheck) | **GET** /sentinel/checks/{checkId} | Get a Sentinel check |
| [**GetSentinelDashboardSummary**](SentinelApi.md#getsentineldashboardsummary) | **GET** /sentinel/dashboard/summary | Get Sentinel dashboard summary |
| [**GetSentinelRun**](SentinelApi.md#getsentinelrun) | **GET** /sentinel/runs/{runId} | Get Sentinel run evidence |
| [**ListLatestSentinelRuns**](SentinelApi.md#listlatestsentinelruns) | **GET** /sentinel/runs | List latest Sentinel runs |
| [**ListSentinelChecks**](SentinelApi.md#listsentinelchecks) | **GET** /sentinel/checks/page | List Sentinel checks |
| [**ListSentinelDashboardIncidents**](SentinelApi.md#listsentineldashboardincidents) | **GET** /sentinel/dashboard/incidents | List recent Sentinel incidents |
| [**ListSentinelLinkedAssets**](SentinelApi.md#listsentinellinkedassets) | **GET** /sentinel/checks/spec-links/page | List compact Sentinel links for one Automation asset type |
| [**ListSentinelRuns**](SentinelApi.md#listsentinelruns) | **GET** /sentinel/runs/page | List Sentinel runs |
| [**SampleSentinelRuns**](SentinelApi.md#samplesentinelruns) | **GET** /sentinel/runs/sample | Sample Sentinel runs |
| [**UpdateSentinelCheck**](SentinelApi.md#updatesentinelcheck) | **PUT** /sentinel/checks/{checkId} | Replace a Sentinel check configuration |

<a id="createsentinelcheck"></a>
# **CreateSentinelCheck**
> SentinelCheck CreateSentinelCheck (SentinelCheckInput sentinelCheckInput, Guid idempotencyKey = null)

Create a Sentinel check


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **sentinelCheckInput** | [**SentinelCheckInput**](SentinelCheckInput.md) |  |  |
| **idempotencyKey** | **Guid** | A caller-generated UUID retained for safe write retries where supported. | [optional]  |

### Return type

[**SentinelCheck**](SentinelCheck.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created check. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="deletesentinelcheck"></a>
# **DeleteSentinelCheck**
> void DeleteSentinelCheck (Guid checkId)

Delete a Sentinel check


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **checkId** | **Guid** | UUIDv7 identifier of the Sentinel check. |  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Check deleted. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="enqueuesentinelrun"></a>
# **EnqueueSentinelRun**
> RunEnqueueResponse EnqueueSentinelRun (Guid checkId, Guid idempotencyKey = null, string region = null)

Queue a Sentinel run


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **checkId** | **Guid** | UUIDv7 identifier of the Sentinel check. |  |
| **idempotencyKey** | **Guid** | A caller-generated UUID retained for safe write retries where supported. | [optional]  |
| **region** | **string** |  | [optional] [default to &quot;local&quot;] |

### Return type

[**RunEnqueueResponse**](RunEnqueueResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Queue acknowledgement and execution id. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getsentinelcheck"></a>
# **GetSentinelCheck**
> SentinelCheck GetSentinelCheck (Guid checkId)

Get a Sentinel check


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **checkId** | **Guid** | UUIDv7 identifier of the Sentinel check. |  |

### Return type

[**SentinelCheck**](SentinelCheck.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested check. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getsentineldashboardsummary"></a>
# **GetSentinelDashboardSummary**
> SentinelDashboardSummary GetSentinelDashboardSummary (string environment)

Get Sentinel dashboard summary


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **environment** | **string** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |  |

### Return type

[**SentinelDashboardSummary**](SentinelDashboardSummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Environment-scoped Sentinel dashboard counters and latency summary. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getsentinelrun"></a>
# **GetSentinelRun**
> SentinelRun GetSentinelRun (Guid runId)

Get Sentinel run evidence


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **runId** | **Guid** | UUIDv7 identifier of the stored run evidence. |  |

### Return type

[**SentinelRun**](SentinelRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Run, retry attempts, response preview, and baseline evidence. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listlatestsentinelruns"></a>
# **ListLatestSentinelRuns**
> List&lt;SentinelRun&gt; ListLatestSentinelRuns (string environment, int size = null)

List latest Sentinel runs


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **environment** | **string** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |  |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |

### Return type

[**List&lt;SentinelRun&gt;**](SentinelRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The latest Sentinel runs for the selected environment. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listsentinelchecks"></a>
# **ListSentinelChecks**
> SentinelCheckPage ListSentinelChecks (string environment, int page = null, int size = null, string search = null)

List Sentinel checks


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **environment** | **string** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |  |
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **string** | Case-insensitive server-side search within the active project. | [optional]  |

### Return type

[**SentinelCheckPage**](SentinelCheckPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of Sentinel checks. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listsentineldashboardincidents"></a>
# **ListSentinelDashboardIncidents**
> List&lt;SentinelIncident&gt; ListSentinelDashboardIncidents (string environment)

List recent Sentinel incidents


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **environment** | **string** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |  |

### Return type

[**List&lt;SentinelIncident&gt;**](SentinelIncident.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recent incidents for the selected Sentinel environment. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listsentinellinkedassets"></a>
# **ListSentinelLinkedAssets**
> SentinelLinkSummaryPage ListSentinelLinkedAssets (string environment, SentinelLinkedAssetCheckType checkType, int page = null, int size = null)

List compact Sentinel links for one Automation asset type


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **environment** | **string** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |  |
| **checkType** | **SentinelLinkedAssetCheckType** | Exact Automation asset type whose Sentinel links should be returned. |  |
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |

### Return type

[**SentinelLinkSummaryPage**](SentinelLinkSummaryPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of normalized asset names and their Sentinel link counts. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listsentinelruns"></a>
# **ListSentinelRuns**
> SentinelRunPage ListSentinelRuns (string environment, int page = null, int size = null, Guid checkId = null, RunStatusCode status = null, string sortBy = null, string sortDirection = null)

List Sentinel runs


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **environment** | **string** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |  |
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **checkId** | **Guid** |  | [optional]  |
| **status** | **RunStatusCode** |  | [optional]  |
| **sortBy** | **string** |  | [optional] [default to &quot;queuedAt&quot;] |
| **sortDirection** | **string** |  | [optional] [default to desc] |

### Return type

[**SentinelRunPage**](SentinelRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of Sentinel runs. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="samplesentinelruns"></a>
# **SampleSentinelRuns**
> List&lt;SentinelRun&gt; SampleSentinelRuns (string environment, int days = null, int size = null)

Sample Sentinel runs


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **environment** | **string** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |  |
| **days** | **int** |  | [optional] [default to 30] |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |

### Return type

[**List&lt;SentinelRun&gt;**](SentinelRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A bounded sample of Sentinel runs for the selected environment. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="updatesentinelcheck"></a>
# **UpdateSentinelCheck**
> SentinelCheck UpdateSentinelCheck (Guid checkId, SentinelCheckInput sentinelCheckInput)

Replace a Sentinel check configuration


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **checkId** | **Guid** | UUIDv7 identifier of the Sentinel check. |  |
| **sentinelCheckInput** | [**SentinelCheckInput**](SentinelCheckInput.md) |  |  |

### Return type

[**SentinelCheck**](SentinelCheck.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated check. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
