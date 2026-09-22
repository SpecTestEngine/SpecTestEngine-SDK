# FragmentsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**compileDraftFragments**](FragmentsApi.md#compiledraftfragments) | **POST** /test/spec/fragment/compile-draft | Compile inline fragment DSL into a specification draft |
| [**compileFragments**](FragmentsApi.md#compilefragments) | **POST** /test/spec/fragment/compile | Compile fragments into a specification draft |
| [**createFragment**](FragmentsApi.md#createfragment) | **POST** /test/spec/fragment/create | Create a specification fragment |
| [**deleteFragment**](FragmentsApi.md#deletefragment) | **DELETE** /test/spec/fragment/by-id | Delete a fragment |
| [**getFragment**](FragmentsApi.md#getfragment) | **GET** /test/spec/fragment/by-id/{fragmentId} | Get a fragment |
| [**getFragmentCatalog**](FragmentsApi.md#getfragmentcatalog) | **GET** /test/spec/fragment/catalog | Get the fragment DSL catalog for an API type |
| [**getFragmentSummary**](FragmentsApi.md#getfragmentsummary) | **GET** /test/spec/fragment/summary | Count fragments by API type |
| [**listFragments**](FragmentsApi.md#listfragments) | **GET** /test/spec/fragment/page | List specification fragments |
| [**saveFragmentsAsSpecification**](FragmentsApi.md#savefragmentsasspecification) | **POST** /test/spec/fragment/save-as-spec | Compile saved fragments and persist the result in the matching protocol engine |
| [**updateFragment**](FragmentsApi.md#updatefragment) | **PUT** /test/spec/fragment/by-id | Replace a fragment |



## compileDraftFragments

> CompiledSpecification compileDraftFragments(fragmentDraftAssembly, format)

Compile inline fragment DSL into a specification draft

### Example

```ts
import {
  Configuration,
  FragmentsApi,
} from '@spectestengine/sdk';
import type { CompileDraftFragmentsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FragmentsApi(config);

  const body = {
    // FragmentDraftAssembly
    fragmentDraftAssembly: ...,
    // ContentFormat | Serialization format used for the returned specification source. (optional)
    format: ...,
  } satisfies CompileDraftFragmentsRequest;

  try {
    const data = await api.compileDraftFragments(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fragmentDraftAssembly** | [FragmentDraftAssembly](FragmentDraftAssembly.md) |  | |
| **format** | `ContentFormat` | Serialization format used for the returned specification source. | [Optional] [Defaults to `undefined`] [Enum: JSON, YAML, XML] |

### Return type

[**CompiledSpecification**](CompiledSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The compiled and protocol-validated specification draft. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## compileFragments

> CompiledSpecification compileFragments(fragmentAssembly, format)

Compile fragments into a specification draft

### Example

```ts
import {
  Configuration,
  FragmentsApi,
} from '@spectestengine/sdk';
import type { CompileFragmentsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FragmentsApi(config);

  const body = {
    // FragmentAssembly
    fragmentAssembly: ...,
    // ContentFormat | Serialization format used for the returned specification source. (optional)
    format: ...,
  } satisfies CompileFragmentsRequest;

  try {
    const data = await api.compileFragments(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fragmentAssembly** | [FragmentAssembly](FragmentAssembly.md) |  | |
| **format** | `ContentFormat` | Serialization format used for the returned specification source. | [Optional] [Defaults to `undefined`] [Enum: JSON, YAML, XML] |

### Return type

[**CompiledSpecification**](CompiledSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The compiled specification draft. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createFragment

> Fragment createFragment(fragmentInput, idempotencyKey)

Create a specification fragment

### Example

```ts
import {
  Configuration,
  FragmentsApi,
} from '@spectestengine/sdk';
import type { CreateFragmentRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FragmentsApi(config);

  const body = {
    // FragmentInput
    fragmentInput: ...,
    // string | A caller-generated UUID retained for safe write retries where supported. (optional)
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CreateFragmentRequest;

  try {
    const data = await api.createFragment(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fragmentInput** | [FragmentInput](FragmentInput.md) |  | |
| **idempotencyKey** | `string` | A caller-generated UUID retained for safe write retries where supported. | [Optional] [Defaults to `undefined`] |

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored fragment. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteFragment

> Fragment deleteFragment(fragmentId)

Delete a fragment

### Example

```ts
import {
  Configuration,
  FragmentsApi,
} from '@spectestengine/sdk';
import type { DeleteFragmentRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FragmentsApi(config);

  const body = {
    // string
    fragmentId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteFragmentRequest;

  try {
    const data = await api.deleteFragment(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fragmentId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted fragment. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFragment

> Fragment getFragment(fragmentId)

Get a fragment

### Example

```ts
import {
  Configuration,
  FragmentsApi,
} from '@spectestengine/sdk';
import type { GetFragmentRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FragmentsApi(config);

  const body = {
    // string
    fragmentId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetFragmentRequest;

  try {
    const data = await api.getFragment(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fragmentId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested fragment. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFragmentCatalog

> FragmentCatalog getFragmentCatalog(specType)

Get the fragment DSL catalog for an API type

### Example

```ts
import {
  Configuration,
  FragmentsApi,
} from '@spectestengine/sdk';
import type { GetFragmentCatalogRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FragmentsApi(config);

  const body = {
    // SpecType
    specType: ...,
  } satisfies GetFragmentCatalogRequest;

  try {
    const data = await api.getFragmentCatalog(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **specType** | `SpecType` |  | [Defaults to `undefined`] [Enum: REST, SOAP, GRAPHQL, STREAMING] |

### Return type

[**FragmentCatalog**](FragmentCatalog.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Compatible fragment types, fields, editor modes, and starter templates. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFragmentSummary

> FragmentSummary getFragmentSummary()

Count fragments by API type

### Example

```ts
import {
  Configuration,
  FragmentsApi,
} from '@spectestengine/sdk';
import type { GetFragmentSummaryRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FragmentsApi(config);

  try {
    const data = await api.getFragmentSummary();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**FragmentSummary**](FragmentSummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | REST, SOAP, and GraphQL fragment counts. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listFragments

> FragmentPage listFragments(page, size, search, specType, type)

List specification fragments

### Example

```ts
import {
  Configuration,
  FragmentsApi,
} from '@spectestengine/sdk';
import type { ListFragmentsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FragmentsApi(config);

  const body = {
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
    // string | Case-insensitive server-side search within the active project. (optional)
    search: search_example,
    // SpecType | Filter the library to one API protocol. (optional)
    specType: ...,
    // FragmentType (optional)
    type: ...,
  } satisfies ListFragmentsRequest;

  try {
    const data = await api.listFragments(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | `number` | Zero-based page index. | [Optional] [Defaults to `0`] |
| **size** | `number` | Maximum number of results returned in one page. | [Optional] [Defaults to `20`] |
| **search** | `string` | Case-insensitive server-side search within the active project. | [Optional] [Defaults to `undefined`] |
| **specType** | `SpecType` | Filter the library to one API protocol. | [Optional] [Defaults to `undefined`] [Enum: REST, SOAP, GRAPHQL, STREAMING] |
| **type** | `FragmentType` |  | [Optional] [Defaults to `undefined`] [Enum: URL_METHOD, HEADER, BODY, REQUEST_ATTACHMENT, HEADER_ASSERTION, BODY_ASSERTION, ATTACHMENT_ASSERTION, SOAP_REQUEST, SOAP_ASSERTION, GRAPHQL_OPERATION, GRAPHQL_ASSERTION, STREAM_REQUEST, STREAM_SCHEMA, STREAM_SEND, STREAM_EXPECT, STREAM_CONTROL, STREAM_ASSERTION] |

### Return type

[**FragmentPage**](FragmentPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of reusable fragments. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## saveFragmentsAsSpecification

> Specification saveFragmentsAsSpecification(specName, fragmentAssembly, description, format, idempotencyKey)

Compile saved fragments and persist the result in the matching protocol engine

### Example

```ts
import {
  Configuration,
  FragmentsApi,
} from '@spectestengine/sdk';
import type { SaveFragmentsAsSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FragmentsApi(config);

  const body = {
    // string
    specName: specName_example,
    // FragmentAssembly
    fragmentAssembly: ...,
    // string (optional)
    description: description_example,
    // ContentFormat | Serialization format used for the returned specification source. (optional)
    format: ...,
    // string | A caller-generated UUID retained for safe write retries where supported. (optional)
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies SaveFragmentsAsSpecificationRequest;

  try {
    const data = await api.saveFragmentsAsSpecification(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **specName** | `string` |  | [Defaults to `undefined`] |
| **fragmentAssembly** | [FragmentAssembly](FragmentAssembly.md) |  | |
| **description** | `string` |  | [Optional] [Defaults to `undefined`] |
| **format** | `ContentFormat` | Serialization format used for the returned specification source. | [Optional] [Defaults to `undefined`] [Enum: JSON, YAML, XML] |
| **idempotencyKey** | `string` | A caller-generated UUID retained for safe write retries where supported. | [Optional] [Defaults to `undefined`] |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The persisted REST, SOAP, or GraphQL specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateFragment

> Fragment updateFragment(fragmentId, fragmentInput)

Replace a fragment

### Example

```ts
import {
  Configuration,
  FragmentsApi,
} from '@spectestengine/sdk';
import type { UpdateFragmentRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FragmentsApi(config);

  const body = {
    // string
    fragmentId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // FragmentInput
    fragmentInput: ...,
  } satisfies UpdateFragmentRequest;

  try {
    const data = await api.updateFragment(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fragmentId** | `string` |  | [Defaults to `undefined`] |
| **fragmentInput** | [FragmentInput](FragmentInput.md) |  | |

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated fragment. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

