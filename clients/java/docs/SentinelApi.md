# SentinelApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSentinelCheck**](SentinelApi.md#createSentinelCheck) | **POST** /sentinel/checks | Create a Sentinel check |
| [**createSentinelCheckWithHttpInfo**](SentinelApi.md#createSentinelCheckWithHttpInfo) | **POST** /sentinel/checks | Create a Sentinel check |
| [**deleteSentinelCheck**](SentinelApi.md#deleteSentinelCheck) | **DELETE** /sentinel/checks/{checkId} | Delete a Sentinel check |
| [**deleteSentinelCheckWithHttpInfo**](SentinelApi.md#deleteSentinelCheckWithHttpInfo) | **DELETE** /sentinel/checks/{checkId} | Delete a Sentinel check |
| [**enqueueSentinelRun**](SentinelApi.md#enqueueSentinelRun) | **POST** /sentinel/checks/{checkId}/run | Queue a Sentinel run |
| [**enqueueSentinelRunWithHttpInfo**](SentinelApi.md#enqueueSentinelRunWithHttpInfo) | **POST** /sentinel/checks/{checkId}/run | Queue a Sentinel run |
| [**getSentinelCheck**](SentinelApi.md#getSentinelCheck) | **GET** /sentinel/checks/{checkId} | Get a Sentinel check |
| [**getSentinelCheckWithHttpInfo**](SentinelApi.md#getSentinelCheckWithHttpInfo) | **GET** /sentinel/checks/{checkId} | Get a Sentinel check |
| [**getSentinelDashboardSummary**](SentinelApi.md#getSentinelDashboardSummary) | **GET** /sentinel/dashboard/summary | Get Sentinel dashboard summary |
| [**getSentinelDashboardSummaryWithHttpInfo**](SentinelApi.md#getSentinelDashboardSummaryWithHttpInfo) | **GET** /sentinel/dashboard/summary | Get Sentinel dashboard summary |
| [**getSentinelRun**](SentinelApi.md#getSentinelRun) | **GET** /sentinel/runs/{runId} | Get Sentinel run evidence |
| [**getSentinelRunWithHttpInfo**](SentinelApi.md#getSentinelRunWithHttpInfo) | **GET** /sentinel/runs/{runId} | Get Sentinel run evidence |
| [**listLatestSentinelRuns**](SentinelApi.md#listLatestSentinelRuns) | **GET** /sentinel/runs | List latest Sentinel runs |
| [**listLatestSentinelRunsWithHttpInfo**](SentinelApi.md#listLatestSentinelRunsWithHttpInfo) | **GET** /sentinel/runs | List latest Sentinel runs |
| [**listSentinelChecks**](SentinelApi.md#listSentinelChecks) | **GET** /sentinel/checks/page | List Sentinel checks |
| [**listSentinelChecksWithHttpInfo**](SentinelApi.md#listSentinelChecksWithHttpInfo) | **GET** /sentinel/checks/page | List Sentinel checks |
| [**listSentinelDashboardIncidents**](SentinelApi.md#listSentinelDashboardIncidents) | **GET** /sentinel/dashboard/incidents | List recent Sentinel incidents |
| [**listSentinelDashboardIncidentsWithHttpInfo**](SentinelApi.md#listSentinelDashboardIncidentsWithHttpInfo) | **GET** /sentinel/dashboard/incidents | List recent Sentinel incidents |
| [**listSentinelLinkedAssets**](SentinelApi.md#listSentinelLinkedAssets) | **GET** /sentinel/checks/spec-links/page | List compact Sentinel links for one Automation asset type |
| [**listSentinelLinkedAssetsWithHttpInfo**](SentinelApi.md#listSentinelLinkedAssetsWithHttpInfo) | **GET** /sentinel/checks/spec-links/page | List compact Sentinel links for one Automation asset type |
| [**listSentinelRuns**](SentinelApi.md#listSentinelRuns) | **GET** /sentinel/runs/page | List Sentinel runs |
| [**listSentinelRunsWithHttpInfo**](SentinelApi.md#listSentinelRunsWithHttpInfo) | **GET** /sentinel/runs/page | List Sentinel runs |
| [**sampleSentinelRuns**](SentinelApi.md#sampleSentinelRuns) | **GET** /sentinel/runs/sample | Sample Sentinel runs |
| [**sampleSentinelRunsWithHttpInfo**](SentinelApi.md#sampleSentinelRunsWithHttpInfo) | **GET** /sentinel/runs/sample | Sample Sentinel runs |
| [**updateSentinelCheck**](SentinelApi.md#updateSentinelCheck) | **PUT** /sentinel/checks/{checkId} | Replace a Sentinel check configuration |
| [**updateSentinelCheckWithHttpInfo**](SentinelApi.md#updateSentinelCheckWithHttpInfo) | **PUT** /sentinel/checks/{checkId} | Replace a Sentinel check configuration |



## createSentinelCheck

> SentinelCheck createSentinelCheck(createSentinelCheckRequest)

Create a Sentinel check

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        SentinelCheckInput sentinelCheckInput = new SentinelCheckInput(); // SentinelCheckInput |
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateSentinelCheckRequest request = APIcreateSentinelCheckRequest.newBuilder()
                .sentinelCheckInput(sentinelCheckInput)
                .idempotencyKey(idempotencyKey)
                .build();
            SentinelCheck result = apiInstance.createSentinelCheck(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#createSentinelCheck");
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
| createSentinelCheckRequest | [**APIcreateSentinelCheckRequest**](SentinelApi.md#APIcreateSentinelCheckRequest)|-|-|

### Return type

[**SentinelCheck**](SentinelCheck.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created check. |  -  |
| **0** | The request failed. |  -  |

## createSentinelCheckWithHttpInfo

> ApiResponse<SentinelCheck> createSentinelCheckWithHttpInfo(createSentinelCheckRequest)

Create a Sentinel check

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        SentinelCheckInput sentinelCheckInput = new SentinelCheckInput(); // SentinelCheckInput |
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateSentinelCheckRequest request = APIcreateSentinelCheckRequest.newBuilder()
                .sentinelCheckInput(sentinelCheckInput)
                .idempotencyKey(idempotencyKey)
                .build();
            ApiResponse<SentinelCheck> response = apiInstance.createSentinelCheckWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#createSentinelCheck");
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
| createSentinelCheckRequest | [**APIcreateSentinelCheckRequest**](SentinelApi.md#APIcreateSentinelCheckRequest)|-|-|

### Return type

ApiResponse<[**SentinelCheck**](SentinelCheck.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created check. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcreateSentinelCheckRequest"></a>
## APIcreateSentinelCheckRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **sentinelCheckInput** | [**SentinelCheckInput**](SentinelCheckInput.md) |  | |
| **idempotencyKey** | **UUID** | A caller-generated UUID retained for safe write retries where supported. | [optional] |



## deleteSentinelCheck

> void deleteSentinelCheck(deleteSentinelCheckRequest)

Delete a Sentinel check

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        UUID checkId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Sentinel check.
        try {
            APIdeleteSentinelCheckRequest request = APIdeleteSentinelCheckRequest.newBuilder()
                .checkId(checkId)
                .build();
            apiInstance.deleteSentinelCheck(request);
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#deleteSentinelCheck");
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
| deleteSentinelCheckRequest | [**APIdeleteSentinelCheckRequest**](SentinelApi.md#APIdeleteSentinelCheckRequest)|-|-|

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
| **204** | Check deleted. |  -  |
| **0** | The request failed. |  -  |

## deleteSentinelCheckWithHttpInfo

> ApiResponse<Void> deleteSentinelCheckWithHttpInfo(deleteSentinelCheckRequest)

Delete a Sentinel check

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        UUID checkId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Sentinel check.
        try {
            APIdeleteSentinelCheckRequest request = APIdeleteSentinelCheckRequest.newBuilder()
                .checkId(checkId)
                .build();
            ApiResponse<Void> response = apiInstance.deleteSentinelCheckWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#deleteSentinelCheck");
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
| deleteSentinelCheckRequest | [**APIdeleteSentinelCheckRequest**](SentinelApi.md#APIdeleteSentinelCheckRequest)|-|-|

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
| **204** | Check deleted. |  -  |
| **0** | The request failed. |  -  |


<a id="APIdeleteSentinelCheckRequest"></a>
## APIdeleteSentinelCheckRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **checkId** | **UUID** | UUIDv7 identifier of the Sentinel check. | |



## enqueueSentinelRun

> RunEnqueueResponse enqueueSentinelRun(enqueueSentinelRunRequest)

Queue a Sentinel run

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        UUID checkId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Sentinel check.
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        String region = "local"; // String |
        try {
            APIenqueueSentinelRunRequest request = APIenqueueSentinelRunRequest.newBuilder()
                .checkId(checkId)
                .idempotencyKey(idempotencyKey)
                .region(region)
                .build();
            RunEnqueueResponse result = apiInstance.enqueueSentinelRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#enqueueSentinelRun");
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
| enqueueSentinelRunRequest | [**APIenqueueSentinelRunRequest**](SentinelApi.md#APIenqueueSentinelRunRequest)|-|-|

### Return type

[**RunEnqueueResponse**](RunEnqueueResponse.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Queue acknowledgement and execution id. |  -  |
| **0** | The request failed. |  -  |

## enqueueSentinelRunWithHttpInfo

> ApiResponse<RunEnqueueResponse> enqueueSentinelRunWithHttpInfo(enqueueSentinelRunRequest)

Queue a Sentinel run

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        UUID checkId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Sentinel check.
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        String region = "local"; // String |
        try {
            APIenqueueSentinelRunRequest request = APIenqueueSentinelRunRequest.newBuilder()
                .checkId(checkId)
                .idempotencyKey(idempotencyKey)
                .region(region)
                .build();
            ApiResponse<RunEnqueueResponse> response = apiInstance.enqueueSentinelRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#enqueueSentinelRun");
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
| enqueueSentinelRunRequest | [**APIenqueueSentinelRunRequest**](SentinelApi.md#APIenqueueSentinelRunRequest)|-|-|

### Return type

ApiResponse<[**RunEnqueueResponse**](RunEnqueueResponse.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Queue acknowledgement and execution id. |  -  |
| **0** | The request failed. |  -  |


<a id="APIenqueueSentinelRunRequest"></a>
## APIenqueueSentinelRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **checkId** | **UUID** | UUIDv7 identifier of the Sentinel check. | |
| **idempotencyKey** | **UUID** | A caller-generated UUID retained for safe write retries where supported. | [optional] |
| **region** | **String** |  | [optional] [default to local] |



## getSentinelCheck

> SentinelCheck getSentinelCheck(getSentinelCheckRequest)

Get a Sentinel check

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        UUID checkId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Sentinel check.
        try {
            APIgetSentinelCheckRequest request = APIgetSentinelCheckRequest.newBuilder()
                .checkId(checkId)
                .build();
            SentinelCheck result = apiInstance.getSentinelCheck(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#getSentinelCheck");
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
| getSentinelCheckRequest | [**APIgetSentinelCheckRequest**](SentinelApi.md#APIgetSentinelCheckRequest)|-|-|

### Return type

[**SentinelCheck**](SentinelCheck.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested check. |  -  |
| **0** | The request failed. |  -  |

## getSentinelCheckWithHttpInfo

> ApiResponse<SentinelCheck> getSentinelCheckWithHttpInfo(getSentinelCheckRequest)

Get a Sentinel check

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        UUID checkId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Sentinel check.
        try {
            APIgetSentinelCheckRequest request = APIgetSentinelCheckRequest.newBuilder()
                .checkId(checkId)
                .build();
            ApiResponse<SentinelCheck> response = apiInstance.getSentinelCheckWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#getSentinelCheck");
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
| getSentinelCheckRequest | [**APIgetSentinelCheckRequest**](SentinelApi.md#APIgetSentinelCheckRequest)|-|-|

### Return type

ApiResponse<[**SentinelCheck**](SentinelCheck.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested check. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetSentinelCheckRequest"></a>
## APIgetSentinelCheckRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **checkId** | **UUID** | UUIDv7 identifier of the Sentinel check. | |



## getSentinelDashboardSummary

> SentinelDashboardSummary getSentinelDashboardSummary(getSentinelDashboardSummaryRequest)

Get Sentinel dashboard summary

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        String environment = "environment_example"; // String | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
        try {
            APIgetSentinelDashboardSummaryRequest request = APIgetSentinelDashboardSummaryRequest.newBuilder()
                .environment(environment)
                .build();
            SentinelDashboardSummary result = apiInstance.getSentinelDashboardSummary(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#getSentinelDashboardSummary");
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
| getSentinelDashboardSummaryRequest | [**APIgetSentinelDashboardSummaryRequest**](SentinelApi.md#APIgetSentinelDashboardSummaryRequest)|-|-|

### Return type

[**SentinelDashboardSummary**](SentinelDashboardSummary.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Environment-scoped Sentinel dashboard counters and latency summary. |  -  |
| **0** | The request failed. |  -  |

## getSentinelDashboardSummaryWithHttpInfo

> ApiResponse<SentinelDashboardSummary> getSentinelDashboardSummaryWithHttpInfo(getSentinelDashboardSummaryRequest)

Get Sentinel dashboard summary

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        String environment = "environment_example"; // String | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
        try {
            APIgetSentinelDashboardSummaryRequest request = APIgetSentinelDashboardSummaryRequest.newBuilder()
                .environment(environment)
                .build();
            ApiResponse<SentinelDashboardSummary> response = apiInstance.getSentinelDashboardSummaryWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#getSentinelDashboardSummary");
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
| getSentinelDashboardSummaryRequest | [**APIgetSentinelDashboardSummaryRequest**](SentinelApi.md#APIgetSentinelDashboardSummaryRequest)|-|-|

### Return type

ApiResponse<[**SentinelDashboardSummary**](SentinelDashboardSummary.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Environment-scoped Sentinel dashboard counters and latency summary. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetSentinelDashboardSummaryRequest"></a>
## APIgetSentinelDashboardSummaryRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **environment** | **String** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. | |



## getSentinelRun

> SentinelRun getSentinelRun(getSentinelRunRequest)

Get Sentinel run evidence

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIgetSentinelRunRequest request = APIgetSentinelRunRequest.newBuilder()
                .runId(runId)
                .build();
            SentinelRun result = apiInstance.getSentinelRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#getSentinelRun");
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
| getSentinelRunRequest | [**APIgetSentinelRunRequest**](SentinelApi.md#APIgetSentinelRunRequest)|-|-|

### Return type

[**SentinelRun**](SentinelRun.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Run, retry attempts, response preview, and baseline evidence. |  -  |
| **0** | The request failed. |  -  |

## getSentinelRunWithHttpInfo

> ApiResponse<SentinelRun> getSentinelRunWithHttpInfo(getSentinelRunRequest)

Get Sentinel run evidence

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIgetSentinelRunRequest request = APIgetSentinelRunRequest.newBuilder()
                .runId(runId)
                .build();
            ApiResponse<SentinelRun> response = apiInstance.getSentinelRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#getSentinelRun");
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
| getSentinelRunRequest | [**APIgetSentinelRunRequest**](SentinelApi.md#APIgetSentinelRunRequest)|-|-|

### Return type

ApiResponse<[**SentinelRun**](SentinelRun.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Run, retry attempts, response preview, and baseline evidence. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetSentinelRunRequest"></a>
## APIgetSentinelRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## listLatestSentinelRuns

> List<SentinelRun> listLatestSentinelRuns(listLatestSentinelRunsRequest)

List latest Sentinel runs

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        String environment = "environment_example"; // String | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIlistLatestSentinelRunsRequest request = APIlistLatestSentinelRunsRequest.newBuilder()
                .environment(environment)
                .size(size)
                .build();
            List<SentinelRun> result = apiInstance.listLatestSentinelRuns(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#listLatestSentinelRuns");
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
| listLatestSentinelRunsRequest | [**APIlistLatestSentinelRunsRequest**](SentinelApi.md#APIlistLatestSentinelRunsRequest)|-|-|

### Return type

[**List&lt;SentinelRun&gt;**](SentinelRun.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The latest Sentinel runs for the selected environment. |  -  |
| **0** | The request failed. |  -  |

## listLatestSentinelRunsWithHttpInfo

> ApiResponse<List<SentinelRun>> listLatestSentinelRunsWithHttpInfo(listLatestSentinelRunsRequest)

List latest Sentinel runs

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        String environment = "environment_example"; // String | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIlistLatestSentinelRunsRequest request = APIlistLatestSentinelRunsRequest.newBuilder()
                .environment(environment)
                .size(size)
                .build();
            ApiResponse<List<SentinelRun>> response = apiInstance.listLatestSentinelRunsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#listLatestSentinelRuns");
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
| listLatestSentinelRunsRequest | [**APIlistLatestSentinelRunsRequest**](SentinelApi.md#APIlistLatestSentinelRunsRequest)|-|-|

### Return type

ApiResponse<[**List&lt;SentinelRun&gt;**](SentinelRun.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The latest Sentinel runs for the selected environment. |  -  |
| **0** | The request failed. |  -  |


<a id="APIlistLatestSentinelRunsRequest"></a>
## APIlistLatestSentinelRunsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **environment** | **String** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. | |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |



## listSentinelChecks

> SentinelCheckPage listSentinelChecks(listSentinelChecksRequest)

List Sentinel checks

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        String environment = "environment_example"; // String | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistSentinelChecksRequest request = APIlistSentinelChecksRequest.newBuilder()
                .environment(environment)
                .page(page)
                .size(size)
                .search(search)
                .build();
            SentinelCheckPage result = apiInstance.listSentinelChecks(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#listSentinelChecks");
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
| listSentinelChecksRequest | [**APIlistSentinelChecksRequest**](SentinelApi.md#APIlistSentinelChecksRequest)|-|-|

### Return type

[**SentinelCheckPage**](SentinelCheckPage.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of Sentinel checks. |  -  |
| **0** | The request failed. |  -  |

## listSentinelChecksWithHttpInfo

> ApiResponse<SentinelCheckPage> listSentinelChecksWithHttpInfo(listSentinelChecksRequest)

List Sentinel checks

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        String environment = "environment_example"; // String | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistSentinelChecksRequest request = APIlistSentinelChecksRequest.newBuilder()
                .environment(environment)
                .page(page)
                .size(size)
                .search(search)
                .build();
            ApiResponse<SentinelCheckPage> response = apiInstance.listSentinelChecksWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#listSentinelChecks");
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
| listSentinelChecksRequest | [**APIlistSentinelChecksRequest**](SentinelApi.md#APIlistSentinelChecksRequest)|-|-|

### Return type

ApiResponse<[**SentinelCheckPage**](SentinelCheckPage.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of Sentinel checks. |  -  |
| **0** | The request failed. |  -  |


<a id="APIlistSentinelChecksRequest"></a>
## APIlistSentinelChecksRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **environment** | **String** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. | |
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **String** | Case-insensitive server-side search within the active project. | [optional] |



## listSentinelDashboardIncidents

> List<SentinelIncident> listSentinelDashboardIncidents(listSentinelDashboardIncidentsRequest)

List recent Sentinel incidents

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        String environment = "environment_example"; // String | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
        try {
            APIlistSentinelDashboardIncidentsRequest request = APIlistSentinelDashboardIncidentsRequest.newBuilder()
                .environment(environment)
                .build();
            List<SentinelIncident> result = apiInstance.listSentinelDashboardIncidents(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#listSentinelDashboardIncidents");
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
| listSentinelDashboardIncidentsRequest | [**APIlistSentinelDashboardIncidentsRequest**](SentinelApi.md#APIlistSentinelDashboardIncidentsRequest)|-|-|

### Return type

[**List&lt;SentinelIncident&gt;**](SentinelIncident.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recent incidents for the selected Sentinel environment. |  -  |
| **0** | The request failed. |  -  |

## listSentinelDashboardIncidentsWithHttpInfo

> ApiResponse<List<SentinelIncident>> listSentinelDashboardIncidentsWithHttpInfo(listSentinelDashboardIncidentsRequest)

List recent Sentinel incidents

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        String environment = "environment_example"; // String | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
        try {
            APIlistSentinelDashboardIncidentsRequest request = APIlistSentinelDashboardIncidentsRequest.newBuilder()
                .environment(environment)
                .build();
            ApiResponse<List<SentinelIncident>> response = apiInstance.listSentinelDashboardIncidentsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#listSentinelDashboardIncidents");
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
| listSentinelDashboardIncidentsRequest | [**APIlistSentinelDashboardIncidentsRequest**](SentinelApi.md#APIlistSentinelDashboardIncidentsRequest)|-|-|

### Return type

ApiResponse<[**List&lt;SentinelIncident&gt;**](SentinelIncident.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recent incidents for the selected Sentinel environment. |  -  |
| **0** | The request failed. |  -  |


<a id="APIlistSentinelDashboardIncidentsRequest"></a>
## APIlistSentinelDashboardIncidentsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **environment** | **String** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. | |



## listSentinelLinkedAssets

> SentinelLinkSummaryPage listSentinelLinkedAssets(listSentinelLinkedAssetsRequest)

List compact Sentinel links for one Automation asset type

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        String environment = "environment_example"; // String | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
        SentinelLinkedAssetCheckType checkType = SentinelLinkedAssetCheckType.fromValue("REST"); // SentinelLinkedAssetCheckType | Exact Automation asset type whose Sentinel links should be returned.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIlistSentinelLinkedAssetsRequest request = APIlistSentinelLinkedAssetsRequest.newBuilder()
                .environment(environment)
                .checkType(checkType)
                .page(page)
                .size(size)
                .build();
            SentinelLinkSummaryPage result = apiInstance.listSentinelLinkedAssets(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#listSentinelLinkedAssets");
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
| listSentinelLinkedAssetsRequest | [**APIlistSentinelLinkedAssetsRequest**](SentinelApi.md#APIlistSentinelLinkedAssetsRequest)|-|-|

### Return type

[**SentinelLinkSummaryPage**](SentinelLinkSummaryPage.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of normalized asset names and their Sentinel link counts. |  -  |
| **0** | The request failed. |  -  |

## listSentinelLinkedAssetsWithHttpInfo

> ApiResponse<SentinelLinkSummaryPage> listSentinelLinkedAssetsWithHttpInfo(listSentinelLinkedAssetsRequest)

List compact Sentinel links for one Automation asset type

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        String environment = "environment_example"; // String | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
        SentinelLinkedAssetCheckType checkType = SentinelLinkedAssetCheckType.fromValue("REST"); // SentinelLinkedAssetCheckType | Exact Automation asset type whose Sentinel links should be returned.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIlistSentinelLinkedAssetsRequest request = APIlistSentinelLinkedAssetsRequest.newBuilder()
                .environment(environment)
                .checkType(checkType)
                .page(page)
                .size(size)
                .build();
            ApiResponse<SentinelLinkSummaryPage> response = apiInstance.listSentinelLinkedAssetsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#listSentinelLinkedAssets");
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
| listSentinelLinkedAssetsRequest | [**APIlistSentinelLinkedAssetsRequest**](SentinelApi.md#APIlistSentinelLinkedAssetsRequest)|-|-|

### Return type

ApiResponse<[**SentinelLinkSummaryPage**](SentinelLinkSummaryPage.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of normalized asset names and their Sentinel link counts. |  -  |
| **0** | The request failed. |  -  |


<a id="APIlistSentinelLinkedAssetsRequest"></a>
## APIlistSentinelLinkedAssetsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **environment** | **String** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. | |
| **checkType** | [**SentinelLinkedAssetCheckType**](.md) | Exact Automation asset type whose Sentinel links should be returned. | [enum: REST, SOAP, GRAPHQL, STREAMING, FLOW] |
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |



## listSentinelRuns

> SentinelRunPage listSentinelRuns(listSentinelRunsRequest)

List Sentinel runs

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        String environment = "environment_example"; // String | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        UUID checkId = UUID.randomUUID(); // UUID |
        RunStatus status = RunStatus.fromValue("QUEUED"); // RunStatus |
        String sortBy = "queuedAt"; // String |
        String sortDirection = "asc"; // String |
        try {
            APIlistSentinelRunsRequest request = APIlistSentinelRunsRequest.newBuilder()
                .environment(environment)
                .page(page)
                .size(size)
                .checkId(checkId)
                .status(status)
                .sortBy(sortBy)
                .sortDirection(sortDirection)
                .build();
            SentinelRunPage result = apiInstance.listSentinelRuns(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#listSentinelRuns");
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
| listSentinelRunsRequest | [**APIlistSentinelRunsRequest**](SentinelApi.md#APIlistSentinelRunsRequest)|-|-|

### Return type

[**SentinelRunPage**](SentinelRunPage.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of Sentinel runs. |  -  |
| **0** | The request failed. |  -  |

## listSentinelRunsWithHttpInfo

> ApiResponse<SentinelRunPage> listSentinelRunsWithHttpInfo(listSentinelRunsRequest)

List Sentinel runs

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        String environment = "environment_example"; // String | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        UUID checkId = UUID.randomUUID(); // UUID |
        RunStatus status = RunStatus.fromValue("QUEUED"); // RunStatus |
        String sortBy = "queuedAt"; // String |
        String sortDirection = "asc"; // String |
        try {
            APIlistSentinelRunsRequest request = APIlistSentinelRunsRequest.newBuilder()
                .environment(environment)
                .page(page)
                .size(size)
                .checkId(checkId)
                .status(status)
                .sortBy(sortBy)
                .sortDirection(sortDirection)
                .build();
            ApiResponse<SentinelRunPage> response = apiInstance.listSentinelRunsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#listSentinelRuns");
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
| listSentinelRunsRequest | [**APIlistSentinelRunsRequest**](SentinelApi.md#APIlistSentinelRunsRequest)|-|-|

### Return type

ApiResponse<[**SentinelRunPage**](SentinelRunPage.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of Sentinel runs. |  -  |
| **0** | The request failed. |  -  |


<a id="APIlistSentinelRunsRequest"></a>
## APIlistSentinelRunsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **environment** | **String** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. | |
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **checkId** | **UUID** |  | [optional] |
| **status** | [**RunStatus**](.md) |  | [optional] [enum: QUEUED, RUNNING, PASS, RECOVERED, FAIL, ERROR, SKIPPED] |
| **sortBy** | **String** |  | [optional] [default to queuedAt] |
| **sortDirection** | **String** |  | [optional] [default to desc] [enum: asc, desc] |



## sampleSentinelRuns

> List<SentinelRun> sampleSentinelRuns(sampleSentinelRunsRequest)

Sample Sentinel runs

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        String environment = "environment_example"; // String | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
        Integer days = 30; // Integer |
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIsampleSentinelRunsRequest request = APIsampleSentinelRunsRequest.newBuilder()
                .environment(environment)
                .days(days)
                .size(size)
                .build();
            List<SentinelRun> result = apiInstance.sampleSentinelRuns(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#sampleSentinelRuns");
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
| sampleSentinelRunsRequest | [**APIsampleSentinelRunsRequest**](SentinelApi.md#APIsampleSentinelRunsRequest)|-|-|

### Return type

[**List&lt;SentinelRun&gt;**](SentinelRun.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A bounded sample of Sentinel runs for the selected environment. |  -  |
| **0** | The request failed. |  -  |

## sampleSentinelRunsWithHttpInfo

> ApiResponse<List<SentinelRun>> sampleSentinelRunsWithHttpInfo(sampleSentinelRunsRequest)

Sample Sentinel runs

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        String environment = "environment_example"; // String | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
        Integer days = 30; // Integer |
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIsampleSentinelRunsRequest request = APIsampleSentinelRunsRequest.newBuilder()
                .environment(environment)
                .days(days)
                .size(size)
                .build();
            ApiResponse<List<SentinelRun>> response = apiInstance.sampleSentinelRunsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#sampleSentinelRuns");
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
| sampleSentinelRunsRequest | [**APIsampleSentinelRunsRequest**](SentinelApi.md#APIsampleSentinelRunsRequest)|-|-|

### Return type

ApiResponse<[**List&lt;SentinelRun&gt;**](SentinelRun.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A bounded sample of Sentinel runs for the selected environment. |  -  |
| **0** | The request failed. |  -  |


<a id="APIsampleSentinelRunsRequest"></a>
## APIsampleSentinelRunsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **environment** | **String** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. | |
| **days** | **Integer** |  | [optional] [default to 30] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |



## updateSentinelCheck

> SentinelCheck updateSentinelCheck(updateSentinelCheckRequest)

Replace a Sentinel check configuration

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        UUID checkId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Sentinel check.
        SentinelCheckInput sentinelCheckInput = new SentinelCheckInput(); // SentinelCheckInput |
        try {
            APIupdateSentinelCheckRequest request = APIupdateSentinelCheckRequest.newBuilder()
                .checkId(checkId)
                .sentinelCheckInput(sentinelCheckInput)
                .build();
            SentinelCheck result = apiInstance.updateSentinelCheck(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#updateSentinelCheck");
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
| updateSentinelCheckRequest | [**APIupdateSentinelCheckRequest**](SentinelApi.md#APIupdateSentinelCheckRequest)|-|-|

### Return type

[**SentinelCheck**](SentinelCheck.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated check. |  -  |
| **0** | The request failed. |  -  |

## updateSentinelCheckWithHttpInfo

> ApiResponse<SentinelCheck> updateSentinelCheckWithHttpInfo(updateSentinelCheckRequest)

Replace a Sentinel check configuration

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SentinelApi;
import software.ste.sdk.generated.api.SentinelApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SentinelApi apiInstance = new SentinelApi(defaultClient);
        UUID checkId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the Sentinel check.
        SentinelCheckInput sentinelCheckInput = new SentinelCheckInput(); // SentinelCheckInput |
        try {
            APIupdateSentinelCheckRequest request = APIupdateSentinelCheckRequest.newBuilder()
                .checkId(checkId)
                .sentinelCheckInput(sentinelCheckInput)
                .build();
            ApiResponse<SentinelCheck> response = apiInstance.updateSentinelCheckWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SentinelApi#updateSentinelCheck");
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
| updateSentinelCheckRequest | [**APIupdateSentinelCheckRequest**](SentinelApi.md#APIupdateSentinelCheckRequest)|-|-|

### Return type

ApiResponse<[**SentinelCheck**](SentinelCheck.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated check. |  -  |
| **0** | The request failed. |  -  |


<a id="APIupdateSentinelCheckRequest"></a>
## APIupdateSentinelCheckRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **checkId** | **UUID** | UUIDv7 identifier of the Sentinel check. | |
| **sentinelCheckInput** | [**SentinelCheckInput**](SentinelCheckInput.md) |  | |
