# SpecTestEngine.Sdk.Api.GraphQLSpecificationsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CaptureGraphqlSpecificationAttachmentVisualDiff**](GraphQLSpecificationsApi.md#capturegraphqlspecificationattachmentvisualdiff) | **POST** /test/graphql-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed GraphQL attachment assertion |
| [**CreateGraphqlSpecification**](GraphQLSpecificationsApi.md#creategraphqlspecification) | **POST** /test/graphql-spec/create | Create a GraphQL specification |
| [**DeleteGraphqlSpecification**](GraphQLSpecificationsApi.md#deletegraphqlspecification) | **DELETE** /test/graphql-spec/by-id | Delete a GraphQL specification |
| [**GetGraphqlSpecification**](GraphQLSpecificationsApi.md#getgraphqlspecification) | **GET** /test/graphql-spec/by-id | Get a GraphQL specification |
| [**GetGraphqlSpecificationRun**](GraphQLSpecificationsApi.md#getgraphqlspecificationrun) | **GET** /test/graphql-spec/run/history/by-run-id/{runId} | Get saved GraphQL run evidence |
| [**ListGraphqlSpecificationRuns**](GraphQLSpecificationsApi.md#listgraphqlspecificationruns) | **GET** /test/graphql-spec/run/page/by-spec-id/{specId} | List saved GraphQL runs |
| [**ListGraphqlSpecifications**](GraphQLSpecificationsApi.md#listgraphqlspecifications) | **GET** /test/graphql-spec/page | List GraphQL specifications |
| [**PreviewGraphqlSpecificationRecovery**](GraphQLSpecificationsApi.md#previewgraphqlspecificationrecovery) | **POST** /test/graphql-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a GraphQL specification version |
| [**RestoreGraphqlSpecificationFromRun**](GraphQLSpecificationsApi.md#restoregraphqlspecificationfromrun) | **PUT** /test/graphql-spec/recovery/{specId}/from-run/{runId}/restore | Restore a GraphQL specification version |
| [**RunGraphqlSpecification**](GraphQLSpecificationsApi.md#rungraphqlspecification) | **POST** /test/graphql-spec/run/by-id | Run a saved GraphQL specification |
| [**TestGraphqlSpecificationRecoveryVersion**](GraphQLSpecificationsApi.md#testgraphqlspecificationrecoveryversion) | **POST** /test/graphql-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous GraphQL specification version |
| [**UpdateGraphqlSpecification**](GraphQLSpecificationsApi.md#updategraphqlspecification) | **PUT** /test/graphql-spec/by-id | Replace a GraphQL specification definition |

<a id="capturegraphqlspecificationattachmentvisualdiff"></a>
# **CaptureGraphqlSpecificationAttachmentVisualDiff**
> SpecificationRun CaptureGraphqlSpecificationAttachmentVisualDiff (Guid specId, DocumentVisualDiffCaptureRunRequest documentVisualDiffCaptureRunRequest)

Create a visual diff from a failed GraphQL attachment assertion

Explicitly reruns the saved GraphQL specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status.


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

<a id="creategraphqlspecification"></a>
# **CreateGraphqlSpecification**
> Specification CreateGraphqlSpecification (string specName, string body, string description = null, Guid idempotencyKey = null)

Create a GraphQL specification


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
| **200** | The stored GraphQL specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="deletegraphqlspecification"></a>
# **DeleteGraphqlSpecification**
> Specification DeleteGraphqlSpecification (Guid specId)

Delete a GraphQL specification


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
| **200** | The deleted GraphQL specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getgraphqlspecification"></a>
# **GetGraphqlSpecification**
> Specification GetGraphqlSpecification (Guid specId)

Get a GraphQL specification


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
| **200** | The requested GraphQL specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getgraphqlspecificationrun"></a>
# **GetGraphqlSpecificationRun**
> SpecificationRun GetGraphqlSpecificationRun (Guid runId)

Get saved GraphQL run evidence


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

<a id="listgraphqlspecificationruns"></a>
# **ListGraphqlSpecificationRuns**
> SpecificationRunPage ListGraphqlSpecificationRuns (Guid specId, int page = null, int size = null)

List saved GraphQL runs


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

<a id="listgraphqlspecifications"></a>
# **ListGraphqlSpecifications**
> SpecificationPage ListGraphqlSpecifications (int page = null, int size = null, string search = null)

List GraphQL specifications


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
| **200** | A page of GraphQL specifications. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="previewgraphqlspecificationrecovery"></a>
# **PreviewGraphqlSpecificationRecovery**
> SpecificationRecoveryPreview PreviewGraphqlSpecificationRecovery (Guid specId, Guid runId)

Preview restoring a GraphQL specification version

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

<a id="restoregraphqlspecificationfromrun"></a>
# **RestoreGraphqlSpecificationFromRun**
> Specification RestoreGraphqlSpecificationFromRun (Guid specId, Guid runId)

Restore a GraphQL specification version

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

<a id="rungraphqlspecification"></a>
# **RunGraphqlSpecification**
> SpecificationRun RunGraphqlSpecification (Guid specId)

Run a saved GraphQL specification


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

<a id="testgraphqlspecificationrecoveryversion"></a>
# **TestGraphqlSpecificationRecoveryVersion**
> SpecificationRun TestGraphqlSpecificationRecoveryVersion (Guid specId, Guid runId)

Test a previous GraphQL specification version

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

<a id="updategraphqlspecification"></a>
# **UpdateGraphqlSpecification**
> Specification UpdateGraphqlSpecification (Guid specId, string body, string description = null)

Replace a GraphQL specification definition


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
| **200** | The updated GraphQL specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
