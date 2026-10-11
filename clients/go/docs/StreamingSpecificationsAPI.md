# \StreamingSpecificationsAPI

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CancelStreamingSpecificationRun**](StreamingSpecificationsAPI.md#CancelStreamingSpecificationRun) | **Post** /test/streaming-spec/run/history/by-run-id/{runId}/cancel | Cancel an active streaming run
[**CreateStreamingSpecification**](StreamingSpecificationsAPI.md#CreateStreamingSpecification) | **Post** /test/streaming-spec/create | Create a streaming specification
[**DeleteStreamingSpecification**](StreamingSpecificationsAPI.md#DeleteStreamingSpecification) | **Delete** /test/streaming-spec/by-id | Delete a streaming specification
[**GetStreamingCapabilities**](StreamingSpecificationsAPI.md#GetStreamingCapabilities) | **Get** /engine/streaming/capabilities | Get streaming engine capabilities and enforced limits
[**GetStreamingSpecification**](StreamingSpecificationsAPI.md#GetStreamingSpecification) | **Get** /test/streaming-spec/by-id | Get a streaming specification
[**GetStreamingSpecificationRun**](StreamingSpecificationsAPI.md#GetStreamingSpecificationRun) | **Get** /test/streaming-spec/run/history/by-run-id/{runId} | Get streaming run state and bounded semantic evidence
[**GetStreamingSpecificationRunTranscript**](StreamingSpecificationsAPI.md#GetStreamingSpecificationRunTranscript) | **Get** /test/streaming-spec/run/history/by-run-id/{runId}/transcript | Page a bounded streaming run transcript
[**ListStreamingSpecificationRuns**](StreamingSpecificationsAPI.md#ListStreamingSpecificationRuns) | **Get** /test/streaming-spec/run/page/by-spec-id/{specId} | List runs for a saved streaming specification
[**ListStreamingSpecifications**](StreamingSpecificationsAPI.md#ListStreamingSpecifications) | **Get** /test/streaming-spec/page | List streaming specifications
[**PreviewStreamingSpecificationRecovery**](StreamingSpecificationsAPI.md#PreviewStreamingSpecificationRecovery) | **Post** /test/streaming-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a Streaming specification version
[**RestoreStreamingSpecificationFromRun**](StreamingSpecificationsAPI.md#RestoreStreamingSpecificationFromRun) | **Put** /test/streaming-spec/recovery/{specId}/from-run/{runId}/restore | Restore a Streaming specification version
[**RunStreamingSpecification**](StreamingSpecificationsAPI.md#RunStreamingSpecification) | **Post** /test/streaming-spec/run/by-id/{specId} | Queue a saved streaming specification run
[**RunStreamingSpecificationDraft**](StreamingSpecificationsAPI.md#RunStreamingSpecificationDraft) | **Post** /test/streaming-spec/run/draft | Queue a bounded streaming specification draft run
[**TestStreamingSpecificationRecoveryVersion**](StreamingSpecificationsAPI.md#TestStreamingSpecificationRecoveryVersion) | **Post** /test/streaming-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous Streaming specification version
[**UpdateStreamingSpecification**](StreamingSpecificationsAPI.md#UpdateStreamingSpecification) | **Put** /test/streaming-spec/by-id | Replace a streaming specification definition
[**ValidateStreamingSpecificationDraft**](StreamingSpecificationsAPI.md#ValidateStreamingSpecificationDraft) | **Post** /test/streaming-spec/validate-draft | Validate and detect the transport of a streaming specification draft



## CancelStreamingSpecificationRun

> StreamingRun CancelStreamingSpecificationRun(ctx, runId).Execute()

Cancel an active streaming run

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
	resp, r, err := apiClient.StreamingSpecificationsAPI.CancelStreamingSpecificationRun(context.Background(), runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.CancelStreamingSpecificationRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CancelStreamingSpecificationRun`: StreamingRun
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.CancelStreamingSpecificationRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiCancelStreamingSpecificationRunRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**StreamingRun**](StreamingRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateStreamingSpecification

> StreamingSpecification CreateStreamingSpecification(ctx).SpecName(specName).Body(body).Description(description).IdempotencyKey(idempotencyKey).Execute()

Create a streaming specification

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
	specName := "specName_example" // string | User-facing specification name within the active project.
	body := "body_example" // string |
	description := "description_example" // string | Optional user-facing description stored with the asset. (optional)
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | A caller-generated UUID retained for safe write retries where supported. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StreamingSpecificationsAPI.CreateStreamingSpecification(context.Background()).SpecName(specName).Body(body).Description(description).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.CreateStreamingSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateStreamingSpecification`: StreamingSpecification
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.CreateStreamingSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateStreamingSpecificationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specName** | **string** | User-facing specification name within the active project. |
 **body** | **string** |  |
 **description** | **string** | Optional user-facing description stored with the asset. |
 **idempotencyKey** | **string** | A caller-generated UUID retained for safe write retries where supported. |

### Return type

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteStreamingSpecification

> StreamingSpecification DeleteStreamingSpecification(ctx).SpecId(specId).Execute()

Delete a streaming specification

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
	specId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved specification.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StreamingSpecificationsAPI.DeleteStreamingSpecification(context.Background()).SpecId(specId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.DeleteStreamingSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteStreamingSpecification`: StreamingSpecification
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.DeleteStreamingSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDeleteStreamingSpecificationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specId** | **string** | UUIDv7 identifier of the saved specification. |

### Return type

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetStreamingCapabilities

> StreamingCapabilities GetStreamingCapabilities(ctx).Execute()

Get streaming engine capabilities and enforced limits

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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StreamingSpecificationsAPI.GetStreamingCapabilities(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.GetStreamingCapabilities``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetStreamingCapabilities`: StreamingCapabilities
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.GetStreamingCapabilities`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetStreamingCapabilitiesRequest struct via the builder pattern


### Return type

[**StreamingCapabilities**](StreamingCapabilities.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetStreamingSpecification

> StreamingSpecification GetStreamingSpecification(ctx).SpecId(specId).Execute()

Get a streaming specification

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
	specId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved specification.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StreamingSpecificationsAPI.GetStreamingSpecification(context.Background()).SpecId(specId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.GetStreamingSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetStreamingSpecification`: StreamingSpecification
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.GetStreamingSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetStreamingSpecificationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specId** | **string** | UUIDv7 identifier of the saved specification. |

### Return type

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetStreamingSpecificationRun

> StreamingRun GetStreamingSpecificationRun(ctx, runId).Execute()

Get streaming run state and bounded semantic evidence

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
	resp, r, err := apiClient.StreamingSpecificationsAPI.GetStreamingSpecificationRun(context.Background(), runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.GetStreamingSpecificationRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetStreamingSpecificationRun`: StreamingRun
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.GetStreamingSpecificationRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetStreamingSpecificationRunRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**StreamingRun**](StreamingRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetStreamingSpecificationRunTranscript

> StreamingTranscriptPage GetStreamingSpecificationRunTranscript(ctx, runId).Page(page).Size(size).Execute()

Page a bounded streaming run transcript

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
	page := int32(56) // int32 | Zero-based page index. (optional) (default to 0)
	size := int32(56) // int32 |  (optional) (default to 100)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StreamingSpecificationsAPI.GetStreamingSpecificationRunTranscript(context.Background(), runId).Page(page).Size(size).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.GetStreamingSpecificationRunTranscript``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetStreamingSpecificationRunTranscript`: StreamingTranscriptPage
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.GetStreamingSpecificationRunTranscript`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetStreamingSpecificationRunTranscriptRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** |  | [default to 100]

### Return type

[**StreamingTranscriptPage**](StreamingTranscriptPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListStreamingSpecificationRuns

> StreamingRunPage ListStreamingSpecificationRuns(ctx, specId).Page(page).Size(size).Execute()

List runs for a saved streaming specification

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
	specId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved specification.
	page := int32(56) // int32 | Zero-based page index. (optional) (default to 0)
	size := int32(56) // int32 | Maximum number of results returned in one page. (optional) (default to 20)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StreamingSpecificationsAPI.ListStreamingSpecificationRuns(context.Background(), specId).Page(page).Size(size).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.ListStreamingSpecificationRuns``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListStreamingSpecificationRuns`: StreamingRunPage
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.ListStreamingSpecificationRuns`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |

### Other Parameters

Other parameters are passed through a pointer to a apiListStreamingSpecificationRunsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** | Maximum number of results returned in one page. | [default to 20]

### Return type

[**StreamingRunPage**](StreamingRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListStreamingSpecifications

> StreamingSpecificationPage ListStreamingSpecifications(ctx).Page(page).Size(size).Search(search).Transport(transport).Execute()

List streaming specifications

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
	transport := openapiclient.StreamingTransport("WEBSOCKET") // StreamingTransport | Filter by streaming transport. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StreamingSpecificationsAPI.ListStreamingSpecifications(context.Background()).Page(page).Size(size).Search(search).Transport(transport).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.ListStreamingSpecifications``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListStreamingSpecifications`: StreamingSpecificationPage
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.ListStreamingSpecifications`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListStreamingSpecificationsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** | Maximum number of results returned in one page. | [default to 20]
 **search** | **string** | Case-insensitive server-side search within the active project. |
 **transport** | [**StreamingTransport**](StreamingTransport.md) | Filter by streaming transport. |

### Return type

[**StreamingSpecificationPage**](StreamingSpecificationPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PreviewStreamingSpecificationRecovery

> SpecificationRecoveryPreview PreviewStreamingSpecificationRecovery(ctx, specId, runId).Execute()

Preview restoring a Streaming specification version



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
	specId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved specification.
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the stored run evidence.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StreamingSpecificationsAPI.PreviewStreamingSpecificationRecovery(context.Background(), specId, runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.PreviewStreamingSpecificationRecovery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PreviewStreamingSpecificationRecovery`: SpecificationRecoveryPreview
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.PreviewStreamingSpecificationRecovery`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiPreviewStreamingSpecificationRecoveryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**SpecificationRecoveryPreview**](SpecificationRecoveryPreview.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RestoreStreamingSpecificationFromRun

> StreamingSpecification RestoreStreamingSpecificationFromRun(ctx, specId, runId).Execute()

Restore a Streaming specification version



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
	specId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved specification.
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the stored run evidence.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StreamingSpecificationsAPI.RestoreStreamingSpecificationFromRun(context.Background(), specId, runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.RestoreStreamingSpecificationFromRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RestoreStreamingSpecificationFromRun`: StreamingSpecification
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.RestoreStreamingSpecificationFromRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiRestoreStreamingSpecificationFromRunRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RunStreamingSpecification

> StreamingRunAccepted RunStreamingSpecification(ctx, specId).Execute()

Queue a saved streaming specification run

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
	specId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved specification.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StreamingSpecificationsAPI.RunStreamingSpecification(context.Background(), specId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.RunStreamingSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RunStreamingSpecification`: StreamingRunAccepted
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.RunStreamingSpecification`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |

### Other Parameters

Other parameters are passed through a pointer to a apiRunStreamingSpecificationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**StreamingRunAccepted**](StreamingRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RunStreamingSpecificationDraft

> StreamingRunAccepted RunStreamingSpecificationDraft(ctx).Body(body).SpecName(specName).Execute()

Queue a bounded streaming specification draft run

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
	body := "body_example" // string |
	specName := "specName_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StreamingSpecificationsAPI.RunStreamingSpecificationDraft(context.Background()).Body(body).SpecName(specName).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.RunStreamingSpecificationDraft``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RunStreamingSpecificationDraft`: StreamingRunAccepted
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.RunStreamingSpecificationDraft`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRunStreamingSpecificationDraftRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **string** |  |
 **specName** | **string** |  |

### Return type

[**StreamingRunAccepted**](StreamingRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestStreamingSpecificationRecoveryVersion

> StreamingRun TestStreamingSpecificationRecoveryVersion(ctx, specId, runId).Execute()

Test a previous Streaming specification version



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
	specId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved specification.
	runId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the stored run evidence.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StreamingSpecificationsAPI.TestStreamingSpecificationRecoveryVersion(context.Background(), specId, runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.TestStreamingSpecificationRecoveryVersion``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TestStreamingSpecificationRecoveryVersion`: StreamingRun
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.TestStreamingSpecificationRecoveryVersion`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiTestStreamingSpecificationRecoveryVersionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**StreamingRun**](StreamingRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateStreamingSpecification

> StreamingSpecification UpdateStreamingSpecification(ctx).SpecId(specId).Body(body).Description(description).Execute()

Replace a streaming specification definition

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
	specId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the saved specification.
	body := "body_example" // string |
	description := "description_example" // string | Optional user-facing description stored with the asset. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StreamingSpecificationsAPI.UpdateStreamingSpecification(context.Background()).SpecId(specId).Body(body).Description(description).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.UpdateStreamingSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateStreamingSpecification`: StreamingSpecification
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.UpdateStreamingSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateStreamingSpecificationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specId** | **string** | UUIDv7 identifier of the saved specification. |
 **body** | **string** |  |
 **description** | **string** | Optional user-facing description stored with the asset. |

### Return type

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ValidateStreamingSpecificationDraft

> StreamingDraftValidation ValidateStreamingSpecificationDraft(ctx).Body(body).Execute()

Validate and detect the transport of a streaming specification draft

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
	body := "body_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StreamingSpecificationsAPI.ValidateStreamingSpecificationDraft(context.Background()).Body(body).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StreamingSpecificationsAPI.ValidateStreamingSpecificationDraft``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ValidateStreamingSpecificationDraft`: StreamingDraftValidation
	fmt.Fprintf(os.Stdout, "Response from `StreamingSpecificationsAPI.ValidateStreamingSpecificationDraft`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiValidateStreamingSpecificationDraftRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **string** |  |

### Return type

[**StreamingDraftValidation**](StreamingDraftValidation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
