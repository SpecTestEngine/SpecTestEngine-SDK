# FlowsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**captureFlowStepAttachmentVisualDiff**](FlowsApi.md#captureFlowStepAttachmentVisualDiff) | **POST** /test/flow/run/by-id/{flowId}/visual-diff-captures | Create a visual diff from a failed flow-step attachment assertion |
| [**captureFlowStepAttachmentVisualDiffWithHttpInfo**](FlowsApi.md#captureFlowStepAttachmentVisualDiffWithHttpInfo) | **POST** /test/flow/run/by-id/{flowId}/visual-diff-captures | Create a visual diff from a failed flow-step attachment assertion |
| [**createFlow**](FlowsApi.md#createFlow) | **POST** /test/flow/create | Create a test flow |
| [**createFlowWithHttpInfo**](FlowsApi.md#createFlowWithHttpInfo) | **POST** /test/flow/create | Create a test flow |
| [**deleteFlow**](FlowsApi.md#deleteFlow) | **DELETE** /test/flow/by-id | Delete a test flow |
| [**deleteFlowWithHttpInfo**](FlowsApi.md#deleteFlowWithHttpInfo) | **DELETE** /test/flow/by-id | Delete a test flow |
| [**getFlow**](FlowsApi.md#getFlow) | **GET** /test/flow/by-id/{flowId} | Get a test flow |
| [**getFlowWithHttpInfo**](FlowsApi.md#getFlowWithHttpInfo) | **GET** /test/flow/by-id/{flowId} | Get a test flow |
| [**getFlowRun**](FlowsApi.md#getFlowRun) | **GET** /test/flow/run/saved/{runId} | Get a saved flow run |
| [**getFlowRunWithHttpInfo**](FlowsApi.md#getFlowRunWithHttpInfo) | **GET** /test/flow/run/saved/{runId} | Get a saved flow run |
| [**listFlowRuns**](FlowsApi.md#listFlowRuns) | **GET** /test/flow/run/by-flow-id/{flowId}/page | List saved runs for a flow |
| [**listFlowRunsWithHttpInfo**](FlowsApi.md#listFlowRunsWithHttpInfo) | **GET** /test/flow/run/by-flow-id/{flowId}/page | List saved runs for a flow |
| [**listFlows**](FlowsApi.md#listFlows) | **GET** /test/flow/page | List test flows |
| [**listFlowsWithHttpInfo**](FlowsApi.md#listFlowsWithHttpInfo) | **GET** /test/flow/page | List test flows |
| [**runFlow**](FlowsApi.md#runFlow) | **POST** /test/flow/run/by-id/{flowId} | Run a saved flow |
| [**runFlowWithHttpInfo**](FlowsApi.md#runFlowWithHttpInfo) | **POST** /test/flow/run/by-id/{flowId} | Run a saved flow |
| [**runFlowBatch**](FlowsApi.md#runFlowBatch) | **POST** /test/flow/run/batch | Run multiple saved flows |
| [**runFlowBatchWithHttpInfo**](FlowsApi.md#runFlowBatchWithHttpInfo) | **POST** /test/flow/run/batch | Run multiple saved flows |
| [**updateFlow**](FlowsApi.md#updateFlow) | **PUT** /test/flow/by-id | Replace a test flow |
| [**updateFlowWithHttpInfo**](FlowsApi.md#updateFlowWithHttpInfo) | **PUT** /test/flow/by-id | Replace a test flow |



## captureFlowStepAttachmentVisualDiff

> FlowRun captureFlowStepAttachmentVisualDiff(captureFlowStepAttachmentVisualDiffRequest)

Create a visual diff from a failed flow-step attachment assertion

Explicitly reruns the saved flow and captures one failed PDF or image response from the selected API step. The flow and attachment assertion retain their real status.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        UUID flowId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved test flow.
        FlowDocumentVisualDiffCaptureRunRequest flowDocumentVisualDiffCaptureRunRequest = new FlowDocumentVisualDiffCaptureRunRequest(); // FlowDocumentVisualDiffCaptureRunRequest |
        try {
            APIcaptureFlowStepAttachmentVisualDiffRequest request = APIcaptureFlowStepAttachmentVisualDiffRequest.newBuilder()
                .flowId(flowId)
                .flowDocumentVisualDiffCaptureRunRequest(flowDocumentVisualDiffCaptureRunRequest)
                .build();
            FlowRun result = apiInstance.captureFlowStepAttachmentVisualDiff(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#captureFlowStepAttachmentVisualDiff");
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
| captureFlowStepAttachmentVisualDiffRequest | [**APIcaptureFlowStepAttachmentVisualDiffRequest**](FlowsApi.md#APIcaptureFlowStepAttachmentVisualDiffRequest)|-|-|

### Return type

[**FlowRun**](FlowRun.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete flow run evidence containing the temporary visual diff link in the selected step. |  -  |
| **0** | The request failed. |  -  |

## captureFlowStepAttachmentVisualDiffWithHttpInfo

> ApiResponse<FlowRun> captureFlowStepAttachmentVisualDiffWithHttpInfo(captureFlowStepAttachmentVisualDiffRequest)

Create a visual diff from a failed flow-step attachment assertion

Explicitly reruns the saved flow and captures one failed PDF or image response from the selected API step. The flow and attachment assertion retain their real status.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        UUID flowId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved test flow.
        FlowDocumentVisualDiffCaptureRunRequest flowDocumentVisualDiffCaptureRunRequest = new FlowDocumentVisualDiffCaptureRunRequest(); // FlowDocumentVisualDiffCaptureRunRequest |
        try {
            APIcaptureFlowStepAttachmentVisualDiffRequest request = APIcaptureFlowStepAttachmentVisualDiffRequest.newBuilder()
                .flowId(flowId)
                .flowDocumentVisualDiffCaptureRunRequest(flowDocumentVisualDiffCaptureRunRequest)
                .build();
            ApiResponse<FlowRun> response = apiInstance.captureFlowStepAttachmentVisualDiffWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#captureFlowStepAttachmentVisualDiff");
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
| captureFlowStepAttachmentVisualDiffRequest | [**APIcaptureFlowStepAttachmentVisualDiffRequest**](FlowsApi.md#APIcaptureFlowStepAttachmentVisualDiffRequest)|-|-|

### Return type

ApiResponse<[**FlowRun**](FlowRun.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete flow run evidence containing the temporary visual diff link in the selected step. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcaptureFlowStepAttachmentVisualDiffRequest"></a>
## APIcaptureFlowStepAttachmentVisualDiffRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **flowId** | **UUID** | UUIDv7 identifier of the saved test flow. | |
| **flowDocumentVisualDiffCaptureRunRequest** | [**FlowDocumentVisualDiffCaptureRunRequest**](FlowDocumentVisualDiffCaptureRunRequest.md) |  | |



## createFlow

> Flow createFlow(createFlowRequest)

Create a test flow

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        FlowInput flowInput = new FlowInput(); // FlowInput |
        ContentFormat format = ContentFormat.fromValue("JSON"); // ContentFormat | Serialization format used for the returned specification source.
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateFlowRequest request = APIcreateFlowRequest.newBuilder()
                .flowInput(flowInput)
                .format(format)
                .idempotencyKey(idempotencyKey)
                .build();
            Flow result = apiInstance.createFlow(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#createFlow");
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
| createFlowRequest | [**APIcreateFlowRequest**](FlowsApi.md#APIcreateFlowRequest)|-|-|

### Return type

[**Flow**](Flow.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored flow. |  -  |
| **0** | The request failed. |  -  |

## createFlowWithHttpInfo

> ApiResponse<Flow> createFlowWithHttpInfo(createFlowRequest)

Create a test flow

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        FlowInput flowInput = new FlowInput(); // FlowInput |
        ContentFormat format = ContentFormat.fromValue("JSON"); // ContentFormat | Serialization format used for the returned specification source.
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateFlowRequest request = APIcreateFlowRequest.newBuilder()
                .flowInput(flowInput)
                .format(format)
                .idempotencyKey(idempotencyKey)
                .build();
            ApiResponse<Flow> response = apiInstance.createFlowWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#createFlow");
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
| createFlowRequest | [**APIcreateFlowRequest**](FlowsApi.md#APIcreateFlowRequest)|-|-|

### Return type

ApiResponse<[**Flow**](Flow.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored flow. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcreateFlowRequest"></a>
## APIcreateFlowRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **flowInput** | [**FlowInput**](FlowInput.md) |  | |
| **format** | [**ContentFormat**](.md) | Serialization format used for the returned specification source. | [optional] [default to JSON] [enum: JSON, YAML, XML] |
| **idempotencyKey** | **UUID** | A caller-generated UUID retained for safe write retries where supported. | [optional] |



## deleteFlow

> void deleteFlow(deleteFlowRequest)

Delete a test flow

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        UUID flowId = UUID.randomUUID(); // UUID |
        try {
            APIdeleteFlowRequest request = APIdeleteFlowRequest.newBuilder()
                .flowId(flowId)
                .build();
            apiInstance.deleteFlow(request);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#deleteFlow");
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
| deleteFlowRequest | [**APIdeleteFlowRequest**](FlowsApi.md#APIdeleteFlowRequest)|-|-|

### Return type


null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Flow deleted. |  -  |
| **0** | The request failed. |  -  |

## deleteFlowWithHttpInfo

> ApiResponse<Void> deleteFlowWithHttpInfo(deleteFlowRequest)

Delete a test flow

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        UUID flowId = UUID.randomUUID(); // UUID |
        try {
            APIdeleteFlowRequest request = APIdeleteFlowRequest.newBuilder()
                .flowId(flowId)
                .build();
            ApiResponse<Void> response = apiInstance.deleteFlowWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#deleteFlow");
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
| deleteFlowRequest | [**APIdeleteFlowRequest**](FlowsApi.md#APIdeleteFlowRequest)|-|-|

### Return type


ApiResponse<Void>

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Flow deleted. |  -  |
| **0** | The request failed. |  -  |


<a id="APIdeleteFlowRequest"></a>
## APIdeleteFlowRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **flowId** | **UUID** |  | |



## getFlow

> Flow getFlow(getFlowRequest)

Get a test flow

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        UUID flowId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved test flow.
        try {
            APIgetFlowRequest request = APIgetFlowRequest.newBuilder()
                .flowId(flowId)
                .build();
            Flow result = apiInstance.getFlow(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#getFlow");
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
| getFlowRequest | [**APIgetFlowRequest**](FlowsApi.md#APIgetFlowRequest)|-|-|

### Return type

[**Flow**](Flow.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested flow. |  -  |
| **0** | The request failed. |  -  |

## getFlowWithHttpInfo

> ApiResponse<Flow> getFlowWithHttpInfo(getFlowRequest)

Get a test flow

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        UUID flowId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved test flow.
        try {
            APIgetFlowRequest request = APIgetFlowRequest.newBuilder()
                .flowId(flowId)
                .build();
            ApiResponse<Flow> response = apiInstance.getFlowWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#getFlow");
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
| getFlowRequest | [**APIgetFlowRequest**](FlowsApi.md#APIgetFlowRequest)|-|-|

### Return type

ApiResponse<[**Flow**](Flow.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested flow. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetFlowRequest"></a>
## APIgetFlowRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **flowId** | **UUID** | UUIDv7 identifier of the saved test flow. | |



## getFlowRun

> FlowRun getFlowRun(getFlowRunRequest)

Get a saved flow run

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID |
        try {
            APIgetFlowRunRequest request = APIgetFlowRunRequest.newBuilder()
                .runId(runId)
                .build();
            FlowRun result = apiInstance.getFlowRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#getFlowRun");
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
| getFlowRunRequest | [**APIgetFlowRunRequest**](FlowsApi.md#APIgetFlowRunRequest)|-|-|

### Return type

[**FlowRun**](FlowRun.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete persisted flow run evidence. |  -  |
| **0** | The request failed. |  -  |

## getFlowRunWithHttpInfo

> ApiResponse<FlowRun> getFlowRunWithHttpInfo(getFlowRunRequest)

Get a saved flow run

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID |
        try {
            APIgetFlowRunRequest request = APIgetFlowRunRequest.newBuilder()
                .runId(runId)
                .build();
            ApiResponse<FlowRun> response = apiInstance.getFlowRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#getFlowRun");
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
| getFlowRunRequest | [**APIgetFlowRunRequest**](FlowsApi.md#APIgetFlowRunRequest)|-|-|

### Return type

ApiResponse<[**FlowRun**](FlowRun.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete persisted flow run evidence. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetFlowRunRequest"></a>
## APIgetFlowRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **runId** | **UUID** |  | |



## listFlowRuns

> FlowRunPage listFlowRuns(listFlowRunsRequest)

List saved runs for a flow

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        UUID flowId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved test flow.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIlistFlowRunsRequest request = APIlistFlowRunsRequest.newBuilder()
                .flowId(flowId)
                .page(page)
                .size(size)
                .build();
            FlowRunPage result = apiInstance.listFlowRuns(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#listFlowRuns");
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
| listFlowRunsRequest | [**APIlistFlowRunsRequest**](FlowsApi.md#APIlistFlowRunsRequest)|-|-|

### Return type

[**FlowRunPage**](FlowRunPage.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of lightweight persisted flow run summaries. |  -  |
| **0** | The request failed. |  -  |

## listFlowRunsWithHttpInfo

> ApiResponse<FlowRunPage> listFlowRunsWithHttpInfo(listFlowRunsRequest)

List saved runs for a flow

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        UUID flowId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved test flow.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIlistFlowRunsRequest request = APIlistFlowRunsRequest.newBuilder()
                .flowId(flowId)
                .page(page)
                .size(size)
                .build();
            ApiResponse<FlowRunPage> response = apiInstance.listFlowRunsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#listFlowRuns");
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
| listFlowRunsRequest | [**APIlistFlowRunsRequest**](FlowsApi.md#APIlistFlowRunsRequest)|-|-|

### Return type

ApiResponse<[**FlowRunPage**](FlowRunPage.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of lightweight persisted flow run summaries. |  -  |
| **0** | The request failed. |  -  |


<a id="APIlistFlowRunsRequest"></a>
## APIlistFlowRunsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **flowId** | **UUID** | UUIDv7 identifier of the saved test flow. | |
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |



## listFlows

> FlowPage listFlows(listFlowsRequest)

List test flows

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistFlowsRequest request = APIlistFlowsRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .build();
            FlowPage result = apiInstance.listFlows(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#listFlows");
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
| listFlowsRequest | [**APIlistFlowsRequest**](FlowsApi.md#APIlistFlowsRequest)|-|-|

### Return type

[**FlowPage**](FlowPage.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of flow summaries. |  -  |
| **0** | The request failed. |  -  |

## listFlowsWithHttpInfo

> ApiResponse<FlowPage> listFlowsWithHttpInfo(listFlowsRequest)

List test flows

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistFlowsRequest request = APIlistFlowsRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .build();
            ApiResponse<FlowPage> response = apiInstance.listFlowsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#listFlows");
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
| listFlowsRequest | [**APIlistFlowsRequest**](FlowsApi.md#APIlistFlowsRequest)|-|-|

### Return type

ApiResponse<[**FlowPage**](FlowPage.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of flow summaries. |  -  |
| **0** | The request failed. |  -  |


<a id="APIlistFlowsRequest"></a>
## APIlistFlowsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **String** | Case-insensitive server-side search within the active project. | [optional] |



## runFlow

> FlowRun runFlow(runFlowRequest)

Run a saved flow

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        UUID flowId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved test flow.
        Boolean watch = false; // Boolean | Create a browser watch token when the flow contains visible browser steps.
        try {
            APIrunFlowRequest request = APIrunFlowRequest.newBuilder()
                .flowId(flowId)
                .watch(watch)
                .build();
            FlowRun result = apiInstance.runFlow(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#runFlow");
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
| runFlowRequest | [**APIrunFlowRequest**](FlowsApi.md#APIrunFlowRequest)|-|-|

### Return type

[**FlowRun**](FlowRun.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete flow run evidence. |  -  |
| **0** | The request failed. |  -  |

## runFlowWithHttpInfo

> ApiResponse<FlowRun> runFlowWithHttpInfo(runFlowRequest)

Run a saved flow

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        UUID flowId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved test flow.
        Boolean watch = false; // Boolean | Create a browser watch token when the flow contains visible browser steps.
        try {
            APIrunFlowRequest request = APIrunFlowRequest.newBuilder()
                .flowId(flowId)
                .watch(watch)
                .build();
            ApiResponse<FlowRun> response = apiInstance.runFlowWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#runFlow");
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
| runFlowRequest | [**APIrunFlowRequest**](FlowsApi.md#APIrunFlowRequest)|-|-|

### Return type

ApiResponse<[**FlowRun**](FlowRun.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete flow run evidence. |  -  |
| **0** | The request failed. |  -  |


<a id="APIrunFlowRequest"></a>
## APIrunFlowRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **flowId** | **UUID** | UUIDv7 identifier of the saved test flow. | |
| **watch** | **Boolean** | Create a browser watch token when the flow contains visible browser steps. | [optional] [default to false] |



## runFlowBatch

> List<FlowRun> runFlowBatch(runFlowBatchRequest)

Run multiple saved flows

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        RunFlowBatchRequest runFlowBatchRequest = new RunFlowBatchRequest(); // RunFlowBatchRequest |
        try {
            APIrunFlowBatchRequest request = APIrunFlowBatchRequest.newBuilder()
                .runFlowBatchRequest(runFlowBatchRequest)
                .build();
            List<FlowRun> result = apiInstance.runFlowBatch(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#runFlowBatch");
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
| runFlowBatchRequest | [**APIrunFlowBatchRequest**](FlowsApi.md#APIrunFlowBatchRequest)|-|-|

### Return type

[**List&lt;FlowRun&gt;**](FlowRun.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete evidence for every requested flow. |  -  |
| **0** | The request failed. |  -  |

## runFlowBatchWithHttpInfo

> ApiResponse<List<FlowRun>> runFlowBatchWithHttpInfo(runFlowBatchRequest)

Run multiple saved flows

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        RunFlowBatchRequest runFlowBatchRequest = new RunFlowBatchRequest(); // RunFlowBatchRequest |
        try {
            APIrunFlowBatchRequest request = APIrunFlowBatchRequest.newBuilder()
                .runFlowBatchRequest(runFlowBatchRequest)
                .build();
            ApiResponse<List<FlowRun>> response = apiInstance.runFlowBatchWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#runFlowBatch");
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
| runFlowBatchRequest | [**APIrunFlowBatchRequest**](FlowsApi.md#APIrunFlowBatchRequest)|-|-|

### Return type

ApiResponse<[**List&lt;FlowRun&gt;**](FlowRun.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete evidence for every requested flow. |  -  |
| **0** | The request failed. |  -  |


<a id="APIrunFlowBatchRequest"></a>
## APIrunFlowBatchRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **runFlowBatchRequest** | [**RunFlowBatchRequest**](RunFlowBatchRequest.md) |  | |



## updateFlow

> Flow updateFlow(updateFlowRequest)

Replace a test flow

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        UUID flowId = UUID.randomUUID(); // UUID |
        FlowInput flowInput = new FlowInput(); // FlowInput |
        ContentFormat format = ContentFormat.fromValue("JSON"); // ContentFormat | Serialization format used for the returned specification source.
        try {
            APIupdateFlowRequest request = APIupdateFlowRequest.newBuilder()
                .flowId(flowId)
                .flowInput(flowInput)
                .format(format)
                .build();
            Flow result = apiInstance.updateFlow(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#updateFlow");
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
| updateFlowRequest | [**APIupdateFlowRequest**](FlowsApi.md#APIupdateFlowRequest)|-|-|

### Return type

[**Flow**](Flow.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated flow. |  -  |
| **0** | The request failed. |  -  |

## updateFlowWithHttpInfo

> ApiResponse<Flow> updateFlowWithHttpInfo(updateFlowRequest)

Replace a test flow

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.FlowsApi;
import software.ste.sdk.generated.api.FlowsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        UUID flowId = UUID.randomUUID(); // UUID |
        FlowInput flowInput = new FlowInput(); // FlowInput |
        ContentFormat format = ContentFormat.fromValue("JSON"); // ContentFormat | Serialization format used for the returned specification source.
        try {
            APIupdateFlowRequest request = APIupdateFlowRequest.newBuilder()
                .flowId(flowId)
                .flowInput(flowInput)
                .format(format)
                .build();
            ApiResponse<Flow> response = apiInstance.updateFlowWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#updateFlow");
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
| updateFlowRequest | [**APIupdateFlowRequest**](FlowsApi.md#APIupdateFlowRequest)|-|-|

### Return type

ApiResponse<[**Flow**](Flow.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated flow. |  -  |
| **0** | The request failed. |  -  |


<a id="APIupdateFlowRequest"></a>
## APIupdateFlowRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **flowId** | **UUID** |  | |
| **flowInput** | [**FlowInput**](FlowInput.md) |  | |
| **format** | [**ContentFormat**](.md) | Serialization format used for the returned specification source. | [optional] [default to JSON] [enum: JSON, YAML, XML] |


