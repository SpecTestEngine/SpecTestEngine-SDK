# GraphQlSpecificationsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**captureGraphqlSpecificationAttachmentVisualDiff**](GraphQlSpecificationsApi.md#captureGraphqlSpecificationAttachmentVisualDiff) | **POST** /test/graphql-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed GraphQL attachment assertion |
| [**captureGraphqlSpecificationAttachmentVisualDiffWithHttpInfo**](GraphQlSpecificationsApi.md#captureGraphqlSpecificationAttachmentVisualDiffWithHttpInfo) | **POST** /test/graphql-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed GraphQL attachment assertion |
| [**createGraphqlSpecification**](GraphQlSpecificationsApi.md#createGraphqlSpecification) | **POST** /test/graphql-spec/create | Create a GraphQL specification |
| [**createGraphqlSpecificationWithHttpInfo**](GraphQlSpecificationsApi.md#createGraphqlSpecificationWithHttpInfo) | **POST** /test/graphql-spec/create | Create a GraphQL specification |
| [**deleteGraphqlSpecification**](GraphQlSpecificationsApi.md#deleteGraphqlSpecification) | **DELETE** /test/graphql-spec/by-id | Delete a GraphQL specification |
| [**deleteGraphqlSpecificationWithHttpInfo**](GraphQlSpecificationsApi.md#deleteGraphqlSpecificationWithHttpInfo) | **DELETE** /test/graphql-spec/by-id | Delete a GraphQL specification |
| [**getGraphqlSpecification**](GraphQlSpecificationsApi.md#getGraphqlSpecification) | **GET** /test/graphql-spec/by-id | Get a GraphQL specification |
| [**getGraphqlSpecificationWithHttpInfo**](GraphQlSpecificationsApi.md#getGraphqlSpecificationWithHttpInfo) | **GET** /test/graphql-spec/by-id | Get a GraphQL specification |
| [**getGraphqlSpecificationRun**](GraphQlSpecificationsApi.md#getGraphqlSpecificationRun) | **GET** /test/graphql-spec/run/history/by-run-id/{runId} | Get saved GraphQL run evidence |
| [**getGraphqlSpecificationRunWithHttpInfo**](GraphQlSpecificationsApi.md#getGraphqlSpecificationRunWithHttpInfo) | **GET** /test/graphql-spec/run/history/by-run-id/{runId} | Get saved GraphQL run evidence |
| [**listGraphqlSpecificationRuns**](GraphQlSpecificationsApi.md#listGraphqlSpecificationRuns) | **GET** /test/graphql-spec/run/page/by-spec-id/{specId} | List saved GraphQL runs |
| [**listGraphqlSpecificationRunsWithHttpInfo**](GraphQlSpecificationsApi.md#listGraphqlSpecificationRunsWithHttpInfo) | **GET** /test/graphql-spec/run/page/by-spec-id/{specId} | List saved GraphQL runs |
| [**listGraphqlSpecifications**](GraphQlSpecificationsApi.md#listGraphqlSpecifications) | **GET** /test/graphql-spec/page | List GraphQL specifications |
| [**listGraphqlSpecificationsWithHttpInfo**](GraphQlSpecificationsApi.md#listGraphqlSpecificationsWithHttpInfo) | **GET** /test/graphql-spec/page | List GraphQL specifications |
| [**previewGraphqlSpecificationRecovery**](GraphQlSpecificationsApi.md#previewGraphqlSpecificationRecovery) | **POST** /test/graphql-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a GraphQL specification version |
| [**previewGraphqlSpecificationRecoveryWithHttpInfo**](GraphQlSpecificationsApi.md#previewGraphqlSpecificationRecoveryWithHttpInfo) | **POST** /test/graphql-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a GraphQL specification version |
| [**restoreGraphqlSpecificationFromRun**](GraphQlSpecificationsApi.md#restoreGraphqlSpecificationFromRun) | **PUT** /test/graphql-spec/recovery/{specId}/from-run/{runId}/restore | Restore a GraphQL specification version |
| [**restoreGraphqlSpecificationFromRunWithHttpInfo**](GraphQlSpecificationsApi.md#restoreGraphqlSpecificationFromRunWithHttpInfo) | **PUT** /test/graphql-spec/recovery/{specId}/from-run/{runId}/restore | Restore a GraphQL specification version |
| [**runGraphqlSpecification**](GraphQlSpecificationsApi.md#runGraphqlSpecification) | **POST** /test/graphql-spec/run/by-id | Run a saved GraphQL specification |
| [**runGraphqlSpecificationWithHttpInfo**](GraphQlSpecificationsApi.md#runGraphqlSpecificationWithHttpInfo) | **POST** /test/graphql-spec/run/by-id | Run a saved GraphQL specification |
| [**testGraphqlSpecificationRecoveryVersion**](GraphQlSpecificationsApi.md#testGraphqlSpecificationRecoveryVersion) | **POST** /test/graphql-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous GraphQL specification version |
| [**testGraphqlSpecificationRecoveryVersionWithHttpInfo**](GraphQlSpecificationsApi.md#testGraphqlSpecificationRecoveryVersionWithHttpInfo) | **POST** /test/graphql-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous GraphQL specification version |
| [**updateGraphqlSpecification**](GraphQlSpecificationsApi.md#updateGraphqlSpecification) | **PUT** /test/graphql-spec/by-id | Replace a GraphQL specification definition |
| [**updateGraphqlSpecificationWithHttpInfo**](GraphQlSpecificationsApi.md#updateGraphqlSpecificationWithHttpInfo) | **PUT** /test/graphql-spec/by-id | Replace a GraphQL specification definition |



## captureGraphqlSpecificationAttachmentVisualDiff

> SpecificationRun captureGraphqlSpecificationAttachmentVisualDiff(captureGraphqlSpecificationAttachmentVisualDiffRequest)

Create a visual diff from a failed GraphQL attachment assertion

Explicitly reruns the saved GraphQL specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        DocumentVisualDiffCaptureRunRequest documentVisualDiffCaptureRunRequest = new DocumentVisualDiffCaptureRunRequest(); // DocumentVisualDiffCaptureRunRequest |
        try {
            APIcaptureGraphqlSpecificationAttachmentVisualDiffRequest request = APIcaptureGraphqlSpecificationAttachmentVisualDiffRequest.newBuilder()
                .specId(specId)
                .documentVisualDiffCaptureRunRequest(documentVisualDiffCaptureRunRequest)
                .build();
            SpecificationRun result = apiInstance.captureGraphqlSpecificationAttachmentVisualDiff(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#captureGraphqlSpecificationAttachmentVisualDiff");
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
| captureGraphqlSpecificationAttachmentVisualDiffRequest | [**APIcaptureGraphqlSpecificationAttachmentVisualDiffRequest**](GraphQlSpecificationsApi.md#APIcaptureGraphqlSpecificationAttachmentVisualDiffRequest)|-|-|

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

## captureGraphqlSpecificationAttachmentVisualDiffWithHttpInfo

> ApiResponse<SpecificationRun> captureGraphqlSpecificationAttachmentVisualDiffWithHttpInfo(captureGraphqlSpecificationAttachmentVisualDiffRequest)

Create a visual diff from a failed GraphQL attachment assertion

Explicitly reruns the saved GraphQL specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        DocumentVisualDiffCaptureRunRequest documentVisualDiffCaptureRunRequest = new DocumentVisualDiffCaptureRunRequest(); // DocumentVisualDiffCaptureRunRequest |
        try {
            APIcaptureGraphqlSpecificationAttachmentVisualDiffRequest request = APIcaptureGraphqlSpecificationAttachmentVisualDiffRequest.newBuilder()
                .specId(specId)
                .documentVisualDiffCaptureRunRequest(documentVisualDiffCaptureRunRequest)
                .build();
            ApiResponse<SpecificationRun> response = apiInstance.captureGraphqlSpecificationAttachmentVisualDiffWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#captureGraphqlSpecificationAttachmentVisualDiff");
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
| captureGraphqlSpecificationAttachmentVisualDiffRequest | [**APIcaptureGraphqlSpecificationAttachmentVisualDiffRequest**](GraphQlSpecificationsApi.md#APIcaptureGraphqlSpecificationAttachmentVisualDiffRequest)|-|-|

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


<a id="APIcaptureGraphqlSpecificationAttachmentVisualDiffRequest"></a>
## APIcaptureGraphqlSpecificationAttachmentVisualDiffRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **documentVisualDiffCaptureRunRequest** | [**DocumentVisualDiffCaptureRunRequest**](DocumentVisualDiffCaptureRunRequest.md) |  | |



## createGraphqlSpecification

> Specification createGraphqlSpecification(createGraphqlSpecificationRequest)

Create a GraphQL specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        String specName = "specName_example"; // String | User-facing specification name within the active project.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateGraphqlSpecificationRequest request = APIcreateGraphqlSpecificationRequest.newBuilder()
                .specName(specName)
                .body(body)
                .description(description)
                .idempotencyKey(idempotencyKey)
                .build();
            Specification result = apiInstance.createGraphqlSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#createGraphqlSpecification");
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
| createGraphqlSpecificationRequest | [**APIcreateGraphqlSpecificationRequest**](GraphQlSpecificationsApi.md#APIcreateGraphqlSpecificationRequest)|-|-|

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

## createGraphqlSpecificationWithHttpInfo

> ApiResponse<Specification> createGraphqlSpecificationWithHttpInfo(createGraphqlSpecificationRequest)

Create a GraphQL specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        String specName = "specName_example"; // String | User-facing specification name within the active project.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateGraphqlSpecificationRequest request = APIcreateGraphqlSpecificationRequest.newBuilder()
                .specName(specName)
                .body(body)
                .description(description)
                .idempotencyKey(idempotencyKey)
                .build();
            ApiResponse<Specification> response = apiInstance.createGraphqlSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#createGraphqlSpecification");
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
| createGraphqlSpecificationRequest | [**APIcreateGraphqlSpecificationRequest**](GraphQlSpecificationsApi.md#APIcreateGraphqlSpecificationRequest)|-|-|

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
| **200** | The stored GraphQL specification. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcreateGraphqlSpecificationRequest"></a>
## APIcreateGraphqlSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specName** | **String** | User-facing specification name within the active project. | |
| **body** | **String** |  | |
| **description** | **String** | Optional user-facing description stored with the asset. | [optional] |
| **idempotencyKey** | **UUID** | A caller-generated UUID retained for safe write retries where supported. | [optional] |



## deleteGraphqlSpecification

> Specification deleteGraphqlSpecification(deleteGraphqlSpecificationRequest)

Delete a GraphQL specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIdeleteGraphqlSpecificationRequest request = APIdeleteGraphqlSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            Specification result = apiInstance.deleteGraphqlSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#deleteGraphqlSpecification");
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
| deleteGraphqlSpecificationRequest | [**APIdeleteGraphqlSpecificationRequest**](GraphQlSpecificationsApi.md#APIdeleteGraphqlSpecificationRequest)|-|-|

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

## deleteGraphqlSpecificationWithHttpInfo

> ApiResponse<Specification> deleteGraphqlSpecificationWithHttpInfo(deleteGraphqlSpecificationRequest)

Delete a GraphQL specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIdeleteGraphqlSpecificationRequest request = APIdeleteGraphqlSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            ApiResponse<Specification> response = apiInstance.deleteGraphqlSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#deleteGraphqlSpecification");
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
| deleteGraphqlSpecificationRequest | [**APIdeleteGraphqlSpecificationRequest**](GraphQlSpecificationsApi.md#APIdeleteGraphqlSpecificationRequest)|-|-|

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
| **200** | The deleted GraphQL specification. |  -  |
| **0** | The request failed. |  -  |


<a id="APIdeleteGraphqlSpecificationRequest"></a>
## APIdeleteGraphqlSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |



## getGraphqlSpecification

> Specification getGraphqlSpecification(getGraphqlSpecificationRequest)

Get a GraphQL specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIgetGraphqlSpecificationRequest request = APIgetGraphqlSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            Specification result = apiInstance.getGraphqlSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#getGraphqlSpecification");
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
| getGraphqlSpecificationRequest | [**APIgetGraphqlSpecificationRequest**](GraphQlSpecificationsApi.md#APIgetGraphqlSpecificationRequest)|-|-|

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

## getGraphqlSpecificationWithHttpInfo

> ApiResponse<Specification> getGraphqlSpecificationWithHttpInfo(getGraphqlSpecificationRequest)

Get a GraphQL specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIgetGraphqlSpecificationRequest request = APIgetGraphqlSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            ApiResponse<Specification> response = apiInstance.getGraphqlSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#getGraphqlSpecification");
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
| getGraphqlSpecificationRequest | [**APIgetGraphqlSpecificationRequest**](GraphQlSpecificationsApi.md#APIgetGraphqlSpecificationRequest)|-|-|

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
| **200** | The requested GraphQL specification. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetGraphqlSpecificationRequest"></a>
## APIgetGraphqlSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |



## getGraphqlSpecificationRun

> SpecificationRun getGraphqlSpecificationRun(getGraphqlSpecificationRunRequest)

Get saved GraphQL run evidence

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIgetGraphqlSpecificationRunRequest request = APIgetGraphqlSpecificationRunRequest.newBuilder()
                .runId(runId)
                .build();
            SpecificationRun result = apiInstance.getGraphqlSpecificationRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#getGraphqlSpecificationRun");
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
| getGraphqlSpecificationRunRequest | [**APIgetGraphqlSpecificationRunRequest**](GraphQlSpecificationsApi.md#APIgetGraphqlSpecificationRunRequest)|-|-|

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

## getGraphqlSpecificationRunWithHttpInfo

> ApiResponse<SpecificationRun> getGraphqlSpecificationRunWithHttpInfo(getGraphqlSpecificationRunRequest)

Get saved GraphQL run evidence

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIgetGraphqlSpecificationRunRequest request = APIgetGraphqlSpecificationRunRequest.newBuilder()
                .runId(runId)
                .build();
            ApiResponse<SpecificationRun> response = apiInstance.getGraphqlSpecificationRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#getGraphqlSpecificationRun");
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
| getGraphqlSpecificationRunRequest | [**APIgetGraphqlSpecificationRunRequest**](GraphQlSpecificationsApi.md#APIgetGraphqlSpecificationRunRequest)|-|-|

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


<a id="APIgetGraphqlSpecificationRunRequest"></a>
## APIgetGraphqlSpecificationRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## listGraphqlSpecificationRuns

> SpecificationRunPage listGraphqlSpecificationRuns(listGraphqlSpecificationRunsRequest)

List saved GraphQL runs

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIlistGraphqlSpecificationRunsRequest request = APIlistGraphqlSpecificationRunsRequest.newBuilder()
                .specId(specId)
                .page(page)
                .size(size)
                .build();
            SpecificationRunPage result = apiInstance.listGraphqlSpecificationRuns(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#listGraphqlSpecificationRuns");
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
| listGraphqlSpecificationRunsRequest | [**APIlistGraphqlSpecificationRunsRequest**](GraphQlSpecificationsApi.md#APIlistGraphqlSpecificationRunsRequest)|-|-|

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

## listGraphqlSpecificationRunsWithHttpInfo

> ApiResponse<SpecificationRunPage> listGraphqlSpecificationRunsWithHttpInfo(listGraphqlSpecificationRunsRequest)

List saved GraphQL runs

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIlistGraphqlSpecificationRunsRequest request = APIlistGraphqlSpecificationRunsRequest.newBuilder()
                .specId(specId)
                .page(page)
                .size(size)
                .build();
            ApiResponse<SpecificationRunPage> response = apiInstance.listGraphqlSpecificationRunsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#listGraphqlSpecificationRuns");
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
| listGraphqlSpecificationRunsRequest | [**APIlistGraphqlSpecificationRunsRequest**](GraphQlSpecificationsApi.md#APIlistGraphqlSpecificationRunsRequest)|-|-|

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


<a id="APIlistGraphqlSpecificationRunsRequest"></a>
## APIlistGraphqlSpecificationRunsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |



## listGraphqlSpecifications

> SpecificationPage listGraphqlSpecifications(listGraphqlSpecificationsRequest)

List GraphQL specifications

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistGraphqlSpecificationsRequest request = APIlistGraphqlSpecificationsRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .build();
            SpecificationPage result = apiInstance.listGraphqlSpecifications(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#listGraphqlSpecifications");
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
| listGraphqlSpecificationsRequest | [**APIlistGraphqlSpecificationsRequest**](GraphQlSpecificationsApi.md#APIlistGraphqlSpecificationsRequest)|-|-|

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

## listGraphqlSpecificationsWithHttpInfo

> ApiResponse<SpecificationPage> listGraphqlSpecificationsWithHttpInfo(listGraphqlSpecificationsRequest)

List GraphQL specifications

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistGraphqlSpecificationsRequest request = APIlistGraphqlSpecificationsRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .build();
            ApiResponse<SpecificationPage> response = apiInstance.listGraphqlSpecificationsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#listGraphqlSpecifications");
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
| listGraphqlSpecificationsRequest | [**APIlistGraphqlSpecificationsRequest**](GraphQlSpecificationsApi.md#APIlistGraphqlSpecificationsRequest)|-|-|

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
| **200** | A page of GraphQL specifications. |  -  |
| **0** | The request failed. |  -  |


<a id="APIlistGraphqlSpecificationsRequest"></a>
## APIlistGraphqlSpecificationsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **String** | Case-insensitive server-side search within the active project. | [optional] |



## previewGraphqlSpecificationRecovery

> SpecificationRecoveryPreview previewGraphqlSpecificationRecovery(previewGraphqlSpecificationRecoveryRequest)

Preview restoring a GraphQL specification version

Compares the current specification with the exact DSL snapshot retained by a completed PASS or FAIL run. No expectations are regenerated.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIpreviewGraphqlSpecificationRecoveryRequest request = APIpreviewGraphqlSpecificationRecoveryRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            SpecificationRecoveryPreview result = apiInstance.previewGraphqlSpecificationRecovery(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#previewGraphqlSpecificationRecovery");
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
| previewGraphqlSpecificationRecoveryRequest | [**APIpreviewGraphqlSpecificationRecoveryRequest**](GraphQlSpecificationsApi.md#APIpreviewGraphqlSpecificationRecoveryRequest)|-|-|

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

## previewGraphqlSpecificationRecoveryWithHttpInfo

> ApiResponse<SpecificationRecoveryPreview> previewGraphqlSpecificationRecoveryWithHttpInfo(previewGraphqlSpecificationRecoveryRequest)

Preview restoring a GraphQL specification version

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
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIpreviewGraphqlSpecificationRecoveryRequest request = APIpreviewGraphqlSpecificationRecoveryRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            ApiResponse<SpecificationRecoveryPreview> response = apiInstance.previewGraphqlSpecificationRecoveryWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#previewGraphqlSpecificationRecovery");
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
| previewGraphqlSpecificationRecoveryRequest | [**APIpreviewGraphqlSpecificationRecoveryRequest**](GraphQlSpecificationsApi.md#APIpreviewGraphqlSpecificationRecoveryRequest)|-|-|

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


<a id="APIpreviewGraphqlSpecificationRecoveryRequest"></a>
## APIpreviewGraphqlSpecificationRecoveryRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## restoreGraphqlSpecificationFromRun

> Specification restoreGraphqlSpecificationFromRun(restoreGraphqlSpecificationFromRunRequest)

Restore a GraphQL specification version

Replaces only the current DSL content with the exact snapshot retained by a completed PASS or FAIL run. The specification id, name, description, and stable identity are preserved.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIrestoreGraphqlSpecificationFromRunRequest request = APIrestoreGraphqlSpecificationFromRunRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            Specification result = apiInstance.restoreGraphqlSpecificationFromRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#restoreGraphqlSpecificationFromRun");
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
| restoreGraphqlSpecificationFromRunRequest | [**APIrestoreGraphqlSpecificationFromRunRequest**](GraphQlSpecificationsApi.md#APIrestoreGraphqlSpecificationFromRunRequest)|-|-|

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

## restoreGraphqlSpecificationFromRunWithHttpInfo

> ApiResponse<Specification> restoreGraphqlSpecificationFromRunWithHttpInfo(restoreGraphqlSpecificationFromRunRequest)

Restore a GraphQL specification version

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
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIrestoreGraphqlSpecificationFromRunRequest request = APIrestoreGraphqlSpecificationFromRunRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            ApiResponse<Specification> response = apiInstance.restoreGraphqlSpecificationFromRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#restoreGraphqlSpecificationFromRun");
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
| restoreGraphqlSpecificationFromRunRequest | [**APIrestoreGraphqlSpecificationFromRunRequest**](GraphQlSpecificationsApi.md#APIrestoreGraphqlSpecificationFromRunRequest)|-|-|

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


<a id="APIrestoreGraphqlSpecificationFromRunRequest"></a>
## APIrestoreGraphqlSpecificationFromRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## runGraphqlSpecification

> SpecificationRun runGraphqlSpecification(runGraphqlSpecificationRequest)

Run a saved GraphQL specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIrunGraphqlSpecificationRequest request = APIrunGraphqlSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            SpecificationRun result = apiInstance.runGraphqlSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#runGraphqlSpecification");
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
| runGraphqlSpecificationRequest | [**APIrunGraphqlSpecificationRequest**](GraphQlSpecificationsApi.md#APIrunGraphqlSpecificationRequest)|-|-|

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

## runGraphqlSpecificationWithHttpInfo

> ApiResponse<SpecificationRun> runGraphqlSpecificationWithHttpInfo(runGraphqlSpecificationRequest)

Run a saved GraphQL specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIrunGraphqlSpecificationRequest request = APIrunGraphqlSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            ApiResponse<SpecificationRun> response = apiInstance.runGraphqlSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#runGraphqlSpecification");
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
| runGraphqlSpecificationRequest | [**APIrunGraphqlSpecificationRequest**](GraphQlSpecificationsApi.md#APIrunGraphqlSpecificationRequest)|-|-|

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


<a id="APIrunGraphqlSpecificationRequest"></a>
## APIrunGraphqlSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |



## testGraphqlSpecificationRecoveryVersion

> SpecificationRun testGraphqlSpecificationRecoveryVersion(testGraphqlSpecificationRecoveryVersionRequest)

Test a previous GraphQL specification version

Executes the exact DSL snapshot retained by the selected completed PASS or FAIL run against the current API without changing the saved specification.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APItestGraphqlSpecificationRecoveryVersionRequest request = APItestGraphqlSpecificationRecoveryVersionRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            SpecificationRun result = apiInstance.testGraphqlSpecificationRecoveryVersion(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#testGraphqlSpecificationRecoveryVersion");
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
| testGraphqlSpecificationRecoveryVersionRequest | [**APItestGraphqlSpecificationRecoveryVersionRequest**](GraphQlSpecificationsApi.md#APItestGraphqlSpecificationRecoveryVersionRequest)|-|-|

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

## testGraphqlSpecificationRecoveryVersionWithHttpInfo

> ApiResponse<SpecificationRun> testGraphqlSpecificationRecoveryVersionWithHttpInfo(testGraphqlSpecificationRecoveryVersionRequest)

Test a previous GraphQL specification version

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
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APItestGraphqlSpecificationRecoveryVersionRequest request = APItestGraphqlSpecificationRecoveryVersionRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            ApiResponse<SpecificationRun> response = apiInstance.testGraphqlSpecificationRecoveryVersionWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#testGraphqlSpecificationRecoveryVersion");
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
| testGraphqlSpecificationRecoveryVersionRequest | [**APItestGraphqlSpecificationRecoveryVersionRequest**](GraphQlSpecificationsApi.md#APItestGraphqlSpecificationRecoveryVersionRequest)|-|-|

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


<a id="APItestGraphqlSpecificationRecoveryVersionRequest"></a>
## APItestGraphqlSpecificationRecoveryVersionRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## updateGraphqlSpecification

> Specification updateGraphqlSpecification(updateGraphqlSpecificationRequest)

Replace a GraphQL specification definition

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        try {
            APIupdateGraphqlSpecificationRequest request = APIupdateGraphqlSpecificationRequest.newBuilder()
                .specId(specId)
                .body(body)
                .description(description)
                .build();
            Specification result = apiInstance.updateGraphqlSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#updateGraphqlSpecification");
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
| updateGraphqlSpecificationRequest | [**APIupdateGraphqlSpecificationRequest**](GraphQlSpecificationsApi.md#APIupdateGraphqlSpecificationRequest)|-|-|

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

## updateGraphqlSpecificationWithHttpInfo

> ApiResponse<Specification> updateGraphqlSpecificationWithHttpInfo(updateGraphqlSpecificationRequest)

Replace a GraphQL specification definition

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi;
import software.ste.sdk.generated.api.GraphQlSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GraphQlSpecificationsApi apiInstance = new GraphQlSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        try {
            APIupdateGraphqlSpecificationRequest request = APIupdateGraphqlSpecificationRequest.newBuilder()
                .specId(specId)
                .body(body)
                .description(description)
                .build();
            ApiResponse<Specification> response = apiInstance.updateGraphqlSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GraphQlSpecificationsApi#updateGraphqlSpecification");
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
| updateGraphqlSpecificationRequest | [**APIupdateGraphqlSpecificationRequest**](GraphQlSpecificationsApi.md#APIupdateGraphqlSpecificationRequest)|-|-|

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
| **200** | The updated GraphQL specification. |  -  |
| **0** | The request failed. |  -  |


<a id="APIupdateGraphqlSpecificationRequest"></a>
## APIupdateGraphqlSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **body** | **String** |  | |
| **description** | **String** | Optional user-facing description stored with the asset. | [optional] |
