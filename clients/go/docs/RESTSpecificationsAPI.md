# \RESTSpecificationsAPI

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CaptureRestSpecificationAttachmentVisualDiff**](RESTSpecificationsAPI.md#CaptureRestSpecificationAttachmentVisualDiff) | **Post** /test/rest-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed REST attachment assertion
[**CreateRestSpecification**](RESTSpecificationsAPI.md#CreateRestSpecification) | **Post** /test/rest-spec/create | Create a REST specification
[**DeleteRestSpecification**](RESTSpecificationsAPI.md#DeleteRestSpecification) | **Delete** /test/rest-spec/by-id | Delete a REST specification
[**GetRestSpecification**](RESTSpecificationsAPI.md#GetRestSpecification) | **Get** /test/rest-spec/by-id | Get a REST specification
[**GetRestSpecificationRun**](RESTSpecificationsAPI.md#GetRestSpecificationRun) | **Get** /test/rest-spec/run/history/by-run-id/{runId} | Get saved REST run evidence
[**ListRestSpecificationRuns**](RESTSpecificationsAPI.md#ListRestSpecificationRuns) | **Get** /test/rest-spec/run/page/by-spec-id/{specId} | List saved REST runs
[**ListRestSpecifications**](RESTSpecificationsAPI.md#ListRestSpecifications) | **Get** /test/rest-spec/page | List REST specifications
[**PreviewRestSpecificationRecovery**](RESTSpecificationsAPI.md#PreviewRestSpecificationRecovery) | **Post** /test/rest-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a REST specification version
[**RestoreRestSpecificationFromRun**](RESTSpecificationsAPI.md#RestoreRestSpecificationFromRun) | **Put** /test/rest-spec/recovery/{specId}/from-run/{runId}/restore | Restore a REST specification version
[**RunRestSpecification**](RESTSpecificationsAPI.md#RunRestSpecification) | **Post** /test/rest-spec/run/by-id | Run a saved REST specification
[**TestRestSpecificationRecoveryVersion**](RESTSpecificationsAPI.md#TestRestSpecificationRecoveryVersion) | **Post** /test/rest-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous REST specification version
[**UpdateRestSpecification**](RESTSpecificationsAPI.md#UpdateRestSpecification) | **Put** /test/rest-spec/by-id | Replace a REST specification definition



## CaptureRestSpecificationAttachmentVisualDiff

> SpecificationRun CaptureRestSpecificationAttachmentVisualDiff(ctx, specId).DocumentVisualDiffCaptureRunRequest(documentVisualDiffCaptureRunRequest).Execute()

Create a visual diff from a failed REST attachment assertion



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
	resp, r, err := apiClient.RESTSpecificationsAPI.CaptureRestSpecificationAttachmentVisualDiff(context.Background(), specId).DocumentVisualDiffCaptureRunRequest(documentVisualDiffCaptureRunRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RESTSpecificationsAPI.CaptureRestSpecificationAttachmentVisualDiff``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CaptureRestSpecificationAttachmentVisualDiff`: SpecificationRun
	fmt.Fprintf(os.Stdout, "Response from `RESTSpecificationsAPI.CaptureRestSpecificationAttachmentVisualDiff`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |

### Other Parameters

Other parameters are passed through a pointer to a apiCaptureRestSpecificationAttachmentVisualDiffRequest struct via the builder pattern


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


## CreateRestSpecification

> Specification CreateRestSpecification(ctx).SpecName(specName).Body(body).Description(description).IdempotencyKey(idempotencyKey).Execute()

Create a REST specification

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
	resp, r, err := apiClient.RESTSpecificationsAPI.CreateRestSpecification(context.Background()).SpecName(specName).Body(body).Description(description).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RESTSpecificationsAPI.CreateRestSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateRestSpecification`: Specification
	fmt.Fprintf(os.Stdout, "Response from `RESTSpecificationsAPI.CreateRestSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateRestSpecificationRequest struct via the builder pattern


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


## DeleteRestSpecification

> Specification DeleteRestSpecification(ctx).SpecId(specId).Execute()

Delete a REST specification

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
	resp, r, err := apiClient.RESTSpecificationsAPI.DeleteRestSpecification(context.Background()).SpecId(specId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RESTSpecificationsAPI.DeleteRestSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteRestSpecification`: Specification
	fmt.Fprintf(os.Stdout, "Response from `RESTSpecificationsAPI.DeleteRestSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDeleteRestSpecificationRequest struct via the builder pattern


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


## GetRestSpecification

> Specification GetRestSpecification(ctx).SpecId(specId).Execute()

Get a REST specification

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
	resp, r, err := apiClient.RESTSpecificationsAPI.GetRestSpecification(context.Background()).SpecId(specId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RESTSpecificationsAPI.GetRestSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetRestSpecification`: Specification
	fmt.Fprintf(os.Stdout, "Response from `RESTSpecificationsAPI.GetRestSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetRestSpecificationRequest struct via the builder pattern


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


## GetRestSpecificationRun

> SpecificationRun GetRestSpecificationRun(ctx, runId).Execute()

Get saved REST run evidence

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
	resp, r, err := apiClient.RESTSpecificationsAPI.GetRestSpecificationRun(context.Background(), runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RESTSpecificationsAPI.GetRestSpecificationRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetRestSpecificationRun`: SpecificationRun
	fmt.Fprintf(os.Stdout, "Response from `RESTSpecificationsAPI.GetRestSpecificationRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetRestSpecificationRunRequest struct via the builder pattern


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


## ListRestSpecificationRuns

> SpecificationRunPage ListRestSpecificationRuns(ctx, specId).Page(page).Size(size).Execute()

List saved REST runs

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
	resp, r, err := apiClient.RESTSpecificationsAPI.ListRestSpecificationRuns(context.Background(), specId).Page(page).Size(size).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RESTSpecificationsAPI.ListRestSpecificationRuns``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListRestSpecificationRuns`: SpecificationRunPage
	fmt.Fprintf(os.Stdout, "Response from `RESTSpecificationsAPI.ListRestSpecificationRuns`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |

### Other Parameters

Other parameters are passed through a pointer to a apiListRestSpecificationRunsRequest struct via the builder pattern


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


## ListRestSpecifications

> SpecificationPage ListRestSpecifications(ctx).Page(page).Size(size).Search(search).Execute()

List REST specifications

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
	resp, r, err := apiClient.RESTSpecificationsAPI.ListRestSpecifications(context.Background()).Page(page).Size(size).Search(search).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RESTSpecificationsAPI.ListRestSpecifications``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListRestSpecifications`: SpecificationPage
	fmt.Fprintf(os.Stdout, "Response from `RESTSpecificationsAPI.ListRestSpecifications`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListRestSpecificationsRequest struct via the builder pattern


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


## PreviewRestSpecificationRecovery

> SpecificationRecoveryPreview PreviewRestSpecificationRecovery(ctx, specId, runId).Execute()

Preview restoring a REST specification version



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
	resp, r, err := apiClient.RESTSpecificationsAPI.PreviewRestSpecificationRecovery(context.Background(), specId, runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RESTSpecificationsAPI.PreviewRestSpecificationRecovery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PreviewRestSpecificationRecovery`: SpecificationRecoveryPreview
	fmt.Fprintf(os.Stdout, "Response from `RESTSpecificationsAPI.PreviewRestSpecificationRecovery`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiPreviewRestSpecificationRecoveryRequest struct via the builder pattern


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


## RestoreRestSpecificationFromRun

> Specification RestoreRestSpecificationFromRun(ctx, specId, runId).Execute()

Restore a REST specification version



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
	resp, r, err := apiClient.RESTSpecificationsAPI.RestoreRestSpecificationFromRun(context.Background(), specId, runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RESTSpecificationsAPI.RestoreRestSpecificationFromRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RestoreRestSpecificationFromRun`: Specification
	fmt.Fprintf(os.Stdout, "Response from `RESTSpecificationsAPI.RestoreRestSpecificationFromRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiRestoreRestSpecificationFromRunRequest struct via the builder pattern


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


## RunRestSpecification

> SpecificationRun RunRestSpecification(ctx).SpecId(specId).Execute()

Run a saved REST specification



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
	resp, r, err := apiClient.RESTSpecificationsAPI.RunRestSpecification(context.Background()).SpecId(specId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RESTSpecificationsAPI.RunRestSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RunRestSpecification`: SpecificationRun
	fmt.Fprintf(os.Stdout, "Response from `RESTSpecificationsAPI.RunRestSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRunRestSpecificationRequest struct via the builder pattern


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


## TestRestSpecificationRecoveryVersion

> SpecificationRun TestRestSpecificationRecoveryVersion(ctx, specId, runId).Execute()

Test a previous REST specification version



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
	resp, r, err := apiClient.RESTSpecificationsAPI.TestRestSpecificationRecoveryVersion(context.Background(), specId, runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RESTSpecificationsAPI.TestRestSpecificationRecoveryVersion``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TestRestSpecificationRecoveryVersion`: SpecificationRun
	fmt.Fprintf(os.Stdout, "Response from `RESTSpecificationsAPI.TestRestSpecificationRecoveryVersion`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiTestRestSpecificationRecoveryVersionRequest struct via the builder pattern


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


## UpdateRestSpecification

> Specification UpdateRestSpecification(ctx).SpecId(specId).Body(body).Description(description).Execute()

Replace a REST specification definition

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
	resp, r, err := apiClient.RESTSpecificationsAPI.UpdateRestSpecification(context.Background()).SpecId(specId).Body(body).Description(description).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RESTSpecificationsAPI.UpdateRestSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateRestSpecification`: Specification
	fmt.Fprintf(os.Stdout, "Response from `RESTSpecificationsAPI.UpdateRestSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateRestSpecificationRequest struct via the builder pattern


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
