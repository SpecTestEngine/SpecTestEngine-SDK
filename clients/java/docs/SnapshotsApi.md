# SnapshotsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**compareSnapshotStep**](SnapshotsApi.md#compareSnapshotStep) | **POST** /test/snapshot/diff/step | Compare snapshot step payloads |
| [**compareSnapshotStepWithHttpInfo**](SnapshotsApi.md#compareSnapshotStepWithHttpInfo) | **POST** /test/snapshot/diff/step | Compare snapshot step payloads |
| [**compareSnapshotToRunBatch**](SnapshotsApi.md#compareSnapshotToRunBatch) | **GET** /test/snapshot/diff/snapshot/{snapshotId}/batch/{batchId} | Compare a snapshot with a run batch |
| [**compareSnapshotToRunBatchWithHttpInfo**](SnapshotsApi.md#compareSnapshotToRunBatchWithHttpInfo) | **GET** /test/snapshot/diff/snapshot/{snapshotId}/batch/{batchId} | Compare a snapshot with a run batch |
| [**compareSnapshots**](SnapshotsApi.md#compareSnapshots) | **GET** /test/snapshot/diff/snapshot/{leftSnapshotId}/snapshot/{rightSnapshotId} | Compare two snapshots |
| [**compareSnapshotsWithHttpInfo**](SnapshotsApi.md#compareSnapshotsWithHttpInfo) | **GET** /test/snapshot/diff/snapshot/{leftSnapshotId}/snapshot/{rightSnapshotId} | Compare two snapshots |
| [**createSnapshot**](SnapshotsApi.md#createSnapshot) | **POST** /test/snapshot/create | Create a snapshot baseline |
| [**createSnapshotWithHttpInfo**](SnapshotsApi.md#createSnapshotWithHttpInfo) | **POST** /test/snapshot/create | Create a snapshot baseline |
| [**getSnapshot**](SnapshotsApi.md#getSnapshot) | **GET** /test/snapshot/by-id/{snapshotId} | Get a snapshot |
| [**getSnapshotWithHttpInfo**](SnapshotsApi.md#getSnapshotWithHttpInfo) | **GET** /test/snapshot/by-id/{snapshotId} | Get a snapshot |
| [**listSnapshots**](SnapshotsApi.md#listSnapshots) | **GET** /test/snapshot/page | List snapshots |
| [**listSnapshotsWithHttpInfo**](SnapshotsApi.md#listSnapshotsWithHttpInfo) | **GET** /test/snapshot/page | List snapshots |



## compareSnapshotStep

> SnapshotStepDiff compareSnapshotStep(compareSnapshotStepRequest)

Compare snapshot step payloads

Produce a field-level definition and behavior diff for one API, UI macro, or browser-action step.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SnapshotsApi;
import software.ste.sdk.generated.api.SnapshotsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
        SnapshotStepDiffInput snapshotStepDiffInput = new SnapshotStepDiffInput(); // SnapshotStepDiffInput |
        try {
            APIcompareSnapshotStepRequest request = APIcompareSnapshotStepRequest.newBuilder()
                .snapshotStepDiffInput(snapshotStepDiffInput)
                .build();
            SnapshotStepDiff result = apiInstance.compareSnapshotStep(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SnapshotsApi#compareSnapshotStep");
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
| compareSnapshotStepRequest | [**APIcompareSnapshotStepRequest**](SnapshotsApi.md#APIcompareSnapshotStepRequest)|-|-|

### Return type

[**SnapshotStepDiff**](SnapshotStepDiff.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A grouped, field-level step comparison suitable for a review UI. |  -  |
| **0** | The request failed. |  -  |

## compareSnapshotStepWithHttpInfo

> ApiResponse<SnapshotStepDiff> compareSnapshotStepWithHttpInfo(compareSnapshotStepRequest)

Compare snapshot step payloads

Produce a field-level definition and behavior diff for one API, UI macro, or browser-action step.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SnapshotsApi;
import software.ste.sdk.generated.api.SnapshotsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
        SnapshotStepDiffInput snapshotStepDiffInput = new SnapshotStepDiffInput(); // SnapshotStepDiffInput |
        try {
            APIcompareSnapshotStepRequest request = APIcompareSnapshotStepRequest.newBuilder()
                .snapshotStepDiffInput(snapshotStepDiffInput)
                .build();
            ApiResponse<SnapshotStepDiff> response = apiInstance.compareSnapshotStepWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SnapshotsApi#compareSnapshotStep");
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
| compareSnapshotStepRequest | [**APIcompareSnapshotStepRequest**](SnapshotsApi.md#APIcompareSnapshotStepRequest)|-|-|

### Return type

ApiResponse<[**SnapshotStepDiff**](SnapshotStepDiff.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A grouped, field-level step comparison suitable for a review UI. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcompareSnapshotStepRequest"></a>
## APIcompareSnapshotStepRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **snapshotStepDiffInput** | [**SnapshotStepDiffInput**](SnapshotStepDiffInput.md) |  | |



## compareSnapshotToRunBatch

> SnapshotDiff compareSnapshotToRunBatch(compareSnapshotToRunBatchRequest)

Compare a snapshot with a run batch

Compare a saved baseline with fresh run-batch evidence before promoting a new snapshot.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SnapshotsApi;
import software.ste.sdk.generated.api.SnapshotsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
        UUID snapshotId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved snapshot baseline.
        UUID batchId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved run batch.
        try {
            APIcompareSnapshotToRunBatchRequest request = APIcompareSnapshotToRunBatchRequest.newBuilder()
                .snapshotId(snapshotId)
                .batchId(batchId)
                .build();
            SnapshotDiff result = apiInstance.compareSnapshotToRunBatch(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SnapshotsApi#compareSnapshotToRunBatch");
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
| compareSnapshotToRunBatchRequest | [**APIcompareSnapshotToRunBatchRequest**](SnapshotsApi.md#APIcompareSnapshotToRunBatchRequest)|-|-|

### Return type

[**SnapshotDiff**](SnapshotDiff.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The classified baseline-to-batch comparison. |  -  |
| **0** | The request failed. |  -  |

## compareSnapshotToRunBatchWithHttpInfo

> ApiResponse<SnapshotDiff> compareSnapshotToRunBatchWithHttpInfo(compareSnapshotToRunBatchRequest)

Compare a snapshot with a run batch

Compare a saved baseline with fresh run-batch evidence before promoting a new snapshot.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SnapshotsApi;
import software.ste.sdk.generated.api.SnapshotsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
        UUID snapshotId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved snapshot baseline.
        UUID batchId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved run batch.
        try {
            APIcompareSnapshotToRunBatchRequest request = APIcompareSnapshotToRunBatchRequest.newBuilder()
                .snapshotId(snapshotId)
                .batchId(batchId)
                .build();
            ApiResponse<SnapshotDiff> response = apiInstance.compareSnapshotToRunBatchWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SnapshotsApi#compareSnapshotToRunBatch");
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
| compareSnapshotToRunBatchRequest | [**APIcompareSnapshotToRunBatchRequest**](SnapshotsApi.md#APIcompareSnapshotToRunBatchRequest)|-|-|

### Return type

ApiResponse<[**SnapshotDiff**](SnapshotDiff.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The classified baseline-to-batch comparison. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcompareSnapshotToRunBatchRequest"></a>
## APIcompareSnapshotToRunBatchRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **snapshotId** | **UUID** | UUIDv7 identifier of the saved snapshot baseline. | |
| **batchId** | **UUID** | UUIDv7 identifier of the saved run batch. | |



## compareSnapshots

> SnapshotDiff compareSnapshots(compareSnapshotsRequest)

Compare two snapshots

Compare two saved baselines and classify new, removed, regressed, improved, and stable subjects.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SnapshotsApi;
import software.ste.sdk.generated.api.SnapshotsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
        UUID leftSnapshotId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the baseline side of the comparison.
        UUID rightSnapshotId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the candidate side of the comparison.
        try {
            APIcompareSnapshotsRequest request = APIcompareSnapshotsRequest.newBuilder()
                .leftSnapshotId(leftSnapshotId)
                .rightSnapshotId(rightSnapshotId)
                .build();
            SnapshotDiff result = apiInstance.compareSnapshots(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SnapshotsApi#compareSnapshots");
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
| compareSnapshotsRequest | [**APIcompareSnapshotsRequest**](SnapshotsApi.md#APIcompareSnapshotsRequest)|-|-|

### Return type

[**SnapshotDiff**](SnapshotDiff.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The classified snapshot comparison. |  -  |
| **0** | The request failed. |  -  |

## compareSnapshotsWithHttpInfo

> ApiResponse<SnapshotDiff> compareSnapshotsWithHttpInfo(compareSnapshotsRequest)

Compare two snapshots

Compare two saved baselines and classify new, removed, regressed, improved, and stable subjects.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SnapshotsApi;
import software.ste.sdk.generated.api.SnapshotsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
        UUID leftSnapshotId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the baseline side of the comparison.
        UUID rightSnapshotId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the candidate side of the comparison.
        try {
            APIcompareSnapshotsRequest request = APIcompareSnapshotsRequest.newBuilder()
                .leftSnapshotId(leftSnapshotId)
                .rightSnapshotId(rightSnapshotId)
                .build();
            ApiResponse<SnapshotDiff> response = apiInstance.compareSnapshotsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SnapshotsApi#compareSnapshots");
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
| compareSnapshotsRequest | [**APIcompareSnapshotsRequest**](SnapshotsApi.md#APIcompareSnapshotsRequest)|-|-|

### Return type

ApiResponse<[**SnapshotDiff**](SnapshotDiff.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The classified snapshot comparison. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcompareSnapshotsRequest"></a>
## APIcompareSnapshotsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **leftSnapshotId** | **UUID** | UUIDv7 identifier of the baseline side of the comparison. | |
| **rightSnapshotId** | **UUID** | UUIDv7 identifier of the candidate side of the comparison. | |



## createSnapshot

> Snapshot createSnapshot(createSnapshotRequest)

Create a snapshot baseline

Promote all or a selected subset of one run batch into a versioned baseline for later regression comparison.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SnapshotsApi;
import software.ste.sdk.generated.api.SnapshotsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
        SnapshotInput snapshotInput = new SnapshotInput(); // SnapshotInput |
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateSnapshotRequest request = APIcreateSnapshotRequest.newBuilder()
                .snapshotInput(snapshotInput)
                .idempotencyKey(idempotencyKey)
                .build();
            Snapshot result = apiInstance.createSnapshot(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SnapshotsApi#createSnapshot");
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
| createSnapshotRequest | [**APIcreateSnapshotRequest**](SnapshotsApi.md#APIcreateSnapshotRequest)|-|-|

### Return type

[**Snapshot**](Snapshot.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created snapshot baseline. |  -  |
| **0** | The request failed. |  -  |

## createSnapshotWithHttpInfo

> ApiResponse<Snapshot> createSnapshotWithHttpInfo(createSnapshotRequest)

Create a snapshot baseline

Promote all or a selected subset of one run batch into a versioned baseline for later regression comparison.

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SnapshotsApi;
import software.ste.sdk.generated.api.SnapshotsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
        SnapshotInput snapshotInput = new SnapshotInput(); // SnapshotInput |
        UUID idempotencyKey = UUID.randomUUID(); // UUID | A caller-generated UUID retained for safe write retries where supported.
        try {
            APIcreateSnapshotRequest request = APIcreateSnapshotRequest.newBuilder()
                .snapshotInput(snapshotInput)
                .idempotencyKey(idempotencyKey)
                .build();
            ApiResponse<Snapshot> response = apiInstance.createSnapshotWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SnapshotsApi#createSnapshot");
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
| createSnapshotRequest | [**APIcreateSnapshotRequest**](SnapshotsApi.md#APIcreateSnapshotRequest)|-|-|

### Return type

ApiResponse<[**Snapshot**](Snapshot.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created snapshot baseline. |  -  |
| **0** | The request failed. |  -  |


<a id="APIcreateSnapshotRequest"></a>
## APIcreateSnapshotRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **snapshotInput** | [**SnapshotInput**](SnapshotInput.md) |  | |
| **idempotencyKey** | **UUID** | A caller-generated UUID retained for safe write retries where supported. | [optional] |



## getSnapshot

> Snapshot getSnapshot(getSnapshotRequest)

Get a snapshot

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SnapshotsApi;
import software.ste.sdk.generated.api.SnapshotsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
        UUID snapshotId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved snapshot baseline.
        try {
            APIgetSnapshotRequest request = APIgetSnapshotRequest.newBuilder()
                .snapshotId(snapshotId)
                .build();
            Snapshot result = apiInstance.getSnapshot(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SnapshotsApi#getSnapshot");
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
| getSnapshotRequest | [**APIgetSnapshotRequest**](SnapshotsApi.md#APIgetSnapshotRequest)|-|-|

### Return type

[**Snapshot**](Snapshot.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested snapshot and its baseline evidence. |  -  |
| **0** | The request failed. |  -  |

## getSnapshotWithHttpInfo

> ApiResponse<Snapshot> getSnapshotWithHttpInfo(getSnapshotRequest)

Get a snapshot

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SnapshotsApi;
import software.ste.sdk.generated.api.SnapshotsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
        UUID snapshotId = UUID.randomUUID(); // UUID | UUIDv7 identifier of the saved snapshot baseline.
        try {
            APIgetSnapshotRequest request = APIgetSnapshotRequest.newBuilder()
                .snapshotId(snapshotId)
                .build();
            ApiResponse<Snapshot> response = apiInstance.getSnapshotWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SnapshotsApi#getSnapshot");
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
| getSnapshotRequest | [**APIgetSnapshotRequest**](SnapshotsApi.md#APIgetSnapshotRequest)|-|-|

### Return type

ApiResponse<[**Snapshot**](Snapshot.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested snapshot and its baseline evidence. |  -  |
| **0** | The request failed. |  -  |


<a id="APIgetSnapshotRequest"></a>
## APIgetSnapshotRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **snapshotId** | **UUID** | UUIDv7 identifier of the saved snapshot baseline. | |



## listSnapshots

> SnapshotPage listSnapshots(listSnapshotsRequest)

List snapshots

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SnapshotsApi;
import software.ste.sdk.generated.api.SnapshotsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistSnapshotsRequest request = APIlistSnapshotsRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .build();
            SnapshotPage result = apiInstance.listSnapshots(request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SnapshotsApi#listSnapshots");
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
| listSnapshotsRequest | [**APIlistSnapshotsRequest**](SnapshotsApi.md#APIlistSnapshotsRequest)|-|-|

### Return type

[**SnapshotPage**](SnapshotPage.md)


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of snapshot baselines in the active project. |  -  |
| **0** | The request failed. |  -  |

## listSnapshotsWithHttpInfo

> ApiResponse<SnapshotPage> listSnapshotsWithHttpInfo(listSnapshotsRequest)

List snapshots

### Example

```java
// Import classes:
import software.ste.sdk.generated.ApiClient;
import software.ste.sdk.generated.ApiException;
import software.ste.sdk.generated.ApiResponse;
import software.ste.sdk.generated.Configuration;
import software.ste.sdk.generated.auth.*;
import software.ste.sdk.generated.models.*;
import software.ste.sdk.generated.api.SnapshotsApi;
import software.ste.sdk.generated.api.SnapshotsApi.*;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://app.ste.software");

        // Configure HTTP bearer authorization: BearerAuth
        HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
        BearerAuth.setBearerToken("BEARER TOKEN");

        SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
        Integer page = 0; // Integer | Zero-based page index.
        Integer size = 20; // Integer | Maximum number of results returned in one page.
        String search = "search_example"; // String | Case-insensitive server-side search within the active project.
        try {
            APIlistSnapshotsRequest request = APIlistSnapshotsRequest.newBuilder()
                .page(page)
                .size(size)
                .search(search)
                .build();
            ApiResponse<SnapshotPage> response = apiInstance.listSnapshotsWithHttpInfo(request);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SnapshotsApi#listSnapshots");
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
| listSnapshotsRequest | [**APIlistSnapshotsRequest**](SnapshotsApi.md#APIlistSnapshotsRequest)|-|-|

### Return type

ApiResponse<[**SnapshotPage**](SnapshotPage.md)>


### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of snapshot baselines in the active project. |  -  |
| **0** | The request failed. |  -  |


<a id="APIlistSnapshotsRequest"></a>
## APIlistSnapshotsRequest
### Properties

|     Name      |    Type       | Description   |     Notes    |
| ------------- | ------------- | ------------- | -------------|
| **page** | **Integer** | Zero-based page index. | [optional] [default to 0] |
| **size** | **Integer** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **String** | Case-insensitive server-side search within the active project. | [optional] |


