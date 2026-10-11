# \SentinelAPI

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateSentinelCheck**](SentinelAPI.md#CreateSentinelCheck) | **Post** /sentinel/checks | Create a Sentinel check
[**DeleteSentinelCheck**](SentinelAPI.md#DeleteSentinelCheck) | **Delete** /sentinel/checks/{checkId} | Delete a Sentinel check
[**EnqueueSentinelRun**](SentinelAPI.md#EnqueueSentinelRun) | **Post** /sentinel/checks/{checkId}/run | Queue a Sentinel run
[**GetSentinelCheck**](SentinelAPI.md#GetSentinelCheck) | **Get** /sentinel/checks/{checkId} | Get a Sentinel check
[**GetSentinelDashboardSummary**](SentinelAPI.md#GetSentinelDashboardSummary) | **Get** /sentinel/dashboard/summary | Get Sentinel dashboard summary
[**GetSentinelRun**](SentinelAPI.md#GetSentinelRun) | **Get** /sentinel/runs/{runId} | Get Sentinel run evidence
[**ListLatestSentinelRuns**](SentinelAPI.md#ListLatestSentinelRuns) | **Get** /sentinel/runs | List latest Sentinel runs
[**ListSentinelChecks**](SentinelAPI.md#ListSentinelChecks) | **Get** /sentinel/checks/page | List Sentinel checks
[**ListSentinelDashboardIncidents**](SentinelAPI.md#ListSentinelDashboardIncidents) | **Get** /sentinel/dashboard/incidents | List recent Sentinel incidents
[**ListSentinelLinkedAssets**](SentinelAPI.md#ListSentinelLinkedAssets) | **Get** /sentinel/checks/spec-links/page | List compact Sentinel links for one Automation asset type
[**ListSentinelRuns**](SentinelAPI.md#ListSentinelRuns) | **Get** /sentinel/runs/page | List Sentinel runs
[**SampleSentinelRuns**](SentinelAPI.md#SampleSentinelRuns) | **Get** /sentinel/runs/sample | Sample Sentinel runs
[**UpdateSentinelCheck**](SentinelAPI.md#UpdateSentinelCheck) | **Put** /sentinel/checks/{checkId} | Replace a Sentinel check configuration



## CreateSentinelCheck

> SentinelCheck CreateSentinelCheck(ctx).SentinelCheckInput(sentinelCheckInput).IdempotencyKey(idempotencyKey).Execute()

Create a Sentinel check

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
	sentinelCheckInput := *openapiclient.NewSentinelCheckInput("Name_example", "Environment_example", "Type_example", openapiclient.ContentFormat("JSON"), "Definition_example") // SentinelCheckInput |
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | A caller-generated UUID retained for safe write retries where supported. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SentinelAPI.CreateSentinelCheck(context.Background()).SentinelCheckInput(sentinelCheckInput).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SentinelAPI.CreateSentinelCheck``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateSentinelCheck`: SentinelCheck
	fmt.Fprintf(os.Stdout, "Response from `SentinelAPI.CreateSentinelCheck`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateSentinelCheckRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sentinelCheckInput** | [**SentinelCheckInput**](SentinelCheckInput.md) |  |
 **idempotencyKey** | **string** | A caller-generated UUID retained for safe write retries where supported. |

### Return type

[**SentinelCheck**](SentinelCheck.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteSentinelCheck

> DeleteSentinelCheck(ctx, checkId).Execute()

Delete a Sentinel check

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
	checkId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the Sentinel check.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.SentinelAPI.DeleteSentinelCheck(context.Background(), checkId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SentinelAPI.DeleteSentinelCheck``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**checkId** | **string** | UUIDv7 identifier of the Sentinel check. |

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteSentinelCheckRequest struct via the builder pattern


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


## EnqueueSentinelRun

> RunEnqueueResponse EnqueueSentinelRun(ctx, checkId).IdempotencyKey(idempotencyKey).Region(region).Execute()

Queue a Sentinel run

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
	checkId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the Sentinel check.
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | A caller-generated UUID retained for safe write retries where supported. (optional)
	region := "region_example" // string |  (optional) (default to "local")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SentinelAPI.EnqueueSentinelRun(context.Background(), checkId).IdempotencyKey(idempotencyKey).Region(region).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SentinelAPI.EnqueueSentinelRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `EnqueueSentinelRun`: RunEnqueueResponse
	fmt.Fprintf(os.Stdout, "Response from `SentinelAPI.EnqueueSentinelRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**checkId** | **string** | UUIDv7 identifier of the Sentinel check. |

### Other Parameters

Other parameters are passed through a pointer to a apiEnqueueSentinelRunRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A caller-generated UUID retained for safe write retries where supported. |
 **region** | **string** |  | [default to &quot;local&quot;]

### Return type

[**RunEnqueueResponse**](RunEnqueueResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSentinelCheck

> SentinelCheck GetSentinelCheck(ctx, checkId).Execute()

Get a Sentinel check

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
	checkId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the Sentinel check.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SentinelAPI.GetSentinelCheck(context.Background(), checkId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SentinelAPI.GetSentinelCheck``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSentinelCheck`: SentinelCheck
	fmt.Fprintf(os.Stdout, "Response from `SentinelAPI.GetSentinelCheck`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**checkId** | **string** | UUIDv7 identifier of the Sentinel check. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetSentinelCheckRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**SentinelCheck**](SentinelCheck.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSentinelDashboardSummary

> SentinelDashboardSummary GetSentinelDashboardSummary(ctx).Environment(environment).Execute()

Get Sentinel dashboard summary

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
	environment := "environment_example" // string | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SentinelAPI.GetSentinelDashboardSummary(context.Background()).Environment(environment).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SentinelAPI.GetSentinelDashboardSummary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSentinelDashboardSummary`: SentinelDashboardSummary
	fmt.Fprintf(os.Stdout, "Response from `SentinelAPI.GetSentinelDashboardSummary`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetSentinelDashboardSummaryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **string** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |

### Return type

[**SentinelDashboardSummary**](SentinelDashboardSummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSentinelRun

> SentinelRun GetSentinelRun(ctx, runId).Execute()

Get Sentinel run evidence

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
	resp, r, err := apiClient.SentinelAPI.GetSentinelRun(context.Background(), runId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SentinelAPI.GetSentinelRun``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSentinelRun`: SentinelRun
	fmt.Fprintf(os.Stdout, "Response from `SentinelAPI.GetSentinelRun`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**runId** | **string** | UUIDv7 identifier of the stored run evidence. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetSentinelRunRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**SentinelRun**](SentinelRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListLatestSentinelRuns

> []SentinelRun ListLatestSentinelRuns(ctx).Environment(environment).Size(size).Execute()

List latest Sentinel runs

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
	environment := "environment_example" // string | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
	size := int32(56) // int32 | Maximum number of results returned in one page. (optional) (default to 20)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SentinelAPI.ListLatestSentinelRuns(context.Background()).Environment(environment).Size(size).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SentinelAPI.ListLatestSentinelRuns``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListLatestSentinelRuns`: []SentinelRun
	fmt.Fprintf(os.Stdout, "Response from `SentinelAPI.ListLatestSentinelRuns`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListLatestSentinelRunsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **string** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |
 **size** | **int32** | Maximum number of results returned in one page. | [default to 20]

### Return type

[**[]SentinelRun**](SentinelRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSentinelChecks

> SentinelCheckPage ListSentinelChecks(ctx).Environment(environment).Page(page).Size(size).Search(search).Execute()

List Sentinel checks

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
	environment := "environment_example" // string | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
	page := int32(56) // int32 | Zero-based page index. (optional) (default to 0)
	size := int32(56) // int32 | Maximum number of results returned in one page. (optional) (default to 20)
	search := "search_example" // string | Case-insensitive server-side search within the active project. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SentinelAPI.ListSentinelChecks(context.Background()).Environment(environment).Page(page).Size(size).Search(search).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SentinelAPI.ListSentinelChecks``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSentinelChecks`: SentinelCheckPage
	fmt.Fprintf(os.Stdout, "Response from `SentinelAPI.ListSentinelChecks`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListSentinelChecksRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **string** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |
 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** | Maximum number of results returned in one page. | [default to 20]
 **search** | **string** | Case-insensitive server-side search within the active project. |

### Return type

[**SentinelCheckPage**](SentinelCheckPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSentinelDashboardIncidents

> []SentinelIncident ListSentinelDashboardIncidents(ctx).Environment(environment).Execute()

List recent Sentinel incidents

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
	environment := "environment_example" // string | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SentinelAPI.ListSentinelDashboardIncidents(context.Background()).Environment(environment).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SentinelAPI.ListSentinelDashboardIncidents``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSentinelDashboardIncidents`: []SentinelIncident
	fmt.Fprintf(os.Stdout, "Response from `SentinelAPI.ListSentinelDashboardIncidents`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListSentinelDashboardIncidentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **string** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |

### Return type

[**[]SentinelIncident**](SentinelIncident.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSentinelLinkedAssets

> SentinelLinkSummaryPage ListSentinelLinkedAssets(ctx).Environment(environment).CheckType(checkType).Page(page).Size(size).Execute()

List compact Sentinel links for one Automation asset type

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
	environment := "environment_example" // string | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
	checkType := openapiclient.SentinelLinkedAssetCheckType("REST") // SentinelLinkedAssetCheckType | Exact Automation asset type whose Sentinel links should be returned.
	page := int32(56) // int32 | Zero-based page index. (optional) (default to 0)
	size := int32(56) // int32 | Maximum number of results returned in one page. (optional) (default to 20)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SentinelAPI.ListSentinelLinkedAssets(context.Background()).Environment(environment).CheckType(checkType).Page(page).Size(size).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SentinelAPI.ListSentinelLinkedAssets``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSentinelLinkedAssets`: SentinelLinkSummaryPage
	fmt.Fprintf(os.Stdout, "Response from `SentinelAPI.ListSentinelLinkedAssets`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListSentinelLinkedAssetsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **string** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |
 **checkType** | [**SentinelLinkedAssetCheckType**](SentinelLinkedAssetCheckType.md) | Exact Automation asset type whose Sentinel links should be returned. |
 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** | Maximum number of results returned in one page. | [default to 20]

### Return type

[**SentinelLinkSummaryPage**](SentinelLinkSummaryPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSentinelRuns

> SentinelRunPage ListSentinelRuns(ctx).Environment(environment).Page(page).Size(size).CheckId(checkId).Status(status).SortBy(sortBy).SortDirection(sortDirection).Execute()

List Sentinel runs

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
	environment := "environment_example" // string | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
	page := int32(56) // int32 | Zero-based page index. (optional) (default to 0)
	size := int32(56) // int32 | Maximum number of results returned in one page. (optional) (default to 20)
	checkId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |  (optional)
	status := openapiclient.RunStatus("QUEUED") // RunStatus |  (optional)
	sortBy := "sortBy_example" // string |  (optional) (default to "queuedAt")
	sortDirection := "sortDirection_example" // string |  (optional) (default to "desc")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SentinelAPI.ListSentinelRuns(context.Background()).Environment(environment).Page(page).Size(size).CheckId(checkId).Status(status).SortBy(sortBy).SortDirection(sortDirection).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SentinelAPI.ListSentinelRuns``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSentinelRuns`: SentinelRunPage
	fmt.Fprintf(os.Stdout, "Response from `SentinelAPI.ListSentinelRuns`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListSentinelRunsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **string** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |
 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** | Maximum number of results returned in one page. | [default to 20]
 **checkId** | **string** |  |
 **status** | [**RunStatus**](RunStatus.md) |  |
 **sortBy** | **string** |  | [default to &quot;queuedAt&quot;]
 **sortDirection** | **string** |  | [default to &quot;desc&quot;]

### Return type

[**SentinelRunPage**](SentinelRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SampleSentinelRuns

> []SentinelRun SampleSentinelRuns(ctx).Environment(environment).Days(days).Size(size).Execute()

Sample Sentinel runs

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
	environment := "environment_example" // string | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
	days := int32(56) // int32 |  (optional) (default to 30)
	size := int32(56) // int32 | Maximum number of results returned in one page. (optional) (default to 20)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SentinelAPI.SampleSentinelRuns(context.Background()).Environment(environment).Days(days).Size(size).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SentinelAPI.SampleSentinelRuns``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SampleSentinelRuns`: []SentinelRun
	fmt.Fprintf(os.Stdout, "Response from `SentinelAPI.SampleSentinelRuns`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSampleSentinelRunsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **string** | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |
 **days** | **int32** |  | [default to 30]
 **size** | **int32** | Maximum number of results returned in one page. | [default to 20]

### Return type

[**[]SentinelRun**](SentinelRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateSentinelCheck

> SentinelCheck UpdateSentinelCheck(ctx, checkId).SentinelCheckInput(sentinelCheckInput).Execute()

Replace a Sentinel check configuration

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
	checkId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of the Sentinel check.
	sentinelCheckInput := *openapiclient.NewSentinelCheckInput("Name_example", "Environment_example", "Type_example", openapiclient.ContentFormat("JSON"), "Definition_example") // SentinelCheckInput |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SentinelAPI.UpdateSentinelCheck(context.Background(), checkId).SentinelCheckInput(sentinelCheckInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SentinelAPI.UpdateSentinelCheck``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateSentinelCheck`: SentinelCheck
	fmt.Fprintf(os.Stdout, "Response from `SentinelAPI.UpdateSentinelCheck`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**checkId** | **string** | UUIDv7 identifier of the Sentinel check. |

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateSentinelCheckRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **sentinelCheckInput** | [**SentinelCheckInput**](SentinelCheckInput.md) |  |

### Return type

[**SentinelCheck**](SentinelCheck.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
