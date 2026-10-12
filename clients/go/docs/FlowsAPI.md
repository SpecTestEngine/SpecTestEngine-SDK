# \FlowsAPI

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CaptureFlowStepAttachmentVisualDiff**](FlowsAPI.md#CaptureFlowStepAttachmentVisualDiff) | **Post** /test/flow/run/by-id/{flowId}/visual-diff-captures | Create a visual diff from a failed flow-step attachment assertion
[**CopyFlowRecoveryDraft**](FlowsAPI.md#CopyFlowRecoveryDraft) | **Post** /test/flow/run/saved/{runId}/recovery/copy | Recover an edited draft as an independent new Flow
[**CreateFlow**](FlowsAPI.md#CreateFlow) | **Post** /test/flow/create | Create a test flow
[**CreateFlowRecovery**](FlowsAPI.md#CreateFlowRecovery) | **Post** /test/flow/run/saved/{runId}/recovery | Recover a saved run as a new Flow and new dependency copies
[**DeleteFlow**](FlowsAPI.md#DeleteFlow) | **Delete** /test/flow/by-id | Delete a test flow
[**GetFlow**](FlowsAPI.md#GetFlow) | **Get** /test/flow/by-id/{flowId} | Get a test flow
[**GetFlowRecoveryCurrentDependency**](FlowsAPI.md#GetFlowRecoveryCurrentDependency) | **Get** /test/flow/run/saved/{runId}/recovery/current-dependency | Read one current safe Recovery dependency
[**GetFlowRecoveryDependency**](FlowsAPI.md#GetFlowRecoveryDependency) | **Get** /test/flow/run/saved/{runId}/recovery/dependencies/{dependencyKey} | Inspect one retained safe dependency definition
[**GetFlowRecoveryOperation**](FlowsAPI.md#GetFlowRecoveryOperation) | **Get** /test/flow/run/recovery-operations/{operationId} | Read a Flow recovery outcome without performing writes
[**GetFlowRun**](FlowsAPI.md#GetFlowRun) | **Get** /test/flow/run/saved/{runId} | Get a saved flow run
[**ListFlowRecoveryDependencies**](FlowsAPI.md#ListFlowRecoveryDependencies) | **Get** /test/flow/run/saved/{runId}/recovery/dependencies | List historical dependency versions for Flow recovery
[**ListFlowRuns**](FlowsAPI.md#ListFlowRuns) | **Get** /test/flow/run/by-flow-id/{flowId}/page | List saved runs for a flow
[**ListFlows**](FlowsAPI.md#ListFlows) | **Get** /test/flow/page | List test flows
[**PreviewFlowRecovery**](FlowsAPI.md#PreviewFlowRecovery) | **Get** /test/flow/run/saved/{runId}/recovery/preview | Preview an independent Flow recovery from a saved run
[**RestoreFlowRecoveryDraft**](FlowsAPI.md#RestoreFlowRecoveryDraft) | **Post** /test/flow/run/saved/{runId}/recovery/restore | Restore an edited historical Flow into the current Flow
[**ReviewFlowRecovery**](FlowsAPI.md#ReviewFlowRecovery) | **Get** /test/flow/run/saved/{runId}/recovery/review | Review Flow Recovery for restore or independent copy
[**RunFlow**](FlowsAPI.md#RunFlow) | **Post** /test/flow/run/by-id/{flowId} | Run a saved flow
[**RunFlowBatch**](FlowsAPI.md#RunFlowBatch) | **Post** /test/flow/run/batch | Run multiple saved flows
[**UpdateFlow**](FlowsAPI.md#UpdateFlow) | **Put** /test/flow/by-id | Replace a test flow



## CaptureFlowStepAttachmentVisualDiff

> FlowRun CaptureFlowStepAttachmentVisualDiff(ctx, flowId).FlowDocumentVisualDiffCaptureRunRequest(flowDocumentVisualDiffCaptureRunRequest).Execute()

Create a visual diff from a failed flow-step attachment assertion



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
	flowId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved test flow.
	flowDocumentVisualDiffCaptureRunRequest := *openapiclient.NewFlowDocumentVisualDiffCaptureRunRequest(int32(123), "AttachmentId_example") // FlowDocumentVisualDiffCaptureRunRequest |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.CaptureFlowStepAttachmentVisualDiff(context.Background(), flowId).FlowDocumentVisualDiffCaptureRunRequest(flowDocumentVisualDiffCaptureRunRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.CaptureFlowStepAttachmentVisualDiff``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CaptureFlowStepAttachmentVisualDiff`: FlowRun
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.CaptureFlowStepAttachmentVisualDiff`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**flowId** | **string** | UUIDv7 identifier of the saved test flow. |

### Other Parameters

Other parameters are passed through a pointer to a apiCaptureFlowStepAttachmentVisualDiffRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **flowDocumentVisualDiffCaptureRunRequest** | [**FlowDocumentVisualDiffCaptureRunRequest**](FlowDocumentVisualDiffCaptureRunRequest.md) |  |

### Return type

[**FlowRun**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CopyFlowRecoveryDraft

> FlowRecoveryOperation CopyFlowRecoveryDraft(ctx, runId).IdempotencyKey(idempotencyKey).FlowRecoveryDraftInput(flowRecoveryDraftInput).Execute()

Recover an edited draft as an independent new Flow



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
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	flowRecoveryDraftInput := *openapiclient.NewFlowRecoveryDraftInput("ManifestHash_example", "Mode_example", map[string]interface{}{"key": interface{}(123)}, int64(123), []*string{nil}, map[string]int64{"key": int64(123)}, map[string]interface{}{"key": interface{}(123)}) // FlowRecoveryDraftInput |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.CopyFlowRecoveryDraft(context.Background(), runId).IdempotencyKey(idempotencyKey).FlowRecoveryDraftInput(flowRecoveryDraftInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.CopyFlowRecoveryDraft``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CopyFlowRecoveryDraft`: FlowRecoveryOperation
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.CopyFlowRecoveryDraft`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiCopyFlowRecoveryDraftRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** |  |
 **flowRecoveryDraftInput** | [**FlowRecoveryDraftInput**](FlowRecoveryDraftInput.md) |  |

### Return type

[**FlowRecoveryOperation**](FlowRecoveryOperation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateFlow

> Flow CreateFlow(ctx).FlowInput(flowInput).Format(format).IdempotencyKey(idempotencyKey).Execute()

Create a test flow

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
	flowInput := *openapiclient.NewFlowInput("Name_example", []openapiclient.FlowStepInput{*openapiclient.NewFlowStepInput("StepType_example", int32(123))}) // FlowInput |
	format := openapiclient.ContentFormat("JSON") // ContentFormat | Serialization format used for the returned specification source. (optional) (default to "JSON")
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | A caller-generated UUID retained for safe write retries where supported. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.CreateFlow(context.Background()).FlowInput(flowInput).Format(format).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.CreateFlow``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateFlow`: Flow
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.CreateFlow`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateFlowRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flowInput** | [**FlowInput**](FlowInput.md) |  |
 **format** | [**ContentFormat**](ContentFormat.md) | Serialization format used for the returned specification source. | [default to &quot;JSON&quot;]
 **idempotencyKey** | **string** | A caller-generated UUID retained for safe write retries where supported. |

### Return type

[**Flow**](Flow.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateFlowRecovery

> FlowRecoveryOperation CreateFlowRecovery(ctx, runId).IdempotencyKey(idempotencyKey).FlowRecoveryInput(flowRecoveryInput).Execute()

Recover a saved run as a new Flow and new dependency copies



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
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	flowRecoveryInput := *openapiclient.NewFlowRecoveryInput("ManifestHash_example", "Name_example", map[string]interface{}{"key": interface{}(123)}) // FlowRecoveryInput |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.CreateFlowRecovery(context.Background(), runId).IdempotencyKey(idempotencyKey).FlowRecoveryInput(flowRecoveryInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.CreateFlowRecovery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateFlowRecovery`: FlowRecoveryOperation
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.CreateFlowRecovery`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiCreateFlowRecoveryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** |  |
 **flowRecoveryInput** | [**FlowRecoveryInput**](FlowRecoveryInput.md) |  |

### Return type

[**FlowRecoveryOperation**](FlowRecoveryOperation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteFlow

> DeleteFlow(ctx).FlowId(flowId).Execute()

Delete a test flow

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
	flowId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FlowsAPI.DeleteFlow(context.Background()).FlowId(flowId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.DeleteFlow``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDeleteFlowRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flowId** | **string** |  |

### Return type

 (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFlow

> Flow GetFlow(ctx, flowId).Execute()

Get a test flow

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
	flowId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved test flow.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.GetFlow(context.Background(), flowId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.GetFlow``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFlow`: Flow
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.GetFlow`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**flowId** | **string** | UUIDv7 identifier of the saved test flow. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetFlowRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Flow**](Flow.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFlowRecoveryCurrentDependency

> FlowRecoveryCurrentDependency GetFlowRecoveryCurrentDependency(ctx, runId).Kind(kind).SourceId(sourceId).DependencyKey(dependencyKey).Execute()

Read one current safe Recovery dependency

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
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	kind := "kind_example" // string |
	sourceId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	dependencyKey := "dependencyKey_example" // string | Retained key for an existing occurrence; omit for an explicitly added saved reference. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.GetFlowRecoveryCurrentDependency(context.Background(), runId).Kind(kind).SourceId(sourceId).DependencyKey(dependencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.GetFlowRecoveryCurrentDependency``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFlowRecoveryCurrentDependency`: FlowRecoveryCurrentDependency
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.GetFlowRecoveryCurrentDependency`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetFlowRecoveryCurrentDependencyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **kind** | **string** |  |
 **sourceId** | **string** |  |
 **dependencyKey** | **string** | Retained key for an existing occurrence; omit for an explicitly added saved reference. |

### Return type

[**FlowRecoveryCurrentDependency**](FlowRecoveryCurrentDependency.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFlowRecoveryDependency

> FlowRecoveryDependencyDetail GetFlowRecoveryDependency(ctx, runId, dependencyKey).Execute()

Inspect one retained safe dependency definition

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
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	dependencyKey := "dependencyKey_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.GetFlowRecoveryDependency(context.Background(), runId, dependencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.GetFlowRecoveryDependency``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFlowRecoveryDependency`: FlowRecoveryDependencyDetail
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.GetFlowRecoveryDependency`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** |  |
**dependencyKey** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetFlowRecoveryDependencyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**FlowRecoveryDependencyDetail**](FlowRecoveryDependencyDetail.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFlowRecoveryOperation

> FlowRecoveryOperation GetFlowRecoveryOperation(ctx, operationId).Execute()

Read a Flow recovery outcome without performing writes

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
	operationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.GetFlowRecoveryOperation(context.Background(), operationId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.GetFlowRecoveryOperation``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFlowRecoveryOperation`: FlowRecoveryOperation
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.GetFlowRecoveryOperation`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**operationId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetFlowRecoveryOperationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**FlowRecoveryOperation**](FlowRecoveryOperation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFlowRun

> FlowRun GetFlowRun(ctx, runId).Execute()

Get a saved flow run

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
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.GetFlowRun(context.Background(), runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.GetFlowRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFlowRun`: FlowRun
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.GetFlowRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetFlowRunRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**FlowRun**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListFlowRecoveryDependencies

> FlowRecoveryDependencyPage ListFlowRecoveryDependencies(ctx, runId).Page(page).Size(size).Execute()

List historical dependency versions for Flow recovery

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
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	page := int32(56) // int32 | Zero-based page index. (optional) (default to 0)
	size := int32(56) // int32 |  (optional) (default to 20)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.ListFlowRecoveryDependencies(context.Background(), runId).Page(page).Size(size).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.ListFlowRecoveryDependencies``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListFlowRecoveryDependencies`: FlowRecoveryDependencyPage
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.ListFlowRecoveryDependencies`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiListFlowRecoveryDependenciesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** |  | [default to 20]

### Return type

[**FlowRecoveryDependencyPage**](FlowRecoveryDependencyPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListFlowRuns

> FlowRunPage ListFlowRuns(ctx, flowId).Page(page).Size(size).Execute()

List saved runs for a flow

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
	flowId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved test flow.
	page := int32(56) // int32 | Zero-based page index. (optional) (default to 0)
	size := int32(56) // int32 | Maximum number of results returned in one page. (optional) (default to 20)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.ListFlowRuns(context.Background(), flowId).Page(page).Size(size).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.ListFlowRuns``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListFlowRuns`: FlowRunPage
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.ListFlowRuns`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**flowId** | **string** | UUIDv7 identifier of the saved test flow. |

### Other Parameters

Other parameters are passed through a pointer to a apiListFlowRunsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** | Maximum number of results returned in one page. | [default to 20]

### Return type

[**FlowRunPage**](FlowRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListFlows

> FlowPage ListFlows(ctx).Page(page).Size(size).Search(search).Execute()

List test flows

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
	resp, r, err := apiClient.FlowsAPI.ListFlows(context.Background()).Page(page).Size(size).Search(search).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.ListFlows``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListFlows`: FlowPage
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.ListFlows`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListFlowsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** | Maximum number of results returned in one page. | [default to 20]
 **search** | **string** | Case-insensitive server-side search within the active project. |

### Return type

[**FlowPage**](FlowPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PreviewFlowRecovery

> FlowRecoveryPreview PreviewFlowRecovery(ctx, runId).Execute()

Preview an independent Flow recovery from a saved run



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
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.PreviewFlowRecovery(context.Background(), runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.PreviewFlowRecovery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PreviewFlowRecovery`: FlowRecoveryPreview
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.PreviewFlowRecovery`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiPreviewFlowRecoveryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**FlowRecoveryPreview**](FlowRecoveryPreview.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RestoreFlowRecoveryDraft

> FlowRecoveryOperation RestoreFlowRecoveryDraft(ctx, runId).IdempotencyKey(idempotencyKey).FlowRecoveryDraftInput(flowRecoveryDraftInput).Execute()

Restore an edited historical Flow into the current Flow



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
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	flowRecoveryDraftInput := *openapiclient.NewFlowRecoveryDraftInput("ManifestHash_example", "Mode_example", map[string]interface{}{"key": interface{}(123)}, int64(123), []*string{nil}, map[string]int64{"key": int64(123)}, map[string]interface{}{"key": interface{}(123)}) // FlowRecoveryDraftInput |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.RestoreFlowRecoveryDraft(context.Background(), runId).IdempotencyKey(idempotencyKey).FlowRecoveryDraftInput(flowRecoveryDraftInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.RestoreFlowRecoveryDraft``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RestoreFlowRecoveryDraft`: FlowRecoveryOperation
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.RestoreFlowRecoveryDraft`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiRestoreFlowRecoveryDraftRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** |  |
 **flowRecoveryDraftInput** | [**FlowRecoveryDraftInput**](FlowRecoveryDraftInput.md) |  |

### Return type

[**FlowRecoveryOperation**](FlowRecoveryOperation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ReviewFlowRecovery

> FlowRecoveryReview ReviewFlowRecovery(ctx, runId).Execute()

Review Flow Recovery for restore or independent copy



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
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.ReviewFlowRecovery(context.Background(), runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.ReviewFlowRecovery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ReviewFlowRecovery`: FlowRecoveryReview
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.ReviewFlowRecovery`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiReviewFlowRecoveryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**FlowRecoveryReview**](FlowRecoveryReview.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RunFlow

> FlowRun RunFlow(ctx, flowId).Watch(watch).Execute()

Run a saved flow

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
	flowId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved test flow.
	watch := true // bool | Create a browser watch token when the flow contains visible browser steps. (optional) (default to false)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.RunFlow(context.Background(), flowId).Watch(watch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.RunFlow``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RunFlow`: FlowRun
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.RunFlow`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**flowId** | **string** | UUIDv7 identifier of the saved test flow. |

### Other Parameters

Other parameters are passed through a pointer to a apiRunFlowRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **watch** | **bool** | Create a browser watch token when the flow contains visible browser steps. | [default to false]

### Return type

[**FlowRun**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RunFlowBatch

> []FlowRun RunFlowBatch(ctx).RunFlowBatchRequest(runFlowBatchRequest).Execute()

Run multiple saved flows

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
	runFlowBatchRequest := *openapiclient.NewRunFlowBatchRequest([]string{"0197f0ab-42e7-7a31-8a9c-591a8ee54c12"}) // RunFlowBatchRequest |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.RunFlowBatch(context.Background()).RunFlowBatchRequest(runFlowBatchRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.RunFlowBatch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RunFlowBatch`: []FlowRun
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.RunFlowBatch`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRunFlowBatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runFlowBatchRequest** | [**RunFlowBatchRequest**](RunFlowBatchRequest.md) |  |

### Return type

[**[]FlowRun**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateFlow

> Flow UpdateFlow(ctx).FlowId(flowId).FlowInput(flowInput).Format(format).Execute()

Replace a test flow

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
	flowId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	flowInput := *openapiclient.NewFlowInput("Name_example", []openapiclient.FlowStepInput{*openapiclient.NewFlowStepInput("StepType_example", int32(123))}) // FlowInput |
	format := openapiclient.ContentFormat("JSON") // ContentFormat | Serialization format used for the returned specification source. (optional) (default to "JSON")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlowsAPI.UpdateFlow(context.Background()).FlowId(flowId).FlowInput(flowInput).Format(format).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlowsAPI.UpdateFlow``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateFlow`: Flow
	fmt.Fprintf(os.Stdout, "Response from `FlowsAPI.UpdateFlow`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateFlowRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flowId** | **string** |  |
 **flowInput** | [**FlowInput**](FlowInput.md) |  |
 **format** | [**ContentFormat**](ContentFormat.md) | Serialization format used for the returned specification source. | [default to &quot;JSON&quot;]

### Return type

[**Flow**](Flow.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
