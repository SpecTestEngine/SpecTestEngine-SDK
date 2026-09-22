# SpecTestEngine.Sdk.Api.FlowsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CaptureFlowStepAttachmentVisualDiff**](FlowsApi.md#captureflowstepattachmentvisualdiff) | **POST** /test/flow/run/by-id/{flowId}/visual-diff-captures | Create a visual diff from a failed flow-step attachment assertion |
| [**CreateFlow**](FlowsApi.md#createflow) | **POST** /test/flow/create | Create a test flow |
| [**DeleteFlow**](FlowsApi.md#deleteflow) | **DELETE** /test/flow/by-id | Delete a test flow |
| [**GetFlow**](FlowsApi.md#getflow) | **GET** /test/flow/by-id/{flowId} | Get a test flow |
| [**GetFlowRun**](FlowsApi.md#getflowrun) | **GET** /test/flow/run/saved/{runId} | Get a saved flow run |
| [**ListFlowRuns**](FlowsApi.md#listflowruns) | **GET** /test/flow/run/by-flow-id/{flowId}/page | List saved runs for a flow |
| [**ListFlows**](FlowsApi.md#listflows) | **GET** /test/flow/page | List test flows |
| [**RunFlow**](FlowsApi.md#runflow) | **POST** /test/flow/run/by-id/{flowId} | Run a saved flow |
| [**RunFlowBatch**](FlowsApi.md#runflowbatch) | **POST** /test/flow/run/batch | Run multiple saved flows |
| [**UpdateFlow**](FlowsApi.md#updateflow) | **PUT** /test/flow/by-id | Replace a test flow |

<a id="captureflowstepattachmentvisualdiff"></a>
# **CaptureFlowStepAttachmentVisualDiff**
> FlowRun CaptureFlowStepAttachmentVisualDiff (Guid flowId, FlowDocumentVisualDiffCaptureRunRequest flowDocumentVisualDiffCaptureRunRequest)

Create a visual diff from a failed flow-step attachment assertion

Explicitly reruns the saved flow and captures one failed PDF or image response from the selected API step. The flow and attachment assertion retain their real status.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **flowId** | **Guid** | UUIDv7 identifier of the saved test flow. |  |
| **flowDocumentVisualDiffCaptureRunRequest** | [**FlowDocumentVisualDiffCaptureRunRequest**](FlowDocumentVisualDiffCaptureRunRequest.md) |  |  |

### Return type

[**FlowRun**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete flow run evidence containing the temporary visual diff link in the selected step. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="createflow"></a>
# **CreateFlow**
> Flow CreateFlow (FlowInput flowInput, ContentFormat format = null, Guid idempotencyKey = null)

Create a test flow


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **flowInput** | [**FlowInput**](FlowInput.md) |  |  |
| **format** | **ContentFormat** | Serialization format used for the returned specification source. | [optional]  |
| **idempotencyKey** | **Guid** | A caller-generated UUID retained for safe write retries where supported. | [optional]  |

### Return type

[**Flow**](Flow.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored flow. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="deleteflow"></a>
# **DeleteFlow**
> void DeleteFlow (Guid flowId)

Delete a test flow


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **flowId** | **Guid** |  |  |

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
| **204** | Flow deleted. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getflow"></a>
# **GetFlow**
> Flow GetFlow (Guid flowId)

Get a test flow


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **flowId** | **Guid** | UUIDv7 identifier of the saved test flow. |  |

### Return type

[**Flow**](Flow.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested flow. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getflowrun"></a>
# **GetFlowRun**
> FlowRun GetFlowRun (Guid runId)

Get a saved flow run


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **runId** | **Guid** |  |  |

### Return type

[**FlowRun**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete persisted flow run evidence. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listflowruns"></a>
# **ListFlowRuns**
> FlowRunPage ListFlowRuns (Guid flowId, int page = null, int size = null)

List saved runs for a flow


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **flowId** | **Guid** | UUIDv7 identifier of the saved test flow. |  |
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |

### Return type

[**FlowRunPage**](FlowRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of lightweight persisted flow run summaries. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listflows"></a>
# **ListFlows**
> FlowPage ListFlows (int page = null, int size = null, string search = null)

List test flows


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **string** | Case-insensitive server-side search within the active project. | [optional]  |

### Return type

[**FlowPage**](FlowPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of flow summaries. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="runflow"></a>
# **RunFlow**
> FlowRun RunFlow (Guid flowId, bool watch = null)

Run a saved flow


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **flowId** | **Guid** | UUIDv7 identifier of the saved test flow. |  |
| **watch** | **bool** | Create a browser watch token when the flow contains visible browser steps. | [optional] [default to false] |

### Return type

[**FlowRun**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete flow run evidence. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="runflowbatch"></a>
# **RunFlowBatch**
> List&lt;FlowRun&gt; RunFlowBatch (RunFlowBatchRequest runFlowBatchRequest)

Run multiple saved flows


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **runFlowBatchRequest** | [**RunFlowBatchRequest**](RunFlowBatchRequest.md) |  |  |

### Return type

[**List&lt;FlowRun&gt;**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete evidence for every requested flow. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="updateflow"></a>
# **UpdateFlow**
> Flow UpdateFlow (Guid flowId, FlowInput flowInput, ContentFormat format = null)

Replace a test flow


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **flowId** | **Guid** |  |  |
| **flowInput** | [**FlowInput**](FlowInput.md) |  |  |
| **format** | **ContentFormat** | Serialization format used for the returned specification source. | [optional]  |

### Return type

[**Flow**](Flow.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated flow. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

