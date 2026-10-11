# SpecTestEngine.Sdk.Api.FragmentsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CompileDraftFragments**](FragmentsApi.md#compiledraftfragments) | **POST** /test/spec/fragment/compile-draft | Compile inline fragment DSL into a specification draft |
| [**CompileFragments**](FragmentsApi.md#compilefragments) | **POST** /test/spec/fragment/compile | Compile fragments into a specification draft |
| [**CreateFragment**](FragmentsApi.md#createfragment) | **POST** /test/spec/fragment/create | Create a specification fragment |
| [**DeleteFragment**](FragmentsApi.md#deletefragment) | **DELETE** /test/spec/fragment/by-id | Delete a fragment |
| [**GetFragment**](FragmentsApi.md#getfragment) | **GET** /test/spec/fragment/by-id/{fragmentId} | Get a fragment |
| [**GetFragmentCatalog**](FragmentsApi.md#getfragmentcatalog) | **GET** /test/spec/fragment/catalog | Get the fragment DSL catalog for an API type |
| [**GetFragmentSummary**](FragmentsApi.md#getfragmentsummary) | **GET** /test/spec/fragment/summary | Count fragments by API type |
| [**ListFragments**](FragmentsApi.md#listfragments) | **GET** /test/spec/fragment/page | List specification fragments |
| [**SaveFragmentsAsSpecification**](FragmentsApi.md#savefragmentsasspecification) | **POST** /test/spec/fragment/save-as-spec | Compile saved fragments and persist the result in the matching protocol engine |
| [**UpdateFragment**](FragmentsApi.md#updatefragment) | **PUT** /test/spec/fragment/by-id | Replace a fragment |

<a id="compiledraftfragments"></a>
# **CompileDraftFragments**
> CompiledSpecification CompileDraftFragments (FragmentDraftAssembly fragmentDraftAssembly, ContentFormat format = null)

Compile inline fragment DSL into a specification draft


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **fragmentDraftAssembly** | [**FragmentDraftAssembly**](FragmentDraftAssembly.md) |  |  |
| **format** | **ContentFormat** | Serialization format used for the returned specification source. | [optional]  |

### Return type

[**CompiledSpecification**](CompiledSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The compiled and protocol-validated specification draft. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="compilefragments"></a>
# **CompileFragments**
> CompiledSpecification CompileFragments (FragmentAssembly fragmentAssembly, ContentFormat format = null)

Compile fragments into a specification draft


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **fragmentAssembly** | [**FragmentAssembly**](FragmentAssembly.md) |  |  |
| **format** | **ContentFormat** | Serialization format used for the returned specification source. | [optional]  |

### Return type

[**CompiledSpecification**](CompiledSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The compiled specification draft. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="createfragment"></a>
# **CreateFragment**
> Fragment CreateFragment (FragmentInput fragmentInput, Guid idempotencyKey = null)

Create a specification fragment


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **fragmentInput** | [**FragmentInput**](FragmentInput.md) |  |  |
| **idempotencyKey** | **Guid** | A caller-generated UUID retained for safe write retries where supported. | [optional]  |

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored fragment. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="deletefragment"></a>
# **DeleteFragment**
> Fragment DeleteFragment (Guid fragmentId)

Delete a fragment


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **fragmentId** | **Guid** |  |  |

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted fragment. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getfragment"></a>
# **GetFragment**
> Fragment GetFragment (Guid fragmentId)

Get a fragment


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **fragmentId** | **Guid** |  |  |

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested fragment. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getfragmentcatalog"></a>
# **GetFragmentCatalog**
> FragmentCatalog GetFragmentCatalog (SpecType specType)

Get the fragment DSL catalog for an API type


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specType** | **SpecType** |  |  |

### Return type

[**FragmentCatalog**](FragmentCatalog.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Compatible fragment types, fields, editor modes, and starter templates. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getfragmentsummary"></a>
# **GetFragmentSummary**
> FragmentSummary GetFragmentSummary ()

Count fragments by API type


### Parameters
This endpoint does not need any parameter.
### Return type

[**FragmentSummary**](FragmentSummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | REST, SOAP, and GraphQL fragment counts. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listfragments"></a>
# **ListFragments**
> FragmentPage ListFragments (int page = null, int size = null, string search = null, SpecType specType = null, FragmentType type = null)

List specification fragments


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **string** | Case-insensitive server-side search within the active project. | [optional]  |
| **specType** | **SpecType** | Filter the library to one API protocol. | [optional]  |
| **type** | **FragmentType** |  | [optional]  |

### Return type

[**FragmentPage**](FragmentPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of reusable fragments. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="savefragmentsasspecification"></a>
# **SaveFragmentsAsSpecification**
> Specification SaveFragmentsAsSpecification (string specName, FragmentAssembly fragmentAssembly, string description = null, ContentFormat format = null, Guid idempotencyKey = null)

Compile saved fragments and persist the result in the matching protocol engine


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **specName** | **string** |  |  |
| **fragmentAssembly** | [**FragmentAssembly**](FragmentAssembly.md) |  |  |
| **description** | **string** |  | [optional]  |
| **format** | **ContentFormat** | Serialization format used for the returned specification source. | [optional]  |
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
| **200** | The persisted REST, SOAP, or GraphQL specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="updatefragment"></a>
# **UpdateFragment**
> Fragment UpdateFragment (Guid fragmentId, FragmentInput fragmentInput)

Replace a fragment


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **fragmentId** | **Guid** |  |  |
| **fragmentInput** | [**FragmentInput**](FragmentInput.md) |  |  |

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated fragment. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
