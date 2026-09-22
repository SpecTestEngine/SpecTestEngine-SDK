# \SnapshotsAPI

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CompareSnapshotStep**](SnapshotsAPI.md#CompareSnapshotStep) | **Post** /test/snapshot/diff/step | Compare snapshot step payloads
[**CompareSnapshotToRunBatch**](SnapshotsAPI.md#CompareSnapshotToRunBatch) | **Get** /test/snapshot/diff/snapshot/{snapshotId}/batch/{batchId} | Compare a snapshot with a run batch
[**CompareSnapshots**](SnapshotsAPI.md#CompareSnapshots) | **Get** /test/snapshot/diff/snapshot/{leftSnapshotId}/snapshot/{rightSnapshotId} | Compare two snapshots
[**CreateSnapshot**](SnapshotsAPI.md#CreateSnapshot) | **Post** /test/snapshot/create | Create a snapshot baseline
[**GetSnapshot**](SnapshotsAPI.md#GetSnapshot) | **Get** /test/snapshot/by-id/{snapshotId} | Get a snapshot
[**ListSnapshots**](SnapshotsAPI.md#ListSnapshots) | **Get** /test/snapshot/page | List snapshots



## CompareSnapshotStep

> SnapshotStepDiff CompareSnapshotStep(ctx).SnapshotStepDiffInput(snapshotStepDiffInput).Execute()

Compare snapshot step payloads



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/SpecTestEngine/SpecTestEngine-SDK/clients/go"
)

func main() {
	snapshotStepDiffInput := *openapiclient.NewSnapshotStepDiffInput(openapiclient.SnapshotStepType("API_SPEC")) // SnapshotStepDiffInput |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SnapshotsAPI.CompareSnapshotStep(context.Background()).SnapshotStepDiffInput(snapshotStepDiffInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SnapshotsAPI.CompareSnapshotStep``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CompareSnapshotStep`: SnapshotStepDiff
	fmt.Fprintf(os.Stdout, "Response from `SnapshotsAPI.CompareSnapshotStep`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCompareSnapshotStepRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshotStepDiffInput** | [**SnapshotStepDiffInput**](SnapshotStepDiffInput.md) |  |

### Return type

[**SnapshotStepDiff**](SnapshotStepDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CompareSnapshotToRunBatch

> SnapshotDiff CompareSnapshotToRunBatch(ctx, snapshotId, batchId).Execute()

Compare a snapshot with a run batch



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/SpecTestEngine/SpecTestEngine-SDK/clients/go"
)

func main() {
	snapshotId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved snapshot baseline.
	batchId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved run batch.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SnapshotsAPI.CompareSnapshotToRunBatch(context.Background(), snapshotId, batchId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SnapshotsAPI.CompareSnapshotToRunBatch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CompareSnapshotToRunBatch`: SnapshotDiff
	fmt.Fprintf(os.Stdout, "Response from `SnapshotsAPI.CompareSnapshotToRunBatch`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**snapshotId** | **string** | UUIDv7 identifier of the saved snapshot baseline. |
**batchId** | **string** | UUIDv7 identifier of the saved run batch. |

### Other Parameters

Other parameters are passed through a pointer to a apiCompareSnapshotToRunBatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**SnapshotDiff**](SnapshotDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CompareSnapshots

> SnapshotDiff CompareSnapshots(ctx, leftSnapshotId, rightSnapshotId).Execute()

Compare two snapshots



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/SpecTestEngine/SpecTestEngine-SDK/clients/go"
)

func main() {
	leftSnapshotId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the baseline side of the comparison.
	rightSnapshotId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the candidate side of the comparison.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SnapshotsAPI.CompareSnapshots(context.Background(), leftSnapshotId, rightSnapshotId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SnapshotsAPI.CompareSnapshots``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CompareSnapshots`: SnapshotDiff
	fmt.Fprintf(os.Stdout, "Response from `SnapshotsAPI.CompareSnapshots`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**leftSnapshotId** | **string** | UUIDv7 identifier of the baseline side of the comparison. |
**rightSnapshotId** | **string** | UUIDv7 identifier of the candidate side of the comparison. |

### Other Parameters

Other parameters are passed through a pointer to a apiCompareSnapshotsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**SnapshotDiff**](SnapshotDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateSnapshot

> Snapshot CreateSnapshot(ctx).SnapshotInput(snapshotInput).IdempotencyKey(idempotencyKey).Execute()

Create a snapshot baseline



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/SpecTestEngine/SpecTestEngine-SDK/clients/go"
)

func main() {
	snapshotInput := *openapiclient.NewSnapshotInput("staging-release-baseline", "2026.07", "0197f0ab-42e7-7a31-8a9c-591a8ee54c12", "Environment_example") // SnapshotInput |
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | A caller-generated UUID retained for safe write retries where supported. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SnapshotsAPI.CreateSnapshot(context.Background()).SnapshotInput(snapshotInput).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SnapshotsAPI.CreateSnapshot``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateSnapshot`: Snapshot
	fmt.Fprintf(os.Stdout, "Response from `SnapshotsAPI.CreateSnapshot`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateSnapshotRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshotInput** | [**SnapshotInput**](SnapshotInput.md) |  |
 **idempotencyKey** | **string** | A caller-generated UUID retained for safe write retries where supported. |

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSnapshot

> Snapshot GetSnapshot(ctx, snapshotId).Execute()

Get a snapshot

### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/SpecTestEngine/SpecTestEngine-SDK/clients/go"
)

func main() {
	snapshotId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved snapshot baseline.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SnapshotsAPI.GetSnapshot(context.Background(), snapshotId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SnapshotsAPI.GetSnapshot``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSnapshot`: Snapshot
	fmt.Fprintf(os.Stdout, "Response from `SnapshotsAPI.GetSnapshot`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**snapshotId** | **string** | UUIDv7 identifier of the saved snapshot baseline. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetSnapshotRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSnapshots

> SnapshotPage ListSnapshots(ctx).Page(page).Size(size).Search(search).Execute()

List snapshots

### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/SpecTestEngine/SpecTestEngine-SDK/clients/go"
)

func main() {
	page := int32(56) // int32 | Zero-based page index. (optional) (default to 0)
	size := int32(56) // int32 | Maximum number of results returned in one page. (optional) (default to 20)
	search := "search_example" // string | Case-insensitive server-side search within the active project. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SnapshotsAPI.ListSnapshots(context.Background()).Page(page).Size(size).Search(search).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SnapshotsAPI.ListSnapshots``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSnapshots`: SnapshotPage
	fmt.Fprintf(os.Stdout, "Response from `SnapshotsAPI.ListSnapshots`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListSnapshotsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** | Maximum number of results returned in one page. | [default to 20]
 **search** | **string** | Case-insensitive server-side search within the active project. |

### Return type

[**SnapshotPage**](SnapshotPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

