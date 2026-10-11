# StreamingSpecificationsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelStreamingSpecificationRun**](StreamingSpecificationsApi.md#cancelStreamingSpecificationRun) | **POST** /test/streaming-spec/run/history/by-run-id/{runId}/cancel | Cancel an active streaming run |
| [**cancelStreamingSpecificationRunWithHttpInfo**](StreamingSpecificationsApi.md#cancelStreamingSpecificationRunWithHttpInfo) | **POST** /test/streaming-spec/run/history/by-run-id/{runId}/cancel | Cancel an active streaming run |
| [**createStreamingSpecification**](StreamingSpecificationsApi.md#createStreamingSpecification) | **POST** /test/streaming-spec/create | Create a streaming specification |
| [**createStreamingSpecificationWithHttpInfo**](StreamingSpecificationsApi.md#createStreamingSpecificationWithHttpInfo) | **POST** /test/streaming-spec/create | Create a streaming specification |
| [**deleteStreamingSpecification**](StreamingSpecificationsApi.md#deleteStreamingSpecification) | **DELETE** /test/streaming-spec/by-id | Delete a streaming specification |
| [**deleteStreamingSpecificationWithHttpInfo**](StreamingSpecificationsApi.md#deleteStreamingSpecificationWithHttpInfo) | **DELETE** /test/streaming-spec/by-id | Delete a streaming specification |
| [**getStreamingCapabilities**](StreamingSpecificationsApi.md#getStreamingCapabilities) | **GET** /engine/streaming/capabilities | Get streaming engine capabilities and enforced limits |
| [**getStreamingCapabilitiesWithHttpInfo**](StreamingSpecificationsApi.md#getStreamingCapabilitiesWithHttpInfo) | **GET** /engine/streaming/capabilities | Get streaming engine capabilities and enforced limits |
| [**getStreamingSpecification**](StreamingSpecificationsApi.md#getStreamingSpecification) | **GET** /test/streaming-spec/by-id | Get a streaming specification |
| [**getStreamingSpecificationWithHttpInfo**](StreamingSpecificationsApi.md#getStreamingSpecificationWithHttpInfo) | **GET** /test/streaming-spec/by-id | Get a streaming specification |
| [**getStreamingSpecificationRun**](StreamingSpecificationsApi.md#getStreamingSpecificationRun) | **GET** /test/streaming-spec/run/history/by-run-id/{runId} | Get streaming run state and bounded semantic evidence |
| [**getStreamingSpecificationRunWithHttpInfo**](StreamingSpecificationsApi.md#getStreamingSpecificationRunWithHttpInfo) | **GET** /test/streaming-spec/run/history/by-run-id/{runId} | Get streaming run state and bounded semantic evidence |
| [**getStreamingSpecificationRunTranscript**](StreamingSpecificationsApi.md#getStreamingSpecificationRunTranscript) | **GET** /test/streaming-spec/run/history/by-run-id/{runId}/transcript | Page a bounded streaming run transcript |
| [**getStreamingSpecificationRunTranscriptWithHttpInfo**](StreamingSpecificationsApi.md#getStreamingSpecificationRunTranscriptWithHttpInfo) | **GET** /test/streaming-spec/run/history/by-run-id/{runId}/transcript | Page a bounded streaming run transcript |
| [**listStreamingSpecificationRuns**](StreamingSpecificationsApi.md#listStreamingSpecificationRuns) | **GET** /test/streaming-spec/run/page/by-spec-id/{specId} | List runs for a saved streaming specification |
| [**listStreamingSpecificationRunsWithHttpInfo**](StreamingSpecificationsApi.md#listStreamingSpecificationRunsWithHttpInfo) | **GET** /test/streaming-spec/run/page/by-spec-id/{specId} | List runs for a saved streaming specification |
| [**listStreamingSpecifications**](StreamingSpecificationsApi.md#listStreamingSpecifications) | **GET** /test/streaming-spec/page | List streaming specifications |
| [**listStreamingSpecificationsWithHttpInfo**](StreamingSpecificationsApi.md#listStreamingSpecificationsWithHttpInfo) | **GET** /test/streaming-spec/page | List streaming specifications |
| [**previewStreamingSpecificationRecovery**](StreamingSpecificationsApi.md#previewStreamingSpecificationRecovery) | **POST** /test/streaming-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a Streaming specification version |
| [**previewStreamingSpecificationRecoveryWithHttpInfo**](StreamingSpecificationsApi.md#previewStreamingSpecificationRecoveryWithHttpInfo) | **POST** /test/streaming-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a Streaming specification version |
| [**restoreStreamingSpecificationFromRun**](StreamingSpecificationsApi.md#restoreStreamingSpecificationFromRun) | **PUT** /test/streaming-spec/recovery/{specId}/from-run/{runId}/restore | Restore a Streaming specification version |
| [**restoreStreamingSpecificationFromRunWithHttpInfo**](StreamingSpecificationsApi.md#restoreStreamingSpecificationFromRunWithHttpInfo) | **PUT** /test/streaming-spec/recovery/{specId}/from-run/{runId}/restore | Restore a Streaming specification version |
| [**runStreamingSpecification**](StreamingSpecificationsApi.md#runStreamingSpecification) | **POST** /test/streaming-spec/run/by-id/{specId} | Queue a saved streaming specification run |
| [**runStreamingSpecificationWithHttpInfo**](StreamingSpecificationsApi.md#runStreamingSpecificationWithHttpInfo) | **POST** /test/streaming-spec/run/by-id/{specId} | Queue a saved streaming specification run |
| [**runStreamingSpecificationDraft**](StreamingSpecificationsApi.md#runStreamingSpecificationDraft) | **POST** /test/streaming-spec/run/draft | Queue a bounded streaming specification draft run |
| [**runStreamingSpecificationDraftWithHttpInfo**](StreamingSpecificationsApi.md#runStreamingSpecificationDraftWithHttpInfo) | **POST** /test/streaming-spec/run/draft | Queue a bounded streaming specification draft run |
| [**testStreamingSpecificationRecoveryVersion**](StreamingSpecificationsApi.md#testStreamingSpecificationRecoveryVersion) | **POST** /test/streaming-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous Streaming specification version |
| [**testStreamingSpecificationRecoveryVersionWithHttpInfo**](StreamingSpecificationsApi.md#testStreamingSpecificationRecoveryVersionWithHttpInfo) | **POST** /test/streaming-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous Streaming specification version |
| [**updateStreamingSpecification**](StreamingSpecificationsApi.md#updateStreamingSpecification) | **PUT** /test/streaming-spec/by-id | Replace a streaming specification definition |
| [**updateStreamingSpecificationWithHttpInfo**](StreamingSpecificationsApi.md#updateStreamingSpecificationWithHttpInfo) | **PUT** /test/streaming-spec/by-id | Replace a streaming specification definition |
| [**validateStreamingSpecificationDraft**](StreamingSpecificationsApi.md#validateStreamingSpecificationDraft) | **POST** /test/streaming-spec/validate-draft | Validate and detect the transport of a streaming specification draft |
| [**validateStreamingSpecificationDraftWithHttpInfo**](StreamingSpecificationsApi.md#validateStreamingSpecificationDraftWithHttpInfo) | **POST** /test/streaming-spec/validate-draft | Validate and detect the transport of a streaming specification draft |



## cancelStreamingSpecificationRun

> StreamingRun cancelStreamingSpecificationRun(cancelStreamingSpecificationRunRequest)

Cancel an active streaming run

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIcancelStreamingSpecificationRunRequest request = APIcancelStreamingSpecificationRunRequest.newBuilder()
                .runId(runId)
                .build();
            StreamingRun result = apiInstance.cancelStreamingSpecificationRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#cancelStreamingSpecificationRun");
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
| cancelStreamingSpecificationRunRequest | [**APIcancelStreamingSpecificationRunRequest**](StreamingSpecificationsApi.md#APIcancelStreamingSpecificationRunRequest)|-|-|

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

## cancelStreamingSpecificationRunWithHttpInfo

> ApiResponse<StreamingRun> cancelStreamingSpecificationRunWithHttpInfo(cancelStreamingSpecificationRunRequest)

Cancel an active streaming run

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIcancelStreamingSpecificationRunRequest request = APIcancelStreamingSpecificationRunRequest.newBuilder()
                .runId(runId)
                .build();
            ApiResponse<StreamingRun> response = apiInstance.cancelStreamingSpecificationRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#cancelStreamingSpecificationRun");
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
| cancelStreamingSpecificationRunRequest | [**APIcancelStreamingSpecificationRunRequest**](StreamingSpecificationsApi.md#APIcancelStreamingSpecificationRunRequest)|-|-|

### Return type

ApiResponse<[**StreamingRun**](StreamingRun.md)>


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


<a id="APIcancelStreamingSpecificationRunRequest"></a>
## APIcancelStreamingSpecificationRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## createStreamingSpecification

> StreamingSpecification createStreamingSpecification(createStreamingSpecificationRequest)

Create a streaming specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        String specName = "specName_example"; // String | User-facing specification name within the active project.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateStreamingSpecificationRequest request = APIcreateStreamingSpecificationRequest.newBuilder()
                .specName(specName)
                .body(body)
                .description(description)
                .idempotencyKey(idempotencyKey)
                .build();
            StreamingSpecification result = apiInstance.createStreamingSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#createStreamingSpecification");
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
| createStreamingSpecificationRequest | [**APIcreateStreamingSpecificationRequest**](StreamingSpecificationsApi.md#APIcreateStreamingSpecificationRequest)|-|-|

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

## createStreamingSpecificationWithHttpInfo

> ApiResponse<StreamingSpecification> createStreamingSpecificationWithHttpInfo(createStreamingSpecificationRequest)

Create a streaming specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        String specName = "specName_example"; // String | User-facing specification name within the active project.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateStreamingSpecificationRequest request = APIcreateStreamingSpecificationRequest.newBuilder()
                .specName(specName)
                .body(body)
                .description(description)
                .idempotencyKey(idempotencyKey)
                .build();
            ApiResponse<StreamingSpecification> response = apiInstance.createStreamingSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#createStreamingSpecification");
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
| createStreamingSpecificationRequest | [**APIcreateStreamingSpecificationRequest**](StreamingSpecificationsApi.md#APIcreateStreamingSpecificationRequest)|-|-|

### Return type

ApiResponse<[**StreamingSpecification**](StreamingSpecification.md)>


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


<a id="APIcreateStreamingSpecificationRequest"></a>
## APIcreateStreamingSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specName** | **String** | User-facing specification name within the active project. | |
| **body** | **String** |  | |
| **description** | **String** | Optional user-facing description stored with the asset. | [optional] |
| **idempotencyKey** | **UUID** | A caller-generated UUID retained for safe write retries where supported. | [optional] |



## deleteStreamingSpecification

> StreamingSpecification deleteStreamingSpecification(deleteStreamingSpecificationRequest)

Delete a streaming specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIdeleteStreamingSpecificationRequest request = APIdeleteStreamingSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            StreamingSpecification result = apiInstance.deleteStreamingSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#deleteStreamingSpecification");
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
| deleteStreamingSpecificationRequest | [**APIdeleteStreamingSpecificationRequest**](StreamingSpecificationsApi.md#APIdeleteStreamingSpecificationRequest)|-|-|

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

## deleteStreamingSpecificationWithHttpInfo

> ApiResponse<StreamingSpecification> deleteStreamingSpecificationWithHttpInfo(deleteStreamingSpecificationRequest)

Delete a streaming specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIdeleteStreamingSpecificationRequest request = APIdeleteStreamingSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            ApiResponse<StreamingSpecification> response = apiInstance.deleteStreamingSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#deleteStreamingSpecification");
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
| deleteStreamingSpecificationRequest | [**APIdeleteStreamingSpecificationRequest**](StreamingSpecificationsApi.md#APIdeleteStreamingSpecificationRequest)|-|-|

### Return type

ApiResponse<[**StreamingSpecification**](StreamingSpecification.md)>


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


<a id="APIdeleteStreamingSpecificationRequest"></a>
## APIdeleteStreamingSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |



## getStreamingCapabilities

> StreamingCapabilities getStreamingCapabilities()

Get streaming engine capabilities and enforced limits

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        try {
            StreamingCapabilities result = apiInstance.getStreamingCapabilities();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#getStreamingCapabilities");
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

## getStreamingCapabilitiesWithHttpInfo

> ApiResponse<StreamingCapabilities> getStreamingCapabilitiesWithHttpInfo()

Get streaming engine capabilities and enforced limits

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        try {
            ApiResponse<StreamingCapabilities> response = apiInstance.getStreamingCapabilitiesWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#getStreamingCapabilities");
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

ApiResponse<[**StreamingCapabilities**](StreamingCapabilities.md)>


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


## getStreamingSpecification

> StreamingSpecification getStreamingSpecification(getStreamingSpecificationRequest)

Get a streaming specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIgetStreamingSpecificationRequest request = APIgetStreamingSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            StreamingSpecification result = apiInstance.getStreamingSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#getStreamingSpecification");
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
| getStreamingSpecificationRequest | [**APIgetStreamingSpecificationRequest**](StreamingSpecificationsApi.md#APIgetStreamingSpecificationRequest)|-|-|

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

## getStreamingSpecificationWithHttpInfo

> ApiResponse<StreamingSpecification> getStreamingSpecificationWithHttpInfo(getStreamingSpecificationRequest)

Get a streaming specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIgetStreamingSpecificationRequest request = APIgetStreamingSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            ApiResponse<StreamingSpecification> response = apiInstance.getStreamingSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#getStreamingSpecification");
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
| getStreamingSpecificationRequest | [**APIgetStreamingSpecificationRequest**](StreamingSpecificationsApi.md#APIgetStreamingSpecificationRequest)|-|-|

### Return type

ApiResponse<[**StreamingSpecification**](StreamingSpecification.md)>


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


<a id="APIgetStreamingSpecificationRequest"></a>
## APIgetStreamingSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |



## getStreamingSpecificationRun

> StreamingRun getStreamingSpecificationRun(getStreamingSpecificationRunRequest)

Get streaming run state and bounded semantic evidence

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIgetStreamingSpecificationRunRequest request = APIgetStreamingSpecificationRunRequest.newBuilder()
                .runId(runId)
                .build();
            StreamingRun result = apiInstance.getStreamingSpecificationRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#getStreamingSpecificationRun");
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
| getStreamingSpecificationRunRequest | [**APIgetStreamingSpecificationRunRequest**](StreamingSpecificationsApi.md#APIgetStreamingSpecificationRunRequest)|-|-|

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

## getStreamingSpecificationRunWithHttpInfo

> ApiResponse<StreamingRun> getStreamingSpecificationRunWithHttpInfo(getStreamingSpecificationRunRequest)

Get streaming run state and bounded semantic evidence

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIgetStreamingSpecificationRunRequest request = APIgetStreamingSpecificationRunRequest.newBuilder()
                .runId(runId)
                .build();
            ApiResponse<StreamingRun> response = apiInstance.getStreamingSpecificationRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#getStreamingSpecificationRun");
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
| getStreamingSpecificationRunRequest | [**APIgetStreamingSpecificationRunRequest**](StreamingSpecificationsApi.md#APIgetStreamingSpecificationRunRequest)|-|-|

### Return type

ApiResponse<[**StreamingRun**](StreamingRun.md)>


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


<a id="APIgetStreamingSpecificationRunRequest"></a>
## APIgetStreamingSpecificationRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## getStreamingSpecificationRunTranscript

> StreamingTranscriptPage getStreamingSpecificationRunTranscript(getStreamingSpecificationRunTranscriptRequest)

Page a bounded streaming run transcript

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 100; // Integer |
        try {
            APIgetStreamingSpecificationRunTranscriptRequest request = APIgetStreamingSpecificationRunTranscriptRequest.newBuilder()
                .runId(runId)
                .page(page)
                .size(size)
                .build();
            StreamingTranscriptPage result = apiInstance.getStreamingSpecificationRunTranscript(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#getStreamingSpecificationRunTranscript");
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
| getStreamingSpecificationRunTranscriptRequest | [**APIgetStreamingSpecificationRunTranscriptRequest**](StreamingSpecificationsApi.md#APIgetStreamingSpecificationRunTranscriptRequest)|-|-|

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

## getStreamingSpecificationRunTranscriptWithHttpInfo

> ApiResponse<StreamingTranscriptPage> getStreamingSpecificationRunTranscriptWithHttpInfo(getStreamingSpecificationRunTranscriptRequest)

Page a bounded streaming run transcript

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 100; // Integer |
        try {
            APIgetStreamingSpecificationRunTranscriptRequest request = APIgetStreamingSpecificationRunTranscriptRequest.newBuilder()
                .runId(runId)
                .page(page)
                .size(size)
                .build();
            ApiResponse<StreamingTranscriptPage> response = apiInstance.getStreamingSpecificationRunTranscriptWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#getStreamingSpecificationRunTranscript");
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
| getStreamingSpecificationRunTranscriptRequest | [**APIgetStreamingSpecificationRunTranscriptRequest**](StreamingSpecificationsApi.md#APIgetStreamingSpecificationRunTranscriptRequest)|-|-|

### Return type

ApiResponse<[**StreamingTranscriptPage**](StreamingTranscriptPage.md)>


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


<a id="APIgetStreamingSpecificationRunTranscriptRequest"></a>
## APIgetStreamingSpecificationRunTranscriptRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** |  | [optional] [default to 100] |



## listStreamingSpecificationRuns

> StreamingRunPage listStreamingSpecificationRuns(listStreamingSpecificationRunsRequest)

List runs for a saved streaming specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIlistStreamingSpecificationRunsRequest request = APIlistStreamingSpecificationRunsRequest.newBuilder()
                .specId(specId)
                .page(page)
                .size(size)
                .build();
            StreamingRunPage result = apiInstance.listStreamingSpecificationRuns(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#listStreamingSpecificationRuns");
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
| listStreamingSpecificationRunsRequest | [**APIlistStreamingSpecificationRunsRequest**](StreamingSpecificationsApi.md#APIlistStreamingSpecificationRunsRequest)|-|-|

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

## listStreamingSpecificationRunsWithHttpInfo

> ApiResponse<StreamingRunPage> listStreamingSpecificationRunsWithHttpInfo(listStreamingSpecificationRunsRequest)

List runs for a saved streaming specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIlistStreamingSpecificationRunsRequest request = APIlistStreamingSpecificationRunsRequest.newBuilder()
                .specId(specId)
                .page(page)
                .size(size)
                .build();
            ApiResponse<StreamingRunPage> response = apiInstance.listStreamingSpecificationRunsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#listStreamingSpecificationRuns");
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
| listStreamingSpecificationRunsRequest | [**APIlistStreamingSpecificationRunsRequest**](StreamingSpecificationsApi.md#APIlistStreamingSpecificationRunsRequest)|-|-|

### Return type

ApiResponse<[**StreamingRunPage**](StreamingRunPage.md)>


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


<a id="APIlistStreamingSpecificationRunsRequest"></a>
## APIlistStreamingSpecificationRunsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |



## listStreamingSpecifications

> StreamingSpecificationPage listStreamingSpecifications(listStreamingSpecificationsRequest)

List streaming specifications

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        StreamingTransport transport = StreamingTransport.fromValue("WEBSOCKET"); // StreamingTransport | Filter by streaming transport.
        try {
            APIlistStreamingSpecificationsRequest request = APIlistStreamingSpecificationsRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .transport(transport)
                .build();
            StreamingSpecificationPage result = apiInstance.listStreamingSpecifications(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#listStreamingSpecifications");
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
| listStreamingSpecificationsRequest | [**APIlistStreamingSpecificationsRequest**](StreamingSpecificationsApi.md#APIlistStreamingSpecificationsRequest)|-|-|

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

## listStreamingSpecificationsWithHttpInfo

> ApiResponse<StreamingSpecificationPage> listStreamingSpecificationsWithHttpInfo(listStreamingSpecificationsRequest)

List streaming specifications

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        StreamingTransport transport = StreamingTransport.fromValue("WEBSOCKET"); // StreamingTransport | Filter by streaming transport.
        try {
            APIlistStreamingSpecificationsRequest request = APIlistStreamingSpecificationsRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .transport(transport)
                .build();
            ApiResponse<StreamingSpecificationPage> response = apiInstance.listStreamingSpecificationsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#listStreamingSpecifications");
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
| listStreamingSpecificationsRequest | [**APIlistStreamingSpecificationsRequest**](StreamingSpecificationsApi.md#APIlistStreamingSpecificationsRequest)|-|-|

### Return type

ApiResponse<[**StreamingSpecificationPage**](StreamingSpecificationPage.md)>


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


<a id="APIlistStreamingSpecificationsRequest"></a>
## APIlistStreamingSpecificationsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **String** | Case-insensitive server-side search within the active project. | [optional] |
| **transport** | [**StreamingTransport**](.md) | Filter by streaming transport. | [optional] [enum: WEBSOCKET, SSE, GRPC, MQTT] |



## previewStreamingSpecificationRecovery

> SpecificationRecoveryPreview previewStreamingSpecificationRecovery(previewStreamingSpecificationRecoveryRequest)

Preview restoring a Streaming specification version

Compares the current specification with the exact DSL snapshot retained by a completed PASS or FAIL run. No expectations are regenerated.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIpreviewStreamingSpecificationRecoveryRequest request = APIpreviewStreamingSpecificationRecoveryRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            SpecificationRecoveryPreview result = apiInstance.previewStreamingSpecificationRecovery(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#previewStreamingSpecificationRecovery");
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
| previewStreamingSpecificationRecoveryRequest | [**APIpreviewStreamingSpecificationRecoveryRequest**](StreamingSpecificationsApi.md#APIpreviewStreamingSpecificationRecoveryRequest)|-|-|

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

## previewStreamingSpecificationRecoveryWithHttpInfo

> ApiResponse<SpecificationRecoveryPreview> previewStreamingSpecificationRecoveryWithHttpInfo(previewStreamingSpecificationRecoveryRequest)

Preview restoring a Streaming specification version

Compares the current specification with the exact DSL snapshot retained by a completed PASS or FAIL run. No expectations are regenerated.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIpreviewStreamingSpecificationRecoveryRequest request = APIpreviewStreamingSpecificationRecoveryRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            ApiResponse<SpecificationRecoveryPreview> response = apiInstance.previewStreamingSpecificationRecoveryWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#previewStreamingSpecificationRecovery");
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
| previewStreamingSpecificationRecoveryRequest | [**APIpreviewStreamingSpecificationRecoveryRequest**](StreamingSpecificationsApi.md#APIpreviewStreamingSpecificationRecoveryRequest)|-|-|

### Return type

ApiResponse<[**SpecificationRecoveryPreview**](SpecificationRecoveryPreview.md)>


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


<a id="APIpreviewStreamingSpecificationRecoveryRequest"></a>
## APIpreviewStreamingSpecificationRecoveryRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## restoreStreamingSpecificationFromRun

> StreamingSpecification restoreStreamingSpecificationFromRun(restoreStreamingSpecificationFromRunRequest)

Restore a Streaming specification version

Replaces only the current DSL content with the exact snapshot retained by a completed PASS or FAIL run. The specification id, name, description, and stable identity are preserved.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIrestoreStreamingSpecificationFromRunRequest request = APIrestoreStreamingSpecificationFromRunRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            StreamingSpecification result = apiInstance.restoreStreamingSpecificationFromRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#restoreStreamingSpecificationFromRun");
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
| restoreStreamingSpecificationFromRunRequest | [**APIrestoreStreamingSpecificationFromRunRequest**](StreamingSpecificationsApi.md#APIrestoreStreamingSpecificationFromRunRequest)|-|-|

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

## restoreStreamingSpecificationFromRunWithHttpInfo

> ApiResponse<StreamingSpecification> restoreStreamingSpecificationFromRunWithHttpInfo(restoreStreamingSpecificationFromRunRequest)

Restore a Streaming specification version

Replaces only the current DSL content with the exact snapshot retained by a completed PASS or FAIL run. The specification id, name, description, and stable identity are preserved.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIrestoreStreamingSpecificationFromRunRequest request = APIrestoreStreamingSpecificationFromRunRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            ApiResponse<StreamingSpecification> response = apiInstance.restoreStreamingSpecificationFromRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#restoreStreamingSpecificationFromRun");
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
| restoreStreamingSpecificationFromRunRequest | [**APIrestoreStreamingSpecificationFromRunRequest**](StreamingSpecificationsApi.md#APIrestoreStreamingSpecificationFromRunRequest)|-|-|

### Return type

ApiResponse<[**StreamingSpecification**](StreamingSpecification.md)>


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


<a id="APIrestoreStreamingSpecificationFromRunRequest"></a>
## APIrestoreStreamingSpecificationFromRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## runStreamingSpecification

> StreamingRunAccepted runStreamingSpecification(runStreamingSpecificationRequest)

Queue a saved streaming specification run

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIrunStreamingSpecificationRequest request = APIrunStreamingSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            StreamingRunAccepted result = apiInstance.runStreamingSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#runStreamingSpecification");
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
| runStreamingSpecificationRequest | [**APIrunStreamingSpecificationRequest**](StreamingSpecificationsApi.md#APIrunStreamingSpecificationRequest)|-|-|

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

## runStreamingSpecificationWithHttpInfo

> ApiResponse<StreamingRunAccepted> runStreamingSpecificationWithHttpInfo(runStreamingSpecificationRequest)

Queue a saved streaming specification run

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIrunStreamingSpecificationRequest request = APIrunStreamingSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            ApiResponse<StreamingRunAccepted> response = apiInstance.runStreamingSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#runStreamingSpecification");
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
| runStreamingSpecificationRequest | [**APIrunStreamingSpecificationRequest**](StreamingSpecificationsApi.md#APIrunStreamingSpecificationRequest)|-|-|

### Return type

ApiResponse<[**StreamingRunAccepted**](StreamingRunAccepted.md)>


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


<a id="APIrunStreamingSpecificationRequest"></a>
## APIrunStreamingSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |



## runStreamingSpecificationDraft

> StreamingRunAccepted runStreamingSpecificationDraft(runStreamingSpecificationDraftRequest)

Queue a bounded streaming specification draft run

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        String body = "body_example"; // String |
        String specName = "specName_example"; // String |
        try {
            APIrunStreamingSpecificationDraftRequest request = APIrunStreamingSpecificationDraftRequest.newBuilder()
                .body(body)
                .specName(specName)
                .build();
            StreamingRunAccepted result = apiInstance.runStreamingSpecificationDraft(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#runStreamingSpecificationDraft");
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
| runStreamingSpecificationDraftRequest | [**APIrunStreamingSpecificationDraftRequest**](StreamingSpecificationsApi.md#APIrunStreamingSpecificationDraftRequest)|-|-|

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

## runStreamingSpecificationDraftWithHttpInfo

> ApiResponse<StreamingRunAccepted> runStreamingSpecificationDraftWithHttpInfo(runStreamingSpecificationDraftRequest)

Queue a bounded streaming specification draft run

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        String body = "body_example"; // String |
        String specName = "specName_example"; // String |
        try {
            APIrunStreamingSpecificationDraftRequest request = APIrunStreamingSpecificationDraftRequest.newBuilder()
                .body(body)
                .specName(specName)
                .build();
            ApiResponse<StreamingRunAccepted> response = apiInstance.runStreamingSpecificationDraftWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#runStreamingSpecificationDraft");
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
| runStreamingSpecificationDraftRequest | [**APIrunStreamingSpecificationDraftRequest**](StreamingSpecificationsApi.md#APIrunStreamingSpecificationDraftRequest)|-|-|

### Return type

ApiResponse<[**StreamingRunAccepted**](StreamingRunAccepted.md)>


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


<a id="APIrunStreamingSpecificationDraftRequest"></a>
## APIrunStreamingSpecificationDraftRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **body** | **String** |  | |
| **specName** | **String** |  | [optional] |



## testStreamingSpecificationRecoveryVersion

> StreamingRun testStreamingSpecificationRecoveryVersion(testStreamingSpecificationRecoveryVersionRequest)

Test a previous Streaming specification version

Executes the exact DSL snapshot retained by the selected completed PASS or FAIL run against the current API without changing the saved specification.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APItestStreamingSpecificationRecoveryVersionRequest request = APItestStreamingSpecificationRecoveryVersionRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            StreamingRun result = apiInstance.testStreamingSpecificationRecoveryVersion(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#testStreamingSpecificationRecoveryVersion");
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
| testStreamingSpecificationRecoveryVersionRequest | [**APItestStreamingSpecificationRecoveryVersionRequest**](StreamingSpecificationsApi.md#APItestStreamingSpecificationRecoveryVersionRequest)|-|-|

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

## testStreamingSpecificationRecoveryVersionWithHttpInfo

> ApiResponse<StreamingRun> testStreamingSpecificationRecoveryVersionWithHttpInfo(testStreamingSpecificationRecoveryVersionRequest)

Test a previous Streaming specification version

Executes the exact DSL snapshot retained by the selected completed PASS or FAIL run against the current API without changing the saved specification.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APItestStreamingSpecificationRecoveryVersionRequest request = APItestStreamingSpecificationRecoveryVersionRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            ApiResponse<StreamingRun> response = apiInstance.testStreamingSpecificationRecoveryVersionWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#testStreamingSpecificationRecoveryVersion");
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
| testStreamingSpecificationRecoveryVersionRequest | [**APItestStreamingSpecificationRecoveryVersionRequest**](StreamingSpecificationsApi.md#APItestStreamingSpecificationRecoveryVersionRequest)|-|-|

### Return type

ApiResponse<[**StreamingRun**](StreamingRun.md)>


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


<a id="APItestStreamingSpecificationRecoveryVersionRequest"></a>
## APItestStreamingSpecificationRecoveryVersionRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## updateStreamingSpecification

> StreamingSpecification updateStreamingSpecification(updateStreamingSpecificationRequest)

Replace a streaming specification definition

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        try {
            APIupdateStreamingSpecificationRequest request = APIupdateStreamingSpecificationRequest.newBuilder()
                .specId(specId)
                .body(body)
                .description(description)
                .build();
            StreamingSpecification result = apiInstance.updateStreamingSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#updateStreamingSpecification");
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
| updateStreamingSpecificationRequest | [**APIupdateStreamingSpecificationRequest**](StreamingSpecificationsApi.md#APIupdateStreamingSpecificationRequest)|-|-|

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

## updateStreamingSpecificationWithHttpInfo

> ApiResponse<StreamingSpecification> updateStreamingSpecificationWithHttpInfo(updateStreamingSpecificationRequest)

Replace a streaming specification definition

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        try {
            APIupdateStreamingSpecificationRequest request = APIupdateStreamingSpecificationRequest.newBuilder()
                .specId(specId)
                .body(body)
                .description(description)
                .build();
            ApiResponse<StreamingSpecification> response = apiInstance.updateStreamingSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#updateStreamingSpecification");
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
| updateStreamingSpecificationRequest | [**APIupdateStreamingSpecificationRequest**](StreamingSpecificationsApi.md#APIupdateStreamingSpecificationRequest)|-|-|

### Return type

ApiResponse<[**StreamingSpecification**](StreamingSpecification.md)>


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


<a id="APIupdateStreamingSpecificationRequest"></a>
## APIupdateStreamingSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **body** | **String** |  | |
| **description** | **String** | Optional user-facing description stored with the asset. | [optional] |



## validateStreamingSpecificationDraft

> StreamingDraftValidation validateStreamingSpecificationDraft(validateStreamingSpecificationDraftRequest)

Validate and detect the transport of a streaming specification draft

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        String body = "body_example"; // String |
        try {
            APIvalidateStreamingSpecificationDraftRequest request = APIvalidateStreamingSpecificationDraftRequest.newBuilder()
                .body(body)
                .build();
            StreamingDraftValidation result = apiInstance.validateStreamingSpecificationDraft(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#validateStreamingSpecificationDraft");
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
| validateStreamingSpecificationDraftRequest | [**APIvalidateStreamingSpecificationDraftRequest**](StreamingSpecificationsApi.md#APIvalidateStreamingSpecificationDraftRequest)|-|-|

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

## validateStreamingSpecificationDraftWithHttpInfo

> ApiResponse<StreamingDraftValidation> validateStreamingSpecificationDraftWithHttpInfo(validateStreamingSpecificationDraftRequest)

Validate and detect the transport of a streaming specification draft

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.StreamingSpecificationsApi;
import software.ste.sdk.generated.api.StreamingSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        StreamingSpecificationsApi apiInstance = new StreamingSpecificationsApi(defaultClient);
        String body = "body_example"; // String |
        try {
            APIvalidateStreamingSpecificationDraftRequest request = APIvalidateStreamingSpecificationDraftRequest.newBuilder()
                .body(body)
                .build();
            ApiResponse<StreamingDraftValidation> response = apiInstance.validateStreamingSpecificationDraftWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling StreamingSpecificationsApi#validateStreamingSpecificationDraft");
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
| validateStreamingSpecificationDraftRequest | [**APIvalidateStreamingSpecificationDraftRequest**](StreamingSpecificationsApi.md#APIvalidateStreamingSpecificationDraftRequest)|-|-|

### Return type

ApiResponse<[**StreamingDraftValidation**](StreamingDraftValidation.md)>


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


<a id="APIvalidateStreamingSpecificationDraftRequest"></a>
## APIvalidateStreamingSpecificationDraftRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **body** | **String** |  | |
