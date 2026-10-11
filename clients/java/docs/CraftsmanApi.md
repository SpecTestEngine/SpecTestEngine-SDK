# CraftsmanApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelCraftsmanRun**](CraftsmanApi.md#cancelCraftsmanRun) | **POST** /sentinel/request-workspaces/runs/{runId}/cancel | Cancel a queued or active Craftsman run |
| [**cancelCraftsmanRunWithHttpInfo**](CraftsmanApi.md#cancelCraftsmanRunWithHttpInfo) | **POST** /sentinel/request-workspaces/runs/{runId}/cancel | Cancel a queued or active Craftsman run |
| [**createRequestNode**](CraftsmanApi.md#createRequestNode) | **POST** /sentinel/request-workspaces/{workspaceId}/nodes | Add a folder or saved request |
| [**createRequestNodeWithHttpInfo**](CraftsmanApi.md#createRequestNodeWithHttpInfo) | **POST** /sentinel/request-workspaces/{workspaceId}/nodes | Add a folder or saved request |
| [**createRequestWorkspace**](CraftsmanApi.md#createRequestWorkspace) | **POST** /sentinel/request-workspaces | Create a request workspace |
| [**createRequestWorkspaceWithHttpInfo**](CraftsmanApi.md#createRequestWorkspaceWithHttpInfo) | **POST** /sentinel/request-workspaces | Create a request workspace |
| [**deleteRequestNode**](CraftsmanApi.md#deleteRequestNode) | **DELETE** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId} | Delete a folder or saved request |
| [**deleteRequestNodeWithHttpInfo**](CraftsmanApi.md#deleteRequestNodeWithHttpInfo) | **DELETE** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId} | Delete a folder or saved request |
| [**deleteRequestWorkspace**](CraftsmanApi.md#deleteRequestWorkspace) | **DELETE** /sentinel/request-workspaces/{workspaceId} | Delete a request workspace |
| [**deleteRequestWorkspaceWithHttpInfo**](CraftsmanApi.md#deleteRequestWorkspaceWithHttpInfo) | **DELETE** /sentinel/request-workspaces/{workspaceId} | Delete a request workspace |
| [**getCraftsmanRun**](CraftsmanApi.md#getCraftsmanRun) | **GET** /sentinel/request-workspaces/runs/{runId} | Get Craftsman run lifecycle and evidence |
| [**getCraftsmanRunWithHttpInfo**](CraftsmanApi.md#getCraftsmanRunWithHttpInfo) | **GET** /sentinel/request-workspaces/runs/{runId} | Get Craftsman run lifecycle and evidence |
| [**getCraftsmanRunTranscript**](CraftsmanApi.md#getCraftsmanRunTranscript) | **GET** /sentinel/request-workspaces/runs/{runId}/transcript | Get a Craftsman Streaming semantic transcript |
| [**getCraftsmanRunTranscriptWithHttpInfo**](CraftsmanApi.md#getCraftsmanRunTranscriptWithHttpInfo) | **GET** /sentinel/request-workspaces/runs/{runId}/transcript | Get a Craftsman Streaming semantic transcript |
| [**getDocumentAsset**](CraftsmanApi.md#getDocumentAsset) | **GET** /sentinel/document-assets/{assetId} | Resolve request attachment metadata |
| [**getDocumentAssetWithHttpInfo**](CraftsmanApi.md#getDocumentAssetWithHttpInfo) | **GET** /sentinel/document-assets/{assetId} | Resolve request attachment metadata |
| [**getRequestWorkspace**](CraftsmanApi.md#getRequestWorkspace) | **GET** /sentinel/request-workspaces/{workspaceId} | Get a request workspace |
| [**getRequestWorkspaceWithHttpInfo**](CraftsmanApi.md#getRequestWorkspaceWithHttpInfo) | **GET** /sentinel/request-workspaces/{workspaceId} | Get a request workspace |
| [**listRequestWorkspaces**](CraftsmanApi.md#listRequestWorkspaces) | **GET** /sentinel/request-workspaces/page | List request workspaces |
| [**listRequestWorkspacesWithHttpInfo**](CraftsmanApi.md#listRequestWorkspacesWithHttpInfo) | **GET** /sentinel/request-workspaces/page | List request workspaces |
| [**queueCraftsmanStreamingRun**](CraftsmanApi.md#queueCraftsmanStreamingRun) | **POST** /sentinel/request-workspaces/runs/streaming | Queue a standalone bounded Streaming session |
| [**queueCraftsmanStreamingRunWithHttpInfo**](CraftsmanApi.md#queueCraftsmanStreamingRunWithHttpInfo) | **POST** /sentinel/request-workspaces/runs/streaming | Queue a standalone bounded Streaming session |
| [**queueCraftsmanWorkflowRun**](CraftsmanApi.md#queueCraftsmanWorkflowRun) | **POST** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId}/runs | Queue a saved request or mixed-protocol Workflow run |
| [**queueCraftsmanWorkflowRunWithHttpInfo**](CraftsmanApi.md#queueCraftsmanWorkflowRunWithHttpInfo) | **POST** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId}/runs | Queue a saved request or mixed-protocol Workflow run |
| [**updateRequestNode**](CraftsmanApi.md#updateRequestNode) | **PUT** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId} | Update a folder or saved request |
| [**updateRequestNodeWithHttpInfo**](CraftsmanApi.md#updateRequestNodeWithHttpInfo) | **PUT** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId} | Update a folder or saved request |
| [**updateRequestWorkspace**](CraftsmanApi.md#updateRequestWorkspace) | **PUT** /sentinel/request-workspaces/{workspaceId} | Replace request workspace metadata and variables |
| [**updateRequestWorkspaceWithHttpInfo**](CraftsmanApi.md#updateRequestWorkspaceWithHttpInfo) | **PUT** /sentinel/request-workspaces/{workspaceId} | Replace request workspace metadata and variables |
| [**uploadDocumentAsset**](CraftsmanApi.md#uploadDocumentAsset) | **POST** /sentinel/document-assets | Upload a reusable request attachment |
| [**uploadDocumentAssetWithHttpInfo**](CraftsmanApi.md#uploadDocumentAssetWithHttpInfo) | **POST** /sentinel/document-assets | Upload a reusable request attachment |



## cancelCraftsmanRun

> CraftsmanRun cancelCraftsmanRun(cancelCraftsmanRunRequest)

Cancel a queued or active Craftsman run

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIcancelCraftsmanRunRequest request = APIcancelCraftsmanRunRequest.newBuilder()
                .runId(runId)
                .build();
            CraftsmanRun result = apiInstance.cancelCraftsmanRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#cancelCraftsmanRun");
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
| cancelCraftsmanRunRequest | [**APIcancelCraftsmanRunRequest**](CraftsmanApi.md#APIcancelCraftsmanRunRequest)|-|-|

### Return type

[**CraftsmanRun**](CraftsmanRun.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated lifecycle after cooperative cancellation was requested. |  -  |
| **0** | The request failed. |  -  |

## cancelCraftsmanRunWithHttpInfo

> ApiResponse<CraftsmanRun> cancelCraftsmanRunWithHttpInfo(cancelCraftsmanRunRequest)

Cancel a queued or active Craftsman run

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIcancelCraftsmanRunRequest request = APIcancelCraftsmanRunRequest.newBuilder()
                .runId(runId)
                .build();
            ApiResponse<CraftsmanRun> response = apiInstance.cancelCraftsmanRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#cancelCraftsmanRun");
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
| cancelCraftsmanRunRequest | [**APIcancelCraftsmanRunRequest**](CraftsmanApi.md#APIcancelCraftsmanRunRequest)|-|-|

### Return type

ApiResponse<[**CraftsmanRun**](CraftsmanRun.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated lifecycle after cooperative cancellation was requested. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcancelCraftsmanRunRequest"></a>
## APIcancelCraftsmanRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## createRequestNode

> RequestNode createRequestNode(createRequestNodeRequest)

Add a folder or saved request

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID workspaceId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Craftsman request workspace.
        RequestNodeInput requestNodeInput = new RequestNodeInput(); // RequestNodeInput |
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateRequestNodeRequest request = APIcreateRequestNodeRequest.newBuilder()
                .workspaceId(workspaceId)
                .requestNodeInput(requestNodeInput)
                .idempotencyKey(idempotencyKey)
                .build();
            RequestNode result = apiInstance.createRequestNode(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#createRequestNode");
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
| createRequestNodeRequest | [**APIcreateRequestNodeRequest**](CraftsmanApi.md#APIcreateRequestNodeRequest)|-|-|

### Return type

[**RequestNode**](RequestNode.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created workspace node. |  -  |
| **0** | The request failed. |  -  |

## createRequestNodeWithHttpInfo

> ApiResponse<RequestNode> createRequestNodeWithHttpInfo(createRequestNodeRequest)

Add a folder or saved request

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID workspaceId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Craftsman request workspace.
        RequestNodeInput requestNodeInput = new RequestNodeInput(); // RequestNodeInput |
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateRequestNodeRequest request = APIcreateRequestNodeRequest.newBuilder()
                .workspaceId(workspaceId)
                .requestNodeInput(requestNodeInput)
                .idempotencyKey(idempotencyKey)
                .build();
            ApiResponse<RequestNode> response = apiInstance.createRequestNodeWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#createRequestNode");
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
| createRequestNodeRequest | [**APIcreateRequestNodeRequest**](CraftsmanApi.md#APIcreateRequestNodeRequest)|-|-|

### Return type

ApiResponse<[**RequestNode**](RequestNode.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created workspace node. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcreateRequestNodeRequest"></a>
## APIcreateRequestNodeRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **workspaceId** | **UUID** | UUIDv7 identifier of the Craftsman request workspace. | |
| **requestNodeInput** | [**RequestNodeInput**](RequestNodeInput.md) |  | |
| **idempotencyKey** | **UUID** | A caller-generated UUID retained for safe write retries where supported. | [optional] |



## createRequestWorkspace

> RequestWorkspace createRequestWorkspace(createRequestWorkspaceRequest)

Create a request workspace

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        RequestWorkspaceInput requestWorkspaceInput = new RequestWorkspaceInput(); // RequestWorkspaceInput |
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateRequestWorkspaceRequest request = APIcreateRequestWorkspaceRequest.newBuilder()
                .requestWorkspaceInput(requestWorkspaceInput)
                .idempotencyKey(idempotencyKey)
                .build();
            RequestWorkspace result = apiInstance.createRequestWorkspace(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#createRequestWorkspace");
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
| createRequestWorkspaceRequest | [**APIcreateRequestWorkspaceRequest**](CraftsmanApi.md#APIcreateRequestWorkspaceRequest)|-|-|

### Return type

[**RequestWorkspace**](RequestWorkspace.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created workspace. |  -  |
| **0** | The request failed. |  -  |

## createRequestWorkspaceWithHttpInfo

> ApiResponse<RequestWorkspace> createRequestWorkspaceWithHttpInfo(createRequestWorkspaceRequest)

Create a request workspace

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        RequestWorkspaceInput requestWorkspaceInput = new RequestWorkspaceInput(); // RequestWorkspaceInput |
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateRequestWorkspaceRequest request = APIcreateRequestWorkspaceRequest.newBuilder()
                .requestWorkspaceInput(requestWorkspaceInput)
                .idempotencyKey(idempotencyKey)
                .build();
            ApiResponse<RequestWorkspace> response = apiInstance.createRequestWorkspaceWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#createRequestWorkspace");
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
| createRequestWorkspaceRequest | [**APIcreateRequestWorkspaceRequest**](CraftsmanApi.md#APIcreateRequestWorkspaceRequest)|-|-|

### Return type

ApiResponse<[**RequestWorkspace**](RequestWorkspace.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created workspace. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcreateRequestWorkspaceRequest"></a>
## APIcreateRequestWorkspaceRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **requestWorkspaceInput** | [**RequestWorkspaceInput**](RequestWorkspaceInput.md) |  | |
| **idempotencyKey** | **UUID** | A caller-generated UUID retained for safe write retries where supported. | [optional] |



## deleteRequestNode

> void deleteRequestNode(deleteRequestNodeRequest)

Delete a folder or saved request

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID workspaceId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Craftsman request workspace.
        UUID nodeId = UUID.randomUUID(); // UUID |
        try {
            APIdeleteRequestNodeRequest request = APIdeleteRequestNodeRequest.newBuilder()
                .workspaceId(workspaceId)
                .nodeId(nodeId)
                .build();
            apiInstance.deleteRequestNode(request);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#deleteRequestNode");
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
| deleteRequestNodeRequest | [**APIdeleteRequestNodeRequest**](CraftsmanApi.md#APIdeleteRequestNodeRequest)|-|-|

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
| **204** | Workspace node deleted. |  -  |
| **0** | The request failed. |  -  |

## deleteRequestNodeWithHttpInfo

> ApiResponse<Void> deleteRequestNodeWithHttpInfo(deleteRequestNodeRequest)

Delete a folder or saved request

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID workspaceId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Craftsman request workspace.
        UUID nodeId = UUID.randomUUID(); // UUID |
        try {
            APIdeleteRequestNodeRequest request = APIdeleteRequestNodeRequest.newBuilder()
                .workspaceId(workspaceId)
                .nodeId(nodeId)
                .build();
            ApiResponse<Void> response = apiInstance.deleteRequestNodeWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#deleteRequestNode");
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
| deleteRequestNodeRequest | [**APIdeleteRequestNodeRequest**](CraftsmanApi.md#APIdeleteRequestNodeRequest)|-|-|

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
| **204** | Workspace node deleted. |  -  |
| **0** | The request failed. |  -  |


<a id="APIdeleteRequestNodeRequest"></a>
## APIdeleteRequestNodeRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **workspaceId** | **UUID** | UUIDv7 identifier of the Craftsman request workspace. | |
| **nodeId** | **UUID** |  | |



## deleteRequestWorkspace

> void deleteRequestWorkspace(deleteRequestWorkspaceRequest)

Delete a request workspace

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID workspaceId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Craftsman request workspace.
        try {
            APIdeleteRequestWorkspaceRequest request = APIdeleteRequestWorkspaceRequest.newBuilder()
                .workspaceId(workspaceId)
                .build();
            apiInstance.deleteRequestWorkspace(request);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#deleteRequestWorkspace");
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
| deleteRequestWorkspaceRequest | [**APIdeleteRequestWorkspaceRequest**](CraftsmanApi.md#APIdeleteRequestWorkspaceRequest)|-|-|

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
| **204** | Workspace deleted. |  -  |
| **0** | The request failed. |  -  |

## deleteRequestWorkspaceWithHttpInfo

> ApiResponse<Void> deleteRequestWorkspaceWithHttpInfo(deleteRequestWorkspaceRequest)

Delete a request workspace

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID workspaceId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Craftsman request workspace.
        try {
            APIdeleteRequestWorkspaceRequest request = APIdeleteRequestWorkspaceRequest.newBuilder()
                .workspaceId(workspaceId)
                .build();
            ApiResponse<Void> response = apiInstance.deleteRequestWorkspaceWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#deleteRequestWorkspace");
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
| deleteRequestWorkspaceRequest | [**APIdeleteRequestWorkspaceRequest**](CraftsmanApi.md#APIdeleteRequestWorkspaceRequest)|-|-|

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
| **204** | Workspace deleted. |  -  |
| **0** | The request failed. |  -  |


<a id="APIdeleteRequestWorkspaceRequest"></a>
## APIdeleteRequestWorkspaceRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **workspaceId** | **UUID** | UUIDv7 identifier of the Craftsman request workspace. | |



## getCraftsmanRun

> CraftsmanRun getCraftsmanRun(getCraftsmanRunRequest)

Get Craftsman run lifecycle and evidence

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIgetCraftsmanRunRequest request = APIgetCraftsmanRunRequest.newBuilder()
                .runId(runId)
                .build();
            CraftsmanRun result = apiInstance.getCraftsmanRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#getCraftsmanRun");
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
| getCraftsmanRunRequest | [**APIgetCraftsmanRunRequest**](CraftsmanApi.md#APIgetCraftsmanRunRequest)|-|-|

### Return type

[**CraftsmanRun**](CraftsmanRun.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current lifecycle and terminal result when available. |  -  |
| **0** | The request failed. |  -  |

## getCraftsmanRunWithHttpInfo

> ApiResponse<CraftsmanRun> getCraftsmanRunWithHttpInfo(getCraftsmanRunRequest)

Get Craftsman run lifecycle and evidence

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIgetCraftsmanRunRequest request = APIgetCraftsmanRunRequest.newBuilder()
                .runId(runId)
                .build();
            ApiResponse<CraftsmanRun> response = apiInstance.getCraftsmanRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#getCraftsmanRun");
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
| getCraftsmanRunRequest | [**APIgetCraftsmanRunRequest**](CraftsmanApi.md#APIgetCraftsmanRunRequest)|-|-|

### Return type

ApiResponse<[**CraftsmanRun**](CraftsmanRun.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current lifecycle and terminal result when available. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetCraftsmanRunRequest"></a>
## APIgetCraftsmanRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## getCraftsmanRunTranscript

> Object getCraftsmanRunTranscript(getCraftsmanRunTranscriptRequest)

Get a Craftsman Streaming semantic transcript

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIgetCraftsmanRunTranscriptRequest request = APIgetCraftsmanRunTranscriptRequest.newBuilder()
                .runId(runId)
                .build();
            Object result = apiInstance.getCraftsmanRunTranscript(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#getCraftsmanRunTranscript");
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
| getCraftsmanRunTranscriptRequest | [**APIgetCraftsmanRunTranscriptRequest**](CraftsmanApi.md#APIgetCraftsmanRunTranscriptRequest)|-|-|

### Return type

**Object**


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bounded semantic event transcript captured by Sentinel. Use the completed run result for connection, assertion, and termination evidence required by Generate Spec. |  -  |
| **0** | The request failed. |  -  |

## getCraftsmanRunTranscriptWithHttpInfo

> ApiResponse<Object> getCraftsmanRunTranscriptWithHttpInfo(getCraftsmanRunTranscriptRequest)

Get a Craftsman Streaming semantic transcript

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIgetCraftsmanRunTranscriptRequest request = APIgetCraftsmanRunTranscriptRequest.newBuilder()
                .runId(runId)
                .build();
            ApiResponse<Object> response = apiInstance.getCraftsmanRunTranscriptWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#getCraftsmanRunTranscript");
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
| getCraftsmanRunTranscriptRequest | [**APIgetCraftsmanRunTranscriptRequest**](CraftsmanApi.md#APIgetCraftsmanRunTranscriptRequest)|-|-|

### Return type

ApiResponse<**Object**>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bounded semantic event transcript captured by Sentinel. Use the completed run result for connection, assertion, and termination evidence required by Generate Spec. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetCraftsmanRunTranscriptRequest"></a>
## APIgetCraftsmanRunTranscriptRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## getDocumentAsset

> DocumentAssetReference getDocumentAsset(getDocumentAssetRequest)

Resolve request attachment metadata

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID assetId = UUID.randomUUID(); // UUID |
        String fieldName = "file"; // String |
        String contentId = "contentId_example"; // String |
        try {
            APIgetDocumentAssetRequest request = APIgetDocumentAssetRequest.newBuilder()
                .assetId(assetId)
                .fieldName(fieldName)
                .contentId(contentId)
                .build();
            DocumentAssetReference result = apiInstance.getDocumentAsset(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#getDocumentAsset");
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
| getDocumentAssetRequest | [**APIgetDocumentAssetRequest**](CraftsmanApi.md#APIgetDocumentAssetRequest)|-|-|

### Return type

[**DocumentAssetReference**](DocumentAssetReference.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attachment metadata suitable for reuse in a saved request or specification. |  -  |
| **0** | The request failed. |  -  |

## getDocumentAssetWithHttpInfo

> ApiResponse<DocumentAssetReference> getDocumentAssetWithHttpInfo(getDocumentAssetRequest)

Resolve request attachment metadata

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID assetId = UUID.randomUUID(); // UUID |
        String fieldName = "file"; // String |
        String contentId = "contentId_example"; // String |
        try {
            APIgetDocumentAssetRequest request = APIgetDocumentAssetRequest.newBuilder()
                .assetId(assetId)
                .fieldName(fieldName)
                .contentId(contentId)
                .build();
            ApiResponse<DocumentAssetReference> response = apiInstance.getDocumentAssetWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#getDocumentAsset");
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
| getDocumentAssetRequest | [**APIgetDocumentAssetRequest**](CraftsmanApi.md#APIgetDocumentAssetRequest)|-|-|

### Return type

ApiResponse<[**DocumentAssetReference**](DocumentAssetReference.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attachment metadata suitable for reuse in a saved request or specification. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetDocumentAssetRequest"></a>
## APIgetDocumentAssetRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **assetId** | **UUID** |  | |
| **fieldName** | **String** |  | [optional] [default to file] |
| **contentId** | **String** |  | [optional] |



## getRequestWorkspace

> RequestWorkspace getRequestWorkspace(getRequestWorkspaceRequest)

Get a request workspace

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID workspaceId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Craftsman request workspace.
        try {
            APIgetRequestWorkspaceRequest request = APIgetRequestWorkspaceRequest.newBuilder()
                .workspaceId(workspaceId)
                .build();
            RequestWorkspace result = apiInstance.getRequestWorkspace(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#getRequestWorkspace");
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
| getRequestWorkspaceRequest | [**APIgetRequestWorkspaceRequest**](CraftsmanApi.md#APIgetRequestWorkspaceRequest)|-|-|

### Return type

[**RequestWorkspace**](RequestWorkspace.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The complete workspace tree. |  -  |
| **0** | The request failed. |  -  |

## getRequestWorkspaceWithHttpInfo

> ApiResponse<RequestWorkspace> getRequestWorkspaceWithHttpInfo(getRequestWorkspaceRequest)

Get a request workspace

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID workspaceId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Craftsman request workspace.
        try {
            APIgetRequestWorkspaceRequest request = APIgetRequestWorkspaceRequest.newBuilder()
                .workspaceId(workspaceId)
                .build();
            ApiResponse<RequestWorkspace> response = apiInstance.getRequestWorkspaceWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#getRequestWorkspace");
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
| getRequestWorkspaceRequest | [**APIgetRequestWorkspaceRequest**](CraftsmanApi.md#APIgetRequestWorkspaceRequest)|-|-|

### Return type

ApiResponse<[**RequestWorkspace**](RequestWorkspace.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The complete workspace tree. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetRequestWorkspaceRequest"></a>
## APIgetRequestWorkspaceRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **workspaceId** | **UUID** | UUIDv7 identifier of the Craftsman request workspace. | |



## listRequestWorkspaces

> RequestWorkspacePage listRequestWorkspaces(listRequestWorkspacesRequest)

List request workspaces

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistRequestWorkspacesRequest request = APIlistRequestWorkspacesRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .build();
            RequestWorkspacePage result = apiInstance.listRequestWorkspaces(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#listRequestWorkspaces");
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
| listRequestWorkspacesRequest | [**APIlistRequestWorkspacesRequest**](CraftsmanApi.md#APIlistRequestWorkspacesRequest)|-|-|

### Return type

[**RequestWorkspacePage**](RequestWorkspacePage.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of request workspaces. |  -  |
| **0** | The request failed. |  -  |

## listRequestWorkspacesWithHttpInfo

> ApiResponse<RequestWorkspacePage> listRequestWorkspacesWithHttpInfo(listRequestWorkspacesRequest)

List request workspaces

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistRequestWorkspacesRequest request = APIlistRequestWorkspacesRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .build();
            ApiResponse<RequestWorkspacePage> response = apiInstance.listRequestWorkspacesWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#listRequestWorkspaces");
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
| listRequestWorkspacesRequest | [**APIlistRequestWorkspacesRequest**](CraftsmanApi.md#APIlistRequestWorkspacesRequest)|-|-|

### Return type

ApiResponse<[**RequestWorkspacePage**](RequestWorkspacePage.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of request workspaces. |  -  |
| **0** | The request failed. |  -  |


<a id="APIlistRequestWorkspacesRequest"></a>
## APIlistRequestWorkspacesRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **String** | Case-insensitive server-side search within the active project. | [optional] |



## queueCraftsmanStreamingRun

> CraftsmanRunAccepted queueCraftsmanStreamingRun(queueCraftsmanStreamingRunRequest)

Queue a standalone bounded Streaming session

Standalone sessions require concrete values and do not inherit Workflow variables.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        CraftsmanStreamingRunInput craftsmanStreamingRunInput = new CraftsmanStreamingRunInput(); // CraftsmanStreamingRunInput |
        try {
            APIqueueCraftsmanStreamingRunRequest request = APIqueueCraftsmanStreamingRunRequest.newBuilder()
                .craftsmanStreamingRunInput(craftsmanStreamingRunInput)
                .build();
            CraftsmanRunAccepted result = apiInstance.queueCraftsmanStreamingRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#queueCraftsmanStreamingRun");
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
| queueCraftsmanStreamingRunRequest | [**APIqueueCraftsmanStreamingRunRequest**](CraftsmanApi.md#APIqueueCraftsmanStreamingRunRequest)|-|-|

### Return type

[**CraftsmanRunAccepted**](CraftsmanRunAccepted.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The bounded session was accepted. |  -  |
| **0** | The request failed. |  -  |

## queueCraftsmanStreamingRunWithHttpInfo

> ApiResponse<CraftsmanRunAccepted> queueCraftsmanStreamingRunWithHttpInfo(queueCraftsmanStreamingRunRequest)

Queue a standalone bounded Streaming session

Standalone sessions require concrete values and do not inherit Workflow variables.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        CraftsmanStreamingRunInput craftsmanStreamingRunInput = new CraftsmanStreamingRunInput(); // CraftsmanStreamingRunInput |
        try {
            APIqueueCraftsmanStreamingRunRequest request = APIqueueCraftsmanStreamingRunRequest.newBuilder()
                .craftsmanStreamingRunInput(craftsmanStreamingRunInput)
                .build();
            ApiResponse<CraftsmanRunAccepted> response = apiInstance.queueCraftsmanStreamingRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#queueCraftsmanStreamingRun");
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
| queueCraftsmanStreamingRunRequest | [**APIqueueCraftsmanStreamingRunRequest**](CraftsmanApi.md#APIqueueCraftsmanStreamingRunRequest)|-|-|

### Return type

ApiResponse<[**CraftsmanRunAccepted**](CraftsmanRunAccepted.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The bounded session was accepted. |  -  |
| **0** | The request failed. |  -  |


<a id="APIqueueCraftsmanStreamingRunRequest"></a>
## APIqueueCraftsmanStreamingRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **craftsmanStreamingRunInput** | [**CraftsmanStreamingRunInput**](CraftsmanStreamingRunInput.md) |  | |



## queueCraftsmanWorkflowRun

> CraftsmanRunAccepted queueCraftsmanWorkflowRun(queueCraftsmanWorkflowRunRequest)

Queue a saved request or mixed-protocol Workflow run

Supports REST, SOAP, GraphQL, WebSocket/WSS, SSE, gRPC Streaming, and MQTT nodes. Poll the returned run id.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID workspaceId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Craftsman request workspace.
        UUID nodeId = UUID.randomUUID(); // UUID |
        RequestChainRunInput requestChainRunInput = new RequestChainRunInput(); // RequestChainRunInput |
        try {
            APIqueueCraftsmanWorkflowRunRequest request = APIqueueCraftsmanWorkflowRunRequest.newBuilder()
                .workspaceId(workspaceId)
                .nodeId(nodeId)
                .requestChainRunInput(requestChainRunInput)
                .build();
            CraftsmanRunAccepted result = apiInstance.queueCraftsmanWorkflowRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#queueCraftsmanWorkflowRun");
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
| queueCraftsmanWorkflowRunRequest | [**APIqueueCraftsmanWorkflowRunRequest**](CraftsmanApi.md#APIqueueCraftsmanWorkflowRunRequest)|-|-|

### Return type

[**CraftsmanRunAccepted**](CraftsmanRunAccepted.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The bounded Craftsman run was accepted. |  -  |
| **0** | The request failed. |  -  |

## queueCraftsmanWorkflowRunWithHttpInfo

> ApiResponse<CraftsmanRunAccepted> queueCraftsmanWorkflowRunWithHttpInfo(queueCraftsmanWorkflowRunRequest)

Queue a saved request or mixed-protocol Workflow run

Supports REST, SOAP, GraphQL, WebSocket/WSS, SSE, gRPC Streaming, and MQTT nodes. Poll the returned run id.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID workspaceId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Craftsman request workspace.
        UUID nodeId = UUID.randomUUID(); // UUID |
        RequestChainRunInput requestChainRunInput = new RequestChainRunInput(); // RequestChainRunInput |
        try {
            APIqueueCraftsmanWorkflowRunRequest request = APIqueueCraftsmanWorkflowRunRequest.newBuilder()
                .workspaceId(workspaceId)
                .nodeId(nodeId)
                .requestChainRunInput(requestChainRunInput)
                .build();
            ApiResponse<CraftsmanRunAccepted> response = apiInstance.queueCraftsmanWorkflowRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#queueCraftsmanWorkflowRun");
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
| queueCraftsmanWorkflowRunRequest | [**APIqueueCraftsmanWorkflowRunRequest**](CraftsmanApi.md#APIqueueCraftsmanWorkflowRunRequest)|-|-|

### Return type

ApiResponse<[**CraftsmanRunAccepted**](CraftsmanRunAccepted.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The bounded Craftsman run was accepted. |  -  |
| **0** | The request failed. |  -  |


<a id="APIqueueCraftsmanWorkflowRunRequest"></a>
## APIqueueCraftsmanWorkflowRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **workspaceId** | **UUID** | UUIDv7 identifier of the Craftsman request workspace. | |
| **nodeId** | **UUID** |  | |
| **requestChainRunInput** | [**RequestChainRunInput**](RequestChainRunInput.md) |  | [optional] |



## updateRequestNode

> RequestNode updateRequestNode(updateRequestNodeRequest)

Update a folder or saved request

Replaces the selected node definition. STREAMING requests use streamingSpec and do not accept HTTP request fields.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID workspaceId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Craftsman request workspace.
        UUID nodeId = UUID.randomUUID(); // UUID |
        RequestNodeInput requestNodeInput = new RequestNodeInput(); // RequestNodeInput |
        try {
            APIupdateRequestNodeRequest request = APIupdateRequestNodeRequest.newBuilder()
                .workspaceId(workspaceId)
                .nodeId(nodeId)
                .requestNodeInput(requestNodeInput)
                .build();
            RequestNode result = apiInstance.updateRequestNode(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#updateRequestNode");
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
| updateRequestNodeRequest | [**APIupdateRequestNodeRequest**](CraftsmanApi.md#APIupdateRequestNodeRequest)|-|-|

### Return type

[**RequestNode**](RequestNode.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated workspace node. |  -  |
| **0** | The request failed. |  -  |

## updateRequestNodeWithHttpInfo

> ApiResponse<RequestNode> updateRequestNodeWithHttpInfo(updateRequestNodeRequest)

Update a folder or saved request

Replaces the selected node definition. STREAMING requests use streamingSpec and do not accept HTTP request fields.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID workspaceId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Craftsman request workspace.
        UUID nodeId = UUID.randomUUID(); // UUID |
        RequestNodeInput requestNodeInput = new RequestNodeInput(); // RequestNodeInput |
        try {
            APIupdateRequestNodeRequest request = APIupdateRequestNodeRequest.newBuilder()
                .workspaceId(workspaceId)
                .nodeId(nodeId)
                .requestNodeInput(requestNodeInput)
                .build();
            ApiResponse<RequestNode> response = apiInstance.updateRequestNodeWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#updateRequestNode");
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
| updateRequestNodeRequest | [**APIupdateRequestNodeRequest**](CraftsmanApi.md#APIupdateRequestNodeRequest)|-|-|

### Return type

ApiResponse<[**RequestNode**](RequestNode.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated workspace node. |  -  |
| **0** | The request failed. |  -  |


<a id="APIupdateRequestNodeRequest"></a>
## APIupdateRequestNodeRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **workspaceId** | **UUID** | UUIDv7 identifier of the Craftsman request workspace. | |
| **nodeId** | **UUID** |  | |
| **requestNodeInput** | [**RequestNodeInput**](RequestNodeInput.md) |  | |



## updateRequestWorkspace

> RequestWorkspace updateRequestWorkspace(updateRequestWorkspaceRequest)

Replace request workspace metadata and variables

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID workspaceId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Craftsman request workspace.
        RequestWorkspaceInput requestWorkspaceInput = new RequestWorkspaceInput(); // RequestWorkspaceInput |
        try {
            APIupdateRequestWorkspaceRequest request = APIupdateRequestWorkspaceRequest.newBuilder()
                .workspaceId(workspaceId)
                .requestWorkspaceInput(requestWorkspaceInput)
                .build();
            RequestWorkspace result = apiInstance.updateRequestWorkspace(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#updateRequestWorkspace");
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
| updateRequestWorkspaceRequest | [**APIupdateRequestWorkspaceRequest**](CraftsmanApi.md#APIupdateRequestWorkspaceRequest)|-|-|

### Return type

[**RequestWorkspace**](RequestWorkspace.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated workspace. |  -  |
| **0** | The request failed. |  -  |

## updateRequestWorkspaceWithHttpInfo

> ApiResponse<RequestWorkspace> updateRequestWorkspaceWithHttpInfo(updateRequestWorkspaceRequest)

Replace request workspace metadata and variables

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        UUID workspaceId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Craftsman request workspace.
        RequestWorkspaceInput requestWorkspaceInput = new RequestWorkspaceInput(); // RequestWorkspaceInput |
        try {
            APIupdateRequestWorkspaceRequest request = APIupdateRequestWorkspaceRequest.newBuilder()
                .workspaceId(workspaceId)
                .requestWorkspaceInput(requestWorkspaceInput)
                .build();
            ApiResponse<RequestWorkspace> response = apiInstance.updateRequestWorkspaceWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#updateRequestWorkspace");
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
| updateRequestWorkspaceRequest | [**APIupdateRequestWorkspaceRequest**](CraftsmanApi.md#APIupdateRequestWorkspaceRequest)|-|-|

### Return type

ApiResponse<[**RequestWorkspace**](RequestWorkspace.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated workspace. |  -  |
| **0** | The request failed. |  -  |


<a id="APIupdateRequestWorkspaceRequest"></a>
## APIupdateRequestWorkspaceRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **workspaceId** | **UUID** | UUIDv7 identifier of the Craftsman request workspace. | |
| **requestWorkspaceInput** | [**RequestWorkspaceInput**](RequestWorkspaceInput.md) |  | |



## uploadDocumentAsset

> DocumentAssetReference uploadDocumentAsset(uploadDocumentAssetRequest)

Upload a reusable request attachment

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        File _file = new File("/path/to/file"); // File |
        String fieldName = "file"; // String |
        String contentId = "contentId_example"; // String |
        try {
            APIuploadDocumentAssetRequest request = APIuploadDocumentAssetRequest.newBuilder()
                ._file(_file)
                .fieldName(fieldName)
                .contentId(contentId)
                .build();
            DocumentAssetReference result = apiInstance.uploadDocumentAsset(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#uploadDocumentAsset");
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
| uploadDocumentAssetRequest | [**APIuploadDocumentAssetRequest**](CraftsmanApi.md#APIuploadDocumentAssetRequest)|-|-|

### Return type

[**DocumentAssetReference**](DocumentAssetReference.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Immutable content-addressed attachment reference. |  -  |
| **0** | The request failed. |  -  |

## uploadDocumentAssetWithHttpInfo

> ApiResponse<DocumentAssetReference> uploadDocumentAssetWithHttpInfo(uploadDocumentAssetRequest)

Upload a reusable request attachment

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.CraftsmanApi;
import software.ste.sdk.generated.api.CraftsmanApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        CraftsmanApi apiInstance = new CraftsmanApi(defaultClient);
        File _file = new File("/path/to/file"); // File |
        String fieldName = "file"; // String |
        String contentId = "contentId_example"; // String |
        try {
            APIuploadDocumentAssetRequest request = APIuploadDocumentAssetRequest.newBuilder()
                ._file(_file)
                .fieldName(fieldName)
                .contentId(contentId)
                .build();
            ApiResponse<DocumentAssetReference> response = apiInstance.uploadDocumentAssetWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CraftsmanApi#uploadDocumentAsset");
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
| uploadDocumentAssetRequest | [**APIuploadDocumentAssetRequest**](CraftsmanApi.md#APIuploadDocumentAssetRequest)|-|-|

### Return type

ApiResponse<[**DocumentAssetReference**](DocumentAssetReference.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Immutable content-addressed attachment reference. |  -  |
| **0** | The request failed. |  -  |


<a id="APIuploadDocumentAssetRequest"></a>
## APIuploadDocumentAssetRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **_file** | **File** |  | |
| **fieldName** | **String** |  | [optional] [default to file] |
| **contentId** | **String** |  | [optional] |
