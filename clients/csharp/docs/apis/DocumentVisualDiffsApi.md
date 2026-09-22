# SpecTestEngine.Sdk.Api.DocumentVisualDiffsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetDocumentVisualDiff**](DocumentVisualDiffsApi.md#getdocumentvisualdiff) | **GET** /browser/visual/document-diffs/{visualDiffId} | Get a visual document diff |
| [**GetDocumentVisualDiffArtifact**](DocumentVisualDiffsApi.md#getdocumentvisualdiffartifact) | **GET** /browser/visual/document-diffs/{visualDiffId}/artifacts/{artifactId} | Download a rendered visual diff page |
| [**PrepareDocumentVisualDiffBaseline**](DocumentVisualDiffsApi.md#preparedocumentvisualdiffbaseline) | **POST** /browser/visual/document-diffs/{visualDiffId}/baseline | Preview or create an attachment baseline update draft |
| [**RegenerateDocumentVisualDiff**](DocumentVisualDiffsApi.md#regeneratedocumentvisualdiff) | **POST** /browser/visual/document-diffs/{visualDiffId}/regenerate | Regenerate a visual document diff |
| [**UploadDocumentVisualDiffExpected**](DocumentVisualDiffsApi.md#uploaddocumentvisualdiffexpected) | **POST** /browser/visual/document-diffs/{visualDiffId}/expected | Upload a reference document and create a diff generation |

<a id="getdocumentvisualdiff"></a>
# **GetDocumentVisualDiff**
> DocumentVisualDiff GetDocumentVisualDiff (Guid visualDiffId)

Get a visual document diff

Returns the protected viewer URL, TTL, immutable generations, and page-level artifact references.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **visualDiffId** | **Guid** | UUIDv7 identifier of an organization-scoped visual document diff session. |  |

### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Visual diff metadata scoped to the token company and active project. |  -  |
| **410** | Derived visual artifacts expired; source run metadata remains available. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getdocumentvisualdiffartifact"></a>
# **GetDocumentVisualDiffArtifact**
> System.IO.Stream GetDocumentVisualDiffArtifact (Guid visualDiffId, Guid artifactId)

Download a rendered visual diff page


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **visualDiffId** | **Guid** | UUIDv7 identifier of an organization-scoped visual document diff session. |  |
| **artifactId** | **Guid** |  |  |

### Return type

**System.IO.Stream**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Decrypted PNG page. The encrypted derivative remains subject to the diagnostic TTL. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="preparedocumentvisualdiffbaseline"></a>
# **PrepareDocumentVisualDiffBaseline**
> DocumentVisualDiffBaselinePreview PrepareDocumentVisualDiffBaseline (Guid visualDiffId, DocumentVisualDiffBaselineRequest documentVisualDiffBaselineRequest)

Preview or create an attachment baseline update draft

Never silently overwrites a specification. Send confirm=false first, then confirm=true only after review.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **visualDiffId** | **Guid** | UUIDv7 identifier of an organization-scoped visual document diff session. |  |
| **documentVisualDiffBaselineRequest** | [**DocumentVisualDiffBaselineRequest**](DocumentVisualDiffBaselineRequest.md) |  |  |

### Return type

[**DocumentVisualDiffBaselinePreview**](DocumentVisualDiffBaselinePreview.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Baseline hash/fingerprint preview or confirmed update draft. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="regeneratedocumentvisualdiff"></a>
# **RegenerateDocumentVisualDiff**
> DocumentVisualDiff RegenerateDocumentVisualDiff (Guid visualDiffId, DocumentVisualDiffRegenerateRequest documentVisualDiffRegenerateRequest = null)

Regenerate a visual document diff

Creates an immutable generation from the existing rendered pages with new comparison settings and normalized visual exclusion regions.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **visualDiffId** | **Guid** | UUIDv7 identifier of an organization-scoped visual document diff session. |  |
| **documentVisualDiffRegenerateRequest** | [**DocumentVisualDiffRegenerateRequest**](DocumentVisualDiffRegenerateRequest.md) |  | [optional]  |

### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Visual diff with a new current generation. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="uploaddocumentvisualdiffexpected"></a>
# **UploadDocumentVisualDiffExpected**
> DocumentVisualDiff UploadDocumentVisualDiffExpected (Guid visualDiffId, System.IO.Stream expected, double colorThreshold = null)

Upload a reference document and create a diff generation

The uploaded PDF or image is rendered in memory and discarded. Only encrypted page images and diff metadata remain until TTL expiry.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **visualDiffId** | **Guid** | UUIDv7 identifier of an organization-scoped visual document diff session. |  |
| **expected** | **System.IO.Stream****System.IO.Stream** |  |  |
| **colorThreshold** | **double** |  | [optional] [default to 24D] |

### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The visual diff with a new current generation. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

