# SpecTestEngine.Sdk.Api.SOAPSpecificationsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CaptureSoapSpecificationAttachmentVisualDiff**](SOAPSpecificationsApi.md#capturesoapspecificationattachmentvisualdiff) | **POST** /test/soap-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed SOAP attachment assertion |
| [**CreateSoapSpecification**](SOAPSpecificationsApi.md#createsoapspecification) | **POST** /test/soap-spec/create | Create a SOAP specification |
| [**DeleteSoapSpecification**](SOAPSpecificationsApi.md#deletesoapspecification) | **DELETE** /test/soap-spec/by-id | Delete a SOAP specification |
| [**GetSoapSpecification**](SOAPSpecificationsApi.md#getsoapspecification) | **GET** /test/soap-spec/by-id | Get a SOAP specification |
| [**GetSoapSpecificationRun**](SOAPSpecificationsApi.md#getsoapspecificationrun) | **GET** /test/soap-spec/run/history/by-run-id/{runId} | Get saved SOAP run evidence |
| [**ListSoapSpecificationRuns**](SOAPSpecificationsApi.md#listsoapspecificationruns) | **GET** /test/soap-spec/run/page/by-spec-id/{specId} | List saved SOAP runs |
| [**ListSoapSpecifications**](SOAPSpecificationsApi.md#listsoapspecifications) | **GET** /test/soap-spec/page | List SOAP specifications |
| [**PreviewSoapSpecificationRecovery**](SOAPSpecificationsApi.md#previewsoapspecificationrecovery) | **POST** /test/soap-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a SOAP specification version |
| [**RestoreSoapSpecificationFromRun**](SOAPSpecificationsApi.md#restoresoapspecificationfromrun) | **PUT** /test/soap-spec/recovery/{specId}/from-run/{runId}/restore | Restore a SOAP specification version |
| [**RunSoapSpecification**](SOAPSpecificationsApi.md#runsoapspecification) | **POST** /test/soap-spec/run/by-id | Run a saved SOAP specification |
| [**TestSoapSpecificationRecoveryVersion**](SOAPSpecificationsApi.md#testsoapspecificationrecoveryversion) | **POST** /test/soap-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous SOAP specification version |
| [**UpdateSoapSpecification**](SOAPSpecificationsApi.md#updatesoapspecification) | **PUT** /test/soap-spec/by-id | Replace a SOAP specification definition |

<a id="capturesoapspecificationattachmentvisualdiff"></a>
# **CaptureSoapSpecificationAttachmentVisualDiff**
> SpecificationRun CaptureSoapSpecificationAttachmentVisualDiff (Guid specId, DocumentVisualDiffCaptureRunRequest documentVisualDiffCaptureRunRequest)

Create a visual diff from a failed SOAP attachment assertion

Explicitly reruns the saved SOAP specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status.


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

<a id="createsoapspecification"></a>
# **CreateSoapSpecification**
> Specification CreateSoapSpecification (string specName, string body, string description = null, Guid idempotencyKey = null)

Create a SOAP specification


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
| **200** | The stored SOAP specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="deletesoapspecification"></a>
# **DeleteSoapSpecification**
> Specification DeleteSoapSpecification (Guid specId)

Delete a SOAP specification


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
| **200** | The deleted SOAP specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getsoapspecification"></a>
# **GetSoapSpecification**
> Specification GetSoapSpecification (Guid specId)

Get a SOAP specification


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
| **200** | The requested SOAP specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getsoapspecificationrun"></a>
# **GetSoapSpecificationRun**
> SpecificationRun GetSoapSpecificationRun (Guid runId)

Get saved SOAP run evidence


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

<a id="listsoapspecificationruns"></a>
# **ListSoapSpecificationRuns**
> SpecificationRunPage ListSoapSpecificationRuns (Guid specId, int page = null, int size = null)

List saved SOAP runs


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

<a id="listsoapspecifications"></a>
# **ListSoapSpecifications**
> SpecificationPage ListSoapSpecifications (int page = null, int size = null, string search = null)

List SOAP specifications


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
| **200** | A page of SOAP specifications. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="previewsoapspecificationrecovery"></a>
# **PreviewSoapSpecificationRecovery**
> SpecificationRecoveryPreview PreviewSoapSpecificationRecovery (Guid specId, Guid runId)

Preview restoring a SOAP specification version

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

<a id="restoresoapspecificationfromrun"></a>
# **RestoreSoapSpecificationFromRun**
> Specification RestoreSoapSpecificationFromRun (Guid specId, Guid runId)

Restore a SOAP specification version

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

<a id="runsoapspecification"></a>
# **RunSoapSpecification**
> SpecificationRun RunSoapSpecification (Guid specId)

Run a saved SOAP specification


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

<a id="testsoapspecificationrecoveryversion"></a>
# **TestSoapSpecificationRecoveryVersion**
> SpecificationRun TestSoapSpecificationRecoveryVersion (Guid specId, Guid runId)

Test a previous SOAP specification version

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

<a id="updatesoapspecification"></a>
# **UpdateSoapSpecification**
> Specification UpdateSoapSpecification (Guid specId, string body, string description = null)

Replace a SOAP specification definition


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
| **200** | The updated SOAP specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

