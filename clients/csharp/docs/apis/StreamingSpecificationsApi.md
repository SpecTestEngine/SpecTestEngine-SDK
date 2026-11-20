# SpecTestEngine.Sdk.Api.StreamingSpecificationsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CancelStreamingSpecificationRun**](StreamingSpecificationsApi.md#cancelstreamingspecificationrun) | **POST** /test/streaming-spec/run/history/by-run-id/{runId}/cancel | Cancel an active streaming run |
| [**CreateStreamingSpecification**](StreamingSpecificationsApi.md#createstreamingspecification) | **POST** /test/streaming-spec/create | Create a streaming specification |
| [**DeleteStreamingSpecification**](StreamingSpecificationsApi.md#deletestreamingspecification) | **DELETE** /test/streaming-spec/by-id | Delete a streaming specification |
| [**GetStreamingCapabilities**](StreamingSpecificationsApi.md#getstreamingcapabilities) | **GET** /engine/streaming/capabilities | Get streaming engine capabilities and enforced limits |
| [**GetStreamingPreparation**](StreamingSpecificationsApi.md#getstreamingpreparation) | **GET** /test/streaming-spec/preparations/by-ref/{ref} | Read eligible STREAMING Prepare request metadata by stable key |
| [**GetStreamingSpecification**](StreamingSpecificationsApi.md#getstreamingspecification) | **GET** /test/streaming-spec/by-id | Get a streaming specification |
| [**GetStreamingSpecificationRun**](StreamingSpecificationsApi.md#getstreamingspecificationrun) | **GET** /test/streaming-spec/run/history/by-run-id/{runId} | Get streaming run state and bounded semantic evidence |
| [**GetStreamingSpecificationRunTranscript**](StreamingSpecificationsApi.md#getstreamingspecificationruntranscript) | **GET** /test/streaming-spec/run/history/by-run-id/{runId}/transcript | Page a bounded streaming run transcript |
| [**ListStreamingPreparations**](StreamingSpecificationsApi.md#liststreamingpreparations) | **GET** /test/streaming-spec/preparations | List eligible Prepare requests and output declarations |
| [**ListStreamingSpecificationRuns**](StreamingSpecificationsApi.md#liststreamingspecificationruns) | **GET** /test/streaming-spec/run/page/by-spec-id/{specId} | List runs for a saved streaming specification |
| [**ListStreamingSpecifications**](StreamingSpecificationsApi.md#liststreamingspecifications) | **GET** /test/streaming-spec/page | List streaming specifications |
| [**PreviewStreamingSpecificationRecovery**](StreamingSpecificationsApi.md#previewstreamingspecificationrecovery) | **POST** /test/streaming-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a Streaming specification version |
| [**RestoreStreamingSpecificationFromRun**](StreamingSpecificationsApi.md#restorestreamingspecificationfromrun) | **PUT** /test/streaming-spec/recovery/{specId}/from-run/{runId}/restore | Restore a Streaming specification version |
| [**RunStreamingSpecification**](StreamingSpecificationsApi.md#runstreamingspecification) | **POST** /test/streaming-spec/run/by-id/{specId} | Queue a saved streaming specification run |
| [**RunStreamingSpecificationDraft**](StreamingSpecificationsApi.md#runstreamingspecificationdraft) | **POST** /test/streaming-spec/run/draft | Queue a bounded streaming specification draft run |
| [**TestStreamingSpecificationRecoveryVersion**](StreamingSpecificationsApi.md#teststreamingspecificationrecoveryversion) | **POST** /test/streaming-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous Streaming specification version |
| [**UpdateStreamingSpecification**](StreamingSpecificationsApi.md#updatestreamingspecification) | **PUT** /test/streaming-spec/by-id | Replace a streaming specification definition |
| [**ValidateStreamingSpecificationDraft**](StreamingSpecificationsApi.md#validatestreamingspecificationdraft) | **POST** /test/streaming-spec/validate-draft | Validate and detect the transport of a streaming specification draft |

<a id="cancelstreamingspecificationrun"></a>
# **CancelStreamingSpecificationRun**
> StreamingRun CancelStreamingSpecificationRun (Guid runId)

Cancel an active streaming run


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **runId** | **Guid** | UUIDv7 identifier of the stored run evidence. |  |

### Return type

[**StreamingRun**](StreamingRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Cancelled run, or the unchanged result when it was already terminal. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="createstreamingspecification"></a>
# **CreateStreamingSpecification**
> StreamingSpecification CreateStreamingSpecification (string specName, string body, string description = null, Guid idempotencyKey = null)

Create a streaming specification


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specName** | **string** | User-facing specification name within the active project. |  |
| **body** | **string** |  |  |
| **description** | **string** | Optional user-facing description stored with the asset. | [optional]  |
| **idempotencyKey** | **Guid** | A caller-generated UUID retained for safe write retries where supported. | [optional]  |

### Return type

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The stored streaming specification and detected transport. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="deletestreamingspecification"></a>
# **DeleteStreamingSpecification**
> StreamingSpecification DeleteStreamingSpecification (Guid specId)

Delete a streaming specification


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |

### Return type

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted streaming specification. Existing run evidence remains detached and readable. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getstreamingcapabilities"></a>
# **GetStreamingCapabilities**
> StreamingCapabilities GetStreamingCapabilities ()

Get streaming engine capabilities and enforced limits


### Parameters
This endpoint does not need any parameter.
### Return type

[**StreamingCapabilities**](StreamingCapabilities.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Supported transports, codecs, actions, expected* assertion fields, endpoint schemes, and hard limits. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getstreamingpreparation"></a>
# **GetStreamingPreparation**
> PreparationSummary GetStreamingPreparation (string varRef)

Read eligible STREAMING Prepare request metadata by stable key

Same-company current-read metadata only; no definition or runtime values. Missing, unmarked or inaccessible sources cannot be selected.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **varRef** | **string** |  |  |

### Return type

[**PreparationSummary**](PreparationSummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The eligible source and its declared output variables. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getstreamingspecification"></a>
# **GetStreamingSpecification**
> StreamingSpecification GetStreamingSpecification (Guid specId)

Get a streaming specification


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |

### Return type

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested streaming specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getstreamingspecificationrun"></a>
# **GetStreamingSpecificationRun**
> StreamingRun GetStreamingSpecificationRun (Guid runId)

Get streaming run state and bounded semantic evidence


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **runId** | **Guid** | UUIDv7 identifier of the stored run evidence. |  |

### Return type

[**StreamingRun**](StreamingRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current or terminal run metadata and evidence summary. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getstreamingspecificationruntranscript"></a>
# **GetStreamingSpecificationRunTranscript**
> StreamingTranscriptPage GetStreamingSpecificationRunTranscript (Guid runId, int page = null, int size = null)

Page a bounded streaming run transcript


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **runId** | **Guid** | UUIDv7 identifier of the stored run evidence. |  |
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** |  | [optional] [default to 100] |

### Return type

[**StreamingTranscriptPage**](StreamingTranscriptPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One transcript page. Payload exclusions and redactions are already applied. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="liststreamingpreparations"></a>
# **ListStreamingPreparations**
> PreparationPage ListStreamingPreparations (int page = null, int size = null, string search = null)

List eligible Prepare requests and output declarations

Same-company paginated metadata only. Values and full specification definitions are never included. The selected protocol and stableKey are used as preparation.protocol and preparation.ref in the consumer DSL. Any native protocol can prepare any other protocol.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** |  | [optional] [default to 20] |
| **search** | **string** | Case-insensitive server-side search within the active project. | [optional]  |

### Return type

[**PreparationPage**](PreparationPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of eligible STREAMING preparation sources. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="liststreamingspecificationruns"></a>
# **ListStreamingSpecificationRuns**
> StreamingRunPage ListStreamingSpecificationRuns (Guid specId, int page = null, int size = null)

List runs for a saved streaming specification


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |

### Return type

[**StreamingRunPage**](StreamingRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of current and terminal streaming runs. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="liststreamingspecifications"></a>
# **ListStreamingSpecifications**
> StreamingSpecificationPage ListStreamingSpecifications (int page = null, int size = null, string search = null, StreamingTransport transport = null)

List streaming specifications


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **string** | Case-insensitive server-side search within the active project. | [optional]  |
| **transport** | **StreamingTransport** | Filter by streaming transport. | [optional]  |

### Return type

[**StreamingSpecificationPage**](StreamingSpecificationPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of WebSocket/WSS, SSE, gRPC Streaming, and MQTT specifications. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="previewstreamingspecificationrecovery"></a>
# **PreviewStreamingSpecificationRecovery**
> SpecificationRecoveryPreview PreviewStreamingSpecificationRecovery (Guid specId, Guid runId)

Preview restoring a Streaming specification version

Compares the current specification with the exact DSL snapshot retained by a completed PASS or FAIL run. No expectations are regenerated.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |
| **runId** | **Guid** | UUIDv7 identifier of the stored run evidence. |  |

### Return type

[**SpecificationRecoveryPreview**](SpecificationRecoveryPreview.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Definition-only recovery preview. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="restorestreamingspecificationfromrun"></a>
# **RestoreStreamingSpecificationFromRun**
> StreamingSpecification RestoreStreamingSpecificationFromRun (Guid specId, Guid runId)

Restore a Streaming specification version

Replaces only the current DSL content with the exact snapshot retained by a completed PASS or FAIL run. The specification id, name, description, and stable identity are preserved.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |
| **runId** | **Guid** | UUIDv7 identifier of the stored run evidence. |  |

### Return type

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Restored specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="runstreamingspecification"></a>
# **RunStreamingSpecification**
> StreamingRunAccepted RunStreamingSpecification (Guid specId)

Queue a saved streaming specification run


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |

### Return type

[**StreamingRunAccepted**](StreamingRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Run accepted. Poll the returned status URL until the state is terminal. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="runstreamingspecificationdraft"></a>
# **RunStreamingSpecificationDraft**
> StreamingRunAccepted RunStreamingSpecificationDraft (string body, string specName = null)

Queue a bounded streaming specification draft run


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **body** | **string** |  |  |
| **specName** | **string** |  | [optional]  |

### Return type

[**StreamingRunAccepted**](StreamingRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Run accepted. Poll statusUrl, page transcriptUrl, or POST cancelUrl. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="teststreamingspecificationrecoveryversion"></a>
# **TestStreamingSpecificationRecoveryVersion**
> StreamingRun TestStreamingSpecificationRecoveryVersion (Guid specId, Guid runId)

Test a previous Streaming specification version

Executes the exact DSL snapshot retained by the selected completed PASS or FAIL run against the current API without changing the saved specification.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |
| **runId** | **Guid** | UUIDv7 identifier of the stored run evidence. |  |

### Return type

[**StreamingRun**](StreamingRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete terminal test-run evidence for the selected version. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="updatestreamingspecification"></a>
# **UpdateStreamingSpecification**
> StreamingSpecification UpdateStreamingSpecification (Guid specId, string body, string description = null)

Replace a streaming specification definition


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |
| **body** | **string** |  |  |
| **description** | **string** | Optional user-facing description stored with the asset. | [optional]  |

### Return type

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated streaming specification and newly detected transport. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="validatestreamingspecificationdraft"></a>
# **ValidateStreamingSpecificationDraft**
> StreamingDraftValidation ValidateStreamingSpecificationDraft (string body)

Validate and detect the transport of a streaming specification draft


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **body** | **string** |  |  |

### Return type

[**StreamingDraftValidation**](StreamingDraftValidation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid draft with its detected streaming transport. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
