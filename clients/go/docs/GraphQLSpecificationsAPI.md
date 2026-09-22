# \GraphQLSpecificationsAPI

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CaptureGraphqlSpecificationAttachmentVisualDiff**](GraphQLSpecificationsAPI.md#CaptureGraphqlSpecificationAttachmentVisualDiff) | **Post** /test/graphql-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed GraphQL attachment assertion
[**CreateGraphqlSpecification**](GraphQLSpecificationsAPI.md#CreateGraphqlSpecification) | **Post** /test/graphql-spec/create | Create a GraphQL specification
[**DeleteGraphqlSpecification**](GraphQLSpecificationsAPI.md#DeleteGraphqlSpecification) | **Delete** /test/graphql-spec/by-id | Delete a GraphQL specification
[**GetGraphqlSpecification**](GraphQLSpecificationsAPI.md#GetGraphqlSpecification) | **Get** /test/graphql-spec/by-id | Get a GraphQL specification
[**GetGraphqlSpecificationRun**](GraphQLSpecificationsAPI.md#GetGraphqlSpecificationRun) | **Get** /test/graphql-spec/run/history/by-run-id/{runId} | Get saved GraphQL run evidence
[**ListGraphqlSpecificationRuns**](GraphQLSpecificationsAPI.md#ListGraphqlSpecificationRuns) | **Get** /test/graphql-spec/run/page/by-spec-id/{specId} | List saved GraphQL runs
[**ListGraphqlSpecifications**](GraphQLSpecificationsAPI.md#ListGraphqlSpecifications) | **Get** /test/graphql-spec/page | List GraphQL specifications
[**PreviewGraphqlSpecificationRecovery**](GraphQLSpecificationsAPI.md#PreviewGraphqlSpecificationRecovery) | **Post** /test/graphql-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a GraphQL specification version
[**RestoreGraphqlSpecificationFromRun**](GraphQLSpecificationsAPI.md#RestoreGraphqlSpecificationFromRun) | **Put** /test/graphql-spec/recovery/{specId}/from-run/{runId}/restore | Restore a GraphQL specification version
[**RunGraphqlSpecification**](GraphQLSpecificationsAPI.md#RunGraphqlSpecification) | **Post** /test/graphql-spec/run/by-id | Run a saved GraphQL specification
[**TestGraphqlSpecificationRecoveryVersion**](GraphQLSpecificationsAPI.md#TestGraphqlSpecificationRecoveryVersion) | **Post** /test/graphql-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous GraphQL specification version
[**UpdateGraphqlSpecification**](GraphQLSpecificationsAPI.md#UpdateGraphqlSpecification) | **Put** /test/graphql-spec/by-id | Replace a GraphQL specification definition



## CaptureGraphqlSpecificationAttachmentVisualDiff

> SpecificationRun CaptureGraphqlSpecificationAttachmentVisualDiff(ctx, specId).DocumentVisualDiffCaptureRunRequest(documentVisualDiffCaptureRunRequest).Execute()

Create a visual diff from a failed GraphQL attachment assertion



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
	documentVisualDiffCaptureRunRequest := *openapiclient.NewDocumentVisualDiffCaptureRunRequest("AttachmentId_example") // DocumentVisualDiffCaptureRunRequest |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GraphQLSpecificationsAPI.CaptureGraphqlSpecificationAttachmentVisualDiff(context.Background(), specId).DocumentVisualDiffCaptureRunRequest(documentVisualDiffCaptureRunRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GraphQLSpecificationsAPI.CaptureGraphqlSpecificationAttachmentVisualDiff``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CaptureGraphqlSpecificationAttachmentVisualDiff`: SpecificationRun
	fmt.Fprintf(os.Stdout, "Response from `GraphQLSpecificationsAPI.CaptureGraphqlSpecificationAttachmentVisualDiff`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |

### Other Parameters

Other parameters are passed through a pointer to a apiCaptureGraphqlSpecificationAttachmentVisualDiffRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **documentVisualDiffCaptureRunRequest** | [**DocumentVisualDiffCaptureRunRequest**](DocumentVisualDiffCaptureRunRequest.md) |  |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateGraphqlSpecification

> Specification CreateGraphqlSpecification(ctx).SpecName(specName).Body(body).Description(description).IdempotencyKey(idempotencyKey).Execute()

Create a GraphQL specification

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
	resp, r, err := apiClient.GraphQLSpecificationsAPI.CreateGraphqlSpecification(context.Background()).SpecName(specName).Body(body).Description(description).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GraphQLSpecificationsAPI.CreateGraphqlSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateGraphqlSpecification`: Specification
	fmt.Fprintf(os.Stdout, "Response from `GraphQLSpecificationsAPI.CreateGraphqlSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateGraphqlSpecificationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specName** | **string** | User-facing specification name within the active project. |
 **body** | **string** |  |
 **description** | **string** | Optional user-facing description stored with the asset. |
 **idempotencyKey** | **string** | A caller-generated UUID retained for safe write retries where supported. |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteGraphqlSpecification

> Specification DeleteGraphqlSpecification(ctx).SpecId(specId).Execute()

Delete a GraphQL specification

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
	resp, r, err := apiClient.GraphQLSpecificationsAPI.DeleteGraphqlSpecification(context.Background()).SpecId(specId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GraphQLSpecificationsAPI.DeleteGraphqlSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteGraphqlSpecification`: Specification
	fmt.Fprintf(os.Stdout, "Response from `GraphQLSpecificationsAPI.DeleteGraphqlSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDeleteGraphqlSpecificationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specId** | **string** | UUIDv7 identifier of the saved specification. |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetGraphqlSpecification

> Specification GetGraphqlSpecification(ctx).SpecId(specId).Execute()

Get a GraphQL specification

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
	resp, r, err := apiClient.GraphQLSpecificationsAPI.GetGraphqlSpecification(context.Background()).SpecId(specId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GraphQLSpecificationsAPI.GetGraphqlSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetGraphqlSpecification`: Specification
	fmt.Fprintf(os.Stdout, "Response from `GraphQLSpecificationsAPI.GetGraphqlSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetGraphqlSpecificationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specId** | **string** | UUIDv7 identifier of the saved specification. |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetGraphqlSpecificationRun

> SpecificationRun GetGraphqlSpecificationRun(ctx, runId).Execute()

Get saved GraphQL run evidence

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
	resp, r, err := apiClient.GraphQLSpecificationsAPI.GetGraphqlSpecificationRun(context.Background(), runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GraphQLSpecificationsAPI.GetGraphqlSpecificationRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetGraphqlSpecificationRun`: SpecificationRun
	fmt.Fprintf(os.Stdout, "Response from `GraphQLSpecificationsAPI.GetGraphqlSpecificationRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetGraphqlSpecificationRunRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListGraphqlSpecificationRuns

> SpecificationRunPage ListGraphqlSpecificationRuns(ctx, specId).Page(page).Size(size).Execute()

List saved GraphQL runs

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
	resp, r, err := apiClient.GraphQLSpecificationsAPI.ListGraphqlSpecificationRuns(context.Background(), specId).Page(page).Size(size).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GraphQLSpecificationsAPI.ListGraphqlSpecificationRuns``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListGraphqlSpecificationRuns`: SpecificationRunPage
	fmt.Fprintf(os.Stdout, "Response from `GraphQLSpecificationsAPI.ListGraphqlSpecificationRuns`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |

### Other Parameters

Other parameters are passed through a pointer to a apiListGraphqlSpecificationRunsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** | Maximum number of results returned in one page. | [default to 20]

### Return type

[**SpecificationRunPage**](SpecificationRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListGraphqlSpecifications

> SpecificationPage ListGraphqlSpecifications(ctx).Page(page).Size(size).Search(search).Execute()

List GraphQL specifications

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
	resp, r, err := apiClient.GraphQLSpecificationsAPI.ListGraphqlSpecifications(context.Background()).Page(page).Size(size).Search(search).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GraphQLSpecificationsAPI.ListGraphqlSpecifications``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListGraphqlSpecifications`: SpecificationPage
	fmt.Fprintf(os.Stdout, "Response from `GraphQLSpecificationsAPI.ListGraphqlSpecifications`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListGraphqlSpecificationsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** | Maximum number of results returned in one page. | [default to 20]
 **search** | **string** | Case-insensitive server-side search within the active project. |

### Return type

[**SpecificationPage**](SpecificationPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PreviewGraphqlSpecificationRecovery

> SpecificationRecoveryPreview PreviewGraphqlSpecificationRecovery(ctx, specId, runId).Execute()

Preview restoring a GraphQL specification version



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
	resp, r, err := apiClient.GraphQLSpecificationsAPI.PreviewGraphqlSpecificationRecovery(context.Background(), specId, runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GraphQLSpecificationsAPI.PreviewGraphqlSpecificationRecovery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PreviewGraphqlSpecificationRecovery`: SpecificationRecoveryPreview
	fmt.Fprintf(os.Stdout, "Response from `GraphQLSpecificationsAPI.PreviewGraphqlSpecificationRecovery`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiPreviewGraphqlSpecificationRecoveryRequest struct via the builder pattern


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


## RestoreGraphqlSpecificationFromRun

> Specification RestoreGraphqlSpecificationFromRun(ctx, specId, runId).Execute()

Restore a GraphQL specification version



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
	resp, r, err := apiClient.GraphQLSpecificationsAPI.RestoreGraphqlSpecificationFromRun(context.Background(), specId, runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GraphQLSpecificationsAPI.RestoreGraphqlSpecificationFromRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RestoreGraphqlSpecificationFromRun`: Specification
	fmt.Fprintf(os.Stdout, "Response from `GraphQLSpecificationsAPI.RestoreGraphqlSpecificationFromRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiRestoreGraphqlSpecificationFromRunRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RunGraphqlSpecification

> SpecificationRun RunGraphqlSpecification(ctx).SpecId(specId).Execute()

Run a saved GraphQL specification

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
	resp, r, err := apiClient.GraphQLSpecificationsAPI.RunGraphqlSpecification(context.Background()).SpecId(specId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GraphQLSpecificationsAPI.RunGraphqlSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RunGraphqlSpecification`: SpecificationRun
	fmt.Fprintf(os.Stdout, "Response from `GraphQLSpecificationsAPI.RunGraphqlSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRunGraphqlSpecificationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specId** | **string** | UUIDv7 identifier of the saved specification. |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestGraphqlSpecificationRecoveryVersion

> SpecificationRun TestGraphqlSpecificationRecoveryVersion(ctx, specId, runId).Execute()

Test a previous GraphQL specification version



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
	resp, r, err := apiClient.GraphQLSpecificationsAPI.TestGraphqlSpecificationRecoveryVersion(context.Background(), specId, runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GraphQLSpecificationsAPI.TestGraphqlSpecificationRecoveryVersion``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TestGraphqlSpecificationRecoveryVersion`: SpecificationRun
	fmt.Fprintf(os.Stdout, "Response from `GraphQLSpecificationsAPI.TestGraphqlSpecificationRecoveryVersion`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiTestGraphqlSpecificationRecoveryVersionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateGraphqlSpecification

> Specification UpdateGraphqlSpecification(ctx).SpecId(specId).Body(body).Description(description).Execute()

Replace a GraphQL specification definition

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
	resp, r, err := apiClient.GraphQLSpecificationsAPI.UpdateGraphqlSpecification(context.Background()).SpecId(specId).Body(body).Description(description).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GraphQLSpecificationsAPI.UpdateGraphqlSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateGraphqlSpecification`: Specification
	fmt.Fprintf(os.Stdout, "Response from `GraphQLSpecificationsAPI.UpdateGraphqlSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateGraphqlSpecificationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specId** | **string** | UUIDv7 identifier of the saved specification. |
 **body** | **string** |  |
 **description** | **string** | Optional user-facing description stored with the asset. |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

