# \BrowserVisualReviewsAPI

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ExcludeBrowserVisualAreaAndRecompare**](BrowserVisualReviewsAPI.md#ExcludeBrowserVisualAreaAndRecompare) | **Post** /browser/visual/comparisons/{comparisonId}/exclude-and-recompare | Exclude area and recompare
[**GetBrowserVisualArtifactContent**](BrowserVisualReviewsAPI.md#GetBrowserVisualArtifactContent) | **Get** /browser/visual/artifacts/{artifactId}/content | Download Browser visual evidence
[**GetBrowserVisualComparison**](BrowserVisualReviewsAPI.md#GetBrowserVisualComparison) | **Get** /browser/visual/comparisons/{comparisonId} | Get a Browser visual comparison
[**KeepBrowserVisualAsRegression**](BrowserVisualReviewsAPI.md#KeepBrowserVisualAsRegression) | **Post** /browser/visual/comparisons/{comparisonId}/keep-as-regression | Keep as regression
[**UseCurrentBrowserVisualAsNewBaseline**](BrowserVisualReviewsAPI.md#UseCurrentBrowserVisualAsNewBaseline) | **Post** /browser/visual/comparisons/{comparisonId}/use-current-as-new-baseline | Use current as new baseline



## ExcludeBrowserVisualAreaAndRecompare

> BrowserVisualComparison ExcludeBrowserVisualAreaAndRecompare(ctx, comparisonId).BrowserVisualExcludeAndRecompareRequest(browserVisualExcludeAndRecompareRequest).Execute()

Exclude area and recompare



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
	comparisonId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Identifier of an immutable Browser visual comparison generation.
	browserVisualExcludeAndRecompareRequest := *openapiclient.NewBrowserVisualExcludeAndRecompareRequest("ActionId_example", int64(123), []openapiclient.BrowserVisualExcludedRegion{*openapiclient.NewBrowserVisualExcludedRegion(float64(123), float64(123), float64(123), float64(123))}) // BrowserVisualExcludeAndRecompareRequest |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BrowserVisualReviewsAPI.ExcludeBrowserVisualAreaAndRecompare(context.Background(), comparisonId).BrowserVisualExcludeAndRecompareRequest(browserVisualExcludeAndRecompareRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserVisualReviewsAPI.ExcludeBrowserVisualAreaAndRecompare``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ExcludeBrowserVisualAreaAndRecompare`: BrowserVisualComparison
	fmt.Fprintf(os.Stdout, "Response from `BrowserVisualReviewsAPI.ExcludeBrowserVisualAreaAndRecompare`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**comparisonId** | **string** | Identifier of an immutable Browser visual comparison generation. |

### Other Parameters

Other parameters are passed through a pointer to a apiExcludeBrowserVisualAreaAndRecompareRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **browserVisualExcludeAndRecompareRequest** | [**BrowserVisualExcludeAndRecompareRequest**](BrowserVisualExcludeAndRecompareRequest.md) |  |

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetBrowserVisualArtifactContent

> *os.File GetBrowserVisualArtifactContent(ctx, artifactId).Execute()

Download Browser visual evidence



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
	artifactId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BrowserVisualReviewsAPI.GetBrowserVisualArtifactContent(context.Background(), artifactId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserVisualReviewsAPI.GetBrowserVisualArtifactContent``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetBrowserVisualArtifactContent`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `BrowserVisualReviewsAPI.GetBrowserVisualArtifactContent`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artifactId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetBrowserVisualArtifactContentRequest struct via the builder pattern


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


## GetBrowserVisualComparison

> BrowserVisualComparison GetBrowserVisualComparison(ctx, comparisonId).Execute()

Get a Browser visual comparison



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
	comparisonId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Identifier of an immutable Browser visual comparison generation.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BrowserVisualReviewsAPI.GetBrowserVisualComparison(context.Background(), comparisonId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserVisualReviewsAPI.GetBrowserVisualComparison``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetBrowserVisualComparison`: BrowserVisualComparison
	fmt.Fprintf(os.Stdout, "Response from `BrowserVisualReviewsAPI.GetBrowserVisualComparison`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**comparisonId** | **string** | Identifier of an immutable Browser visual comparison generation. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetBrowserVisualComparisonRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## KeepBrowserVisualAsRegression

> BrowserVisualComparison KeepBrowserVisualAsRegression(ctx, comparisonId).BrowserVisualKeepRegressionRequest(browserVisualKeepRegressionRequest).Execute()

Keep as regression



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
	comparisonId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Identifier of an immutable Browser visual comparison generation.
	browserVisualKeepRegressionRequest := *openapiclient.NewBrowserVisualKeepRegressionRequest("ActionId_example", int64(123)) // BrowserVisualKeepRegressionRequest |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BrowserVisualReviewsAPI.KeepBrowserVisualAsRegression(context.Background(), comparisonId).BrowserVisualKeepRegressionRequest(browserVisualKeepRegressionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserVisualReviewsAPI.KeepBrowserVisualAsRegression``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `KeepBrowserVisualAsRegression`: BrowserVisualComparison
	fmt.Fprintf(os.Stdout, "Response from `BrowserVisualReviewsAPI.KeepBrowserVisualAsRegression`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**comparisonId** | **string** | Identifier of an immutable Browser visual comparison generation. |

### Other Parameters

Other parameters are passed through a pointer to a apiKeepBrowserVisualAsRegressionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **browserVisualKeepRegressionRequest** | [**BrowserVisualKeepRegressionRequest**](BrowserVisualKeepRegressionRequest.md) |  |

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UseCurrentBrowserVisualAsNewBaseline

> BrowserVisualComparison UseCurrentBrowserVisualAsNewBaseline(ctx, comparisonId).BrowserVisualPromoteBaselineRequest(browserVisualPromoteBaselineRequest).Execute()

Use current as new baseline



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
	comparisonId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Identifier of an immutable Browser visual comparison generation.
	browserVisualPromoteBaselineRequest := *openapiclient.NewBrowserVisualPromoteBaselineRequest("ActionId_example", int64(123)) // BrowserVisualPromoteBaselineRequest |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BrowserVisualReviewsAPI.UseCurrentBrowserVisualAsNewBaseline(context.Background(), comparisonId).BrowserVisualPromoteBaselineRequest(browserVisualPromoteBaselineRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BrowserVisualReviewsAPI.UseCurrentBrowserVisualAsNewBaseline``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UseCurrentBrowserVisualAsNewBaseline`: BrowserVisualComparison
	fmt.Fprintf(os.Stdout, "Response from `BrowserVisualReviewsAPI.UseCurrentBrowserVisualAsNewBaseline`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**comparisonId** | **string** | Identifier of an immutable Browser visual comparison generation. |

### Other Parameters

Other parameters are passed through a pointer to a apiUseCurrentBrowserVisualAsNewBaselineRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **browserVisualPromoteBaselineRequest** | [**BrowserVisualPromoteBaselineRequest**](BrowserVisualPromoteBaselineRequest.md) |  |

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

