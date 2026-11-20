# \SOAPSpecificationsAPI

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CaptureSoapSpecificationAttachmentVisualDiff**](SOAPSpecificationsAPI.md#CaptureSoapSpecificationAttachmentVisualDiff) | **Post** /test/soap-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed SOAP attachment assertion
[**CreateSoapSpecification**](SOAPSpecificationsAPI.md#CreateSoapSpecification) | **Post** /test/soap-spec/create | Create a SOAP specification
[**DeleteSoapSpecification**](SOAPSpecificationsAPI.md#DeleteSoapSpecification) | **Delete** /test/soap-spec/by-id | Delete a SOAP specification
[**GetSoapPreparation**](SOAPSpecificationsAPI.md#GetSoapPreparation) | **Get** /test/soap-spec/preparations/by-ref/{ref} | Read eligible SOAP Prepare request metadata by stable key
[**GetSoapSpecification**](SOAPSpecificationsAPI.md#GetSoapSpecification) | **Get** /test/soap-spec/by-id | Get a SOAP specification
[**GetSoapSpecificationRun**](SOAPSpecificationsAPI.md#GetSoapSpecificationRun) | **Get** /test/soap-spec/run/history/by-run-id/{runId} | Get saved SOAP run evidence
[**ListSoapPreparations**](SOAPSpecificationsAPI.md#ListSoapPreparations) | **Get** /test/soap-spec/preparations | List eligible Prepare requests and output declarations
[**ListSoapSpecificationRuns**](SOAPSpecificationsAPI.md#ListSoapSpecificationRuns) | **Get** /test/soap-spec/run/page/by-spec-id/{specId} | List saved SOAP runs
[**ListSoapSpecifications**](SOAPSpecificationsAPI.md#ListSoapSpecifications) | **Get** /test/soap-spec/page | List SOAP specifications
[**PreviewSoapSpecificationRecovery**](SOAPSpecificationsAPI.md#PreviewSoapSpecificationRecovery) | **Post** /test/soap-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a SOAP specification version
[**RestoreSoapSpecificationFromRun**](SOAPSpecificationsAPI.md#RestoreSoapSpecificationFromRun) | **Put** /test/soap-spec/recovery/{specId}/from-run/{runId}/restore | Restore a SOAP specification version
[**RunSoapSpecification**](SOAPSpecificationsAPI.md#RunSoapSpecification) | **Post** /test/soap-spec/run/by-id | Run a saved SOAP specification
[**TestSoapSpecificationRecoveryVersion**](SOAPSpecificationsAPI.md#TestSoapSpecificationRecoveryVersion) | **Post** /test/soap-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous SOAP specification version
[**UpdateSoapSpecification**](SOAPSpecificationsAPI.md#UpdateSoapSpecification) | **Put** /test/soap-spec/by-id | Replace a SOAP specification definition



## CaptureSoapSpecificationAttachmentVisualDiff

> SpecificationRun CaptureSoapSpecificationAttachmentVisualDiff(ctx, specId).DocumentVisualDiffCaptureRunRequest(documentVisualDiffCaptureRunRequest).Execute()

Create a visual diff from a failed SOAP attachment assertion



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
	resp, r, err := apiClient.SOAPSpecificationsAPI.CaptureSoapSpecificationAttachmentVisualDiff(context.Background(), specId).DocumentVisualDiffCaptureRunRequest(documentVisualDiffCaptureRunRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SOAPSpecificationsAPI.CaptureSoapSpecificationAttachmentVisualDiff``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CaptureSoapSpecificationAttachmentVisualDiff`: SpecificationRun
	fmt.Fprintf(os.Stdout, "Response from `SOAPSpecificationsAPI.CaptureSoapSpecificationAttachmentVisualDiff`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |

### Other Parameters

Other parameters are passed through a pointer to a apiCaptureSoapSpecificationAttachmentVisualDiffRequest struct via the builder pattern


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


## CreateSoapSpecification

> Specification CreateSoapSpecification(ctx).SpecName(specName).Body(body).Description(description).IdempotencyKey(idempotencyKey).Execute()

Create a SOAP specification

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
	resp, r, err := apiClient.SOAPSpecificationsAPI.CreateSoapSpecification(context.Background()).SpecName(specName).Body(body).Description(description).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SOAPSpecificationsAPI.CreateSoapSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateSoapSpecification`: Specification
	fmt.Fprintf(os.Stdout, "Response from `SOAPSpecificationsAPI.CreateSoapSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateSoapSpecificationRequest struct via the builder pattern


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


## DeleteSoapSpecification

> Specification DeleteSoapSpecification(ctx).SpecId(specId).Execute()

Delete a SOAP specification

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
	resp, r, err := apiClient.SOAPSpecificationsAPI.DeleteSoapSpecification(context.Background()).SpecId(specId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SOAPSpecificationsAPI.DeleteSoapSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteSoapSpecification`: Specification
	fmt.Fprintf(os.Stdout, "Response from `SOAPSpecificationsAPI.DeleteSoapSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDeleteSoapSpecificationRequest struct via the builder pattern


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


## GetSoapPreparation

> PreparationSummary GetSoapPreparation(ctx, ref).Execute()

Read eligible SOAP Prepare request metadata by stable key



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
	ref := "ref_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SOAPSpecificationsAPI.GetSoapPreparation(context.Background(), ref).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SOAPSpecificationsAPI.GetSoapPreparation``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSoapPreparation`: PreparationSummary
	fmt.Fprintf(os.Stdout, "Response from `SOAPSpecificationsAPI.GetSoapPreparation`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**ref** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetSoapPreparationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**PreparationSummary**](PreparationSummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSoapSpecification

> Specification GetSoapSpecification(ctx).SpecId(specId).Execute()

Get a SOAP specification

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
	resp, r, err := apiClient.SOAPSpecificationsAPI.GetSoapSpecification(context.Background()).SpecId(specId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SOAPSpecificationsAPI.GetSoapSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSoapSpecification`: Specification
	fmt.Fprintf(os.Stdout, "Response from `SOAPSpecificationsAPI.GetSoapSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetSoapSpecificationRequest struct via the builder pattern


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


## GetSoapSpecificationRun

> SpecificationRun GetSoapSpecificationRun(ctx, runId).Execute()

Get saved SOAP run evidence

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
	resp, r, err := apiClient.SOAPSpecificationsAPI.GetSoapSpecificationRun(context.Background(), runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SOAPSpecificationsAPI.GetSoapSpecificationRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSoapSpecificationRun`: SpecificationRun
	fmt.Fprintf(os.Stdout, "Response from `SOAPSpecificationsAPI.GetSoapSpecificationRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetSoapSpecificationRunRequest struct via the builder pattern


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


## ListSoapPreparations

> PreparationPage ListSoapPreparations(ctx).Page(page).Size(size).Search(search).Execute()

List eligible Prepare requests and output declarations



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
	size := int32(56) // int32 |  (optional) (default to 20)
	search := "search_example" // string | Case-insensitive server-side search within the active project. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SOAPSpecificationsAPI.ListSoapPreparations(context.Background()).Page(page).Size(size).Search(search).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SOAPSpecificationsAPI.ListSoapPreparations``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSoapPreparations`: PreparationPage
	fmt.Fprintf(os.Stdout, "Response from `SOAPSpecificationsAPI.ListSoapPreparations`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListSoapPreparationsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** |  | [default to 20]
 **search** | **string** | Case-insensitive server-side search within the active project. |

### Return type

[**PreparationPage**](PreparationPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSoapSpecificationRuns

> SpecificationRunPage ListSoapSpecificationRuns(ctx, specId).Page(page).Size(size).Execute()

List saved SOAP runs

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
	resp, r, err := apiClient.SOAPSpecificationsAPI.ListSoapSpecificationRuns(context.Background(), specId).Page(page).Size(size).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SOAPSpecificationsAPI.ListSoapSpecificationRuns``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSoapSpecificationRuns`: SpecificationRunPage
	fmt.Fprintf(os.Stdout, "Response from `SOAPSpecificationsAPI.ListSoapSpecificationRuns`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |

### Other Parameters

Other parameters are passed through a pointer to a apiListSoapSpecificationRunsRequest struct via the builder pattern


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


## ListSoapSpecifications

> SpecificationPage ListSoapSpecifications(ctx).Page(page).Size(size).Search(search).Execute()

List SOAP specifications

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
	resp, r, err := apiClient.SOAPSpecificationsAPI.ListSoapSpecifications(context.Background()).Page(page).Size(size).Search(search).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SOAPSpecificationsAPI.ListSoapSpecifications``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSoapSpecifications`: SpecificationPage
	fmt.Fprintf(os.Stdout, "Response from `SOAPSpecificationsAPI.ListSoapSpecifications`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListSoapSpecificationsRequest struct via the builder pattern


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


## PreviewSoapSpecificationRecovery

> SpecificationRecoveryPreview PreviewSoapSpecificationRecovery(ctx, specId, runId).Execute()

Preview restoring a SOAP specification version



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
	resp, r, err := apiClient.SOAPSpecificationsAPI.PreviewSoapSpecificationRecovery(context.Background(), specId, runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SOAPSpecificationsAPI.PreviewSoapSpecificationRecovery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PreviewSoapSpecificationRecovery`: SpecificationRecoveryPreview
	fmt.Fprintf(os.Stdout, "Response from `SOAPSpecificationsAPI.PreviewSoapSpecificationRecovery`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiPreviewSoapSpecificationRecoveryRequest struct via the builder pattern


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


## RestoreSoapSpecificationFromRun

> Specification RestoreSoapSpecificationFromRun(ctx, specId, runId).Execute()

Restore a SOAP specification version



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
	resp, r, err := apiClient.SOAPSpecificationsAPI.RestoreSoapSpecificationFromRun(context.Background(), specId, runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SOAPSpecificationsAPI.RestoreSoapSpecificationFromRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RestoreSoapSpecificationFromRun`: Specification
	fmt.Fprintf(os.Stdout, "Response from `SOAPSpecificationsAPI.RestoreSoapSpecificationFromRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiRestoreSoapSpecificationFromRunRequest struct via the builder pattern


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


## RunSoapSpecification

> SpecificationRun RunSoapSpecification(ctx).SpecId(specId).Execute()

Run a saved SOAP specification

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
	resp, r, err := apiClient.SOAPSpecificationsAPI.RunSoapSpecification(context.Background()).SpecId(specId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SOAPSpecificationsAPI.RunSoapSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RunSoapSpecification`: SpecificationRun
	fmt.Fprintf(os.Stdout, "Response from `SOAPSpecificationsAPI.RunSoapSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRunSoapSpecificationRequest struct via the builder pattern


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


## TestSoapSpecificationRecoveryVersion

> SpecificationRun TestSoapSpecificationRecoveryVersion(ctx, specId, runId).Execute()

Test a previous SOAP specification version



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
	resp, r, err := apiClient.SOAPSpecificationsAPI.TestSoapSpecificationRecoveryVersion(context.Background(), specId, runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SOAPSpecificationsAPI.TestSoapSpecificationRecoveryVersion``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TestSoapSpecificationRecoveryVersion`: SpecificationRun
	fmt.Fprintf(os.Stdout, "Response from `SOAPSpecificationsAPI.TestSoapSpecificationRecoveryVersion`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**specId** | **string** | UUIDv7 identifier of the saved specification. |
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiTestSoapSpecificationRecoveryVersionRequest struct via the builder pattern


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


## UpdateSoapSpecification

> Specification UpdateSoapSpecification(ctx).SpecId(specId).Body(body).Description(description).Execute()

Replace a SOAP specification definition

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
	resp, r, err := apiClient.SOAPSpecificationsAPI.UpdateSoapSpecification(context.Background()).SpecId(specId).Body(body).Description(description).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SOAPSpecificationsAPI.UpdateSoapSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateSoapSpecification`: Specification
	fmt.Fprintf(os.Stdout, "Response from `SOAPSpecificationsAPI.UpdateSoapSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateSoapSpecificationRequest struct via the builder pattern


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
