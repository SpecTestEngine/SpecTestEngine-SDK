# RunBatchesApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRunBatch**](RunBatchesApi.md#createRunBatch) | **POST** /test/run-batch/create | Create a run batch |
| [**createRunBatchWithHttpInfo**](RunBatchesApi.md#createRunBatchWithHttpInfo) | **POST** /test/run-batch/create | Create a run batch |
| [**getRunBatch**](RunBatchesApi.md#getRunBatch) | **GET** /test/run-batch/by-id/{batchId} | Get a run batch |
| [**getRunBatchWithHttpInfo**](RunBatchesApi.md#getRunBatchWithHttpInfo) | **GET** /test/run-batch/by-id/{batchId} | Get a run batch |
| [**listRunBatches**](RunBatchesApi.md#listRunBatches) | **GET** /test/run-batch/page | List run batches |
| [**listRunBatchesWithHttpInfo**](RunBatchesApi.md#listRunBatchesWithHttpInfo) | **GET** /test/run-batch/page | List run batches |



## createRunBatch

> RunBatch createRunBatch(createRunBatchRequest)

Create a run batch

Collect completed specification, UI macro, and flow runs into one immutable evidence set that can later become a snapshot baseline.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RunBatchesApi;
import software.ste.sdk.generated.api.RunBatchesApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RunBatchesApi apiInstance = new RunBatchesApi(defaultClient);
        RunBatchInput runBatchInput = new RunBatchInput(); // RunBatchInput |
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateRunBatchRequest request = APIcreateRunBatchRequest.newBuilder()
                .runBatchInput(runBatchInput)
                .idempotencyKey(idempotencyKey)
                .build();
            RunBatch result = apiInstance.createRunBatch(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RunBatchesApi#createRunBatch");
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
| createRunBatchRequest | [**APIcreateRunBatchRequest**](RunBatchesApi.md#APIcreateRunBatchRequest)|-|-|

### Return type

[**RunBatch**](RunBatch.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created run batch and its captured evidence items. |  -  |
| **0** | The request failed. |  -  |

## createRunBatchWithHttpInfo

> ApiResponse<RunBatch> createRunBatchWithHttpInfo(createRunBatchRequest)

Create a run batch

Collect completed specification, UI macro, and flow runs into one immutable evidence set that can later become a snapshot baseline.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RunBatchesApi;
import software.ste.sdk.generated.api.RunBatchesApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RunBatchesApi apiInstance = new RunBatchesApi(defaultClient);
        RunBatchInput runBatchInput = new RunBatchInput(); // RunBatchInput |
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateRunBatchRequest request = APIcreateRunBatchRequest.newBuilder()
                .runBatchInput(runBatchInput)
                .idempotencyKey(idempotencyKey)
                .build();
            ApiResponse<RunBatch> response = apiInstance.createRunBatchWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RunBatchesApi#createRunBatch");
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
| createRunBatchRequest | [**APIcreateRunBatchRequest**](RunBatchesApi.md#APIcreateRunBatchRequest)|-|-|

### Return type

ApiResponse<[**RunBatch**](RunBatch.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created run batch and its captured evidence items. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcreateRunBatchRequest"></a>
## APIcreateRunBatchRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **runBatchInput** | [**RunBatchInput**](RunBatchInput.md) |  | |
| **idempotencyKey** | **UUID** | A caller-generated UUID retained for safe write retries where supported. | [optional] |



## getRunBatch

> RunBatch getRunBatch(getRunBatchRequest)

Get a run batch

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RunBatchesApi;
import software.ste.sdk.generated.api.RunBatchesApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RunBatchesApi apiInstance = new RunBatchesApi(defaultClient);
        UUID batchId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved run batch.
        try {
            APIgetRunBatchRequest request = APIgetRunBatchRequest.newBuilder()
                .batchId(batchId)
                .build();
            RunBatch result = apiInstance.getRunBatch(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RunBatchesApi#getRunBatch");
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
| getRunBatchRequest | [**APIgetRunBatchRequest**](RunBatchesApi.md#APIgetRunBatchRequest)|-|-|

### Return type

[**RunBatch**](RunBatch.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested run batch with its captured evidence items. |  -  |
| **0** | The request failed. |  -  |

## getRunBatchWithHttpInfo

> ApiResponse<RunBatch> getRunBatchWithHttpInfo(getRunBatchRequest)

Get a run batch

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RunBatchesApi;
import software.ste.sdk.generated.api.RunBatchesApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RunBatchesApi apiInstance = new RunBatchesApi(defaultClient);
        UUID batchId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved run batch.
        try {
            APIgetRunBatchRequest request = APIgetRunBatchRequest.newBuilder()
                .batchId(batchId)
                .build();
            ApiResponse<RunBatch> response = apiInstance.getRunBatchWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RunBatchesApi#getRunBatch");
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
| getRunBatchRequest | [**APIgetRunBatchRequest**](RunBatchesApi.md#APIgetRunBatchRequest)|-|-|

### Return type

ApiResponse<[**RunBatch**](RunBatch.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested run batch with its captured evidence items. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetRunBatchRequest"></a>
## APIgetRunBatchRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **batchId** | **UUID** | UUIDv7 identifier of the saved run batch. | |



## listRunBatches

> RunBatchPage listRunBatches(listRunBatchesRequest)

List run batches

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RunBatchesApi;
import software.ste.sdk.generated.api.RunBatchesApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RunBatchesApi apiInstance = new RunBatchesApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistRunBatchesRequest request = APIlistRunBatchesRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .build();
            RunBatchPage result = apiInstance.listRunBatches(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RunBatchesApi#listRunBatches");
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
| listRunBatchesRequest | [**APIlistRunBatchesRequest**](RunBatchesApi.md#APIlistRunBatchesRequest)|-|-|

### Return type

[**RunBatchPage**](RunBatchPage.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of run batches in the active project. |  -  |
| **0** | The request failed. |  -  |

## listRunBatchesWithHttpInfo

> ApiResponse<RunBatchPage> listRunBatchesWithHttpInfo(listRunBatchesRequest)

List run batches

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RunBatchesApi;
import software.ste.sdk.generated.api.RunBatchesApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RunBatchesApi apiInstance = new RunBatchesApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistRunBatchesRequest request = APIlistRunBatchesRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .build();
            ApiResponse<RunBatchPage> response = apiInstance.listRunBatchesWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RunBatchesApi#listRunBatches");
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
| listRunBatchesRequest | [**APIlistRunBatchesRequest**](RunBatchesApi.md#APIlistRunBatchesRequest)|-|-|

### Return type

ApiResponse<[**RunBatchPage**](RunBatchPage.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of run batches in the active project. |  -  |
| **0** | The request failed. |  -  |


<a id="APIlistRunBatchesRequest"></a>
## APIlistRunBatchesRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **String** | Case-insensitive server-side search within the active project. | [optional] |


