# \CraftsmanAPI

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CancelCraftsmanRun**](CraftsmanAPI.md#CancelCraftsmanRun) | **Post** /sentinel/request-workspaces/runs/{runId}/cancel | Cancel a queued or active Craftsman run
[**CreateRequestNode**](CraftsmanAPI.md#CreateRequestNode) | **Post** /sentinel/request-workspaces/{workspaceId}/nodes | Add a folder or saved request
[**CreateRequestWorkspace**](CraftsmanAPI.md#CreateRequestWorkspace) | **Post** /sentinel/request-workspaces | Create a request workspace
[**DeleteRequestNode**](CraftsmanAPI.md#DeleteRequestNode) | **Delete** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId} | Delete a folder or saved request
[**DeleteRequestWorkspace**](CraftsmanAPI.md#DeleteRequestWorkspace) | **Delete** /sentinel/request-workspaces/{workspaceId} | Delete a request workspace
[**GetCraftsmanRun**](CraftsmanAPI.md#GetCraftsmanRun) | **Get** /sentinel/request-workspaces/runs/{runId} | Get Craftsman run lifecycle and evidence
[**GetCraftsmanRunTranscript**](CraftsmanAPI.md#GetCraftsmanRunTranscript) | **Get** /sentinel/request-workspaces/runs/{runId}/transcript | Get a Craftsman Streaming semantic transcript
[**GetDocumentAsset**](CraftsmanAPI.md#GetDocumentAsset) | **Get** /sentinel/document-assets/{assetId} | Resolve request attachment metadata
[**GetRequestWorkspace**](CraftsmanAPI.md#GetRequestWorkspace) | **Get** /sentinel/request-workspaces/{workspaceId} | Get a request workspace
[**ListRequestWorkspaces**](CraftsmanAPI.md#ListRequestWorkspaces) | **Get** /sentinel/request-workspaces/page | List request workspaces
[**QueueCraftsmanStreamingRun**](CraftsmanAPI.md#QueueCraftsmanStreamingRun) | **Post** /sentinel/request-workspaces/runs/streaming | Queue a standalone bounded Streaming session
[**QueueCraftsmanWorkflowRun**](CraftsmanAPI.md#QueueCraftsmanWorkflowRun) | **Post** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId}/runs | Queue a saved request or mixed-protocol Workflow run
[**UpdateRequestNode**](CraftsmanAPI.md#UpdateRequestNode) | **Put** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId} | Update a folder or saved request
[**UpdateRequestWorkspace**](CraftsmanAPI.md#UpdateRequestWorkspace) | **Put** /sentinel/request-workspaces/{workspaceId} | Replace request workspace metadata and variables
[**UploadDocumentAsset**](CraftsmanAPI.md#UploadDocumentAsset) | **Post** /sentinel/document-assets | Upload a reusable request attachment



## CancelCraftsmanRun

> CraftsmanRun CancelCraftsmanRun(ctx, runId).Execute()

Cancel a queued or active Craftsman run

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
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the stored run evidence.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CraftsmanAPI.CancelCraftsmanRun(context.Background(), runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.CancelCraftsmanRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CancelCraftsmanRun`: CraftsmanRun
	fmt.Fprintf(os.Stdout, "Response from `CraftsmanAPI.CancelCraftsmanRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiCancelCraftsmanRunRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**CraftsmanRun**](CraftsmanRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateRequestNode

> RequestNode CreateRequestNode(ctx, workspaceId).RequestNodeInput(requestNodeInput).IdempotencyKey(idempotencyKey).Execute()

Add a folder or saved request

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
	workspaceId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the Craftsman request workspace.
	requestNodeInput := *openapiclient.NewRequestNodeInput("Name_example", "Type_example") // RequestNodeInput |
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | A caller-generated UUID retained for safe write retries where supported. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CraftsmanAPI.CreateRequestNode(context.Background(), workspaceId).RequestNodeInput(requestNodeInput).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.CreateRequestNode``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateRequestNode`: RequestNode
	fmt.Fprintf(os.Stdout, "Response from `CraftsmanAPI.CreateRequestNode`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**workspaceId** | **string** | UUIDv7 identifier of the Craftsman request workspace. |

### Other Parameters

Other parameters are passed through a pointer to a apiCreateRequestNodeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **requestNodeInput** | [**RequestNodeInput**](RequestNodeInput.md) |  |
 **idempotencyKey** | **string** | A caller-generated UUID retained for safe write retries where supported. |

### Return type

[**RequestNode**](RequestNode.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateRequestWorkspace

> RequestWorkspace CreateRequestWorkspace(ctx).RequestWorkspaceInput(requestWorkspaceInput).IdempotencyKey(idempotencyKey).Execute()

Create a request workspace

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
	requestWorkspaceInput := *openapiclient.NewRequestWorkspaceInput("Name_example") // RequestWorkspaceInput |
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | A caller-generated UUID retained for safe write retries where supported. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CraftsmanAPI.CreateRequestWorkspace(context.Background()).RequestWorkspaceInput(requestWorkspaceInput).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.CreateRequestWorkspace``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateRequestWorkspace`: RequestWorkspace
	fmt.Fprintf(os.Stdout, "Response from `CraftsmanAPI.CreateRequestWorkspace`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateRequestWorkspaceRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestWorkspaceInput** | [**RequestWorkspaceInput**](RequestWorkspaceInput.md) |  |
 **idempotencyKey** | **string** | A caller-generated UUID retained for safe write retries where supported. |

### Return type

[**RequestWorkspace**](RequestWorkspace.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteRequestNode

> DeleteRequestNode(ctx, workspaceId, nodeId).Execute()

Delete a folder or saved request

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
	workspaceId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the Craftsman request workspace.
	nodeId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CraftsmanAPI.DeleteRequestNode(context.Background(), workspaceId, nodeId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.DeleteRequestNode``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**workspaceId** | **string** | UUIDv7 identifier of the Craftsman request workspace. |
**nodeId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteRequestNodeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



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


## DeleteRequestWorkspace

> DeleteRequestWorkspace(ctx, workspaceId).Execute()

Delete a request workspace

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
	workspaceId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the Craftsman request workspace.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CraftsmanAPI.DeleteRequestWorkspace(context.Background(), workspaceId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.DeleteRequestWorkspace``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**workspaceId** | **string** | UUIDv7 identifier of the Craftsman request workspace. |

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteRequestWorkspaceRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


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


## GetCraftsmanRun

> CraftsmanRun GetCraftsmanRun(ctx, runId).Execute()

Get Craftsman run lifecycle and evidence

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
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the stored run evidence.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CraftsmanAPI.GetCraftsmanRun(context.Background(), runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.GetCraftsmanRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCraftsmanRun`: CraftsmanRun
	fmt.Fprintf(os.Stdout, "Response from `CraftsmanAPI.GetCraftsmanRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetCraftsmanRunRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**CraftsmanRun**](CraftsmanRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCraftsmanRunTranscript

> interface{} GetCraftsmanRunTranscript(ctx, runId).Execute()

Get a Craftsman Streaming semantic transcript

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
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the stored run evidence.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CraftsmanAPI.GetCraftsmanRunTranscript(context.Background(), runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.GetCraftsmanRunTranscript``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCraftsmanRunTranscript`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `CraftsmanAPI.GetCraftsmanRunTranscript`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetCraftsmanRunTranscriptRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

**interface{}**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDocumentAsset

> DocumentAssetReference GetDocumentAsset(ctx, assetId).FieldName(fieldName).ContentId(contentId).Execute()

Resolve request attachment metadata

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
	assetId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	fieldName := "fieldName_example" // string |  (optional) (default to "file")
	contentId := "contentId_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CraftsmanAPI.GetDocumentAsset(context.Background(), assetId).FieldName(fieldName).ContentId(contentId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.GetDocumentAsset``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetDocumentAsset`: DocumentAssetReference
	fmt.Fprintf(os.Stdout, "Response from `CraftsmanAPI.GetDocumentAsset`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**assetId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetDocumentAssetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **fieldName** | **string** |  | [default to &quot;file&quot;]
 **contentId** | **string** |  |

### Return type

[**DocumentAssetReference**](DocumentAssetReference.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetRequestWorkspace

> RequestWorkspace GetRequestWorkspace(ctx, workspaceId).Execute()

Get a request workspace

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
	workspaceId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the Craftsman request workspace.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CraftsmanAPI.GetRequestWorkspace(context.Background(), workspaceId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.GetRequestWorkspace``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetRequestWorkspace`: RequestWorkspace
	fmt.Fprintf(os.Stdout, "Response from `CraftsmanAPI.GetRequestWorkspace`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**workspaceId** | **string** | UUIDv7 identifier of the Craftsman request workspace. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetRequestWorkspaceRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**RequestWorkspace**](RequestWorkspace.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListRequestWorkspaces

> RequestWorkspacePage ListRequestWorkspaces(ctx).Page(page).Size(size).Search(search).Execute()

List request workspaces

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
	resp, r, err := apiClient.CraftsmanAPI.ListRequestWorkspaces(context.Background()).Page(page).Size(size).Search(search).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.ListRequestWorkspaces``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListRequestWorkspaces`: RequestWorkspacePage
	fmt.Fprintf(os.Stdout, "Response from `CraftsmanAPI.ListRequestWorkspaces`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListRequestWorkspacesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** | Maximum number of results returned in one page. | [default to 20]
 **search** | **string** | Case-insensitive server-side search within the active project. |

### Return type

[**RequestWorkspacePage**](RequestWorkspacePage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## QueueCraftsmanStreamingRun

> CraftsmanRunAccepted QueueCraftsmanStreamingRun(ctx).CraftsmanStreamingRunInput(craftsmanStreamingRunInput).Execute()

Queue a standalone bounded Streaming session



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
	craftsmanStreamingRunInput := *openapiclient.NewCraftsmanStreamingRunInput(*openapiclient.NewStreamingDefinition(*openapiclient.NewStreamingDefinitionStream(openapiclient.StreamingTransport("WEBSOCKET"), "Endpoint_example"))) // CraftsmanStreamingRunInput |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CraftsmanAPI.QueueCraftsmanStreamingRun(context.Background()).CraftsmanStreamingRunInput(craftsmanStreamingRunInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.QueueCraftsmanStreamingRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `QueueCraftsmanStreamingRun`: CraftsmanRunAccepted
	fmt.Fprintf(os.Stdout, "Response from `CraftsmanAPI.QueueCraftsmanStreamingRun`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiQueueCraftsmanStreamingRunRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **craftsmanStreamingRunInput** | [**CraftsmanStreamingRunInput**](CraftsmanStreamingRunInput.md) |  |

### Return type

[**CraftsmanRunAccepted**](CraftsmanRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## QueueCraftsmanWorkflowRun

> CraftsmanRunAccepted QueueCraftsmanWorkflowRun(ctx, workspaceId, nodeId).RequestChainRunInput(requestChainRunInput).Execute()

Queue a saved request or mixed-protocol Workflow run



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
	workspaceId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the Craftsman request workspace.
	nodeId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	requestChainRunInput := *openapiclient.NewRequestChainRunInput() // RequestChainRunInput |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CraftsmanAPI.QueueCraftsmanWorkflowRun(context.Background(), workspaceId, nodeId).RequestChainRunInput(requestChainRunInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.QueueCraftsmanWorkflowRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `QueueCraftsmanWorkflowRun`: CraftsmanRunAccepted
	fmt.Fprintf(os.Stdout, "Response from `CraftsmanAPI.QueueCraftsmanWorkflowRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**workspaceId** | **string** | UUIDv7 identifier of the Craftsman request workspace. |
**nodeId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiQueueCraftsmanWorkflowRunRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **requestChainRunInput** | [**RequestChainRunInput**](RequestChainRunInput.md) |  |

### Return type

[**CraftsmanRunAccepted**](CraftsmanRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateRequestNode

> RequestNode UpdateRequestNode(ctx, workspaceId, nodeId).RequestNodeInput(requestNodeInput).Execute()

Update a folder or saved request



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
	workspaceId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the Craftsman request workspace.
	nodeId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	requestNodeInput := *openapiclient.NewRequestNodeInput("Name_example", "Type_example") // RequestNodeInput |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CraftsmanAPI.UpdateRequestNode(context.Background(), workspaceId, nodeId).RequestNodeInput(requestNodeInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.UpdateRequestNode``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateRequestNode`: RequestNode
	fmt.Fprintf(os.Stdout, "Response from `CraftsmanAPI.UpdateRequestNode`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**workspaceId** | **string** | UUIDv7 identifier of the Craftsman request workspace. |
**nodeId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateRequestNodeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **requestNodeInput** | [**RequestNodeInput**](RequestNodeInput.md) |  |

### Return type

[**RequestNode**](RequestNode.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateRequestWorkspace

> RequestWorkspace UpdateRequestWorkspace(ctx, workspaceId).RequestWorkspaceInput(requestWorkspaceInput).Execute()

Replace request workspace metadata and variables

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
	workspaceId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the Craftsman request workspace.
	requestWorkspaceInput := *openapiclient.NewRequestWorkspaceInput("Name_example") // RequestWorkspaceInput |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CraftsmanAPI.UpdateRequestWorkspace(context.Background(), workspaceId).RequestWorkspaceInput(requestWorkspaceInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.UpdateRequestWorkspace``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateRequestWorkspace`: RequestWorkspace
	fmt.Fprintf(os.Stdout, "Response from `CraftsmanAPI.UpdateRequestWorkspace`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**workspaceId** | **string** | UUIDv7 identifier of the Craftsman request workspace. |

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateRequestWorkspaceRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **requestWorkspaceInput** | [**RequestWorkspaceInput**](RequestWorkspaceInput.md) |  |

### Return type

[**RequestWorkspace**](RequestWorkspace.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UploadDocumentAsset

> DocumentAssetReference UploadDocumentAsset(ctx).File(file).FieldName(fieldName).ContentId(contentId).Execute()

Upload a reusable request attachment

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
	file := os.NewFile(1234, "some_file") // *os.File |
	fieldName := "fieldName_example" // string |  (optional) (default to "file")
	contentId := "contentId_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CraftsmanAPI.UploadDocumentAsset(context.Background()).File(file).FieldName(fieldName).ContentId(contentId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CraftsmanAPI.UploadDocumentAsset``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UploadDocumentAsset`: DocumentAssetReference
	fmt.Fprintf(os.Stdout, "Response from `CraftsmanAPI.UploadDocumentAsset`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUploadDocumentAssetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | ***os.File** |  |
 **fieldName** | **string** |  | [default to &quot;file&quot;]
 **contentId** | **string** |  |

### Return type

[**DocumentAssetReference**](DocumentAssetReference.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

