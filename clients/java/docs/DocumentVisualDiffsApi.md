# DocumentVisualDiffsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDocumentVisualDiff**](DocumentVisualDiffsApi.md#getDocumentVisualDiff) | **GET** /browser/visual/document-diffs/{visualDiffId} | Get a visual document diff |
| [**getDocumentVisualDiffWithHttpInfo**](DocumentVisualDiffsApi.md#getDocumentVisualDiffWithHttpInfo) | **GET** /browser/visual/document-diffs/{visualDiffId} | Get a visual document diff |
| [**getDocumentVisualDiffArtifact**](DocumentVisualDiffsApi.md#getDocumentVisualDiffArtifact) | **GET** /browser/visual/document-diffs/{visualDiffId}/artifacts/{artifactId} | Download a rendered visual diff page |
| [**getDocumentVisualDiffArtifactWithHttpInfo**](DocumentVisualDiffsApi.md#getDocumentVisualDiffArtifactWithHttpInfo) | **GET** /browser/visual/document-diffs/{visualDiffId}/artifacts/{artifactId} | Download a rendered visual diff page |
| [**prepareDocumentVisualDiffBaseline**](DocumentVisualDiffsApi.md#prepareDocumentVisualDiffBaseline) | **POST** /browser/visual/document-diffs/{visualDiffId}/baseline | Preview or create an attachment baseline update draft |
| [**prepareDocumentVisualDiffBaselineWithHttpInfo**](DocumentVisualDiffsApi.md#prepareDocumentVisualDiffBaselineWithHttpInfo) | **POST** /browser/visual/document-diffs/{visualDiffId}/baseline | Preview or create an attachment baseline update draft |
| [**regenerateDocumentVisualDiff**](DocumentVisualDiffsApi.md#regenerateDocumentVisualDiff) | **POST** /browser/visual/document-diffs/{visualDiffId}/regenerate | Regenerate a visual document diff |
| [**regenerateDocumentVisualDiffWithHttpInfo**](DocumentVisualDiffsApi.md#regenerateDocumentVisualDiffWithHttpInfo) | **POST** /browser/visual/document-diffs/{visualDiffId}/regenerate | Regenerate a visual document diff |
| [**uploadDocumentVisualDiffExpected**](DocumentVisualDiffsApi.md#uploadDocumentVisualDiffExpected) | **POST** /browser/visual/document-diffs/{visualDiffId}/expected | Upload a reference document and create a diff generation |
| [**uploadDocumentVisualDiffExpectedWithHttpInfo**](DocumentVisualDiffsApi.md#uploadDocumentVisualDiffExpectedWithHttpInfo) | **POST** /browser/visual/document-diffs/{visualDiffId}/expected | Upload a reference document and create a diff generation |



## getDocumentVisualDiff

> DocumentVisualDiff getDocumentVisualDiff(getDocumentVisualDiffRequest)

Get a visual document diff

Returns the protected viewer URL, TTL, immutable generations, and page-level artifact references.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        DocumentVisualDiffsApi apiInstance = new DocumentVisualDiffsApi(defaultClient);
        UUID visualDiffId = UUID.randomUUID(); // UUID | UUIDv7 identifier of an organization-scoped visual document diff session.
        try {
            APIgetDocumentVisualDiffRequest request = APIgetDocumentVisualDiffRequest.newBuilder()
                .visualDiffId(visualDiffId)
                .build();
            DocumentVisualDiff result = apiInstance.getDocumentVisualDiff(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DocumentVisualDiffsApi#getDocumentVisualDiff");
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
| getDocumentVisualDiffRequest | [**APIgetDocumentVisualDiffRequest**](DocumentVisualDiffsApi.md#APIgetDocumentVisualDiffRequest)|-|-|

### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Visual diff metadata scoped to the token company and active project. |  -  |
| **410** | Derived visual artifacts expired; source run metadata remains available. |  -  |
| **0** | The request failed. |  -  |

## getDocumentVisualDiffWithHttpInfo

> ApiResponse<DocumentVisualDiff> getDocumentVisualDiffWithHttpInfo(getDocumentVisualDiffRequest)

Get a visual document diff

Returns the protected viewer URL, TTL, immutable generations, and page-level artifact references.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        DocumentVisualDiffsApi apiInstance = new DocumentVisualDiffsApi(defaultClient);
        UUID visualDiffId = UUID.randomUUID(); // UUID | UUIDv7 identifier of an organization-scoped visual document diff session.
        try {
            APIgetDocumentVisualDiffRequest request = APIgetDocumentVisualDiffRequest.newBuilder()
                .visualDiffId(visualDiffId)
                .build();
            ApiResponse<DocumentVisualDiff> response = apiInstance.getDocumentVisualDiffWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DocumentVisualDiffsApi#getDocumentVisualDiff");
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
| getDocumentVisualDiffRequest | [**APIgetDocumentVisualDiffRequest**](DocumentVisualDiffsApi.md#APIgetDocumentVisualDiffRequest)|-|-|

### Return type

ApiResponse<[**DocumentVisualDiff**](DocumentVisualDiff.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Visual diff metadata scoped to the token company and active project. |  -  |
| **410** | Derived visual artifacts expired; source run metadata remains available. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetDocumentVisualDiffRequest"></a>
## APIgetDocumentVisualDiffRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **visualDiffId** | **UUID** | UUIDv7 identifier of an organization-scoped visual document diff session. | |



## getDocumentVisualDiffArtifact

> File getDocumentVisualDiffArtifact(getDocumentVisualDiffArtifactRequest)

Download a rendered visual diff page

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        DocumentVisualDiffsApi apiInstance = new DocumentVisualDiffsApi(defaultClient);
        UUID visualDiffId = UUID.randomUUID(); // UUID | UUIDv7 identifier of an organization-scoped visual document diff session.
        UUID artifactId = UUID.randomUUID(); // UUID |
        try {
            APIgetDocumentVisualDiffArtifactRequest request = APIgetDocumentVisualDiffArtifactRequest.newBuilder()
                .visualDiffId(visualDiffId)
                .artifactId(artifactId)
                .build();
            File result = apiInstance.getDocumentVisualDiffArtifact(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DocumentVisualDiffsApi#getDocumentVisualDiffArtifact");
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
| getDocumentVisualDiffArtifactRequest | [**APIgetDocumentVisualDiffArtifactRequest**](DocumentVisualDiffsApi.md#APIgetDocumentVisualDiffArtifactRequest)|-|-|

### Return type

[**File**](File.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Decrypted PNG page. The encrypted derivative remains subject to the diagnostic TTL. |  -  |
| **0** | The request failed. |  -  |

## getDocumentVisualDiffArtifactWithHttpInfo

> ApiResponse<File> getDocumentVisualDiffArtifactWithHttpInfo(getDocumentVisualDiffArtifactRequest)

Download a rendered visual diff page

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        DocumentVisualDiffsApi apiInstance = new DocumentVisualDiffsApi(defaultClient);
        UUID visualDiffId = UUID.randomUUID(); // UUID | UUIDv7 identifier of an organization-scoped visual document diff session.
        UUID artifactId = UUID.randomUUID(); // UUID |
        try {
            APIgetDocumentVisualDiffArtifactRequest request = APIgetDocumentVisualDiffArtifactRequest.newBuilder()
                .visualDiffId(visualDiffId)
                .artifactId(artifactId)
                .build();
            ApiResponse<File> response = apiInstance.getDocumentVisualDiffArtifactWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DocumentVisualDiffsApi#getDocumentVisualDiffArtifact");
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
| getDocumentVisualDiffArtifactRequest | [**APIgetDocumentVisualDiffArtifactRequest**](DocumentVisualDiffsApi.md#APIgetDocumentVisualDiffArtifactRequest)|-|-|

### Return type

ApiResponse<[**File**](File.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Decrypted PNG page. The encrypted derivative remains subject to the diagnostic TTL. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetDocumentVisualDiffArtifactRequest"></a>
## APIgetDocumentVisualDiffArtifactRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **visualDiffId** | **UUID** | UUIDv7 identifier of an organization-scoped visual document diff session. | |
| **artifactId** | **UUID** |  | |



## prepareDocumentVisualDiffBaseline

> DocumentVisualDiffBaselinePreview prepareDocumentVisualDiffBaseline(prepareDocumentVisualDiffBaselineRequest)

Preview or create an attachment baseline update draft

Never silently overwrites a specification. Send confirm&#x3D;false first, then confirm&#x3D;true only after review.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        DocumentVisualDiffsApi apiInstance = new DocumentVisualDiffsApi(defaultClient);
        UUID visualDiffId = UUID.randomUUID(); // UUID | UUIDv7 identifier of an organization-scoped visual document diff session.
        DocumentVisualDiffBaselineRequest documentVisualDiffBaselineRequest = new DocumentVisualDiffBaselineRequest(); // DocumentVisualDiffBaselineRequest |
        try {
            APIprepareDocumentVisualDiffBaselineRequest request = APIprepareDocumentVisualDiffBaselineRequest.newBuilder()
                .visualDiffId(visualDiffId)
                .documentVisualDiffBaselineRequest(documentVisualDiffBaselineRequest)
                .build();
            DocumentVisualDiffBaselinePreview result = apiInstance.prepareDocumentVisualDiffBaseline(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DocumentVisualDiffsApi#prepareDocumentVisualDiffBaseline");
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
| prepareDocumentVisualDiffBaselineRequest | [**APIprepareDocumentVisualDiffBaselineRequest**](DocumentVisualDiffsApi.md#APIprepareDocumentVisualDiffBaselineRequest)|-|-|

### Return type

[**DocumentVisualDiffBaselinePreview**](DocumentVisualDiffBaselinePreview.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Baseline hash/fingerprint preview or confirmed update draft. |  -  |
| **0** | The request failed. |  -  |

## prepareDocumentVisualDiffBaselineWithHttpInfo

> ApiResponse<DocumentVisualDiffBaselinePreview> prepareDocumentVisualDiffBaselineWithHttpInfo(prepareDocumentVisualDiffBaselineRequest)

Preview or create an attachment baseline update draft

Never silently overwrites a specification. Send confirm&#x3D;false first, then confirm&#x3D;true only after review.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        DocumentVisualDiffsApi apiInstance = new DocumentVisualDiffsApi(defaultClient);
        UUID visualDiffId = UUID.randomUUID(); // UUID | UUIDv7 identifier of an organization-scoped visual document diff session.
        DocumentVisualDiffBaselineRequest documentVisualDiffBaselineRequest = new DocumentVisualDiffBaselineRequest(); // DocumentVisualDiffBaselineRequest |
        try {
            APIprepareDocumentVisualDiffBaselineRequest request = APIprepareDocumentVisualDiffBaselineRequest.newBuilder()
                .visualDiffId(visualDiffId)
                .documentVisualDiffBaselineRequest(documentVisualDiffBaselineRequest)
                .build();
            ApiResponse<DocumentVisualDiffBaselinePreview> response = apiInstance.prepareDocumentVisualDiffBaselineWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DocumentVisualDiffsApi#prepareDocumentVisualDiffBaseline");
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
| prepareDocumentVisualDiffBaselineRequest | [**APIprepareDocumentVisualDiffBaselineRequest**](DocumentVisualDiffsApi.md#APIprepareDocumentVisualDiffBaselineRequest)|-|-|

### Return type

ApiResponse<[**DocumentVisualDiffBaselinePreview**](DocumentVisualDiffBaselinePreview.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Baseline hash/fingerprint preview or confirmed update draft. |  -  |
| **0** | The request failed. |  -  |


<a id="APIprepareDocumentVisualDiffBaselineRequest"></a>
## APIprepareDocumentVisualDiffBaselineRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **visualDiffId** | **UUID** | UUIDv7 identifier of an organization-scoped visual document diff session. | |
| **documentVisualDiffBaselineRequest** | [**DocumentVisualDiffBaselineRequest**](DocumentVisualDiffBaselineRequest.md) |  | |



## regenerateDocumentVisualDiff

> DocumentVisualDiff regenerateDocumentVisualDiff(regenerateDocumentVisualDiffRequest)

Regenerate a visual document diff

Creates an immutable generation from the existing rendered pages with new comparison settings and normalized visual exclusion regions.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        DocumentVisualDiffsApi apiInstance = new DocumentVisualDiffsApi(defaultClient);
        UUID visualDiffId = UUID.randomUUID(); // UUID | UUIDv7 identifier of an organization-scoped visual document diff session.
        DocumentVisualDiffRegenerateRequest documentVisualDiffRegenerateRequest = new DocumentVisualDiffRegenerateRequest(); // DocumentVisualDiffRegenerateRequest |
        try {
            APIregenerateDocumentVisualDiffRequest request = APIregenerateDocumentVisualDiffRequest.newBuilder()
                .visualDiffId(visualDiffId)
                .documentVisualDiffRegenerateRequest(documentVisualDiffRegenerateRequest)
                .build();
            DocumentVisualDiff result = apiInstance.regenerateDocumentVisualDiff(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DocumentVisualDiffsApi#regenerateDocumentVisualDiff");
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
| regenerateDocumentVisualDiffRequest | [**APIregenerateDocumentVisualDiffRequest**](DocumentVisualDiffsApi.md#APIregenerateDocumentVisualDiffRequest)|-|-|

### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Visual diff with a new current generation. |  -  |
| **0** | The request failed. |  -  |

## regenerateDocumentVisualDiffWithHttpInfo

> ApiResponse<DocumentVisualDiff> regenerateDocumentVisualDiffWithHttpInfo(regenerateDocumentVisualDiffRequest)

Regenerate a visual document diff

Creates an immutable generation from the existing rendered pages with new comparison settings and normalized visual exclusion regions.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        DocumentVisualDiffsApi apiInstance = new DocumentVisualDiffsApi(defaultClient);
        UUID visualDiffId = UUID.randomUUID(); // UUID | UUIDv7 identifier of an organization-scoped visual document diff session.
        DocumentVisualDiffRegenerateRequest documentVisualDiffRegenerateRequest = new DocumentVisualDiffRegenerateRequest(); // DocumentVisualDiffRegenerateRequest |
        try {
            APIregenerateDocumentVisualDiffRequest request = APIregenerateDocumentVisualDiffRequest.newBuilder()
                .visualDiffId(visualDiffId)
                .documentVisualDiffRegenerateRequest(documentVisualDiffRegenerateRequest)
                .build();
            ApiResponse<DocumentVisualDiff> response = apiInstance.regenerateDocumentVisualDiffWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DocumentVisualDiffsApi#regenerateDocumentVisualDiff");
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
| regenerateDocumentVisualDiffRequest | [**APIregenerateDocumentVisualDiffRequest**](DocumentVisualDiffsApi.md#APIregenerateDocumentVisualDiffRequest)|-|-|

### Return type

ApiResponse<[**DocumentVisualDiff**](DocumentVisualDiff.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Visual diff with a new current generation. |  -  |
| **0** | The request failed. |  -  |


<a id="APIregenerateDocumentVisualDiffRequest"></a>
## APIregenerateDocumentVisualDiffRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **visualDiffId** | **UUID** | UUIDv7 identifier of an organization-scoped visual document diff session. | |
| **documentVisualDiffRegenerateRequest** | [**DocumentVisualDiffRegenerateRequest**](DocumentVisualDiffRegenerateRequest.md) |  | [optional] |



## uploadDocumentVisualDiffExpected

> DocumentVisualDiff uploadDocumentVisualDiffExpected(uploadDocumentVisualDiffExpectedRequest)

Upload a reference document and create a diff generation

The uploaded PDF or image is rendered in memory and discarded. Only encrypted page images and diff metadata remain until TTL expiry.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        DocumentVisualDiffsApi apiInstance = new DocumentVisualDiffsApi(defaultClient);
        UUID visualDiffId = UUID.randomUUID(); // UUID | UUIDv7 identifier of an organization-scoped visual document diff session.
        File expected = new File("/path/to/file"); // File |
        Double colorThreshold = 24D; // Double |
        try {
            APIuploadDocumentVisualDiffExpectedRequest request = APIuploadDocumentVisualDiffExpectedRequest.newBuilder()
                .visualDiffId(visualDiffId)
                .expected(expected)
                .colorThreshold(colorThreshold)
                .build();
            DocumentVisualDiff result = apiInstance.uploadDocumentVisualDiffExpected(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DocumentVisualDiffsApi#uploadDocumentVisualDiffExpected");
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
| uploadDocumentVisualDiffExpectedRequest | [**APIuploadDocumentVisualDiffExpectedRequest**](DocumentVisualDiffsApi.md#APIuploadDocumentVisualDiffExpectedRequest)|-|-|

### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The visual diff with a new current generation. |  -  |
| **0** | The request failed. |  -  |

## uploadDocumentVisualDiffExpectedWithHttpInfo

> ApiResponse<DocumentVisualDiff> uploadDocumentVisualDiffExpectedWithHttpInfo(uploadDocumentVisualDiffExpectedRequest)

Upload a reference document and create a diff generation

The uploaded PDF or image is rendered in memory and discarded. Only encrypted page images and diff metadata remain until TTL expiry.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi;
import software.ste.sdk.generated.api.DocumentVisualDiffsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        DocumentVisualDiffsApi apiInstance = new DocumentVisualDiffsApi(defaultClient);
        UUID visualDiffId = UUID.randomUUID(); // UUID | UUIDv7 identifier of an organization-scoped visual document diff session.
        File expected = new File("/path/to/file"); // File |
        Double colorThreshold = 24D; // Double |
        try {
            APIuploadDocumentVisualDiffExpectedRequest request = APIuploadDocumentVisualDiffExpectedRequest.newBuilder()
                .visualDiffId(visualDiffId)
                .expected(expected)
                .colorThreshold(colorThreshold)
                .build();
            ApiResponse<DocumentVisualDiff> response = apiInstance.uploadDocumentVisualDiffExpectedWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DocumentVisualDiffsApi#uploadDocumentVisualDiffExpected");
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
| uploadDocumentVisualDiffExpectedRequest | [**APIuploadDocumentVisualDiffExpectedRequest**](DocumentVisualDiffsApi.md#APIuploadDocumentVisualDiffExpectedRequest)|-|-|

### Return type

ApiResponse<[**DocumentVisualDiff**](DocumentVisualDiff.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The visual diff with a new current generation. |  -  |
| **0** | The request failed. |  -  |


<a id="APIuploadDocumentVisualDiffExpectedRequest"></a>
## APIuploadDocumentVisualDiffExpectedRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **visualDiffId** | **UUID** | UUIDv7 identifier of an organization-scoped visual document diff session. | |
| **expected** | **File** |  | |
| **colorThreshold** | **Double** |  | [optional] [default to 24] |
