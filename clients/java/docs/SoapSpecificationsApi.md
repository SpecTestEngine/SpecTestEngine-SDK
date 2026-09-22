# SoapSpecificationsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**captureSoapSpecificationAttachmentVisualDiff**](SoapSpecificationsApi.md#captureSoapSpecificationAttachmentVisualDiff) | **POST** /test/soap-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed SOAP attachment assertion |
| [**captureSoapSpecificationAttachmentVisualDiffWithHttpInfo**](SoapSpecificationsApi.md#captureSoapSpecificationAttachmentVisualDiffWithHttpInfo) | **POST** /test/soap-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed SOAP attachment assertion |
| [**createSoapSpecification**](SoapSpecificationsApi.md#createSoapSpecification) | **POST** /test/soap-spec/create | Create a SOAP specification |
| [**createSoapSpecificationWithHttpInfo**](SoapSpecificationsApi.md#createSoapSpecificationWithHttpInfo) | **POST** /test/soap-spec/create | Create a SOAP specification |
| [**deleteSoapSpecification**](SoapSpecificationsApi.md#deleteSoapSpecification) | **DELETE** /test/soap-spec/by-id | Delete a SOAP specification |
| [**deleteSoapSpecificationWithHttpInfo**](SoapSpecificationsApi.md#deleteSoapSpecificationWithHttpInfo) | **DELETE** /test/soap-spec/by-id | Delete a SOAP specification |
| [**getSoapSpecification**](SoapSpecificationsApi.md#getSoapSpecification) | **GET** /test/soap-spec/by-id | Get a SOAP specification |
| [**getSoapSpecificationWithHttpInfo**](SoapSpecificationsApi.md#getSoapSpecificationWithHttpInfo) | **GET** /test/soap-spec/by-id | Get a SOAP specification |
| [**getSoapSpecificationRun**](SoapSpecificationsApi.md#getSoapSpecificationRun) | **GET** /test/soap-spec/run/history/by-run-id/{runId} | Get saved SOAP run evidence |
| [**getSoapSpecificationRunWithHttpInfo**](SoapSpecificationsApi.md#getSoapSpecificationRunWithHttpInfo) | **GET** /test/soap-spec/run/history/by-run-id/{runId} | Get saved SOAP run evidence |
| [**listSoapSpecificationRuns**](SoapSpecificationsApi.md#listSoapSpecificationRuns) | **GET** /test/soap-spec/run/page/by-spec-id/{specId} | List saved SOAP runs |
| [**listSoapSpecificationRunsWithHttpInfo**](SoapSpecificationsApi.md#listSoapSpecificationRunsWithHttpInfo) | **GET** /test/soap-spec/run/page/by-spec-id/{specId} | List saved SOAP runs |
| [**listSoapSpecifications**](SoapSpecificationsApi.md#listSoapSpecifications) | **GET** /test/soap-spec/page | List SOAP specifications |
| [**listSoapSpecificationsWithHttpInfo**](SoapSpecificationsApi.md#listSoapSpecificationsWithHttpInfo) | **GET** /test/soap-spec/page | List SOAP specifications |
| [**previewSoapSpecificationRecovery**](SoapSpecificationsApi.md#previewSoapSpecificationRecovery) | **POST** /test/soap-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a SOAP specification version |
| [**previewSoapSpecificationRecoveryWithHttpInfo**](SoapSpecificationsApi.md#previewSoapSpecificationRecoveryWithHttpInfo) | **POST** /test/soap-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a SOAP specification version |
| [**restoreSoapSpecificationFromRun**](SoapSpecificationsApi.md#restoreSoapSpecificationFromRun) | **PUT** /test/soap-spec/recovery/{specId}/from-run/{runId}/restore | Restore a SOAP specification version |
| [**restoreSoapSpecificationFromRunWithHttpInfo**](SoapSpecificationsApi.md#restoreSoapSpecificationFromRunWithHttpInfo) | **PUT** /test/soap-spec/recovery/{specId}/from-run/{runId}/restore | Restore a SOAP specification version |
| [**runSoapSpecification**](SoapSpecificationsApi.md#runSoapSpecification) | **POST** /test/soap-spec/run/by-id | Run a saved SOAP specification |
| [**runSoapSpecificationWithHttpInfo**](SoapSpecificationsApi.md#runSoapSpecificationWithHttpInfo) | **POST** /test/soap-spec/run/by-id | Run a saved SOAP specification |
| [**testSoapSpecificationRecoveryVersion**](SoapSpecificationsApi.md#testSoapSpecificationRecoveryVersion) | **POST** /test/soap-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous SOAP specification version |
| [**testSoapSpecificationRecoveryVersionWithHttpInfo**](SoapSpecificationsApi.md#testSoapSpecificationRecoveryVersionWithHttpInfo) | **POST** /test/soap-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous SOAP specification version |
| [**updateSoapSpecification**](SoapSpecificationsApi.md#updateSoapSpecification) | **PUT** /test/soap-spec/by-id | Replace a SOAP specification definition |
| [**updateSoapSpecificationWithHttpInfo**](SoapSpecificationsApi.md#updateSoapSpecificationWithHttpInfo) | **PUT** /test/soap-spec/by-id | Replace a SOAP specification definition |



## captureSoapSpecificationAttachmentVisualDiff

> SpecificationRun captureSoapSpecificationAttachmentVisualDiff(captureSoapSpecificationAttachmentVisualDiffRequest)

Create a visual diff from a failed SOAP attachment assertion

Explicitly reruns the saved SOAP specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        DocumentVisualDiffCaptureRunRequest documentVisualDiffCaptureRunRequest = new DocumentVisualDiffCaptureRunRequest(); // DocumentVisualDiffCaptureRunRequest |
        try {
            APIcaptureSoapSpecificationAttachmentVisualDiffRequest request = APIcaptureSoapSpecificationAttachmentVisualDiffRequest.newBuilder()
                .specId(specId)
                .documentVisualDiffCaptureRunRequest(documentVisualDiffCaptureRunRequest)
                .build();
            SpecificationRun result = apiInstance.captureSoapSpecificationAttachmentVisualDiff(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#captureSoapSpecificationAttachmentVisualDiff");
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
| captureSoapSpecificationAttachmentVisualDiffRequest | [**APIcaptureSoapSpecificationAttachmentVisualDiffRequest**](SoapSpecificationsApi.md#APIcaptureSoapSpecificationAttachmentVisualDiffRequest)|-|-|

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

## captureSoapSpecificationAttachmentVisualDiffWithHttpInfo

> ApiResponse<SpecificationRun> captureSoapSpecificationAttachmentVisualDiffWithHttpInfo(captureSoapSpecificationAttachmentVisualDiffRequest)

Create a visual diff from a failed SOAP attachment assertion

Explicitly reruns the saved SOAP specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        DocumentVisualDiffCaptureRunRequest documentVisualDiffCaptureRunRequest = new DocumentVisualDiffCaptureRunRequest(); // DocumentVisualDiffCaptureRunRequest |
        try {
            APIcaptureSoapSpecificationAttachmentVisualDiffRequest request = APIcaptureSoapSpecificationAttachmentVisualDiffRequest.newBuilder()
                .specId(specId)
                .documentVisualDiffCaptureRunRequest(documentVisualDiffCaptureRunRequest)
                .build();
            ApiResponse<SpecificationRun> response = apiInstance.captureSoapSpecificationAttachmentVisualDiffWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#captureSoapSpecificationAttachmentVisualDiff");
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
| captureSoapSpecificationAttachmentVisualDiffRequest | [**APIcaptureSoapSpecificationAttachmentVisualDiffRequest**](SoapSpecificationsApi.md#APIcaptureSoapSpecificationAttachmentVisualDiffRequest)|-|-|

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


<a id="APIcaptureSoapSpecificationAttachmentVisualDiffRequest"></a>
## APIcaptureSoapSpecificationAttachmentVisualDiffRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **documentVisualDiffCaptureRunRequest** | [**DocumentVisualDiffCaptureRunRequest**](DocumentVisualDiffCaptureRunRequest.md) |  | |



## createSoapSpecification

> Specification createSoapSpecification(createSoapSpecificationRequest)

Create a SOAP specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        String specName = "specName_example"; // String | User-facing specification name within the active project.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateSoapSpecificationRequest request = APIcreateSoapSpecificationRequest.newBuilder()
                .specName(specName)
                .body(body)
                .description(description)
                .idempotencyKey(idempotencyKey)
                .build();
            Specification result = apiInstance.createSoapSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#createSoapSpecification");
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
| createSoapSpecificationRequest | [**APIcreateSoapSpecificationRequest**](SoapSpecificationsApi.md#APIcreateSoapSpecificationRequest)|-|-|

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
| **200** | The stored SOAP specification. |  -  |
| **0** | The request failed. |  -  |

## createSoapSpecificationWithHttpInfo

> ApiResponse<Specification> createSoapSpecificationWithHttpInfo(createSoapSpecificationRequest)

Create a SOAP specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        String specName = "specName_example"; // String | User-facing specification name within the active project.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateSoapSpecificationRequest request = APIcreateSoapSpecificationRequest.newBuilder()
                .specName(specName)
                .body(body)
                .description(description)
                .idempotencyKey(idempotencyKey)
                .build();
            ApiResponse<Specification> response = apiInstance.createSoapSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#createSoapSpecification");
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
| createSoapSpecificationRequest | [**APIcreateSoapSpecificationRequest**](SoapSpecificationsApi.md#APIcreateSoapSpecificationRequest)|-|-|

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
| **200** | The stored SOAP specification. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcreateSoapSpecificationRequest"></a>
## APIcreateSoapSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specName** | **String** | User-facing specification name within the active project. | |
| **body** | **String** |  | |
| **description** | **String** | Optional user-facing description stored with the asset. | [optional] |
| **idempotencyKey** | **UUID** | A caller-generated UUID retained for safe write retries where supported. | [optional] |



## deleteSoapSpecification

> Specification deleteSoapSpecification(deleteSoapSpecificationRequest)

Delete a SOAP specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIdeleteSoapSpecificationRequest request = APIdeleteSoapSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            Specification result = apiInstance.deleteSoapSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#deleteSoapSpecification");
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
| deleteSoapSpecificationRequest | [**APIdeleteSoapSpecificationRequest**](SoapSpecificationsApi.md#APIdeleteSoapSpecificationRequest)|-|-|

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
| **200** | The deleted SOAP specification. |  -  |
| **0** | The request failed. |  -  |

## deleteSoapSpecificationWithHttpInfo

> ApiResponse<Specification> deleteSoapSpecificationWithHttpInfo(deleteSoapSpecificationRequest)

Delete a SOAP specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIdeleteSoapSpecificationRequest request = APIdeleteSoapSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            ApiResponse<Specification> response = apiInstance.deleteSoapSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#deleteSoapSpecification");
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
| deleteSoapSpecificationRequest | [**APIdeleteSoapSpecificationRequest**](SoapSpecificationsApi.md#APIdeleteSoapSpecificationRequest)|-|-|

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
| **200** | The deleted SOAP specification. |  -  |
| **0** | The request failed. |  -  |


<a id="APIdeleteSoapSpecificationRequest"></a>
## APIdeleteSoapSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |



## getSoapSpecification

> Specification getSoapSpecification(getSoapSpecificationRequest)

Get a SOAP specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIgetSoapSpecificationRequest request = APIgetSoapSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            Specification result = apiInstance.getSoapSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#getSoapSpecification");
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
| getSoapSpecificationRequest | [**APIgetSoapSpecificationRequest**](SoapSpecificationsApi.md#APIgetSoapSpecificationRequest)|-|-|

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
| **200** | The requested SOAP specification. |  -  |
| **0** | The request failed. |  -  |

## getSoapSpecificationWithHttpInfo

> ApiResponse<Specification> getSoapSpecificationWithHttpInfo(getSoapSpecificationRequest)

Get a SOAP specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIgetSoapSpecificationRequest request = APIgetSoapSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            ApiResponse<Specification> response = apiInstance.getSoapSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#getSoapSpecification");
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
| getSoapSpecificationRequest | [**APIgetSoapSpecificationRequest**](SoapSpecificationsApi.md#APIgetSoapSpecificationRequest)|-|-|

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
| **200** | The requested SOAP specification. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetSoapSpecificationRequest"></a>
## APIgetSoapSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |



## getSoapSpecificationRun

> SpecificationRun getSoapSpecificationRun(getSoapSpecificationRunRequest)

Get saved SOAP run evidence

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIgetSoapSpecificationRunRequest request = APIgetSoapSpecificationRunRequest.newBuilder()
                .runId(runId)
                .build();
            SpecificationRun result = apiInstance.getSoapSpecificationRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#getSoapSpecificationRun");
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
| getSoapSpecificationRunRequest | [**APIgetSoapSpecificationRunRequest**](SoapSpecificationsApi.md#APIgetSoapSpecificationRunRequest)|-|-|

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

## getSoapSpecificationRunWithHttpInfo

> ApiResponse<SpecificationRun> getSoapSpecificationRunWithHttpInfo(getSoapSpecificationRunRequest)

Get saved SOAP run evidence

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIgetSoapSpecificationRunRequest request = APIgetSoapSpecificationRunRequest.newBuilder()
                .runId(runId)
                .build();
            ApiResponse<SpecificationRun> response = apiInstance.getSoapSpecificationRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#getSoapSpecificationRun");
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
| getSoapSpecificationRunRequest | [**APIgetSoapSpecificationRunRequest**](SoapSpecificationsApi.md#APIgetSoapSpecificationRunRequest)|-|-|

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


<a id="APIgetSoapSpecificationRunRequest"></a>
## APIgetSoapSpecificationRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## listSoapSpecificationRuns

> SpecificationRunPage listSoapSpecificationRuns(listSoapSpecificationRunsRequest)

List saved SOAP runs

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIlistSoapSpecificationRunsRequest request = APIlistSoapSpecificationRunsRequest.newBuilder()
                .specId(specId)
                .page(page)
                .size(size)
                .build();
            SpecificationRunPage result = apiInstance.listSoapSpecificationRuns(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#listSoapSpecificationRuns");
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
| listSoapSpecificationRunsRequest | [**APIlistSoapSpecificationRunsRequest**](SoapSpecificationsApi.md#APIlistSoapSpecificationRunsRequest)|-|-|

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

## listSoapSpecificationRunsWithHttpInfo

> ApiResponse<SpecificationRunPage> listSoapSpecificationRunsWithHttpInfo(listSoapSpecificationRunsRequest)

List saved SOAP runs

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        try {
            APIlistSoapSpecificationRunsRequest request = APIlistSoapSpecificationRunsRequest.newBuilder()
                .specId(specId)
                .page(page)
                .size(size)
                .build();
            ApiResponse<SpecificationRunPage> response = apiInstance.listSoapSpecificationRunsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#listSoapSpecificationRuns");
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
| listSoapSpecificationRunsRequest | [**APIlistSoapSpecificationRunsRequest**](SoapSpecificationsApi.md#APIlistSoapSpecificationRunsRequest)|-|-|

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


<a id="APIlistSoapSpecificationRunsRequest"></a>
## APIlistSoapSpecificationRunsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |



## listSoapSpecifications

> SpecificationPage listSoapSpecifications(listSoapSpecificationsRequest)

List SOAP specifications

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistSoapSpecificationsRequest request = APIlistSoapSpecificationsRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .build();
            SpecificationPage result = apiInstance.listSoapSpecifications(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#listSoapSpecifications");
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
| listSoapSpecificationsRequest | [**APIlistSoapSpecificationsRequest**](SoapSpecificationsApi.md#APIlistSoapSpecificationsRequest)|-|-|

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
| **200** | A page of SOAP specifications. |  -  |
| **0** | The request failed. |  -  |

## listSoapSpecificationsWithHttpInfo

> ApiResponse<SpecificationPage> listSoapSpecificationsWithHttpInfo(listSoapSpecificationsRequest)

List SOAP specifications

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistSoapSpecificationsRequest request = APIlistSoapSpecificationsRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .build();
            ApiResponse<SpecificationPage> response = apiInstance.listSoapSpecificationsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#listSoapSpecifications");
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
| listSoapSpecificationsRequest | [**APIlistSoapSpecificationsRequest**](SoapSpecificationsApi.md#APIlistSoapSpecificationsRequest)|-|-|

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
| **200** | A page of SOAP specifications. |  -  |
| **0** | The request failed. |  -  |


<a id="APIlistSoapSpecificationsRequest"></a>
## APIlistSoapSpecificationsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **String** | Case-insensitive server-side search within the active project. | [optional] |



## previewSoapSpecificationRecovery

> SpecificationRecoveryPreview previewSoapSpecificationRecovery(previewSoapSpecificationRecoveryRequest)

Preview restoring a SOAP specification version

Compares the current specification with the exact DSL snapshot retained by a completed PASS or FAIL run. No expectations are regenerated.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIpreviewSoapSpecificationRecoveryRequest request = APIpreviewSoapSpecificationRecoveryRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            SpecificationRecoveryPreview result = apiInstance.previewSoapSpecificationRecovery(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#previewSoapSpecificationRecovery");
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
| previewSoapSpecificationRecoveryRequest | [**APIpreviewSoapSpecificationRecoveryRequest**](SoapSpecificationsApi.md#APIpreviewSoapSpecificationRecoveryRequest)|-|-|

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

## previewSoapSpecificationRecoveryWithHttpInfo

> ApiResponse<SpecificationRecoveryPreview> previewSoapSpecificationRecoveryWithHttpInfo(previewSoapSpecificationRecoveryRequest)

Preview restoring a SOAP specification version

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
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIpreviewSoapSpecificationRecoveryRequest request = APIpreviewSoapSpecificationRecoveryRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            ApiResponse<SpecificationRecoveryPreview> response = apiInstance.previewSoapSpecificationRecoveryWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#previewSoapSpecificationRecovery");
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
| previewSoapSpecificationRecoveryRequest | [**APIpreviewSoapSpecificationRecoveryRequest**](SoapSpecificationsApi.md#APIpreviewSoapSpecificationRecoveryRequest)|-|-|

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


<a id="APIpreviewSoapSpecificationRecoveryRequest"></a>
## APIpreviewSoapSpecificationRecoveryRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## restoreSoapSpecificationFromRun

> Specification restoreSoapSpecificationFromRun(restoreSoapSpecificationFromRunRequest)

Restore a SOAP specification version

Replaces only the current DSL content with the exact snapshot retained by a completed PASS or FAIL run. The specification id, name, description, and stable identity are preserved.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIrestoreSoapSpecificationFromRunRequest request = APIrestoreSoapSpecificationFromRunRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            Specification result = apiInstance.restoreSoapSpecificationFromRun(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#restoreSoapSpecificationFromRun");
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
| restoreSoapSpecificationFromRunRequest | [**APIrestoreSoapSpecificationFromRunRequest**](SoapSpecificationsApi.md#APIrestoreSoapSpecificationFromRunRequest)|-|-|

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

## restoreSoapSpecificationFromRunWithHttpInfo

> ApiResponse<Specification> restoreSoapSpecificationFromRunWithHttpInfo(restoreSoapSpecificationFromRunRequest)

Restore a SOAP specification version

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
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APIrestoreSoapSpecificationFromRunRequest request = APIrestoreSoapSpecificationFromRunRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            ApiResponse<Specification> response = apiInstance.restoreSoapSpecificationFromRunWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#restoreSoapSpecificationFromRun");
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
| restoreSoapSpecificationFromRunRequest | [**APIrestoreSoapSpecificationFromRunRequest**](SoapSpecificationsApi.md#APIrestoreSoapSpecificationFromRunRequest)|-|-|

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


<a id="APIrestoreSoapSpecificationFromRunRequest"></a>
## APIrestoreSoapSpecificationFromRunRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## runSoapSpecification

> SpecificationRun runSoapSpecification(runSoapSpecificationRequest)

Run a saved SOAP specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIrunSoapSpecificationRequest request = APIrunSoapSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            SpecificationRun result = apiInstance.runSoapSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#runSoapSpecification");
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
| runSoapSpecificationRequest | [**APIrunSoapSpecificationRequest**](SoapSpecificationsApi.md#APIrunSoapSpecificationRequest)|-|-|

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

## runSoapSpecificationWithHttpInfo

> ApiResponse<SpecificationRun> runSoapSpecificationWithHttpInfo(runSoapSpecificationRequest)

Run a saved SOAP specification

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        try {
            APIrunSoapSpecificationRequest request = APIrunSoapSpecificationRequest.newBuilder()
                .specId(specId)
                .build();
            ApiResponse<SpecificationRun> response = apiInstance.runSoapSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#runSoapSpecification");
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
| runSoapSpecificationRequest | [**APIrunSoapSpecificationRequest**](SoapSpecificationsApi.md#APIrunSoapSpecificationRequest)|-|-|

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


<a id="APIrunSoapSpecificationRequest"></a>
## APIrunSoapSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |



## testSoapSpecificationRecoveryVersion

> SpecificationRun testSoapSpecificationRecoveryVersion(testSoapSpecificationRecoveryVersionRequest)

Test a previous SOAP specification version

Executes the exact DSL snapshot retained by the selected completed PASS or FAIL run against the current API without changing the saved specification.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APItestSoapSpecificationRecoveryVersionRequest request = APItestSoapSpecificationRecoveryVersionRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            SpecificationRun result = apiInstance.testSoapSpecificationRecoveryVersion(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#testSoapSpecificationRecoveryVersion");
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
| testSoapSpecificationRecoveryVersionRequest | [**APItestSoapSpecificationRecoveryVersionRequest**](SoapSpecificationsApi.md#APItestSoapSpecificationRecoveryVersionRequest)|-|-|

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

## testSoapSpecificationRecoveryVersionWithHttpInfo

> ApiResponse<SpecificationRun> testSoapSpecificationRecoveryVersionWithHttpInfo(testSoapSpecificationRecoveryVersionRequest)

Test a previous SOAP specification version

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
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        UUID runId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the stored run evidence.
        try {
            APItestSoapSpecificationRecoveryVersionRequest request = APItestSoapSpecificationRecoveryVersionRequest.newBuilder()
                .specId(specId)
                .runId(runId)
                .build();
            ApiResponse<SpecificationRun> response = apiInstance.testSoapSpecificationRecoveryVersionWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#testSoapSpecificationRecoveryVersion");
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
| testSoapSpecificationRecoveryVersionRequest | [**APItestSoapSpecificationRecoveryVersionRequest**](SoapSpecificationsApi.md#APItestSoapSpecificationRecoveryVersionRequest)|-|-|

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


<a id="APItestSoapSpecificationRecoveryVersionRequest"></a>
## APItestSoapSpecificationRecoveryVersionRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **runId** | **UUID** | UUIDv7 identifier of the stored run evidence. | |



## updateSoapSpecification

> Specification updateSoapSpecification(updateSoapSpecificationRequest)

Replace a SOAP specification definition

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        try {
            APIupdateSoapSpecificationRequest request = APIupdateSoapSpecificationRequest.newBuilder()
                .specId(specId)
                .body(body)
                .description(description)
                .build();
            Specification result = apiInstance.updateSoapSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#updateSoapSpecification");
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
| updateSoapSpecificationRequest | [**APIupdateSoapSpecificationRequest**](SoapSpecificationsApi.md#APIupdateSoapSpecificationRequest)|-|-|

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
| **200** | The updated SOAP specification. |  -  |
| **0** | The request failed. |  -  |

## updateSoapSpecificationWithHttpInfo

> ApiResponse<Specification> updateSoapSpecificationWithHttpInfo(updateSoapSpecificationRequest)

Replace a SOAP specification definition

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SoapSpecificationsApi;
import software.ste.sdk.generated.api.SoapSpecificationsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SoapSpecificationsApi apiInstance = new SoapSpecificationsApi(defaultClient);
        UUID specId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved specification.
        String body = "body_example"; // String |
        String description = "description_example"; // String | Optional user-facing description stored with the asset.
        try {
            APIupdateSoapSpecificationRequest request = APIupdateSoapSpecificationRequest.newBuilder()
                .specId(specId)
                .body(body)
                .description(description)
                .build();
            ApiResponse<Specification> response = apiInstance.updateSoapSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SoapSpecificationsApi#updateSoapSpecification");
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
| updateSoapSpecificationRequest | [**APIupdateSoapSpecificationRequest**](SoapSpecificationsApi.md#APIupdateSoapSpecificationRequest)|-|-|

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
| **200** | The updated SOAP specification. |  -  |
| **0** | The request failed. |  -  |


<a id="APIupdateSoapSpecificationRequest"></a>
## APIupdateSoapSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **specId** | **UUID** | UUIDv7 identifier of the saved specification. | |
| **body** | **String** |  | |
| **description** | **String** | Optional user-facing description stored with the asset. | [optional] |


