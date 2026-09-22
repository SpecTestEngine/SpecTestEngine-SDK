# RestSpecificationsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**captureRestSpecificationAttachmentVisualDiff**](RestSpecificationsApi.md#captureRestSpecificationAttachmentVisualDiff) | **POST** /test/rest-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed REST attachment assertion |
| [**captureRestSpecificationAttachmentVisualDiffWithHttpInfo**](RestSpecificationsApi.md#captureRestSpecificationAttachmentVisualDiffWithHttpInfo) | **POST** /test/rest-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed REST attachment assertion |
| [**createRestSpecification**](RestSpecificationsApi.md#createRestSpecification) | **POST** /test/rest-spec/create | Create a REST specification |
| [**createRestSpecificationWithHttpInfo**](RestSpecificationsApi.md#createRestSpecificationWithHttpInfo) | **POST** /test/rest-spec/create | Create a REST specification |
| [**deleteRestSpecification**](RestSpecificationsApi.md#deleteRestSpecification) | **DELETE** /test/rest-spec/by-id | Delete a REST specification |
| [**deleteRestSpecificationWithHttpInfo**](RestSpecificationsApi.md#deleteRestSpecificationWithHttpInfo) | **DELETE** /test/rest-spec/by-id | Delete a REST specification |
| [**getRestSpecification**](RestSpecificationsApi.md#getRestSpecification) | **GET** /test/rest-spec/by-id | Get a REST specification |
| [**getRestSpecificationWithHttpInfo**](RestSpecificationsApi.md#getRestSpecificationWithHttpInfo) | **GET** /test/rest-spec/by-id | Get a REST specification |
| [**getRestSpecificationRun**](RestSpecificationsApi.md#getRestSpecificationRun) | **GET** /test/rest-spec/run/history/by-run-id/{runId} | Get saved REST run evidence |
| [**getRestSpecificationRunWithHttpInfo**](RestSpecificationsApi.md#getRestSpecificationRunWithHttpInfo) | **GET** /test/rest-spec/run/history/by-run-id/{runId} | Get saved REST run evidence |
| [**listRestSpecificationRuns**](RestSpecificationsApi.md#listRestSpecificationRuns) | **GET** /test/rest-spec/run/page/by-spec-id/{specId} | List saved REST runs |
| [**listRestSpecificationRunsWithHttpInfo**](RestSpecificationsApi.md#listRestSpecificationRunsWithHttpInfo) | **GET** /test/rest-spec/run/page/by-spec-id/{specId} | List saved REST runs |
| [**listRestSpecifications**](RestSpecificationsApi.md#listRestSpecifications) | **GET** /test/rest-spec/page | List REST specifications |
| [**listRestSpecificationsWithHttpInfo**](RestSpecificationsApi.md#listRestSpecificationsWithHttpInfo) | **GET** /test/rest-spec/page | List REST specifications |
| [**previewRestSpecificationRecovery**](RestSpecificationsApi.md#previewRestSpecificationRecovery) | **POST** /test/rest-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a REST specification version |
| [**previewRestSpecificationRecoveryWithHttpInfo**](RestSpecificationsApi.md#previewRestSpecificationRecoveryWithHttpInfo) | **POST** /test/rest-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a REST specification version |
| [**restoreRestSpecificationFromRun**](RestSpecificationsApi.md#restoreRestSpecificationFromRun) | **PUT** /test/rest-spec/recovery/{specId}/from-run/{runId}/restore | Restore a REST specification version |
| [**restoreRestSpecificationFromRunWithHttpInfo**](RestSpecificationsApi.md#restoreRestSpecificationFromRunWithHttpInfo) | **PUT** /test/rest-spec/recovery/{specId}/from-run/{runId}/restore | Restore a REST specification version |
| [**runRestSpecification**](RestSpecificationsApi.md#runRestSpecification) | **POST** /test/rest-spec/run/by-id | Run a saved REST specification |
| [**runRestSpecificationWithHttpInfo**](RestSpecificationsApi.md#runRestSpecificationWithHttpInfo) | **POST** /test/rest-spec/run/by-id | Run a saved REST specification |
| [**testRestSpecificationRecoveryVersion**](RestSpecificationsApi.md#testRestSpecificationRecoveryVersion) | **POST** /test/rest-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous REST specification version |
| [**testRestSpecificationRecoveryVersionWithHttpInfo**](RestSpecificationsApi.md#testRestSpecificationRecoveryVersionWithHttpInfo) | **POST** /test/rest-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous REST specification version |
| [**updateRestSpecification**](RestSpecificationsApi.md#updateRestSpecification) | **PUT** /test/rest-spec/by-id | Replace a REST specification definition |
| [**updateRestSpecificationWithHttpInfo**](RestSpecificationsApi.md#updateRestSpecificationWithHttpInfo) | **PUT** /test/rest-spec/by-id | Replace a REST specification definition |



## captureRestSpecificationAttachmentVisualDiff

> SpecificationRun captureRestSpecificationAttachmentVisualDiff(captureRestSpecificationAttachmentVisualDiffRequest)

Create a visual diff from a failed REST attachment assertion

Explicitly reruns the saved REST specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status; no visual-diff fallback changes the test result.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        DocumentVisualDiffCaptureRunRequest documentVisualDiffCaptureRunRequest = new DocumentVisualDiffCaptureRunRequest(); // DocumentVisualDiffCaptureRunRequest |
        try {
            APIcaptureRestSpecificationAttachmentVisualDiffRequest request = APIcaptureRestSpecificationAttachmentVisualDiffRequest.newBuilder()
                .specId(specId)
                .documentVisualDiffCaptureRunRequest(documentVisualDiffCaptureRunRequest)
                .build();
            SpecificationRun result = apiInstance.captureRestSpecificationAttachmentVisualDiff(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#captureRestSpecificationAttachmentVisualDiff");
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
| captureRestSpecificationAttachmentVisualDiffRequest | [**APIcaptureRestSpecificationAttachmentVisualDiffRequest**](RestSpecificationsApi.md#APIcaptureRestSpecificationAttachmentVisualDiffRequest)|-|-|

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

## captureRestSpecificationAttachmentVisualDiffWithHttpInfo

> ApiResponse<SpecificationRun> captureRestSpecificationAttachmentVisualDiffWithHttpInfo(captureRestSpecificationAttachmentVisualDiffRequest)

Create a visual diff from a failed REST attachment assertion

Explicitly reruns the saved REST specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status; no visual-diff fallback changes the test result.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        DocumentVisualDiffCaptureRunRequest documentVisualDiffCaptureRunRequest = new DocumentVisualDiffCaptureRunRequest(); // DocumentVisualDiffCaptureRunRequest |
        try {
            APIcaptureRestSpecificationAttachmentVisualDiffRequest request = APIcaptureRestSpecificationAttachmentVisualDiffRequest.newBuilder()
                .specId(specId)
                .documentVisualDiffCaptureRunRequest(documentVisualDiffCaptureRunRequest)
                .build();
            ApiResponse<SpecificationRun> response = apiInstance.captureRestSpecificationAttachmentVisualDiffWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#captureRestSpecificationAttachmentVisualDiff");
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
| captureRestSpecificationAttachmentVisualDiffRequest | [**APIcaptureRestSpecificationAttachmentVisualDiffRequest**](RestSpecificationsApi.md#APIcaptureRestSpecificationAttachmentVisualDiffRequest)|-|-|

### Return type

ApiResponse<[**SpecificationRun**](SpecificationRun.md)>


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


<a id="APIcaptureRestSpecificationAttachmentVisualDiffRequest"></a>
## APIcaptureRestSpecificationAttachmentVisualDiffRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **documentVisualDiffCaptureRunRequest** | [**DocumentVisualDiffCaptureRunRequest**](DocumentVisualDiffCaptureRunRequest.md) |  | |



## createRestSpecification

> Specification createRestSpecification(createRestSpecificationRequest)

Create a REST specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        String specName = "specName_example"; // String | User-facing specification name within the active project.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateRestSpecificationRequest request = APIcreateRestSpecificationRequest.newBuilder()
                .specName(specName)
                .body(body)
                .description(description)
                .idempotencyKey(idempotencyKey)
                .build();
            Specification result = apiInstance.createRestSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#createRestSpecification");
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
| createRestSpecificationRequest | [**APIcreateRestSpecificationRequest**](RestSpecificationsApi.md#APIcreateRestSpecificationRequest)|-|-|

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

## createRestSpecificationWithHttpInfo

> ApiResponse<Specification> createRestSpecificationWithHttpInfo(createRestSpecificationRequest)

Create a REST specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        String specName = "specName_example"; // String | User-facing specification name within the active project.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateRestSpecificationRequest request = APIcreateRestSpecificationRequest.newBuilder()
                .specName(specName)
                .body(body)
                .description(description)
                .idempotencyKey(idempotencyKey)
                .build();
            ApiResponse<Specification> response = apiInstance.createRestSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#createRestSpecification");
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
| createRestSpecificationRequest | [**APIcreateRestSpecificationRequest**](RestSpecificationsApi.md#APIcreateRestSpecificationRequest)|-|-|

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
| **200** | The stored REST specification. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcreateRestSpecificationRequest"></a>
## APIcreateRestSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specName** | **String** | User-facing specification name within the active project. | |
| **body** | **String** |  | |
| **description** | **String** | Optional user-facing description stored with the asset. | [optional] |
| **idempotencyKey** | **UUID** | A caller-generated UUID retained for safe write retries where supported. | [optional] |



## deleteRestSpecification

> Specification deleteRestSpecification(deleteRestSpecificationRequest)

Delete a REST specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIdeleteRestSpecificationRequest request = APIdeleteRestSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            Specification result = apiInstance.deleteRestSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#deleteRestSpecification");
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
| deleteRestSpecificationRequest | [**APIdeleteRestSpecificationRequest**](RestSpecificationsApi.md#APIdeleteRestSpecificationRequest)|-|-|

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

## deleteRestSpecificationWithHttpInfo

> ApiResponse<Specification> deleteRestSpecificationWithHttpInfo(deleteRestSpecificationRequest)

Delete a REST specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIdeleteRestSpecificationRequest request = APIdeleteRestSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            ApiResponse<Specification> response = apiInstance.deleteRestSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#deleteRestSpecification");
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
| deleteRestSpecificationRequest | [**APIdeleteRestSpecificationRequest**](RestSpecificationsApi.md#APIdeleteRestSpecificationRequest)|-|-|

### Return type

ApiResponse<[**Specification**](Specification.md)>


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


<a id="APIdeleteRestSpecificationRequest"></a>
## APIdeleteRestSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |



## getRestSpecification

> Specification getRestSpecification(getRestSpecificationRequest)

Get a REST specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIgetRestSpecificationRequest request = APIgetRestSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            Specification result = apiInstance.getRestSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#getRestSpecification");
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
| getRestSpecificationRequest | [**APIgetRestSpecificationRequest**](RestSpecificationsApi.md#APIgetRestSpecificationRequest)|-|-|

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

## getRestSpecificationWithHttpInfo

> ApiResponse<Specification> getRestSpecificationWithHttpInfo(getRestSpecificationRequest)

Get a REST specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIgetRestSpecificationRequest request = APIgetRestSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            ApiResponse<Specification> response = apiInstance.getRestSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#getRestSpecification");
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
| getRestSpecificationRequest | [**APIgetRestSpecificationRequest**](RestSpecificationsApi.md#APIgetRestSpecificationRequest)|-|-|

### Return type

ApiResponse<[**Specification**](Specification.md)>


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


<a id="APIgetRestSpecificationRequest"></a>
## APIgetRestSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |



## getRestSpecificationRun

> SpecificationRun getRestSpecificationRun(getRestSpecificationRunRequest)

Get saved REST run evidence

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIgetRestSpecificationRunRequest request = APIgetRestSpecificationRunRequest.newBuilder()
                .runId(runId)
                .build();
            SpecificationRun result = apiInstance.getRestSpecificationRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#getRestSpecificationRun");
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
| getRestSpecificationRunRequest | [**APIgetRestSpecificationRunRequest**](RestSpecificationsApi.md#APIgetRestSpecificationRunRequest)|-|-|

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

## getRestSpecificationRunWithHttpInfo

> ApiResponse<SpecificationRun> getRestSpecificationRunWithHttpInfo(getRestSpecificationRunRequest)

Get saved REST run evidence

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIgetRestSpecificationRunRequest request = APIgetRestSpecificationRunRequest.newBuilder()
                .runId(runId)
                .build();
            ApiResponse<SpecificationRun> response = apiInstance.getRestSpecificationRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#getRestSpecificationRun");
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
| getRestSpecificationRunRequest | [**APIgetRestSpecificationRunRequest**](RestSpecificationsApi.md#APIgetRestSpecificationRunRequest)|-|-|

### Return type

ApiResponse<[**SpecificationRun**](SpecificationRun.md)>


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


<a id="APIgetRestSpecificationRunRequest"></a>
## APIgetRestSpecificationRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## listRestSpecificationRuns

> SpecificationRunPage listRestSpecificationRuns(listRestSpecificationRunsRequest)

List saved REST runs

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIlistRestSpecificationRunsRequest request = APIlistRestSpecificationRunsRequest.newBuilder()
                .specId(specId)
                .page(page)
                .size(size)
                .build();
            SpecificationRunPage result = apiInstance.listRestSpecificationRuns(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#listRestSpecificationRuns");
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
| listRestSpecificationRunsRequest | [**APIlistRestSpecificationRunsRequest**](RestSpecificationsApi.md#APIlistRestSpecificationRunsRequest)|-|-|

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

## listRestSpecificationRunsWithHttpInfo

> ApiResponse<SpecificationRunPage> listRestSpecificationRunsWithHttpInfo(listRestSpecificationRunsRequest)

List saved REST runs

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIlistRestSpecificationRunsRequest request = APIlistRestSpecificationRunsRequest.newBuilder()
                .specId(specId)
                .page(page)
                .size(size)
                .build();
            ApiResponse<SpecificationRunPage> response = apiInstance.listRestSpecificationRunsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#listRestSpecificationRuns");
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
| listRestSpecificationRunsRequest | [**APIlistRestSpecificationRunsRequest**](RestSpecificationsApi.md#APIlistRestSpecificationRunsRequest)|-|-|

### Return type

ApiResponse<[**SpecificationRunPage**](SpecificationRunPage.md)>


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


<a id="APIlistRestSpecificationRunsRequest"></a>
## APIlistRestSpecificationRunsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |



## listRestSpecifications

> SpecificationPage listRestSpecifications(listRestSpecificationsRequest)

List REST specifications

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistRestSpecificationsRequest request = APIlistRestSpecificationsRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .build();
            SpecificationPage result = apiInstance.listRestSpecifications(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#listRestSpecifications");
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
| listRestSpecificationsRequest | [**APIlistRestSpecificationsRequest**](RestSpecificationsApi.md#APIlistRestSpecificationsRequest)|-|-|

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

## listRestSpecificationsWithHttpInfo

> ApiResponse<SpecificationPage> listRestSpecificationsWithHttpInfo(listRestSpecificationsRequest)

List REST specifications

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistRestSpecificationsRequest request = APIlistRestSpecificationsRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .build();
            ApiResponse<SpecificationPage> response = apiInstance.listRestSpecificationsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#listRestSpecifications");
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
| listRestSpecificationsRequest | [**APIlistRestSpecificationsRequest**](RestSpecificationsApi.md#APIlistRestSpecificationsRequest)|-|-|

### Return type

ApiResponse<[**SpecificationPage**](SpecificationPage.md)>


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


<a id="APIlistRestSpecificationsRequest"></a>
## APIlistRestSpecificationsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **String** | Case-insensitive server-side search within the active project. | [optional] |



## previewRestSpecificationRecovery

> SpecificationRecoveryPreview previewRestSpecificationRecovery(previewRestSpecificationRecoveryRequest)

Preview restoring a REST specification version

Compares the current specification with the exact DSL snapshot retained by a completed PASS or FAIL run. No expectations are regenerated.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIpreviewRestSpecificationRecoveryRequest request = APIpreviewRestSpecificationRecoveryRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            SpecificationRecoveryPreview result = apiInstance.previewRestSpecificationRecovery(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#previewRestSpecificationRecovery");
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
| previewRestSpecificationRecoveryRequest | [**APIpreviewRestSpecificationRecoveryRequest**](RestSpecificationsApi.md#APIpreviewRestSpecificationRecoveryRequest)|-|-|

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

## previewRestSpecificationRecoveryWithHttpInfo

> ApiResponse<SpecificationRecoveryPreview> previewRestSpecificationRecoveryWithHttpInfo(previewRestSpecificationRecoveryRequest)

Preview restoring a REST specification version

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
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIpreviewRestSpecificationRecoveryRequest request = APIpreviewRestSpecificationRecoveryRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            ApiResponse<SpecificationRecoveryPreview> response = apiInstance.previewRestSpecificationRecoveryWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#previewRestSpecificationRecovery");
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
| previewRestSpecificationRecoveryRequest | [**APIpreviewRestSpecificationRecoveryRequest**](RestSpecificationsApi.md#APIpreviewRestSpecificationRecoveryRequest)|-|-|

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


<a id="APIpreviewRestSpecificationRecoveryRequest"></a>
## APIpreviewRestSpecificationRecoveryRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## restoreRestSpecificationFromRun

> Specification restoreRestSpecificationFromRun(restoreRestSpecificationFromRunRequest)

Restore a REST specification version

Replaces only the current DSL content with the exact snapshot retained by a completed PASS or FAIL run. The specification id, name, description, and stable identity are preserved.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIrestoreRestSpecificationFromRunRequest request = APIrestoreRestSpecificationFromRunRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            Specification result = apiInstance.restoreRestSpecificationFromRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#restoreRestSpecificationFromRun");
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
| restoreRestSpecificationFromRunRequest | [**APIrestoreRestSpecificationFromRunRequest**](RestSpecificationsApi.md#APIrestoreRestSpecificationFromRunRequest)|-|-|

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

## restoreRestSpecificationFromRunWithHttpInfo

> ApiResponse<Specification> restoreRestSpecificationFromRunWithHttpInfo(restoreRestSpecificationFromRunRequest)

Restore a REST specification version

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
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIrestoreRestSpecificationFromRunRequest request = APIrestoreRestSpecificationFromRunRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            ApiResponse<Specification> response = apiInstance.restoreRestSpecificationFromRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#restoreRestSpecificationFromRun");
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
| restoreRestSpecificationFromRunRequest | [**APIrestoreRestSpecificationFromRunRequest**](RestSpecificationsApi.md#APIrestoreRestSpecificationFromRunRequest)|-|-|

### Return type

ApiResponse<[**Specification**](Specification.md)>


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


<a id="APIrestoreRestSpecificationFromRunRequest"></a>
## APIrestoreRestSpecificationFromRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## runRestSpecification

> SpecificationRun runRestSpecification(runRestSpecificationRequest)

Run a saved REST specification

Starts and completes one synchronous specification execution.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIrunRestSpecificationRequest request = APIrunRestSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            SpecificationRun result = apiInstance.runRestSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#runRestSpecification");
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
| runRestSpecificationRequest | [**APIrunRestSpecificationRequest**](RestSpecificationsApi.md#APIrunRestSpecificationRequest)|-|-|

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

## runRestSpecificationWithHttpInfo

> ApiResponse<SpecificationRun> runRestSpecificationWithHttpInfo(runRestSpecificationRequest)

Run a saved REST specification

Starts and completes one synchronous specification execution.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIrunRestSpecificationRequest request = APIrunRestSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            ApiResponse<SpecificationRun> response = apiInstance.runRestSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#runRestSpecification");
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
| runRestSpecificationRequest | [**APIrunRestSpecificationRequest**](RestSpecificationsApi.md#APIrunRestSpecificationRequest)|-|-|

### Return type

ApiResponse<[**SpecificationRun**](SpecificationRun.md)>


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


<a id="APIrunRestSpecificationRequest"></a>
## APIrunRestSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |



## testRestSpecificationRecoveryVersion

> SpecificationRun testRestSpecificationRecoveryVersion(testRestSpecificationRecoveryVersionRequest)

Test a previous REST specification version

Executes the exact DSL snapshot retained by the selected completed PASS or FAIL run against the current API without changing the saved specification.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APItestRestSpecificationRecoveryVersionRequest request = APItestRestSpecificationRecoveryVersionRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            SpecificationRun result = apiInstance.testRestSpecificationRecoveryVersion(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#testRestSpecificationRecoveryVersion");
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
| testRestSpecificationRecoveryVersionRequest | [**APItestRestSpecificationRecoveryVersionRequest**](RestSpecificationsApi.md#APItestRestSpecificationRecoveryVersionRequest)|-|-|

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

## testRestSpecificationRecoveryVersionWithHttpInfo

> ApiResponse<SpecificationRun> testRestSpecificationRecoveryVersionWithHttpInfo(testRestSpecificationRecoveryVersionRequest)

Test a previous REST specification version

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
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APItestRestSpecificationRecoveryVersionRequest request = APItestRestSpecificationRecoveryVersionRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            ApiResponse<SpecificationRun> response = apiInstance.testRestSpecificationRecoveryVersionWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#testRestSpecificationRecoveryVersion");
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
| testRestSpecificationRecoveryVersionRequest | [**APItestRestSpecificationRecoveryVersionRequest**](RestSpecificationsApi.md#APItestRestSpecificationRecoveryVersionRequest)|-|-|

### Return type

ApiResponse<[**SpecificationRun**](SpecificationRun.md)>


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


<a id="APItestRestSpecificationRecoveryVersionRequest"></a>
## APItestRestSpecificationRecoveryVersionRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## updateRestSpecification

> Specification updateRestSpecification(updateRestSpecificationRequest)

Replace a REST specification definition

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        try {
            APIupdateRestSpecificationRequest request = APIupdateRestSpecificationRequest.newBuilder()
                .specId(specId)
                .body(body)
                .description(description)
                .build();
            Specification result = apiInstance.updateRestSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#updateRestSpecification");
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
| updateRestSpecificationRequest | [**APIupdateRestSpecificationRequest**](RestSpecificationsApi.md#APIupdateRestSpecificationRequest)|-|-|

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

## updateRestSpecificationWithHttpInfo

> ApiResponse<Specification> updateRestSpecificationWithHttpInfo(updateRestSpecificationRequest)

Replace a REST specification definition

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.RestSpecificationsApi;
import software.ste.sdk.generated.api.RestSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        RestSpecificationsApi apiInstance = new RestSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        try {
            APIupdateRestSpecificationRequest request = APIupdateRestSpecificationRequest.newBuilder()
                .specId(specId)
                .body(body)
                .description(description)
                .build();
            ApiResponse<Specification> response = apiInstance.updateRestSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RestSpecificationsApi#updateRestSpecification");
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
| updateRestSpecificationRequest | [**APIupdateRestSpecificationRequest**](RestSpecificationsApi.md#APIupdateRestSpecificationRequest)|-|-|

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
| **200** | The updated REST specification. |  -  |
| **0** | The request failed. |  -  |


<a id="APIupdateRestSpecificationRequest"></a>
## APIupdateRestSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **body** | **String** |  | |
| **description** | **String** | Optional user-facing description stored with the asset. | [optional] |


