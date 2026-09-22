# GenerationApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createArtifactGenerationProfile**](GenerationApi.md#createArtifactGenerationProfile) | **POST** /artifact-profiles | Create a CI export profile |
| [**createArtifactGenerationProfileWithHttpInfo**](GenerationApi.md#createArtifactGenerationProfileWithHttpInfo) | **POST** /artifact-profiles | Create a CI export profile |
| [**deleteArtifactGenerationProfile**](GenerationApi.md#deleteArtifactGenerationProfile) | **DELETE** /artifact-profiles/{profileId} | Delete a CI export profile |
| [**deleteArtifactGenerationProfileWithHttpInfo**](GenerationApi.md#deleteArtifactGenerationProfileWithHttpInfo) | **DELETE** /artifact-profiles/{profileId} | Delete a CI export profile |
| [**downloadArtifactGenerationProfileArchive**](GenerationApi.md#downloadArtifactGenerationProfileArchive) | **POST** /artifact-profiles/{profileId}/environments/{environmentKey}/atf/archive | Validate and download a CI profile archive |
| [**downloadArtifactGenerationProfileArchiveWithHttpInfo**](GenerationApi.md#downloadArtifactGenerationProfileArchiveWithHttpInfo) | **POST** /artifact-profiles/{profileId}/environments/{environmentKey}/atf/archive | Validate and download a CI profile archive |
| [**downloadAtfProject**](GenerationApi.md#downloadAtfProject) | **POST** /atf/generate/download | Download a generated ATF project |
| [**downloadAtfProjectWithHttpInfo**](GenerationApi.md#downloadAtfProjectWithHttpInfo) | **POST** /atf/generate/download | Download a generated ATF project |
| [**generateFromOpenApiContent**](GenerationApi.md#generateFromOpenApiContent) | **POST** /openapi/generate-from-content | Generate specifications and flows from OpenAPI content |
| [**generateFromOpenApiContentWithHttpInfo**](GenerationApi.md#generateFromOpenApiContentWithHttpInfo) | **POST** /openapi/generate-from-content | Generate specifications and flows from OpenAPI content |
| [**generateSpecification**](GenerationApi.md#generateSpecification) | **POST** /spec/generate | Generate an executable specification from concrete request evidence |
| [**generateSpecificationWithHttpInfo**](GenerationApi.md#generateSpecificationWithHttpInfo) | **POST** /spec/generate | Generate an executable specification from concrete request evidence |
| [**getArtifactGenerationProfile**](GenerationApi.md#getArtifactGenerationProfile) | **GET** /artifact-profiles/{profileId} | Get a CI export profile |
| [**getArtifactGenerationProfileWithHttpInfo**](GenerationApi.md#getArtifactGenerationProfileWithHttpInfo) | **GET** /artifact-profiles/{profileId} | Get a CI export profile |
| [**getAtfProjectValidationResult**](GenerationApi.md#getAtfProjectValidationResult) | **GET** /atf/generate/validate/result/{validationId} | Get ATF validation status or result |
| [**getAtfProjectValidationResultWithHttpInfo**](GenerationApi.md#getAtfProjectValidationResultWithHttpInfo) | **GET** /atf/generate/validate/result/{validationId} | Get ATF validation status or result |
| [**listArtifactGenerationProfiles**](GenerationApi.md#listArtifactGenerationProfiles) | **GET** /artifact-profiles | List CI export profiles |
| [**listArtifactGenerationProfilesWithHttpInfo**](GenerationApi.md#listArtifactGenerationProfilesWithHttpInfo) | **GET** /artifact-profiles | List CI export profiles |
| [**observeAtfProjectValidation**](GenerationApi.md#observeAtfProjectValidation) | **GET** /atf/generate/validate/events/{validationId} | Observe ATF validation progress |
| [**observeAtfProjectValidationWithHttpInfo**](GenerationApi.md#observeAtfProjectValidationWithHttpInfo) | **GET** /atf/generate/validate/events/{validationId} | Observe ATF validation progress |
| [**previewAtfProject**](GenerationApi.md#previewAtfProject) | **POST** /atf/generate/preview | Generate an ATF project preview |
| [**previewAtfProjectWithHttpInfo**](GenerationApi.md#previewAtfProjectWithHttpInfo) | **POST** /atf/generate/preview | Generate an ATF project preview |
| [**refreshArtifactGenerationProfileBundle**](GenerationApi.md#refreshArtifactGenerationProfileBundle) | **POST** /artifact-profiles/{profileId}/environments/{environmentKey}/bundle/refresh | Capture or refresh an environment baseline |
| [**refreshArtifactGenerationProfileBundleWithHttpInfo**](GenerationApi.md#refreshArtifactGenerationProfileBundleWithHttpInfo) | **POST** /artifact-profiles/{profileId}/environments/{environmentKey}/bundle/refresh | Capture or refresh an environment baseline |
| [**startAtfProjectValidation**](GenerationApi.md#startAtfProjectValidation) | **POST** /atf/generate/validate/start | Start asynchronous ATF compile validation |
| [**startAtfProjectValidationWithHttpInfo**](GenerationApi.md#startAtfProjectValidationWithHttpInfo) | **POST** /atf/generate/validate/start | Start asynchronous ATF compile validation |
| [**updateArtifactGenerationProfile**](GenerationApi.md#updateArtifactGenerationProfile) | **PUT** /artifact-profiles/{profileId} | Update a CI export profile |
| [**updateArtifactGenerationProfileWithHttpInfo**](GenerationApi.md#updateArtifactGenerationProfileWithHttpInfo) | **PUT** /artifact-profiles/{profileId} | Update a CI export profile |
| [**validateAtfProject**](GenerationApi.md#validateAtfProject) | **POST** /atf/generate/validate | Validate that an ATF project compiles |
| [**validateAtfProjectWithHttpInfo**](GenerationApi.md#validateAtfProjectWithHttpInfo) | **POST** /atf/generate/validate | Validate that an ATF project compiles |



## createArtifactGenerationProfile

> ArtifactGenerationProfile createArtifactGenerationProfile(createArtifactGenerationProfileRequest)

Create a CI export profile

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        ArtifactGenerationProfileInput artifactGenerationProfileInput = new ArtifactGenerationProfileInput(); // ArtifactGenerationProfileInput |
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateArtifactGenerationProfileRequest request = APIcreateArtifactGenerationProfileRequest.newBuilder()
                .artifactGenerationProfileInput(artifactGenerationProfileInput)
                .idempotencyKey(idempotencyKey)
                .build();
            ArtifactGenerationProfile result = apiInstance.createArtifactGenerationProfile(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#createArtifactGenerationProfile");
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
| createArtifactGenerationProfileRequest | [**APIcreateArtifactGenerationProfileRequest**](GenerationApi.md#APIcreateArtifactGenerationProfileRequest)|-|-|

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored CI export profile. |  -  |
| **0** | The request failed. |  -  |

## createArtifactGenerationProfileWithHttpInfo

> ApiResponse<ArtifactGenerationProfile> createArtifactGenerationProfileWithHttpInfo(createArtifactGenerationProfileRequest)

Create a CI export profile

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        ArtifactGenerationProfileInput artifactGenerationProfileInput = new ArtifactGenerationProfileInput(); // ArtifactGenerationProfileInput |
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateArtifactGenerationProfileRequest request = APIcreateArtifactGenerationProfileRequest.newBuilder()
                .artifactGenerationProfileInput(artifactGenerationProfileInput)
                .idempotencyKey(idempotencyKey)
                .build();
            ApiResponse<ArtifactGenerationProfile> response = apiInstance.createArtifactGenerationProfileWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#createArtifactGenerationProfile");
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
| createArtifactGenerationProfileRequest | [**APIcreateArtifactGenerationProfileRequest**](GenerationApi.md#APIcreateArtifactGenerationProfileRequest)|-|-|

### Return type

ApiResponse<[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored CI export profile. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcreateArtifactGenerationProfileRequest"></a>
## APIcreateArtifactGenerationProfileRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **artifactGenerationProfileInput** | [**ArtifactGenerationProfileInput**](ArtifactGenerationProfileInput.md) |  | |
| **idempotencyKey** | **UUID** | A caller-generated UUID retained for safe write retries where supported. | [optional] |



## deleteArtifactGenerationProfile

> void deleteArtifactGenerationProfile(deleteArtifactGenerationProfileRequest)

Delete a CI export profile

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        UUID profileId = UUID.randomUUID(); // UUID | UUIDv7 identifier of a CI export profile.
        try {
            APIdeleteArtifactGenerationProfileRequest request = APIdeleteArtifactGenerationProfileRequest.newBuilder()
                .profileId(profileId)
                .build();
            apiInstance.deleteArtifactGenerationProfile(request);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#deleteArtifactGenerationProfile");
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
| deleteArtifactGenerationProfileRequest | [**APIdeleteArtifactGenerationProfileRequest**](GenerationApi.md#APIdeleteArtifactGenerationProfileRequest)|-|-|

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
| **204** | The profile was deleted. |  -  |
| **0** | The request failed. |  -  |

## deleteArtifactGenerationProfileWithHttpInfo

> ApiResponse<Void> deleteArtifactGenerationProfileWithHttpInfo(deleteArtifactGenerationProfileRequest)

Delete a CI export profile

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        UUID profileId = UUID.randomUUID(); // UUID | UUIDv7 identifier of a CI export profile.
        try {
            APIdeleteArtifactGenerationProfileRequest request = APIdeleteArtifactGenerationProfileRequest.newBuilder()
                .profileId(profileId)
                .build();
            ApiResponse<Void> response = apiInstance.deleteArtifactGenerationProfileWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#deleteArtifactGenerationProfile");
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
| deleteArtifactGenerationProfileRequest | [**APIdeleteArtifactGenerationProfileRequest**](GenerationApi.md#APIdeleteArtifactGenerationProfileRequest)|-|-|

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
| **204** | The profile was deleted. |  -  |
| **0** | The request failed. |  -  |


<a id="APIdeleteArtifactGenerationProfileRequest"></a>
## APIdeleteArtifactGenerationProfileRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **profileId** | **UUID** | UUIDv7 identifier of a CI export profile. | |



## downloadArtifactGenerationProfileArchive

> File downloadArtifactGenerationProfileArchive(downloadArtifactGenerationProfileArchiveRequest)

Validate and download a CI profile archive

Resolves the environment policy, enforces drift rules, then returns an archive only after the generated project passes compile validation.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        UUID profileId = UUID.randomUUID(); // UUID | UUIDv7 identifier of a CI export profile.
        String environmentKey = "environmentKey_example"; // String | Stable profile environment key such as test, staging, or production.
        try {
            APIdownloadArtifactGenerationProfileArchiveRequest request = APIdownloadArtifactGenerationProfileArchiveRequest.newBuilder()
                .profileId(profileId)
                .environmentKey(environmentKey)
                .build();
            File result = apiInstance.downloadArtifactGenerationProfileArchive(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#downloadArtifactGenerationProfileArchive");
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
| downloadArtifactGenerationProfileArchiveRequest | [**APIdownloadArtifactGenerationProfileArchiveRequest**](GenerationApi.md#APIdownloadArtifactGenerationProfileArchiveRequest)|-|-|

### Return type

[**File**](File.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A compile-validated ATF project archive. |  * Content-Disposition -  <br>  |
| **422** | The generated project did not pass readiness validation; no archive was returned. |  -  |
| **429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
| **0** | The request failed. |  -  |

## downloadArtifactGenerationProfileArchiveWithHttpInfo

> ApiResponse<File> downloadArtifactGenerationProfileArchiveWithHttpInfo(downloadArtifactGenerationProfileArchiveRequest)

Validate and download a CI profile archive

Resolves the environment policy, enforces drift rules, then returns an archive only after the generated project passes compile validation.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        UUID profileId = UUID.randomUUID(); // UUID | UUIDv7 identifier of a CI export profile.
        String environmentKey = "environmentKey_example"; // String | Stable profile environment key such as test, staging, or production.
        try {
            APIdownloadArtifactGenerationProfileArchiveRequest request = APIdownloadArtifactGenerationProfileArchiveRequest.newBuilder()
                .profileId(profileId)
                .environmentKey(environmentKey)
                .build();
            ApiResponse<File> response = apiInstance.downloadArtifactGenerationProfileArchiveWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#downloadArtifactGenerationProfileArchive");
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
| downloadArtifactGenerationProfileArchiveRequest | [**APIdownloadArtifactGenerationProfileArchiveRequest**](GenerationApi.md#APIdownloadArtifactGenerationProfileArchiveRequest)|-|-|

### Return type

ApiResponse<[**File**](File.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A compile-validated ATF project archive. |  * Content-Disposition -  <br>  |
| **422** | The generated project did not pass readiness validation; no archive was returned. |  -  |
| **429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
| **0** | The request failed. |  -  |


<a id="APIdownloadArtifactGenerationProfileArchiveRequest"></a>
## APIdownloadArtifactGenerationProfileArchiveRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **profileId** | **UUID** | UUIDv7 identifier of a CI export profile. | |
| **environmentKey** | **String** | Stable profile environment key such as test, staging, or production. | |



## downloadAtfProject

> File downloadAtfProject(downloadAtfProjectRequest)

Download a generated ATF project

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        AtfGenerationInput atfGenerationInput = new AtfGenerationInput(); // AtfGenerationInput |
        try {
            APIdownloadAtfProjectRequest request = APIdownloadAtfProjectRequest.newBuilder()
                .atfGenerationInput(atfGenerationInput)
                .build();
            File result = apiInstance.downloadAtfProject(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#downloadAtfProject");
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
| downloadAtfProjectRequest | [**APIdownloadAtfProjectRequest**](GenerationApi.md#APIdownloadAtfProjectRequest)|-|-|

### Return type

[**File**](File.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A portable ATF project archive. |  * Content-Disposition -  <br>  |
| **422** | The generated project did not pass readiness validation; no archive was returned. |  -  |
| **429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
| **0** | The request failed. |  -  |

## downloadAtfProjectWithHttpInfo

> ApiResponse<File> downloadAtfProjectWithHttpInfo(downloadAtfProjectRequest)

Download a generated ATF project

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        AtfGenerationInput atfGenerationInput = new AtfGenerationInput(); // AtfGenerationInput |
        try {
            APIdownloadAtfProjectRequest request = APIdownloadAtfProjectRequest.newBuilder()
                .atfGenerationInput(atfGenerationInput)
                .build();
            ApiResponse<File> response = apiInstance.downloadAtfProjectWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#downloadAtfProject");
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
| downloadAtfProjectRequest | [**APIdownloadAtfProjectRequest**](GenerationApi.md#APIdownloadAtfProjectRequest)|-|-|

### Return type

ApiResponse<[**File**](File.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A portable ATF project archive. |  * Content-Disposition -  <br>  |
| **422** | The generated project did not pass readiness validation; no archive was returned. |  -  |
| **429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
| **0** | The request failed. |  -  |


<a id="APIdownloadAtfProjectRequest"></a>
## APIdownloadAtfProjectRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **atfGenerationInput** | [**AtfGenerationInput**](AtfGenerationInput.md) |  | |



## generateFromOpenApiContent

> OpenApiGenerationResult generateFromOpenApiContent(generateFromOpenApiContentRequest)

Generate specifications and flows from OpenAPI content

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        ContentFormat contentFormat = ContentFormat.fromValue("JSON"); // ContentFormat |
        String body = "body_example"; // String |
        Boolean includeNegativeTests = false; // Boolean |
        Boolean generateFlowScenarios = false; // Boolean |
        String generationStrategy = "SCHEMA_BASED"; // String |
        String negativeTestGenerationMode = "STRICT"; // String |
        try {
            APIgenerateFromOpenApiContentRequest request = APIgenerateFromOpenApiContentRequest.newBuilder()
                .contentFormat(contentFormat)
                .body(body)
                .includeNegativeTests(includeNegativeTests)
                .generateFlowScenarios(generateFlowScenarios)
                .generationStrategy(generationStrategy)
                .negativeTestGenerationMode(negativeTestGenerationMode)
                .build();
            OpenApiGenerationResult result = apiInstance.generateFromOpenApiContent(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#generateFromOpenApiContent");
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
| generateFromOpenApiContentRequest | [**APIgenerateFromOpenApiContentRequest**](GenerationApi.md#APIgenerateFromOpenApiContentRequest)|-|-|

### Return type

[**OpenApiGenerationResult**](OpenApiGenerationResult.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated specification drafts, flow drafts, and operation coverage. |  -  |
| **0** | The request failed. |  -  |

## generateFromOpenApiContentWithHttpInfo

> ApiResponse<OpenApiGenerationResult> generateFromOpenApiContentWithHttpInfo(generateFromOpenApiContentRequest)

Generate specifications and flows from OpenAPI content

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        ContentFormat contentFormat = ContentFormat.fromValue("JSON"); // ContentFormat |
        String body = "body_example"; // String |
        Boolean includeNegativeTests = false; // Boolean |
        Boolean generateFlowScenarios = false; // Boolean |
        String generationStrategy = "SCHEMA_BASED"; // String |
        String negativeTestGenerationMode = "STRICT"; // String |
        try {
            APIgenerateFromOpenApiContentRequest request = APIgenerateFromOpenApiContentRequest.newBuilder()
                .contentFormat(contentFormat)
                .body(body)
                .includeNegativeTests(includeNegativeTests)
                .generateFlowScenarios(generateFlowScenarios)
                .generationStrategy(generationStrategy)
                .negativeTestGenerationMode(negativeTestGenerationMode)
                .build();
            ApiResponse<OpenApiGenerationResult> response = apiInstance.generateFromOpenApiContentWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#generateFromOpenApiContent");
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
| generateFromOpenApiContentRequest | [**APIgenerateFromOpenApiContentRequest**](GenerationApi.md#APIgenerateFromOpenApiContentRequest)|-|-|

### Return type

ApiResponse<[**OpenApiGenerationResult**](OpenApiGenerationResult.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated specification drafts, flow drafts, and operation coverage. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgenerateFromOpenApiContentRequest"></a>
## APIgenerateFromOpenApiContentRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **contentFormat** | [**ContentFormat**](.md) |  | [default to JSON] [enum: JSON, YAML, XML] |
| **body** | **String** |  | |
| **includeNegativeTests** | **Boolean** |  | [optional] [default to false] |
| **generateFlowScenarios** | **Boolean** |  | [optional] [default to false] |
| **generationStrategy** | **String** |  | [optional] [default to SCHEMA_BASED] [enum: SCHEMA_BASED, LIVE_API_CALL, HYBRID] |
| **negativeTestGenerationMode** | **String** |  | [optional] [default to EXTENDED] [enum: STRICT, EXTENDED] |



## generateSpecification

> List<SpecGenerationResult> generateSpecification(generateSpecificationRequest)

Generate an executable specification from concrete request evidence

Generates a REST, SOAP, GraphQL, or Streaming specification. Streaming input may contain observedEvidence from a completed Craftsman session; generation derives expectations from that transcript and never opens a second connection. Workflow placeholders must be materialized before this endpoint is called.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        Map<String, Object> requestBody = null; // Map<String, Object> |
        String mode = "FULL"; // String |
        ContentFormat format = ContentFormat.fromValue("JSON"); // ContentFormat |
        List<String> specGenerationTypes = Arrays.asList(); // List<String> | Comma-separated generation variants. Streaming currently accepts POSITIVE only.
        try {
            APIgenerateSpecificationRequest request = APIgenerateSpecificationRequest.newBuilder()
                .requestBody(requestBody)
                .mode(mode)
                .format(format)
                .specGenerationTypes(specGenerationTypes)
                .build();
            List<SpecGenerationResult> result = apiInstance.generateSpecification(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#generateSpecification");
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
| generateSpecificationRequest | [**APIgenerateSpecificationRequest**](GenerationApi.md#APIgenerateSpecificationRequest)|-|-|

### Return type

[**List&lt;SpecGenerationResult&gt;**](SpecGenerationResult.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated executable specification variants. |  -  |
| **0** | The request failed. |  -  |

## generateSpecificationWithHttpInfo

> ApiResponse<List<SpecGenerationResult>> generateSpecificationWithHttpInfo(generateSpecificationRequest)

Generate an executable specification from concrete request evidence

Generates a REST, SOAP, GraphQL, or Streaming specification. Streaming input may contain observedEvidence from a completed Craftsman session; generation derives expectations from that transcript and never opens a second connection. Workflow placeholders must be materialized before this endpoint is called.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        Map<String, Object> requestBody = null; // Map<String, Object> |
        String mode = "FULL"; // String |
        ContentFormat format = ContentFormat.fromValue("JSON"); // ContentFormat |
        List<String> specGenerationTypes = Arrays.asList(); // List<String> | Comma-separated generation variants. Streaming currently accepts POSITIVE only.
        try {
            APIgenerateSpecificationRequest request = APIgenerateSpecificationRequest.newBuilder()
                .requestBody(requestBody)
                .mode(mode)
                .format(format)
                .specGenerationTypes(specGenerationTypes)
                .build();
            ApiResponse<List<SpecGenerationResult>> response = apiInstance.generateSpecificationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#generateSpecification");
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
| generateSpecificationRequest | [**APIgenerateSpecificationRequest**](GenerationApi.md#APIgenerateSpecificationRequest)|-|-|

### Return type

ApiResponse<[**List&lt;SpecGenerationResult&gt;**](SpecGenerationResult.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated executable specification variants. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgenerateSpecificationRequest"></a>
## APIgenerateSpecificationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md) |  | |
| **mode** | **String** |  | [optional] [default to FULL] [enum: FULL, PATHS, HYBRID] |
| **format** | [**ContentFormat**](.md) |  | [optional] [default to JSON] [enum: JSON, YAML, XML] |
| **specGenerationTypes** | [**List&lt;String&gt;**](String.md) | Comma-separated generation variants. Streaming currently accepts POSITIVE only. | [optional] [enum: POSITIVE, NEGATIVE, DUPLICATE] |



## getArtifactGenerationProfile

> ArtifactGenerationProfile getArtifactGenerationProfile(getArtifactGenerationProfileRequest)

Get a CI export profile

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        UUID profileId = UUID.randomUUID(); // UUID | UUIDv7 identifier of a CI export profile.
        try {
            APIgetArtifactGenerationProfileRequest request = APIgetArtifactGenerationProfileRequest.newBuilder()
                .profileId(profileId)
                .build();
            ArtifactGenerationProfile result = apiInstance.getArtifactGenerationProfile(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#getArtifactGenerationProfile");
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
| getArtifactGenerationProfileRequest | [**APIgetArtifactGenerationProfileRequest**](GenerationApi.md#APIgetArtifactGenerationProfileRequest)|-|-|

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested profile. |  -  |
| **0** | The request failed. |  -  |

## getArtifactGenerationProfileWithHttpInfo

> ApiResponse<ArtifactGenerationProfile> getArtifactGenerationProfileWithHttpInfo(getArtifactGenerationProfileRequest)

Get a CI export profile

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        UUID profileId = UUID.randomUUID(); // UUID | UUIDv7 identifier of a CI export profile.
        try {
            APIgetArtifactGenerationProfileRequest request = APIgetArtifactGenerationProfileRequest.newBuilder()
                .profileId(profileId)
                .build();
            ApiResponse<ArtifactGenerationProfile> response = apiInstance.getArtifactGenerationProfileWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#getArtifactGenerationProfile");
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
| getArtifactGenerationProfileRequest | [**APIgetArtifactGenerationProfileRequest**](GenerationApi.md#APIgetArtifactGenerationProfileRequest)|-|-|

### Return type

ApiResponse<[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested profile. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetArtifactGenerationProfileRequest"></a>
## APIgetArtifactGenerationProfileRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **profileId** | **UUID** | UUIDv7 identifier of a CI export profile. | |



## getAtfProjectValidationResult

> AtfValidationResult getAtfProjectValidationResult(getAtfProjectValidationResultRequest)

Get ATF validation status or result

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        String validationId = "validationId_example"; // String | Opaque identifier of a bounded asynchronous ATF validation job.
        try {
            APIgetAtfProjectValidationResultRequest request = APIgetAtfProjectValidationResultRequest.newBuilder()
                .validationId(validationId)
                .build();
            AtfValidationResult result = apiInstance.getAtfProjectValidationResult(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#getAtfProjectValidationResult");
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
| getAtfProjectValidationResultRequest | [**APIgetAtfProjectValidationResultRequest**](GenerationApi.md#APIgetAtfProjectValidationResultRequest)|-|-|

### Return type

[**AtfValidationResult**](AtfValidationResult.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current or terminal validation result. |  -  |
| **409** | The validation job is still running. Retry with the same identifier. |  -  |
| **0** | The request failed. |  -  |

## getAtfProjectValidationResultWithHttpInfo

> ApiResponse<AtfValidationResult> getAtfProjectValidationResultWithHttpInfo(getAtfProjectValidationResultRequest)

Get ATF validation status or result

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        String validationId = "validationId_example"; // String | Opaque identifier of a bounded asynchronous ATF validation job.
        try {
            APIgetAtfProjectValidationResultRequest request = APIgetAtfProjectValidationResultRequest.newBuilder()
                .validationId(validationId)
                .build();
            ApiResponse<AtfValidationResult> response = apiInstance.getAtfProjectValidationResultWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#getAtfProjectValidationResult");
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
| getAtfProjectValidationResultRequest | [**APIgetAtfProjectValidationResultRequest**](GenerationApi.md#APIgetAtfProjectValidationResultRequest)|-|-|

### Return type

ApiResponse<[**AtfValidationResult**](AtfValidationResult.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current or terminal validation result. |  -  |
| **409** | The validation job is still running. Retry with the same identifier. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetAtfProjectValidationResultRequest"></a>
## APIgetAtfProjectValidationResultRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **validationId** | **String** | Opaque identifier of a bounded asynchronous ATF validation job. | |



## listArtifactGenerationProfiles

> List<ArtifactGenerationProfile> listArtifactGenerationProfiles()

List CI export profiles

Lists reusable export definitions used by CI to resolve an environment-specific source bundle and download a compile-validated ATF archive.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        try {
            List<ArtifactGenerationProfile> result = apiInstance.listArtifactGenerationProfiles();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#listArtifactGenerationProfiles");
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

[**List&lt;ArtifactGenerationProfile&gt;**](ArtifactGenerationProfile.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CI export profiles in the active project. |  -  |
| **0** | The request failed. |  -  |

## listArtifactGenerationProfilesWithHttpInfo

> ApiResponse<List<ArtifactGenerationProfile>> listArtifactGenerationProfilesWithHttpInfo()

List CI export profiles

Lists reusable export definitions used by CI to resolve an environment-specific source bundle and download a compile-validated ATF archive.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        try {
            ApiResponse<List<ArtifactGenerationProfile>> response = apiInstance.listArtifactGenerationProfilesWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#listArtifactGenerationProfiles");
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

ApiResponse<[**List&lt;ArtifactGenerationProfile&gt;**](ArtifactGenerationProfile.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CI export profiles in the active project. |  -  |
| **0** | The request failed. |  -  |


## observeAtfProjectValidation

> String observeAtfProjectValidation(observeAtfProjectValidationRequest)

Observe ATF validation progress

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        String validationId = "validationId_example"; // String | Opaque identifier of a bounded asynchronous ATF validation job.
        try {
            APIobserveAtfProjectValidationRequest request = APIobserveAtfProjectValidationRequest.newBuilder()
                .validationId(validationId)
                .build();
            String result = apiInstance.observeAtfProjectValidation(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#observeAtfProjectValidation");
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
| observeAtfProjectValidationRequest | [**APIobserveAtfProjectValidationRequest**](GenerationApi.md#APIobserveAtfProjectValidationRequest)|-|-|

### Return type

**String**


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server-sent validation lifecycle events. If the stream is interrupted, fetch the result endpoint with the same identifier. |  -  |
| **0** | The request failed. |  -  |

## observeAtfProjectValidationWithHttpInfo

> ApiResponse<String> observeAtfProjectValidationWithHttpInfo(observeAtfProjectValidationRequest)

Observe ATF validation progress

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        String validationId = "validationId_example"; // String | Opaque identifier of a bounded asynchronous ATF validation job.
        try {
            APIobserveAtfProjectValidationRequest request = APIobserveAtfProjectValidationRequest.newBuilder()
                .validationId(validationId)
                .build();
            ApiResponse<String> response = apiInstance.observeAtfProjectValidationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#observeAtfProjectValidation");
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
| observeAtfProjectValidationRequest | [**APIobserveAtfProjectValidationRequest**](GenerationApi.md#APIobserveAtfProjectValidationRequest)|-|-|

### Return type

ApiResponse<**String**>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server-sent validation lifecycle events. If the stream is interrupted, fetch the result endpoint with the same identifier. |  -  |
| **0** | The request failed. |  -  |


<a id="APIobserveAtfProjectValidationRequest"></a>
## APIobserveAtfProjectValidationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **validationId** | **String** | Opaque identifier of a bounded asynchronous ATF validation job. | |



## previewAtfProject

> AtfGenerationResult previewAtfProject(previewAtfProjectRequest)

Generate an ATF project preview

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        AtfGenerationInput atfGenerationInput = new AtfGenerationInput(); // AtfGenerationInput |
        try {
            APIpreviewAtfProjectRequest request = APIpreviewAtfProjectRequest.newBuilder()
                .atfGenerationInput(atfGenerationInput)
                .build();
            AtfGenerationResult result = apiInstance.previewAtfProject(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#previewAtfProject");
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
| previewAtfProjectRequest | [**APIpreviewAtfProjectRequest**](GenerationApi.md#APIpreviewAtfProjectRequest)|-|-|

### Return type

[**AtfGenerationResult**](AtfGenerationResult.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated files, manifest, and compatibility notes. |  -  |
| **0** | The request failed. |  -  |

## previewAtfProjectWithHttpInfo

> ApiResponse<AtfGenerationResult> previewAtfProjectWithHttpInfo(previewAtfProjectRequest)

Generate an ATF project preview

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        AtfGenerationInput atfGenerationInput = new AtfGenerationInput(); // AtfGenerationInput |
        try {
            APIpreviewAtfProjectRequest request = APIpreviewAtfProjectRequest.newBuilder()
                .atfGenerationInput(atfGenerationInput)
                .build();
            ApiResponse<AtfGenerationResult> response = apiInstance.previewAtfProjectWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#previewAtfProject");
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
| previewAtfProjectRequest | [**APIpreviewAtfProjectRequest**](GenerationApi.md#APIpreviewAtfProjectRequest)|-|-|

### Return type

ApiResponse<[**AtfGenerationResult**](AtfGenerationResult.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated files, manifest, and compatibility notes. |  -  |
| **0** | The request failed. |  -  |


<a id="APIpreviewAtfProjectRequest"></a>
## APIpreviewAtfProjectRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **atfGenerationInput** | [**AtfGenerationInput**](AtfGenerationInput.md) |  | |



## refreshArtifactGenerationProfileBundle

> ArtifactGenerationProfile refreshArtifactGenerationProfileBundle(refreshArtifactGenerationProfileBundleRequest)

Capture or refresh an environment baseline

Resolves current selected assets and atomically stores the bundle plus its hash for PINNED or FAIL_ON_DRIFT downloads.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        UUID profileId = UUID.randomUUID(); // UUID | UUIDv7 identifier of a CI export profile.
        String environmentKey = "environmentKey_example"; // String | Stable profile environment key such as test, staging, or production.
        try {
            APIrefreshArtifactGenerationProfileBundleRequest request = APIrefreshArtifactGenerationProfileBundleRequest.newBuilder()
                .profileId(profileId)
                .environmentKey(environmentKey)
                .build();
            ArtifactGenerationProfile result = apiInstance.refreshArtifactGenerationProfileBundle(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#refreshArtifactGenerationProfileBundle");
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
| refreshArtifactGenerationProfileBundleRequest | [**APIrefreshArtifactGenerationProfileBundleRequest**](GenerationApi.md#APIrefreshArtifactGenerationProfileBundleRequest)|-|-|

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The refreshed profile. |  -  |
| **0** | The request failed. |  -  |

## refreshArtifactGenerationProfileBundleWithHttpInfo

> ApiResponse<ArtifactGenerationProfile> refreshArtifactGenerationProfileBundleWithHttpInfo(refreshArtifactGenerationProfileBundleRequest)

Capture or refresh an environment baseline

Resolves current selected assets and atomically stores the bundle plus its hash for PINNED or FAIL_ON_DRIFT downloads.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        UUID profileId = UUID.randomUUID(); // UUID | UUIDv7 identifier of a CI export profile.
        String environmentKey = "environmentKey_example"; // String | Stable profile environment key such as test, staging, or production.
        try {
            APIrefreshArtifactGenerationProfileBundleRequest request = APIrefreshArtifactGenerationProfileBundleRequest.newBuilder()
                .profileId(profileId)
                .environmentKey(environmentKey)
                .build();
            ApiResponse<ArtifactGenerationProfile> response = apiInstance.refreshArtifactGenerationProfileBundleWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#refreshArtifactGenerationProfileBundle");
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
| refreshArtifactGenerationProfileBundleRequest | [**APIrefreshArtifactGenerationProfileBundleRequest**](GenerationApi.md#APIrefreshArtifactGenerationProfileBundleRequest)|-|-|

### Return type

ApiResponse<[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The refreshed profile. |  -  |
| **0** | The request failed. |  -  |


<a id="APIrefreshArtifactGenerationProfileBundleRequest"></a>
## APIrefreshArtifactGenerationProfileBundleRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **profileId** | **UUID** | UUIDv7 identifier of a CI export profile. | |
| **environmentKey** | **String** | Stable profile environment key such as test, staging, or production. | |



## startAtfProjectValidation

> AtfValidationStart startAtfProjectValidation(startAtfProjectValidationRequest)

Start asynchronous ATF compile validation

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        AtfGenerationInput atfGenerationInput = new AtfGenerationInput(); // AtfGenerationInput |
        try {
            APIstartAtfProjectValidationRequest request = APIstartAtfProjectValidationRequest.newBuilder()
                .atfGenerationInput(atfGenerationInput)
                .build();
            AtfValidationStart result = apiInstance.startAtfProjectValidation(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#startAtfProjectValidation");
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
| startAtfProjectValidationRequest | [**APIstartAtfProjectValidationRequest**](GenerationApi.md#APIstartAtfProjectValidationRequest)|-|-|

### Return type

[**AtfValidationStart**](AtfValidationStart.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Identifier used to observe the bounded validation job. |  -  |
| **429** | The company or global validation capacity is currently in use. |  -  |
| **0** | The request failed. |  -  |

## startAtfProjectValidationWithHttpInfo

> ApiResponse<AtfValidationStart> startAtfProjectValidationWithHttpInfo(startAtfProjectValidationRequest)

Start asynchronous ATF compile validation

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        AtfGenerationInput atfGenerationInput = new AtfGenerationInput(); // AtfGenerationInput |
        try {
            APIstartAtfProjectValidationRequest request = APIstartAtfProjectValidationRequest.newBuilder()
                .atfGenerationInput(atfGenerationInput)
                .build();
            ApiResponse<AtfValidationStart> response = apiInstance.startAtfProjectValidationWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#startAtfProjectValidation");
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
| startAtfProjectValidationRequest | [**APIstartAtfProjectValidationRequest**](GenerationApi.md#APIstartAtfProjectValidationRequest)|-|-|

### Return type

ApiResponse<[**AtfValidationStart**](AtfValidationStart.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Identifier used to observe the bounded validation job. |  -  |
| **429** | The company or global validation capacity is currently in use. |  -  |
| **0** | The request failed. |  -  |


<a id="APIstartAtfProjectValidationRequest"></a>
## APIstartAtfProjectValidationRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **atfGenerationInput** | [**AtfGenerationInput**](AtfGenerationInput.md) |  | |



## updateArtifactGenerationProfile

> ArtifactGenerationProfile updateArtifactGenerationProfile(updateArtifactGenerationProfileRequest)

Update a CI export profile

Send the revision returned by the latest read. A stale revision is rejected instead of overwriting a teammate&#39;s changes.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        UUID profileId = UUID.randomUUID(); // UUID | UUIDv7 identifier of a CI export profile.
        ArtifactGenerationProfileInput artifactGenerationProfileInput = new ArtifactGenerationProfileInput(); // ArtifactGenerationProfileInput |
        try {
            APIupdateArtifactGenerationProfileRequest request = APIupdateArtifactGenerationProfileRequest.newBuilder()
                .profileId(profileId)
                .artifactGenerationProfileInput(artifactGenerationProfileInput)
                .build();
            ArtifactGenerationProfile result = apiInstance.updateArtifactGenerationProfile(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#updateArtifactGenerationProfile");
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
| updateArtifactGenerationProfileRequest | [**APIupdateArtifactGenerationProfileRequest**](GenerationApi.md#APIupdateArtifactGenerationProfileRequest)|-|-|

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated profile and its next revision. |  -  |
| **409** | The profile was updated after the supplied revision was read. |  -  |
| **0** | The request failed. |  -  |

## updateArtifactGenerationProfileWithHttpInfo

> ApiResponse<ArtifactGenerationProfile> updateArtifactGenerationProfileWithHttpInfo(updateArtifactGenerationProfileRequest)

Update a CI export profile

Send the revision returned by the latest read. A stale revision is rejected instead of overwriting a teammate&#39;s changes.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        UUID profileId = UUID.randomUUID(); // UUID | UUIDv7 identifier of a CI export profile.
        ArtifactGenerationProfileInput artifactGenerationProfileInput = new ArtifactGenerationProfileInput(); // ArtifactGenerationProfileInput |
        try {
            APIupdateArtifactGenerationProfileRequest request = APIupdateArtifactGenerationProfileRequest.newBuilder()
                .profileId(profileId)
                .artifactGenerationProfileInput(artifactGenerationProfileInput)
                .build();
            ApiResponse<ArtifactGenerationProfile> response = apiInstance.updateArtifactGenerationProfileWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#updateArtifactGenerationProfile");
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
| updateArtifactGenerationProfileRequest | [**APIupdateArtifactGenerationProfileRequest**](GenerationApi.md#APIupdateArtifactGenerationProfileRequest)|-|-|

### Return type

ApiResponse<[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated profile and its next revision. |  -  |
| **409** | The profile was updated after the supplied revision was read. |  -  |
| **0** | The request failed. |  -  |


<a id="APIupdateArtifactGenerationProfileRequest"></a>
## APIupdateArtifactGenerationProfileRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **profileId** | **UUID** | UUIDv7 identifier of a CI export profile. | |
| **artifactGenerationProfileInput** | [**ArtifactGenerationProfileInput**](ArtifactGenerationProfileInput.md) |  | |



## validateAtfProject

> AtfValidationResult validateAtfProject(validateAtfProjectRequest)

Validate that an ATF project compiles

Resolves the selected assets, generates the project, and runs a bounded compile validation without creating an archive.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        AtfGenerationInput atfGenerationInput = new AtfGenerationInput(); // AtfGenerationInput |
        try {
            APIvalidateAtfProjectRequest request = APIvalidateAtfProjectRequest.newBuilder()
                .atfGenerationInput(atfGenerationInput)
                .build();
            AtfValidationResult result = apiInstance.validateAtfProject(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#validateAtfProject");
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
| validateAtfProjectRequest | [**APIvalidateAtfProjectRequest**](GenerationApi.md#APIvalidateAtfProjectRequest)|-|-|

### Return type

[**AtfValidationResult**](AtfValidationResult.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Structural and compile readiness for the generated project. |  -  |
| **429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
| **0** | The request failed. |  -  |

## validateAtfProjectWithHttpInfo

> ApiResponse<AtfValidationResult> validateAtfProjectWithHttpInfo(validateAtfProjectRequest)

Validate that an ATF project compiles

Resolves the selected assets, generates the project, and runs a bounded compile validation without creating an archive.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.GenerationApi;
import software.ste.sdk.generated.api.GenerationApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        GenerationApi apiInstance = new GenerationApi(defaultClient);
        AtfGenerationInput atfGenerationInput = new AtfGenerationInput(); // AtfGenerationInput |
        try {
            APIvalidateAtfProjectRequest request = APIvalidateAtfProjectRequest.newBuilder()
                .atfGenerationInput(atfGenerationInput)
                .build();
            ApiResponse<AtfValidationResult> response = apiInstance.validateAtfProjectWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GenerationApi#validateAtfProject");
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
| validateAtfProjectRequest | [**APIvalidateAtfProjectRequest**](GenerationApi.md#APIvalidateAtfProjectRequest)|-|-|

### Return type

ApiResponse<[**AtfValidationResult**](AtfValidationResult.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Structural and compile readiness for the generated project. |  -  |
| **429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
| **0** | The request failed. |  -  |


<a id="APIvalidateAtfProjectRequest"></a>
## APIvalidateAtfProjectRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **atfGenerationInput** | [**AtfGenerationInput**](AtfGenerationInput.md) |  | |


