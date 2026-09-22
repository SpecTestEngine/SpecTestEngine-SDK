# SpecTestEngine.Sdk.Api.CraftsmanApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CancelCraftsmanRun**](CraftsmanApi.md#cancelcraftsmanrun) | **POST** /sentinel/request-workspaces/runs/{runId}/cancel | Cancel a queued or active Craftsman run |
| [**CreateRequestNode**](CraftsmanApi.md#createrequestnode) | **POST** /sentinel/request-workspaces/{workspaceId}/nodes | Add a folder or saved request |
| [**CreateRequestWorkspace**](CraftsmanApi.md#createrequestworkspace) | **POST** /sentinel/request-workspaces | Create a request workspace |
| [**DeleteRequestNode**](CraftsmanApi.md#deleterequestnode) | **DELETE** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId} | Delete a folder or saved request |
| [**DeleteRequestWorkspace**](CraftsmanApi.md#deleterequestworkspace) | **DELETE** /sentinel/request-workspaces/{workspaceId} | Delete a request workspace |
| [**GetCraftsmanRun**](CraftsmanApi.md#getcraftsmanrun) | **GET** /sentinel/request-workspaces/runs/{runId} | Get Craftsman run lifecycle and evidence |
| [**GetCraftsmanRunTranscript**](CraftsmanApi.md#getcraftsmanruntranscript) | **GET** /sentinel/request-workspaces/runs/{runId}/transcript | Get a Craftsman Streaming semantic transcript |
| [**GetDocumentAsset**](CraftsmanApi.md#getdocumentasset) | **GET** /sentinel/document-assets/{assetId} | Resolve request attachment metadata |
| [**GetRequestWorkspace**](CraftsmanApi.md#getrequestworkspace) | **GET** /sentinel/request-workspaces/{workspaceId} | Get a request workspace |
| [**ListRequestWorkspaces**](CraftsmanApi.md#listrequestworkspaces) | **GET** /sentinel/request-workspaces/page | List request workspaces |
| [**QueueCraftsmanStreamingRun**](CraftsmanApi.md#queuecraftsmanstreamingrun) | **POST** /sentinel/request-workspaces/runs/streaming | Queue a standalone bounded Streaming session |
| [**QueueCraftsmanWorkflowRun**](CraftsmanApi.md#queuecraftsmanworkflowrun) | **POST** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId}/runs | Queue a saved request or mixed-protocol Workflow run |
| [**UpdateRequestNode**](CraftsmanApi.md#updaterequestnode) | **PUT** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId} | Update a folder or saved request |
| [**UpdateRequestWorkspace**](CraftsmanApi.md#updaterequestworkspace) | **PUT** /sentinel/request-workspaces/{workspaceId} | Replace request workspace metadata and variables |
| [**UploadDocumentAsset**](CraftsmanApi.md#uploaddocumentasset) | **POST** /sentinel/document-assets | Upload a reusable request attachment |

<a id="cancelcraftsmanrun"></a>
# **CancelCraftsmanRun**
> CraftsmanRun CancelCraftsmanRun (Guid runId)

Cancel a queued or active Craftsman run


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **runId** | **Guid** | UUIDv7 identifier of the stored run evidence. |  |

### Return type

[**CraftsmanRun**](CraftsmanRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated lifecycle after cooperative cancellation was requested. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="createrequestnode"></a>
# **CreateRequestNode**
> RequestNode CreateRequestNode (Guid workspaceId, RequestNodeInput requestNodeInput, Guid idempotencyKey = null)

Add a folder or saved request


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **workspaceId** | **Guid** | UUIDv7 identifier of the Craftsman request workspace. |  |
| **requestNodeInput** | [**RequestNodeInput**](RequestNodeInput.md) |  |  |
| **idempotencyKey** | **Guid** | A caller-generated UUID retained for safe write retries where supported. | [optional]  |

### Return type

[**RequestNode**](RequestNode.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created workspace node. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="createrequestworkspace"></a>
# **CreateRequestWorkspace**
> RequestWorkspace CreateRequestWorkspace (RequestWorkspaceInput requestWorkspaceInput, Guid idempotencyKey = null)

Create a request workspace


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **requestWorkspaceInput** | [**RequestWorkspaceInput**](RequestWorkspaceInput.md) |  |  |
| **idempotencyKey** | **Guid** | A caller-generated UUID retained for safe write retries where supported. | [optional]  |

### Return type

[**RequestWorkspace**](RequestWorkspace.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created workspace. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="deleterequestnode"></a>
# **DeleteRequestNode**
> void DeleteRequestNode (Guid workspaceId, Guid nodeId)

Delete a folder or saved request


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **workspaceId** | **Guid** | UUIDv7 identifier of the Craftsman request workspace. |  |
| **nodeId** | **Guid** |  |  |

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
| **204** | Workspace node deleted. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="deleterequestworkspace"></a>
# **DeleteRequestWorkspace**
> void DeleteRequestWorkspace (Guid workspaceId)

Delete a request workspace


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **workspaceId** | **Guid** | UUIDv7 identifier of the Craftsman request workspace. |  |

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
| **204** | Workspace deleted. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getcraftsmanrun"></a>
# **GetCraftsmanRun**
> CraftsmanRun GetCraftsmanRun (Guid runId)

Get Craftsman run lifecycle and evidence


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **runId** | **Guid** | UUIDv7 identifier of the stored run evidence. |  |

### Return type

[**CraftsmanRun**](CraftsmanRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current lifecycle and terminal result when available. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getcraftsmanruntranscript"></a>
# **GetCraftsmanRunTranscript**
> Object GetCraftsmanRunTranscript (Guid runId)

Get a Craftsman Streaming semantic transcript


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **runId** | **Guid** | UUIDv7 identifier of the stored run evidence. |  |

### Return type

**Object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bounded semantic event transcript captured by Sentinel. Use the completed run result for connection, assertion, and termination evidence required by Generate Spec. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getdocumentasset"></a>
# **GetDocumentAsset**
> DocumentAssetReference GetDocumentAsset (Guid assetId, string fieldName = null, string contentId = null)

Resolve request attachment metadata


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **assetId** | **Guid** |  |  |
| **fieldName** | **string** |  | [optional] [default to &quot;file&quot;] |
| **contentId** | **string** |  | [optional]  |

### Return type

[**DocumentAssetReference**](DocumentAssetReference.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attachment metadata suitable for reuse in a saved request or specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getrequestworkspace"></a>
# **GetRequestWorkspace**
> RequestWorkspace GetRequestWorkspace (Guid workspaceId)

Get a request workspace


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **workspaceId** | **Guid** | UUIDv7 identifier of the Craftsman request workspace. |  |

### Return type

[**RequestWorkspace**](RequestWorkspace.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The complete workspace tree. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listrequestworkspaces"></a>
# **ListRequestWorkspaces**
> RequestWorkspacePage ListRequestWorkspaces (int page = null, int size = null, string search = null)

List request workspaces


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **string** | Case-insensitive server-side search within the active project. | [optional]  |

### Return type

[**RequestWorkspacePage**](RequestWorkspacePage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of request workspaces. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="queuecraftsmanstreamingrun"></a>
# **QueueCraftsmanStreamingRun**
> CraftsmanRunAccepted QueueCraftsmanStreamingRun (CraftsmanStreamingRunInput craftsmanStreamingRunInput)

Queue a standalone bounded Streaming session

Standalone sessions require concrete values and do not inherit Workflow variables.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **craftsmanStreamingRunInput** | [**CraftsmanStreamingRunInput**](CraftsmanStreamingRunInput.md) |  |  |

### Return type

[**CraftsmanRunAccepted**](CraftsmanRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The bounded session was accepted. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="queuecraftsmanworkflowrun"></a>
# **QueueCraftsmanWorkflowRun**
> CraftsmanRunAccepted QueueCraftsmanWorkflowRun (Guid workspaceId, Guid nodeId, RequestChainRunInput requestChainRunInput = null)

Queue a saved request or mixed-protocol Workflow run

Supports REST, SOAP, GraphQL, WebSocket/WSS, SSE, gRPC Streaming, and MQTT nodes. Poll the returned run id.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **workspaceId** | **Guid** | UUIDv7 identifier of the Craftsman request workspace. |  |
| **nodeId** | **Guid** |  |  |
| **requestChainRunInput** | [**RequestChainRunInput**](RequestChainRunInput.md) |  | [optional]  |

### Return type

[**CraftsmanRunAccepted**](CraftsmanRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The bounded Craftsman run was accepted. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="updaterequestnode"></a>
# **UpdateRequestNode**
> RequestNode UpdateRequestNode (Guid workspaceId, Guid nodeId, RequestNodeInput requestNodeInput)

Update a folder or saved request

Replaces the selected node definition. STREAMING requests use streamingSpec and do not accept HTTP request fields.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **workspaceId** | **Guid** | UUIDv7 identifier of the Craftsman request workspace. |  |
| **nodeId** | **Guid** |  |  |
| **requestNodeInput** | [**RequestNodeInput**](RequestNodeInput.md) |  |  |

### Return type

[**RequestNode**](RequestNode.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated workspace node. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="updaterequestworkspace"></a>
# **UpdateRequestWorkspace**
> RequestWorkspace UpdateRequestWorkspace (Guid workspaceId, RequestWorkspaceInput requestWorkspaceInput)

Replace request workspace metadata and variables


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **workspaceId** | **Guid** | UUIDv7 identifier of the Craftsman request workspace. |  |
| **requestWorkspaceInput** | [**RequestWorkspaceInput**](RequestWorkspaceInput.md) |  |  |

### Return type

[**RequestWorkspace**](RequestWorkspace.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated workspace. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="uploaddocumentasset"></a>
# **UploadDocumentAsset**
> DocumentAssetReference UploadDocumentAsset (System.IO.Stream file, string fieldName = null, string contentId = null)

Upload a reusable request attachment


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **file** | **System.IO.Stream****System.IO.Stream** |  |  |
| **fieldName** | **string** |  | [optional] [default to &quot;file&quot;] |
| **contentId** | **string** |  | [optional]  |

### Return type

[**DocumentAssetReference**](DocumentAssetReference.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Immutable content-addressed attachment reference. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

