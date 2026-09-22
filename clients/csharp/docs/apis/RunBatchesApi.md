# SpecTestEngine.Sdk.Api.RunBatchesApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CreateRunBatch**](RunBatchesApi.md#createrunbatch) | **POST** /test/run-batch/create | Create a run batch |
| [**GetRunBatch**](RunBatchesApi.md#getrunbatch) | **GET** /test/run-batch/by-id/{batchId} | Get a run batch |
| [**ListRunBatches**](RunBatchesApi.md#listrunbatches) | **GET** /test/run-batch/page | List run batches |

<a id="createrunbatch"></a>
# **CreateRunBatch**
> RunBatch CreateRunBatch (RunBatchInput runBatchInput, Guid idempotencyKey = null)

Create a run batch

Collect completed specification, UI macro, and flow runs into one immutable evidence set that can later become a snapshot baseline.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **runBatchInput** | [**RunBatchInput**](RunBatchInput.md) |  |  |
| **idempotencyKey** | **Guid** | A caller-generated UUID retained for safe write retries where supported. | [optional]  |

### Return type

[**RunBatch**](RunBatch.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created run batch and its captured evidence items. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getrunbatch"></a>
# **GetRunBatch**
> RunBatch GetRunBatch (Guid batchId)

Get a run batch


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **batchId** | **Guid** | UUIDv7 identifier of the saved run batch. |  |

### Return type

[**RunBatch**](RunBatch.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested run batch with its captured evidence items. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listrunbatches"></a>
# **ListRunBatches**
> RunBatchPage ListRunBatches (int page = null, int size = null, string search = null)

List run batches


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **string** | Case-insensitive server-side search within the active project. | [optional]  |

### Return type

[**RunBatchPage**](RunBatchPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of run batches in the active project. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

