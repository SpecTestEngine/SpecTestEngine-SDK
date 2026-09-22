# FragmentsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**compileDraftFragments**](FragmentsApi.md#compileDraftFragments) | **POST** /test/spec/fragment/compile-draft | Compile inline fragment DSL into a specification draft |
| [**compileDraftFragmentsWithHttpInfo**](FragmentsApi.md#compileDraftFragmentsWithHttpInfo) | **POST** /test/spec/fragment/compile-draft | Compile inline fragment DSL into a specification draft |
| [**compileFragments**](FragmentsApi.md#compileFragments) | **POST** /test/spec/fragment/compile | Compile fragments into a specification draft |
| [**compileFragmentsWithHttpInfo**](FragmentsApi.md#compileFragmentsWithHttpInfo) | **POST** /test/spec/fragment/compile | Compile fragments into a specification draft |
| [**createFragment**](FragmentsApi.md#createFragment) | **POST** /test/spec/fragment/create | Create a specification fragment |
| [**createFragmentWithHttpInfo**](FragmentsApi.md#createFragmentWithHttpInfo) | **POST** /test/spec/fragment/create | Create a specification fragment |
| [**deleteFragment**](FragmentsApi.md#deleteFragment) | **DELETE** /test/spec/fragment/by-id | Delete a fragment |
| [**deleteFragmentWithHttpInfo**](FragmentsApi.md#deleteFragmentWithHttpInfo) | **DELETE** /test/spec/fragment/by-id | Delete a fragment |
| [**getFragment**](FragmentsApi.md#getFragment) | **GET** /test/spec/fragment/by-id/{fragmentId} | Get a fragment |
| [**getFragmentWithHttpInfo**](FragmentsApi.md#getFragmentWithHttpInfo) | **GET** /test/spec/fragment/by-id/{fragmentId} | Get a fragment |
| [**getFragmentCatalog**](FragmentsApi.md#getFragmentCatalog) | **GET** /test/spec/fragment/catalog | Get the fragment DSL catalog for an API type |
| [**getFragmentCatalogWithHttpInfo**](FragmentsApi.md#getFragmentCatalogWithHttpInfo) | **GET** /test/spec/fragment/catalog | Get the fragment DSL catalog for an API type |
| [**getFragmentSummary**](FragmentsApi.md#getFragmentSummary) | **GET** /test/spec/fragment/summary | Count fragments by API type |
| [**getFragmentSummaryWithHttpInfo**](FragmentsApi.md#getFragmentSummaryWithHttpInfo) | **GET** /test/spec/fragment/summary | Count fragments by API type |
| [**listFragments**](FragmentsApi.md#listFragments) | **GET** /test/spec/fragment/page | List specification fragments |
| [**listFragmentsWithHttpInfo**](FragmentsApi.md#listFragmentsWithHttpInfo) | **GET** /test/spec/fragment/page | List specification fragments |
| [**saveFragmentsAsSpecification**](FragmentsApi.md#saveFragmentsAsSpecification) | **POST** /test/spec/fragment/save-as-spec | Compile saved fragments and persist the result in the matching protocol engine |
| [**saveFragmentsAsSpecificationWithHttpInfo**](FragmentsApi.md#saveFragmentsAsSpecificationWithHttpInfo) | **POST** /test/spec/fragment/save-as-spec | Compile saved fragments and persist the result in the matching protocol engine |
| [**updateFragment**](FragmentsApi.md#updateFragment) | **PUT** /test/spec/fragment/by-id | Replace a fragment |
| [**updateFragmentWithHttpInfo**](FragmentsApi.md#updateFragmentWithHttpInfo) | **PUT** /test/spec/fragment/by-id | Replace a fragment |



## compileDraftFragments

> CompiledSpecification compileDraftFragments(compileDraftFragmentsRequest)

Compile inline fragment DSL into a specification draft

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        FragmentDraftAssembly fragmentDraftAssembly = new FragmentDraftAssembly(); // FragmentDraftAssembly |
        ContentFormat format = ContentFormat.fromValue("JSON"); // ContentFormat | Serialization format used for the returned specification source.
        try {
            APIcompileDraftFragmentsRequest request = APIcompileDraftFragmentsRequest.newBuilder()
                .fragmentDraftAssembly(fragmentDraftAssembly)
                .format(format)
                .build();
            CompiledSpecification result = apiInstance.compileDraftFragments(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#compileDraftFragments");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| compileDraftFragmentsRequest | [**APIcompileDraftFragmentsRequest**](FragmentsApi.md#APIcompileDraftFragmentsRequest)|-|-|

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

## compileDraftFragmentsWithHttpInfo

> ApiResponse<CompiledSpecification> compileDraftFragmentsWithHttpInfo(compileDraftFragmentsRequest)

Compile inline fragment DSL into a specification draft

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        FragmentDraftAssembly fragmentDraftAssembly = new FragmentDraftAssembly(); // FragmentDraftAssembly |
        ContentFormat format = ContentFormat.fromValue("JSON"); // ContentFormat | Serialization format used for the returned specification source.
        try {
            APIcompileDraftFragmentsRequest request = APIcompileDraftFragmentsRequest.newBuilder()
                .fragmentDraftAssembly(fragmentDraftAssembly)
                .format(format)
                .build();
            ApiResponse<CompiledSpecification> response = apiInstance.compileDraftFragmentsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#compileDraftFragments");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| compileDraftFragmentsRequest | [**APIcompileDraftFragmentsRequest**](FragmentsApi.md#APIcompileDraftFragmentsRequest)|-|-|

### Return type

ApiResponse<[**CompiledSpecification**](CompiledSpecification.md)>


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


<a id="APIcompileDraftFragmentsRequest"></a>
## APIcompileDraftFragmentsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **fragmentDraftAssembly** | [**FragmentDraftAssembly**](FragmentDraftAssembly.md) |  | |
| **format** | [**ContentFormat**](.md) | Serialization format used for the returned specification source. | [optional] [default to JSON] [enum: JSON, YAML, XML] |



## compileFragments

> CompiledSpecification compileFragments(compileFragmentsRequest)

Compile fragments into a specification draft

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        FragmentAssembly fragmentAssembly = new FragmentAssembly(); // FragmentAssembly |
        ContentFormat format = ContentFormat.fromValue("JSON"); // ContentFormat | Serialization format used for the returned specification source.
        try {
            APIcompileFragmentsRequest request = APIcompileFragmentsRequest.newBuilder()
                .fragmentAssembly(fragmentAssembly)
                .format(format)
                .build();
            CompiledSpecification result = apiInstance.compileFragments(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#compileFragments");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| compileFragmentsRequest | [**APIcompileFragmentsRequest**](FragmentsApi.md#APIcompileFragmentsRequest)|-|-|

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

## compileFragmentsWithHttpInfo

> ApiResponse<CompiledSpecification> compileFragmentsWithHttpInfo(compileFragmentsRequest)

Compile fragments into a specification draft

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        FragmentAssembly fragmentAssembly = new FragmentAssembly(); // FragmentAssembly |
        ContentFormat format = ContentFormat.fromValue("JSON"); // ContentFormat | Serialization format used for the returned specification source.
        try {
            APIcompileFragmentsRequest request = APIcompileFragmentsRequest.newBuilder()
                .fragmentAssembly(fragmentAssembly)
                .format(format)
                .build();
            ApiResponse<CompiledSpecification> response = apiInstance.compileFragmentsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#compileFragments");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| compileFragmentsRequest | [**APIcompileFragmentsRequest**](FragmentsApi.md#APIcompileFragmentsRequest)|-|-|

### Return type

ApiResponse<[**CompiledSpecification**](CompiledSpecification.md)>


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


<a id="APIcompileFragmentsRequest"></a>
## APIcompileFragmentsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **fragmentAssembly** | [**FragmentAssembly**](FragmentAssembly.md) |  | |
| **format** | [**ContentFormat**](.md) | Serialization format used for the returned specification source. | [optional] [default to JSON] [enum: JSON, YAML, XML] |



## createFragment

> Fragment createFragment(createFragmentRequest)

Create a specification fragment

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        FragmentInput fragmentInput = new FragmentInput(); // FragmentInput |
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateFragmentRequest request = APIcreateFragmentRequest.newBuilder()
                .fragmentInput(fragmentInput)
                .idempotencyKey(idempotencyKey)
                .build();
            Fragment result = apiInstance.createFragment(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#createFragment");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| createFragmentRequest | [**APIcreateFragmentRequest**](FragmentsApi.md#APIcreateFragmentRequest)|-|-|

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

## createFragmentWithHttpInfo

> ApiResponse<Fragment> createFragmentWithHttpInfo(createFragmentRequest)

Create a specification fragment

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        FragmentInput fragmentInput = new FragmentInput(); // FragmentInput |
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateFragmentRequest request = APIcreateFragmentRequest.newBuilder()
                .fragmentInput(fragmentInput)
                .idempotencyKey(idempotencyKey)
                .build();
            ApiResponse<Fragment> response = apiInstance.createFragmentWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#createFragment");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| createFragmentRequest | [**APIcreateFragmentRequest**](FragmentsApi.md#APIcreateFragmentRequest)|-|-|

### Return type

ApiResponse<[**Fragment**](Fragment.md)>


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


<a id="APIcreateFragmentRequest"></a>
## APIcreateFragmentRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **fragmentInput** | [**FragmentInput**](FragmentInput.md) |  | |
| **idempotencyKey** | **UUID** | A caller-generated UUID retained for safe write retries where supported. | [optional] |



## deleteFragment

> Fragment deleteFragment(deleteFragmentRequest)

Delete a fragment

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        UUID fragmentId = UUID.randomUUID(); // UUID |
        try {
            APIdeleteFragmentRequest request = APIdeleteFragmentRequest.newBuilder()
                .fragmentId(fragmentId)
                .build();
            Fragment result = apiInstance.deleteFragment(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#deleteFragment");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| deleteFragmentRequest | [**APIdeleteFragmentRequest**](FragmentsApi.md#APIdeleteFragmentRequest)|-|-|

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

## deleteFragmentWithHttpInfo

> ApiResponse<Fragment> deleteFragmentWithHttpInfo(deleteFragmentRequest)

Delete a fragment

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        UUID fragmentId = UUID.randomUUID(); // UUID |
        try {
            APIdeleteFragmentRequest request = APIdeleteFragmentRequest.newBuilder()
                .fragmentId(fragmentId)
                .build();
            ApiResponse<Fragment> response = apiInstance.deleteFragmentWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#deleteFragment");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| deleteFragmentRequest | [**APIdeleteFragmentRequest**](FragmentsApi.md#APIdeleteFragmentRequest)|-|-|

### Return type

ApiResponse<[**Fragment**](Fragment.md)>


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


<a id="APIdeleteFragmentRequest"></a>
## APIdeleteFragmentRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **fragmentId** | **UUID** |  | |



## getFragment

> Fragment getFragment(getFragmentRequest)

Get a fragment

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        UUID fragmentId = UUID.randomUUID(); // UUID |
        try {
            APIgetFragmentRequest request = APIgetFragmentRequest.newBuilder()
                .fragmentId(fragmentId)
                .build();
            Fragment result = apiInstance.getFragment(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#getFragment");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| getFragmentRequest | [**APIgetFragmentRequest**](FragmentsApi.md#APIgetFragmentRequest)|-|-|

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

## getFragmentWithHttpInfo

> ApiResponse<Fragment> getFragmentWithHttpInfo(getFragmentRequest)

Get a fragment

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        UUID fragmentId = UUID.randomUUID(); // UUID |
        try {
            APIgetFragmentRequest request = APIgetFragmentRequest.newBuilder()
                .fragmentId(fragmentId)
                .build();
            ApiResponse<Fragment> response = apiInstance.getFragmentWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#getFragment");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| getFragmentRequest | [**APIgetFragmentRequest**](FragmentsApi.md#APIgetFragmentRequest)|-|-|

### Return type

ApiResponse<[**Fragment**](Fragment.md)>


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


<a id="APIgetFragmentRequest"></a>
## APIgetFragmentRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **fragmentId** | **UUID** |  | |



## getFragmentCatalog

> FragmentCatalog getFragmentCatalog(getFragmentCatalogRequest)

Get the fragment DSL catalog for an API type

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        SpecType specType = SpecType.fromValue("REST"); // SpecType |
        try {
            APIgetFragmentCatalogRequest request = APIgetFragmentCatalogRequest.newBuilder()
                .specType(specType)
                .build();
            FragmentCatalog result = apiInstance.getFragmentCatalog(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#getFragmentCatalog");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| getFragmentCatalogRequest | [**APIgetFragmentCatalogRequest**](FragmentsApi.md#APIgetFragmentCatalogRequest)|-|-|

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

## getFragmentCatalogWithHttpInfo

> ApiResponse<FragmentCatalog> getFragmentCatalogWithHttpInfo(getFragmentCatalogRequest)

Get the fragment DSL catalog for an API type

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        SpecType specType = SpecType.fromValue("REST"); // SpecType |
        try {
            APIgetFragmentCatalogRequest request = APIgetFragmentCatalogRequest.newBuilder()
                .specType(specType)
                .build();
            ApiResponse<FragmentCatalog> response = apiInstance.getFragmentCatalogWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#getFragmentCatalog");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| getFragmentCatalogRequest | [**APIgetFragmentCatalogRequest**](FragmentsApi.md#APIgetFragmentCatalogRequest)|-|-|

### Return type

ApiResponse<[**FragmentCatalog**](FragmentCatalog.md)>


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


<a id="APIgetFragmentCatalogRequest"></a>
## APIgetFragmentCatalogRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specType** | [**SpecType**](.md) |  | [enum: REST, SOAP, GRAPHQL, STREAMING] |



## getFragmentSummary

> FragmentSummary getFragmentSummary()

Count fragments by API type

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        try {
            FragmentSummary result = apiInstance.getFragmentSummary();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#getFragmentSummary");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

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

## getFragmentSummaryWithHttpInfo

> ApiResponse<FragmentSummary> getFragmentSummaryWithHttpInfo()

Count fragments by API type

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        try {
            ApiResponse<FragmentSummary> response = apiInstance.getFragmentSummaryWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#getFragmentSummary");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

ApiResponse<[**FragmentSummary**](FragmentSummary.md)>


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


## listFragments

> FragmentPage listFragments(listFragmentsRequest)

List specification fragments

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        SpecType specType = SpecType.fromValue("REST"); // SpecType | Filter the library to one API protocol.
        FragmentType type = FragmentType.fromValue("URL_METHOD"); // FragmentType |
        try {
            APIlistFragmentsRequest request = APIlistFragmentsRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .specType(specType)
                .type(type)
                .build();
            FragmentPage result = apiInstance.listFragments(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#listFragments");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| listFragmentsRequest | [**APIlistFragmentsRequest**](FragmentsApi.md#APIlistFragmentsRequest)|-|-|

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

## listFragmentsWithHttpInfo

> ApiResponse<FragmentPage> listFragmentsWithHttpInfo(listFragmentsRequest)

List specification fragments

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        SpecType specType = SpecType.fromValue("REST"); // SpecType | Filter the library to one API protocol.
        FragmentType type = FragmentType.fromValue("URL_METHOD"); // FragmentType |
        try {
            APIlistFragmentsRequest request = APIlistFragmentsRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .specType(specType)
                .type(type)
                .build();
            ApiResponse<FragmentPage> response = apiInstance.listFragmentsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#listFragments");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| listFragmentsRequest | [**APIlistFragmentsRequest**](FragmentsApi.md#APIlistFragmentsRequest)|-|-|

### Return type

ApiResponse<[**FragmentPage**](FragmentPage.md)>


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


<a id="APIlistFragmentsRequest"></a>
## APIlistFragmentsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **String** | Case-insensitive server-side search within the active project. | [optional] |
| **specType** | [**SpecType**](.md) | Filter the library to one API protocol. | [optional] [enum: REST, SOAP, GRAPHQL, STREAMING] |
| **type** | [**FragmentType**](.md) |  | [optional] [enum: URL_METHOD, HEADER, BODY, REQUEST_ATTACHMENT, HEADER_ASSERTION, BODY_ASSERTION, ATTACHMENT_ASSERTION, SOAP_REQUEST, SOAP_ASSERTION, GRAPHQL_OPERATION, GRAPHQL_ASSERTION, STREAM_REQUEST, STREAM_SCHEMA, STREAM_SEND, STREAM_EXPECT, STREAM_CONTROL, STREAM_ASSERTION] |



## saveFragmentsAsSpecification

> Specification saveFragmentsAsSpecification(saveFragmentsAsSpecificationRequest)

Compile saved fragments and persist the result in the matching protocol engine

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        String specName = "specName_example"; // String |
        FragmentAssembly fragmentAssembly = new FragmentAssembly(); // FragmentAssembly |
        String description = "description_example"; // String |
        ContentFormat format = ContentFormat.fromValue("JSON"); // ContentFormat | Serialization format used for the returned specification source.
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIsaveFragmentsAsSpecificationRequest request = APIsaveFragmentsAsSpecificationRequest.newBuilder()
                .specName(specName)
                .fragmentAssembly(fragmentAssembly)
                .description(description)
                .format(format)
                .idempotencyKey(idempotencyKey)
                .build();
            Specification result = apiInstance.saveFragmentsAsSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#saveFragmentsAsSpecification");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| saveFragmentsAsSpecificationRequest | [**APIsaveFragmentsAsSpecificationRequest**](FragmentsApi.md#APIsaveFragmentsAsSpecificationRequest)|-|-|

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

## saveFragmentsAsSpecificationWithHttpInfo

> ApiResponse<Specification> saveFragmentsAsSpecificationWithHttpInfo(saveFragmentsAsSpecificationRequest)

Compile saved fragments and persist the result in the matching protocol engine

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        String specName = "specName_example"; // String |
        FragmentAssembly fragmentAssembly = new FragmentAssembly(); // FragmentAssembly |
        String description = "description_example"; // String |
        ContentFormat format = ContentFormat.fromValue("JSON"); // ContentFormat | Serialization format used for the returned specification source.
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIsaveFragmentsAsSpecificationRequest request = APIsaveFragmentsAsSpecificationRequest.newBuilder()
                .specName(specName)
                .fragmentAssembly(fragmentAssembly)
                .description(description)
                .format(format)
                .idempotencyKey(idempotencyKey)
                .build();
            ApiResponse<Specification> response = apiInstance.saveFragmentsAsSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#saveFragmentsAsSpecification");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| saveFragmentsAsSpecificationRequest | [**APIsaveFragmentsAsSpecificationRequest**](FragmentsApi.md#APIsaveFragmentsAsSpecificationRequest)|-|-|

### Return type

ApiResponse<[**Specification**](Specification.md)>


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


<a id="APIsaveFragmentsAsSpecificationRequest"></a>
## APIsaveFragmentsAsSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specName** | **String** |  | |
| **fragmentAssembly** | [**FragmentAssembly**](FragmentAssembly.md) |  | |
| **description** | **String** |  | [optional] |
| **format** | [**ContentFormat**](.md) | Serialization format used for the returned specification source. | [optional] [default to JSON] [enum: JSON, YAML, XML] |
| **idempotencyKey** | **UUID** | A caller-generated UUID retained for safe write retries where supported. | [optional] |



## updateFragment

> Fragment updateFragment(updateFragmentRequest)

Replace a fragment

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        UUID fragmentId = UUID.randomUUID(); // UUID |
        FragmentInput fragmentInput = new FragmentInput(); // FragmentInput |
        try {
            APIupdateFragmentRequest request = APIupdateFragmentRequest.newBuilder()
                .fragmentId(fragmentId)
                .fragmentInput(fragmentInput)
                .build();
            Fragment result = apiInstance.updateFragment(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#updateFragment");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| updateFragmentRequest | [**APIupdateFragmentRequest**](FragmentsApi.md#APIupdateFragmentRequest)|-|-|

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

## updateFragmentWithHttpInfo

> ApiResponse<Fragment> updateFragmentWithHttpInfo(updateFragmentRequest)

Replace a fragment

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FragmentsApi;
import software.ste.sdk.generated.api.FragmentsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FragmentsApi apiInstance = new FragmentsApi(defaultClient);
        UUID fragmentId = UUID.randomUUID(); // UUID |
        FragmentInput fragmentInput = new FragmentInput(); // FragmentInput |
        try {
            APIupdateFragmentRequest request = APIupdateFragmentRequest.newBuilder()
                .fragmentId(fragmentId)
                .fragmentInput(fragmentInput)
                .build();
            ApiResponse<Fragment> response = apiInstance.updateFragmentWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FragmentsApi#updateFragment");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

|    Name      |    Type       | Description   |     Notes    |
|------------- | ------------- | ------------- | -------------|
| updateFragmentRequest | [**APIupdateFragmentRequest**](FragmentsApi.md#APIupdateFragmentRequest)|-|-|

### Return type

ApiResponse<[**Fragment**](Fragment.md)>


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


<a id="APIupdateFragmentRequest"></a>
## APIupdateFragmentRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **fragmentId** | **UUID** |  | |
| **fragmentInput** | [**FragmentInput**](FragmentInput.md) |  | |


