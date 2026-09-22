# \DocumentVisualDiffsAPI

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetDocumentVisualDiff**](DocumentVisualDiffsAPI.md#GetDocumentVisualDiff) | **Get** /browser/visual/document-diffs/{visualDiffId} | Get a visual document diff
[**GetDocumentVisualDiffArtifact**](DocumentVisualDiffsAPI.md#GetDocumentVisualDiffArtifact) | **Get** /browser/visual/document-diffs/{visualDiffId}/artifacts/{artifactId} | Download a rendered visual diff page
[**PrepareDocumentVisualDiffBaseline**](DocumentVisualDiffsAPI.md#PrepareDocumentVisualDiffBaseline) | **Post** /browser/visual/document-diffs/{visualDiffId}/baseline | Preview or create an attachment baseline update draft
[**RegenerateDocumentVisualDiff**](DocumentVisualDiffsAPI.md#RegenerateDocumentVisualDiff) | **Post** /browser/visual/document-diffs/{visualDiffId}/regenerate | Regenerate a visual document diff
[**UploadDocumentVisualDiffExpected**](DocumentVisualDiffsAPI.md#UploadDocumentVisualDiffExpected) | **Post** /browser/visual/document-diffs/{visualDiffId}/expected | Upload a reference document and create a diff generation



## GetDocumentVisualDiff

> DocumentVisualDiff GetDocumentVisualDiff(ctx, visualDiffId).Execute()

Get a visual document diff



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
	visualDiffId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of an organization-scoped visual document diff session.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DocumentVisualDiffsAPI.GetDocumentVisualDiff(context.Background(), visualDiffId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DocumentVisualDiffsAPI.GetDocumentVisualDiff``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetDocumentVisualDiff`: DocumentVisualDiff
	fmt.Fprintf(os.Stdout, "Response from `DocumentVisualDiffsAPI.GetDocumentVisualDiff`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**visualDiffId** | **string** | UUIDv7 identifier of an organization-scoped visual document diff session. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetDocumentVisualDiffRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDocumentVisualDiffArtifact

> *os.File GetDocumentVisualDiffArtifact(ctx, visualDiffId, artifactId).Execute()

Download a rendered visual diff page

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
	visualDiffId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of an organization-scoped visual document diff session.
	artifactId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DocumentVisualDiffsAPI.GetDocumentVisualDiffArtifact(context.Background(), visualDiffId, artifactId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DocumentVisualDiffsAPI.GetDocumentVisualDiffArtifact``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetDocumentVisualDiffArtifact`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `DocumentVisualDiffsAPI.GetDocumentVisualDiffArtifact`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**visualDiffId** | **string** | UUIDv7 identifier of an organization-scoped visual document diff session. |
**artifactId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetDocumentVisualDiffArtifactRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[***os.File**](*os.File.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PrepareDocumentVisualDiffBaseline

> DocumentVisualDiffBaselinePreview PrepareDocumentVisualDiffBaseline(ctx, visualDiffId).DocumentVisualDiffBaselineRequest(documentVisualDiffBaselineRequest).Execute()

Preview or create an attachment baseline update draft



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
	visualDiffId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of an organization-scoped visual document diff session.
	documentVisualDiffBaselineRequest := *openapiclient.NewDocumentVisualDiffBaselineRequest(false, "Mode_example") // DocumentVisualDiffBaselineRequest |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DocumentVisualDiffsAPI.PrepareDocumentVisualDiffBaseline(context.Background(), visualDiffId).DocumentVisualDiffBaselineRequest(documentVisualDiffBaselineRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DocumentVisualDiffsAPI.PrepareDocumentVisualDiffBaseline``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PrepareDocumentVisualDiffBaseline`: DocumentVisualDiffBaselinePreview
	fmt.Fprintf(os.Stdout, "Response from `DocumentVisualDiffsAPI.PrepareDocumentVisualDiffBaseline`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**visualDiffId** | **string** | UUIDv7 identifier of an organization-scoped visual document diff session. |

### Other Parameters

Other parameters are passed through a pointer to a apiPrepareDocumentVisualDiffBaselineRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **documentVisualDiffBaselineRequest** | [**DocumentVisualDiffBaselineRequest**](DocumentVisualDiffBaselineRequest.md) |  |

### Return type

[**DocumentVisualDiffBaselinePreview**](DocumentVisualDiffBaselinePreview.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RegenerateDocumentVisualDiff

> DocumentVisualDiff RegenerateDocumentVisualDiff(ctx, visualDiffId).DocumentVisualDiffRegenerateRequest(documentVisualDiffRegenerateRequest).Execute()

Regenerate a visual document diff



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
	visualDiffId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of an organization-scoped visual document diff session.
	documentVisualDiffRegenerateRequest := *openapiclient.NewDocumentVisualDiffRegenerateRequest() // DocumentVisualDiffRegenerateRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DocumentVisualDiffsAPI.RegenerateDocumentVisualDiff(context.Background(), visualDiffId).DocumentVisualDiffRegenerateRequest(documentVisualDiffRegenerateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DocumentVisualDiffsAPI.RegenerateDocumentVisualDiff``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RegenerateDocumentVisualDiff`: DocumentVisualDiff
	fmt.Fprintf(os.Stdout, "Response from `DocumentVisualDiffsAPI.RegenerateDocumentVisualDiff`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**visualDiffId** | **string** | UUIDv7 identifier of an organization-scoped visual document diff session. |

### Other Parameters

Other parameters are passed through a pointer to a apiRegenerateDocumentVisualDiffRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **documentVisualDiffRegenerateRequest** | [**DocumentVisualDiffRegenerateRequest**](DocumentVisualDiffRegenerateRequest.md) |  |

### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UploadDocumentVisualDiffExpected

> DocumentVisualDiff UploadDocumentVisualDiffExpected(ctx, visualDiffId).Expected(expected).ColorThreshold(colorThreshold).Execute()

Upload a reference document and create a diff generation



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
	visualDiffId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of an organization-scoped visual document diff session.
	expected := os.NewFile(1234, "some_file") // *os.File |
	colorThreshold := float64(1.2) // float64 |  (optional) (default to 24)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DocumentVisualDiffsAPI.UploadDocumentVisualDiffExpected(context.Background(), visualDiffId).Expected(expected).ColorThreshold(colorThreshold).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DocumentVisualDiffsAPI.UploadDocumentVisualDiffExpected``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UploadDocumentVisualDiffExpected`: DocumentVisualDiff
	fmt.Fprintf(os.Stdout, "Response from `DocumentVisualDiffsAPI.UploadDocumentVisualDiffExpected`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**visualDiffId** | **string** | UUIDv7 identifier of an organization-scoped visual document diff session. |

### Other Parameters

Other parameters are passed through a pointer to a apiUploadDocumentVisualDiffExpectedRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **expected** | ***os.File** |  |
 **colorThreshold** | **float64** |  | [default to 24]

### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

