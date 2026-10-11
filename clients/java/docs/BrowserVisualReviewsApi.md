# BrowserVisualReviewsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**excludeBrowserVisualAreaAndRecompare**](BrowserVisualReviewsApi.md#excludeBrowserVisualAreaAndRecompare) | **POST** /browser/visual/comparisons/{comparisonId}/exclude-and-recompare | Exclude area and recompare |
| [**excludeBrowserVisualAreaAndRecompareWithHttpInfo**](BrowserVisualReviewsApi.md#excludeBrowserVisualAreaAndRecompareWithHttpInfo) | **POST** /browser/visual/comparisons/{comparisonId}/exclude-and-recompare | Exclude area and recompare |
| [**getBrowserVisualArtifactContent**](BrowserVisualReviewsApi.md#getBrowserVisualArtifactContent) | **GET** /browser/visual/artifacts/{artifactId}/content | Download Browser visual evidence |
| [**getBrowserVisualArtifactContentWithHttpInfo**](BrowserVisualReviewsApi.md#getBrowserVisualArtifactContentWithHttpInfo) | **GET** /browser/visual/artifacts/{artifactId}/content | Download Browser visual evidence |
| [**getBrowserVisualComparison**](BrowserVisualReviewsApi.md#getBrowserVisualComparison) | **GET** /browser/visual/comparisons/{comparisonId} | Get a Browser visual comparison |
| [**getBrowserVisualComparisonWithHttpInfo**](BrowserVisualReviewsApi.md#getBrowserVisualComparisonWithHttpInfo) | **GET** /browser/visual/comparisons/{comparisonId} | Get a Browser visual comparison |
| [**keepBrowserVisualAsRegression**](BrowserVisualReviewsApi.md#keepBrowserVisualAsRegression) | **POST** /browser/visual/comparisons/{comparisonId}/keep-as-regression | Keep as regression |
| [**keepBrowserVisualAsRegressionWithHttpInfo**](BrowserVisualReviewsApi.md#keepBrowserVisualAsRegressionWithHttpInfo) | **POST** /browser/visual/comparisons/{comparisonId}/keep-as-regression | Keep as regression |
| [**useCurrentBrowserVisualAsNewBaseline**](BrowserVisualReviewsApi.md#useCurrentBrowserVisualAsNewBaseline) | **POST** /browser/visual/comparisons/{comparisonId}/use-current-as-new-baseline | Use current as new baseline |
| [**useCurrentBrowserVisualAsNewBaselineWithHttpInfo**](BrowserVisualReviewsApi.md#useCurrentBrowserVisualAsNewBaselineWithHttpInfo) | **POST** /browser/visual/comparisons/{comparisonId}/use-current-as-new-baseline | Use current as new baseline |



## excludeBrowserVisualAreaAndRecompare

> BrowserVisualComparison excludeBrowserVisualAreaAndRecompare(excludeBrowserVisualAreaAndRecompareRequest)

Exclude area and recompare

Saves normalized exclusion masks in a new assertion revision and creates a child comparison generation with the existing Browser comparator.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        BrowserVisualReviewsApi apiInstance = new BrowserVisualReviewsApi(defaultClient);
        UUID comparisonId = UUID.randomUUID(); // UUID | Identifier of an immutable Browser visual comparison generation.
        BrowserVisualExcludeAndRecompareRequest browserVisualExcludeAndRecompareRequest = new BrowserVisualExcludeAndRecompareRequest(); // BrowserVisualExcludeAndRecompareRequest |
        try {
            APIexcludeBrowserVisualAreaAndRecompareRequest request = APIexcludeBrowserVisualAreaAndRecompareRequest.newBuilder()
                .comparisonId(comparisonId)
                .browserVisualExcludeAndRecompareRequest(browserVisualExcludeAndRecompareRequest)
                .build();
            BrowserVisualComparison result = apiInstance.excludeBrowserVisualAreaAndRecompare(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrowserVisualReviewsApi#excludeBrowserVisualAreaAndRecompare");
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
| excludeBrowserVisualAreaAndRecompareRequest | [**APIexcludeBrowserVisualAreaAndRecompareRequest**](BrowserVisualReviewsApi.md#APIexcludeBrowserVisualAreaAndRecompareRequest)|-|-|

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New comparison generation linked to the source and root comparisons. |  -  |
| **409** | The expected assertion revision is stale or the action id conflicts with another command. |  -  |
| **0** | The request failed. |  -  |

## excludeBrowserVisualAreaAndRecompareWithHttpInfo

> ApiResponse<BrowserVisualComparison> excludeBrowserVisualAreaAndRecompareWithHttpInfo(excludeBrowserVisualAreaAndRecompareRequest)

Exclude area and recompare

Saves normalized exclusion masks in a new assertion revision and creates a child comparison generation with the existing Browser comparator.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        BrowserVisualReviewsApi apiInstance = new BrowserVisualReviewsApi(defaultClient);
        UUID comparisonId = UUID.randomUUID(); // UUID | Identifier of an immutable Browser visual comparison generation.
        BrowserVisualExcludeAndRecompareRequest browserVisualExcludeAndRecompareRequest = new BrowserVisualExcludeAndRecompareRequest(); // BrowserVisualExcludeAndRecompareRequest |
        try {
            APIexcludeBrowserVisualAreaAndRecompareRequest request = APIexcludeBrowserVisualAreaAndRecompareRequest.newBuilder()
                .comparisonId(comparisonId)
                .browserVisualExcludeAndRecompareRequest(browserVisualExcludeAndRecompareRequest)
                .build();
            ApiResponse<BrowserVisualComparison> response = apiInstance.excludeBrowserVisualAreaAndRecompareWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrowserVisualReviewsApi#excludeBrowserVisualAreaAndRecompare");
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
| excludeBrowserVisualAreaAndRecompareRequest | [**APIexcludeBrowserVisualAreaAndRecompareRequest**](BrowserVisualReviewsApi.md#APIexcludeBrowserVisualAreaAndRecompareRequest)|-|-|

### Return type

ApiResponse<[**BrowserVisualComparison**](BrowserVisualComparison.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New comparison generation linked to the source and root comparisons. |  -  |
| **409** | The expected assertion revision is stale or the action id conflicts with another command. |  -  |
| **0** | The request failed. |  -  |


<a id="APIexcludeBrowserVisualAreaAndRecompareRequest"></a>
## APIexcludeBrowserVisualAreaAndRecompareRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **comparisonId** | **UUID** | Identifier of an immutable Browser visual comparison generation. | |
| **browserVisualExcludeAndRecompareRequest** | [**BrowserVisualExcludeAndRecompareRequest**](BrowserVisualExcludeAndRecompareRequest.md) |  | |



## getBrowserVisualArtifactContent

> File getBrowserVisualArtifactContent(getBrowserVisualArtifactContentRequest)

Download Browser visual evidence

Returns a retained PNG baseline, current, or diff artifact after company and project authorization.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        BrowserVisualReviewsApi apiInstance = new BrowserVisualReviewsApi(defaultClient);
        UUID artifactId = UUID.randomUUID(); // UUID |
        try {
            APIgetBrowserVisualArtifactContentRequest request = APIgetBrowserVisualArtifactContentRequest.newBuilder()
                .artifactId(artifactId)
                .build();
            File result = apiInstance.getBrowserVisualArtifactContent(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrowserVisualReviewsApi#getBrowserVisualArtifactContent");
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
| getBrowserVisualArtifactContentRequest | [**APIgetBrowserVisualArtifactContentRequest**](BrowserVisualReviewsApi.md#APIgetBrowserVisualArtifactContentRequest)|-|-|

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
| **200** | PNG visual evidence subject to the configured artifact retention policy. |  -  |
| **410** | The artifact expired; comparison metadata and lineage remain available. |  -  |
| **0** | The request failed. |  -  |

## getBrowserVisualArtifactContentWithHttpInfo

> ApiResponse<File> getBrowserVisualArtifactContentWithHttpInfo(getBrowserVisualArtifactContentRequest)

Download Browser visual evidence

Returns a retained PNG baseline, current, or diff artifact after company and project authorization.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        BrowserVisualReviewsApi apiInstance = new BrowserVisualReviewsApi(defaultClient);
        UUID artifactId = UUID.randomUUID(); // UUID |
        try {
            APIgetBrowserVisualArtifactContentRequest request = APIgetBrowserVisualArtifactContentRequest.newBuilder()
                .artifactId(artifactId)
                .build();
            ApiResponse<File> response = apiInstance.getBrowserVisualArtifactContentWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrowserVisualReviewsApi#getBrowserVisualArtifactContent");
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
| getBrowserVisualArtifactContentRequest | [**APIgetBrowserVisualArtifactContentRequest**](BrowserVisualReviewsApi.md#APIgetBrowserVisualArtifactContentRequest)|-|-|

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
| **200** | PNG visual evidence subject to the configured artifact retention policy. |  -  |
| **410** | The artifact expired; comparison metadata and lineage remain available. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetBrowserVisualArtifactContentRequest"></a>
## APIgetBrowserVisualArtifactContentRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **artifactId** | **UUID** |  | |



## getBrowserVisualComparison

> BrowserVisualComparison getBrowserVisualComparison(getBrowserVisualComparisonRequest)

Get a Browser visual comparison

Returns one immutable comparison generation, its evidence lineage, normalized exclusions, and currently available review actions.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        BrowserVisualReviewsApi apiInstance = new BrowserVisualReviewsApi(defaultClient);
        UUID comparisonId = UUID.randomUUID(); // UUID | Identifier of an immutable Browser visual comparison generation.
        try {
            APIgetBrowserVisualComparisonRequest request = APIgetBrowserVisualComparisonRequest.newBuilder()
                .comparisonId(comparisonId)
                .build();
            BrowserVisualComparison result = apiInstance.getBrowserVisualComparison(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrowserVisualReviewsApi#getBrowserVisualComparison");
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
| getBrowserVisualComparisonRequest | [**APIgetBrowserVisualComparisonRequest**](BrowserVisualReviewsApi.md#APIgetBrowserVisualComparisonRequest)|-|-|

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Browser visual comparison scoped to the token company and active project. |  -  |
| **0** | The request failed. |  -  |

## getBrowserVisualComparisonWithHttpInfo

> ApiResponse<BrowserVisualComparison> getBrowserVisualComparisonWithHttpInfo(getBrowserVisualComparisonRequest)

Get a Browser visual comparison

Returns one immutable comparison generation, its evidence lineage, normalized exclusions, and currently available review actions.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        BrowserVisualReviewsApi apiInstance = new BrowserVisualReviewsApi(defaultClient);
        UUID comparisonId = UUID.randomUUID(); // UUID | Identifier of an immutable Browser visual comparison generation.
        try {
            APIgetBrowserVisualComparisonRequest request = APIgetBrowserVisualComparisonRequest.newBuilder()
                .comparisonId(comparisonId)
                .build();
            ApiResponse<BrowserVisualComparison> response = apiInstance.getBrowserVisualComparisonWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrowserVisualReviewsApi#getBrowserVisualComparison");
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
| getBrowserVisualComparisonRequest | [**APIgetBrowserVisualComparisonRequest**](BrowserVisualReviewsApi.md#APIgetBrowserVisualComparisonRequest)|-|-|

### Return type

ApiResponse<[**BrowserVisualComparison**](BrowserVisualComparison.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Browser visual comparison scoped to the token company and active project. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetBrowserVisualComparisonRequest"></a>
## APIgetBrowserVisualComparisonRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **comparisonId** | **UUID** | Identifier of an immutable Browser visual comparison generation. | |



## keepBrowserVisualAsRegression

> BrowserVisualComparison keepBrowserVisualAsRegression(keepBrowserVisualAsRegressionRequest)

Keep as regression

Confirms the mismatch as a regression without changing the active baseline or assertion exclusions.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        BrowserVisualReviewsApi apiInstance = new BrowserVisualReviewsApi(defaultClient);
        UUID comparisonId = UUID.randomUUID(); // UUID | Identifier of an immutable Browser visual comparison generation.
        BrowserVisualKeepRegressionRequest browserVisualKeepRegressionRequest = new BrowserVisualKeepRegressionRequest(); // BrowserVisualKeepRegressionRequest |
        try {
            APIkeepBrowserVisualAsRegressionRequest request = APIkeepBrowserVisualAsRegressionRequest.newBuilder()
                .comparisonId(comparisonId)
                .browserVisualKeepRegressionRequest(browserVisualKeepRegressionRequest)
                .build();
            BrowserVisualComparison result = apiInstance.keepBrowserVisualAsRegression(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrowserVisualReviewsApi#keepBrowserVisualAsRegression");
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
| keepBrowserVisualAsRegressionRequest | [**APIkeepBrowserVisualAsRegressionRequest**](BrowserVisualReviewsApi.md#APIkeepBrowserVisualAsRegressionRequest)|-|-|

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comparison marked as a confirmed regression. |  -  |
| **0** | The request failed. |  -  |

## keepBrowserVisualAsRegressionWithHttpInfo

> ApiResponse<BrowserVisualComparison> keepBrowserVisualAsRegressionWithHttpInfo(keepBrowserVisualAsRegressionRequest)

Keep as regression

Confirms the mismatch as a regression without changing the active baseline or assertion exclusions.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        BrowserVisualReviewsApi apiInstance = new BrowserVisualReviewsApi(defaultClient);
        UUID comparisonId = UUID.randomUUID(); // UUID | Identifier of an immutable Browser visual comparison generation.
        BrowserVisualKeepRegressionRequest browserVisualKeepRegressionRequest = new BrowserVisualKeepRegressionRequest(); // BrowserVisualKeepRegressionRequest |
        try {
            APIkeepBrowserVisualAsRegressionRequest request = APIkeepBrowserVisualAsRegressionRequest.newBuilder()
                .comparisonId(comparisonId)
                .browserVisualKeepRegressionRequest(browserVisualKeepRegressionRequest)
                .build();
            ApiResponse<BrowserVisualComparison> response = apiInstance.keepBrowserVisualAsRegressionWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrowserVisualReviewsApi#keepBrowserVisualAsRegression");
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
| keepBrowserVisualAsRegressionRequest | [**APIkeepBrowserVisualAsRegressionRequest**](BrowserVisualReviewsApi.md#APIkeepBrowserVisualAsRegressionRequest)|-|-|

### Return type

ApiResponse<[**BrowserVisualComparison**](BrowserVisualComparison.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comparison marked as a confirmed regression. |  -  |
| **0** | The request failed. |  -  |


<a id="APIkeepBrowserVisualAsRegressionRequest"></a>
## APIkeepBrowserVisualAsRegressionRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **comparisonId** | **UUID** | Identifier of an immutable Browser visual comparison generation. | |
| **browserVisualKeepRegressionRequest** | [**BrowserVisualKeepRegressionRequest**](BrowserVisualKeepRegressionRequest.md) |  | |



## useCurrentBrowserVisualAsNewBaseline

> BrowserVisualComparison useCurrentBrowserVisualAsNewBaseline(useCurrentBrowserVisualAsNewBaselineRequest)

Use current as new baseline

Creates and activates a new immutable baseline revision. Historical comparison and baseline evidence remains addressable by Snapshot Timeline.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        BrowserVisualReviewsApi apiInstance = new BrowserVisualReviewsApi(defaultClient);
        UUID comparisonId = UUID.randomUUID(); // UUID | Identifier of an immutable Browser visual comparison generation.
        BrowserVisualPromoteBaselineRequest browserVisualPromoteBaselineRequest = new BrowserVisualPromoteBaselineRequest(); // BrowserVisualPromoteBaselineRequest |
        try {
            APIuseCurrentBrowserVisualAsNewBaselineRequest request = APIuseCurrentBrowserVisualAsNewBaselineRequest.newBuilder()
                .comparisonId(comparisonId)
                .browserVisualPromoteBaselineRequest(browserVisualPromoteBaselineRequest)
                .build();
            BrowserVisualComparison result = apiInstance.useCurrentBrowserVisualAsNewBaseline(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrowserVisualReviewsApi#useCurrentBrowserVisualAsNewBaseline");
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
| useCurrentBrowserVisualAsNewBaselineRequest | [**APIuseCurrentBrowserVisualAsNewBaselineRequest**](BrowserVisualReviewsApi.md#APIuseCurrentBrowserVisualAsNewBaselineRequest)|-|-|

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reviewed comparison with the applied baseline revision. |  -  |
| **409** | The expected assertion revision is stale or the action id conflicts with another command. |  -  |
| **0** | The request failed. |  -  |

## useCurrentBrowserVisualAsNewBaselineWithHttpInfo

> ApiResponse<BrowserVisualComparison> useCurrentBrowserVisualAsNewBaselineWithHttpInfo(useCurrentBrowserVisualAsNewBaselineRequest)

Use current as new baseline

Creates and activates a new immutable baseline revision. Historical comparison and baseline evidence remains addressable by Snapshot Timeline.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi;
import software.ste.sdk.generated.api.BrowserVisualReviewsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        BrowserVisualReviewsApi apiInstance = new BrowserVisualReviewsApi(defaultClient);
        UUID comparisonId = UUID.randomUUID(); // UUID | Identifier of an immutable Browser visual comparison generation.
        BrowserVisualPromoteBaselineRequest browserVisualPromoteBaselineRequest = new BrowserVisualPromoteBaselineRequest(); // BrowserVisualPromoteBaselineRequest |
        try {
            APIuseCurrentBrowserVisualAsNewBaselineRequest request = APIuseCurrentBrowserVisualAsNewBaselineRequest.newBuilder()
                .comparisonId(comparisonId)
                .browserVisualPromoteBaselineRequest(browserVisualPromoteBaselineRequest)
                .build();
            ApiResponse<BrowserVisualComparison> response = apiInstance.useCurrentBrowserVisualAsNewBaselineWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrowserVisualReviewsApi#useCurrentBrowserVisualAsNewBaseline");
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
| useCurrentBrowserVisualAsNewBaselineRequest | [**APIuseCurrentBrowserVisualAsNewBaselineRequest**](BrowserVisualReviewsApi.md#APIuseCurrentBrowserVisualAsNewBaselineRequest)|-|-|

### Return type

ApiResponse<[**BrowserVisualComparison**](BrowserVisualComparison.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reviewed comparison with the applied baseline revision. |  -  |
| **409** | The expected assertion revision is stale or the action id conflicts with another command. |  -  |
| **0** | The request failed. |  -  |


<a id="APIuseCurrentBrowserVisualAsNewBaselineRequest"></a>
## APIuseCurrentBrowserVisualAsNewBaselineRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **comparisonId** | **UUID** | Identifier of an immutable Browser visual comparison generation. | |
| **browserVisualPromoteBaselineRequest** | [**BrowserVisualPromoteBaselineRequest**](BrowserVisualPromoteBaselineRequest.md) |  | |
