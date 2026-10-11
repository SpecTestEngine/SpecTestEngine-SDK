# \FragmentsAPI

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CompileDraftFragments**](FragmentsAPI.md#CompileDraftFragments) | **Post** /test/spec/fragment/compile-draft | Compile inline fragment DSL into a specification draft
[**CompileFragments**](FragmentsAPI.md#CompileFragments) | **Post** /test/spec/fragment/compile | Compile fragments into a specification draft
[**CreateFragment**](FragmentsAPI.md#CreateFragment) | **Post** /test/spec/fragment/create | Create a specification fragment
[**DeleteFragment**](FragmentsAPI.md#DeleteFragment) | **Delete** /test/spec/fragment/by-id | Delete a fragment
[**GetFragment**](FragmentsAPI.md#GetFragment) | **Get** /test/spec/fragment/by-id/{fragmentId} | Get a fragment
[**GetFragmentCatalog**](FragmentsAPI.md#GetFragmentCatalog) | **Get** /test/spec/fragment/catalog | Get the fragment DSL catalog for an API type
[**GetFragmentSummary**](FragmentsAPI.md#GetFragmentSummary) | **Get** /test/spec/fragment/summary | Count fragments by API type
[**ListFragments**](FragmentsAPI.md#ListFragments) | **Get** /test/spec/fragment/page | List specification fragments
[**SaveFragmentsAsSpecification**](FragmentsAPI.md#SaveFragmentsAsSpecification) | **Post** /test/spec/fragment/save-as-spec | Compile saved fragments and persist the result in the matching protocol engine
[**UpdateFragment**](FragmentsAPI.md#UpdateFragment) | **Put** /test/spec/fragment/by-id | Replace a fragment



## CompileDraftFragments

> CompiledSpecification CompileDraftFragments(ctx).FragmentDraftAssembly(fragmentDraftAssembly).Format(format).Execute()

Compile inline fragment DSL into a specification draft

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
	fragmentDraftAssembly := *openapiclient.NewFragmentDraftAssembly(openapiclient.SpecType("REST"), []openapiclient.FragmentDraftInput{*openapiclient.NewFragmentDraftInput(openapiclient.FragmentType("URL_METHOD"), map[string]interface{}{"key": interface{}(123)})}) // FragmentDraftAssembly |
	format := openapiclient.ContentFormat("JSON") // ContentFormat | Serialization format used for the returned specification source. (optional) (default to "JSON")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FragmentsAPI.CompileDraftFragments(context.Background()).FragmentDraftAssembly(fragmentDraftAssembly).Format(format).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FragmentsAPI.CompileDraftFragments``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CompileDraftFragments`: CompiledSpecification
	fmt.Fprintf(os.Stdout, "Response from `FragmentsAPI.CompileDraftFragments`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCompileDraftFragmentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fragmentDraftAssembly** | [**FragmentDraftAssembly**](FragmentDraftAssembly.md) |  |
 **format** | [**ContentFormat**](ContentFormat.md) | Serialization format used for the returned specification source. | [default to &quot;JSON&quot;]

### Return type

[**CompiledSpecification**](CompiledSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CompileFragments

> CompiledSpecification CompileFragments(ctx).FragmentAssembly(fragmentAssembly).Format(format).Execute()

Compile fragments into a specification draft

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
	fragmentAssembly := *openapiclient.NewFragmentAssembly(openapiclient.SpecType("REST"), []string{"0197f0ab-42e7-7a31-8a9c-591a8ee54c12"}) // FragmentAssembly |
	format := openapiclient.ContentFormat("JSON") // ContentFormat | Serialization format used for the returned specification source. (optional) (default to "JSON")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FragmentsAPI.CompileFragments(context.Background()).FragmentAssembly(fragmentAssembly).Format(format).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FragmentsAPI.CompileFragments``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CompileFragments`: CompiledSpecification
	fmt.Fprintf(os.Stdout, "Response from `FragmentsAPI.CompileFragments`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCompileFragmentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fragmentAssembly** | [**FragmentAssembly**](FragmentAssembly.md) |  |
 **format** | [**ContentFormat**](ContentFormat.md) | Serialization format used for the returned specification source. | [default to &quot;JSON&quot;]

### Return type

[**CompiledSpecification**](CompiledSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateFragment

> Fragment CreateFragment(ctx).FragmentInput(fragmentInput).IdempotencyKey(idempotencyKey).Execute()

Create a specification fragment

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
	fragmentInput := *openapiclient.NewFragmentInput("Name_example", openapiclient.SpecType("REST"), openapiclient.FragmentType("URL_METHOD"), map[string]interface{}{"key": interface{}(123)}) // FragmentInput |
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | A caller-generated UUID retained for safe write retries where supported. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FragmentsAPI.CreateFragment(context.Background()).FragmentInput(fragmentInput).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FragmentsAPI.CreateFragment``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateFragment`: Fragment
	fmt.Fprintf(os.Stdout, "Response from `FragmentsAPI.CreateFragment`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateFragmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fragmentInput** | [**FragmentInput**](FragmentInput.md) |  |
 **idempotencyKey** | **string** | A caller-generated UUID retained for safe write retries where supported. |

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteFragment

> Fragment DeleteFragment(ctx).FragmentId(fragmentId).Execute()

Delete a fragment

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
	fragmentId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FragmentsAPI.DeleteFragment(context.Background()).FragmentId(fragmentId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FragmentsAPI.DeleteFragment``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteFragment`: Fragment
	fmt.Fprintf(os.Stdout, "Response from `FragmentsAPI.DeleteFragment`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDeleteFragmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fragmentId** | **string** |  |

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFragment

> Fragment GetFragment(ctx, fragmentId).Execute()

Get a fragment

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
	fragmentId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FragmentsAPI.GetFragment(context.Background(), fragmentId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FragmentsAPI.GetFragment``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFragment`: Fragment
	fmt.Fprintf(os.Stdout, "Response from `FragmentsAPI.GetFragment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fragmentId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetFragmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFragmentCatalog

> FragmentCatalog GetFragmentCatalog(ctx).SpecType(specType).Execute()

Get the fragment DSL catalog for an API type

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
	specType := openapiclient.SpecType("REST") // SpecType |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FragmentsAPI.GetFragmentCatalog(context.Background()).SpecType(specType).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FragmentsAPI.GetFragmentCatalog``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFragmentCatalog`: FragmentCatalog
	fmt.Fprintf(os.Stdout, "Response from `FragmentsAPI.GetFragmentCatalog`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetFragmentCatalogRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specType** | [**SpecType**](SpecType.md) |  |

### Return type

[**FragmentCatalog**](FragmentCatalog.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFragmentSummary

> FragmentSummary GetFragmentSummary(ctx).Execute()

Count fragments by API type

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
	resp, r, err := apiClient.FragmentsAPI.GetFragmentSummary(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FragmentsAPI.GetFragmentSummary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFragmentSummary`: FragmentSummary
	fmt.Fprintf(os.Stdout, "Response from `FragmentsAPI.GetFragmentSummary`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetFragmentSummaryRequest struct via the builder pattern


### Return type

[**FragmentSummary**](FragmentSummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListFragments

> FragmentPage ListFragments(ctx).Page(page).Size(size).Search(search).SpecType(specType).Type_(type_).Execute()

List specification fragments

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
	specType := openapiclient.SpecType("REST") // SpecType | Filter the library to one API protocol. (optional)
	type_ := openapiclient.FragmentType("URL_METHOD") // FragmentType |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FragmentsAPI.ListFragments(context.Background()).Page(page).Size(size).Search(search).SpecType(specType).Type_(type_).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FragmentsAPI.ListFragments``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListFragments`: FragmentPage
	fmt.Fprintf(os.Stdout, "Response from `FragmentsAPI.ListFragments`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListFragmentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int32** | Zero-based page index. | [default to 0]
 **size** | **int32** | Maximum number of results returned in one page. | [default to 20]
 **search** | **string** | Case-insensitive server-side search within the active project. |
 **specType** | [**SpecType**](SpecType.md) | Filter the library to one API protocol. |
 **type_** | [**FragmentType**](FragmentType.md) |  |

### Return type

[**FragmentPage**](FragmentPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SaveFragmentsAsSpecification

> Specification SaveFragmentsAsSpecification(ctx).SpecName(specName).FragmentAssembly(fragmentAssembly).Description(description).Format(format).IdempotencyKey(idempotencyKey).Execute()

Compile saved fragments and persist the result in the matching protocol engine

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
	specName := "specName_example" // string |
	fragmentAssembly := *openapiclient.NewFragmentAssembly(openapiclient.SpecType("REST"), []string{"0197f0ab-42e7-7a31-8a9c-591a8ee54c12"}) // FragmentAssembly |
	description := "description_example" // string |  (optional)
	format := openapiclient.ContentFormat("JSON") // ContentFormat | Serialization format used for the returned specification source. (optional) (default to "JSON")
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | A caller-generated UUID retained for safe write retries where supported. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FragmentsAPI.SaveFragmentsAsSpecification(context.Background()).SpecName(specName).FragmentAssembly(fragmentAssembly).Description(description).Format(format).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FragmentsAPI.SaveFragmentsAsSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SaveFragmentsAsSpecification`: Specification
	fmt.Fprintf(os.Stdout, "Response from `FragmentsAPI.SaveFragmentsAsSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSaveFragmentsAsSpecificationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specName** | **string** |  |
 **fragmentAssembly** | [**FragmentAssembly**](FragmentAssembly.md) |  |
 **description** | **string** |  |
 **format** | [**ContentFormat**](ContentFormat.md) | Serialization format used for the returned specification source. | [default to &quot;JSON&quot;]
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


## UpdateFragment

> Fragment UpdateFragment(ctx).FragmentId(fragmentId).FragmentInput(fragmentInput).Execute()

Replace a fragment

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
	fragmentId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |
	fragmentInput := *openapiclient.NewFragmentInput("Name_example", openapiclient.SpecType("REST"), openapiclient.FragmentType("URL_METHOD"), map[string]interface{}{"key": interface{}(123)}) // FragmentInput |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FragmentsAPI.UpdateFragment(context.Background()).FragmentId(fragmentId).FragmentInput(fragmentInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FragmentsAPI.UpdateFragment``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateFragment`: Fragment
	fmt.Fprintf(os.Stdout, "Response from `FragmentsAPI.UpdateFragment`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateFragmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fragmentId** | **string** |  |
 **fragmentInput** | [**FragmentInput**](FragmentInput.md) |  |

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
