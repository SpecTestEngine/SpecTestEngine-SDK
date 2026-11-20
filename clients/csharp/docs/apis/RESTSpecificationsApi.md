# SpecTestEngine.Sdk.Api.RESTSpecificationsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CaptureRestSpecificationAttachmentVisualDiff**](RESTSpecificationsApi.md#capturerestspecificationattachmentvisualdiff) | **POST** /test/rest-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed REST attachment assertion |
| [**CreateRestSpecification**](RESTSpecificationsApi.md#createrestspecification) | **POST** /test/rest-spec/create | Create a REST specification |
| [**DeleteRestSpecification**](RESTSpecificationsApi.md#deleterestspecification) | **DELETE** /test/rest-spec/by-id | Delete a REST specification |
| [**GetRestPreparation**](RESTSpecificationsApi.md#getrestpreparation) | **GET** /test/rest-spec/preparations/by-ref/{ref} | Read eligible REST Prepare request metadata by stable key |
| [**GetRestSpecification**](RESTSpecificationsApi.md#getrestspecification) | **GET** /test/rest-spec/by-id | Get a REST specification |
| [**GetRestSpecificationRun**](RESTSpecificationsApi.md#getrestspecificationrun) | **GET** /test/rest-spec/run/history/by-run-id/{runId} | Get saved REST run evidence |
| [**ListRestPreparations**](RESTSpecificationsApi.md#listrestpreparations) | **GET** /test/rest-spec/preparations | List eligible Prepare requests and output declarations |
| [**ListRestSpecificationRuns**](RESTSpecificationsApi.md#listrestspecificationruns) | **GET** /test/rest-spec/run/page/by-spec-id/{specId} | List saved REST runs |
| [**ListRestSpecifications**](RESTSpecificationsApi.md#listrestspecifications) | **GET** /test/rest-spec/page | List REST specifications |
| [**PreviewRestSpecificationRecovery**](RESTSpecificationsApi.md#previewrestspecificationrecovery) | **POST** /test/rest-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a REST specification version |
| [**RestoreRestSpecificationFromRun**](RESTSpecificationsApi.md#restorerestspecificationfromrun) | **PUT** /test/rest-spec/recovery/{specId}/from-run/{runId}/restore | Restore a REST specification version |
| [**RunRestSpecification**](RESTSpecificationsApi.md#runrestspecification) | **POST** /test/rest-spec/run/by-id | Run a saved REST specification |
| [**TestRestSpecificationRecoveryVersion**](RESTSpecificationsApi.md#testrestspecificationrecoveryversion) | **POST** /test/rest-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous REST specification version |
| [**UpdateRestSpecification**](RESTSpecificationsApi.md#updaterestspecification) | **PUT** /test/rest-spec/by-id | Replace a REST specification definition |

<a id="capturerestspecificationattachmentvisualdiff"></a>
# **CaptureRestSpecificationAttachmentVisualDiff**
> SpecificationRun CaptureRestSpecificationAttachmentVisualDiff (Guid specId, DocumentVisualDiffCaptureRunRequest documentVisualDiffCaptureRunRequest)

Create a visual diff from a failed REST attachment assertion

Explicitly reruns the saved REST specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status; no visual-diff fallback changes the test result.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |
| **documentVisualDiffCaptureRunRequest** | [**DocumentVisualDiffCaptureRunRequest**](DocumentVisualDiffCaptureRunRequest.md) |  |  |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete failed run evidence containing the temporary visual diff link. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="createrestspecification"></a>
# **CreateRestSpecification**
> Specification CreateRestSpecification (string specName, string body, string description = null, Guid idempotencyKey = null)

Create a REST specification


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specName** | **string** | User-facing specification name within the active project. |  |
| **body** | **string** |  |  |
| **description** | **string** | Optional user-facing description stored with the asset. | [optional]  |
| **idempotencyKey** | **Guid** | A caller-generated UUID retained for safe write retries where supported. | [optional]  |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored REST specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="deleterestspecification"></a>
# **DeleteRestSpecification**
> Specification DeleteRestSpecification (Guid specId)

Delete a REST specification


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted REST specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getrestpreparation"></a>
# **GetRestPreparation**
> PreparationSummary GetRestPreparation (string varRef)

Read eligible REST Prepare request metadata by stable key

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

<a id="getrestspecification"></a>
# **GetRestSpecification**
> Specification GetRestSpecification (Guid specId)

Get a REST specification


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested REST specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getrestspecificationrun"></a>
# **GetRestSpecificationRun**
> SpecificationRun GetRestSpecificationRun (Guid runId)

Get saved REST run evidence


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **runId** | **Guid** | UUIDv7 identifier of the stored run evidence. |  |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete saved run evidence. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listrestpreparations"></a>
# **ListRestPreparations**
> PreparationPage ListRestPreparations (int page = null, int size = null, string search = null)

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
| **200** | A page of eligible REST preparation sources. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listrestspecificationruns"></a>
# **ListRestSpecificationRuns**
> SpecificationRunPage ListRestSpecificationRuns (Guid specId, int page = null, int size = null)

List saved REST runs


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |

### Return type

[**SpecificationRunPage**](SpecificationRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of run summaries. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listrestspecifications"></a>
# **ListRestSpecifications**
> SpecificationPage ListRestSpecifications (int page = null, int size = null, string search = null)

List REST specifications


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **string** | Case-insensitive server-side search within the active project. | [optional]  |

### Return type

[**SpecificationPage**](SpecificationPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of REST specifications. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="previewrestspecificationrecovery"></a>
# **PreviewRestSpecificationRecovery**
> SpecificationRecoveryPreview PreviewRestSpecificationRecovery (Guid specId, Guid runId)

Preview restoring a REST specification version

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

<a id="restorerestspecificationfromrun"></a>
# **RestoreRestSpecificationFromRun**
> Specification RestoreRestSpecificationFromRun (Guid specId, Guid runId)

Restore a REST specification version

Replaces only the current DSL content with the exact snapshot retained by a completed PASS or FAIL run. The specification id, name, description, and stable identity are preserved.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |
| **runId** | **Guid** | UUIDv7 identifier of the stored run evidence. |  |

### Return type

[**Specification**](Specification.md)

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

<a id="runrestspecification"></a>
# **RunRestSpecification**
> SpecificationRun RunRestSpecification (Guid specId)

Run a saved REST specification

Starts and completes one synchronous specification execution.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete run evidence. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="testrestspecificationrecoveryversion"></a>
# **TestRestSpecificationRecoveryVersion**
> SpecificationRun TestRestSpecificationRecoveryVersion (Guid specId, Guid runId)

Test a previous REST specification version

Executes the exact DSL snapshot retained by the selected completed PASS or FAIL run against the current API without changing the saved specification.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |
| **runId** | **Guid** | UUIDv7 identifier of the stored run evidence. |  |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete test-run evidence for the selected version. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="updaterestspecification"></a>
# **UpdateRestSpecification**
> Specification UpdateRestSpecification (Guid specId, string body, string description = null)

Replace a REST specification definition


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specId** | **Guid** | UUIDv7 identifier of the saved specification. |  |
| **body** | **string** |  |  |
| **description** | **string** | Optional user-facing description stored with the asset. | [optional]  |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated REST specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
