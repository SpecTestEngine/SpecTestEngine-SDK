# \GenerationAPI

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateArtifactGenerationProfile**](GenerationAPI.md#CreateArtifactGenerationProfile) | **Post** /artifact-profiles | Create a CI export profile
[**DeleteArtifactGenerationProfile**](GenerationAPI.md#DeleteArtifactGenerationProfile) | **Delete** /artifact-profiles/{profileId} | Delete a CI export profile
[**DownloadArtifactGenerationProfileArchive**](GenerationAPI.md#DownloadArtifactGenerationProfileArchive) | **Post** /artifact-profiles/{profileId}/environments/{environmentKey}/atf/archive | Validate and download a CI profile archive
[**DownloadAtfProject**](GenerationAPI.md#DownloadAtfProject) | **Post** /atf/generate/download | Download a generated ATF project
[**GenerateFromOpenApiContent**](GenerationAPI.md#GenerateFromOpenApiContent) | **Post** /openapi/generate-from-content | Generate specifications and flows from OpenAPI content
[**GenerateSpecification**](GenerationAPI.md#GenerateSpecification) | **Post** /spec/generate | Generate an executable specification from concrete request evidence
[**GetArtifactGenerationProfile**](GenerationAPI.md#GetArtifactGenerationProfile) | **Get** /artifact-profiles/{profileId} | Get a CI export profile
[**GetAtfProjectValidationResult**](GenerationAPI.md#GetAtfProjectValidationResult) | **Get** /atf/generate/validate/result/{validationId} | Get ATF validation status or result
[**ListArtifactGenerationProfiles**](GenerationAPI.md#ListArtifactGenerationProfiles) | **Get** /artifact-profiles | List CI export profiles
[**ObserveAtfProjectValidation**](GenerationAPI.md#ObserveAtfProjectValidation) | **Get** /atf/generate/validate/events/{validationId} | Observe ATF validation progress
[**PreviewAtfProject**](GenerationAPI.md#PreviewAtfProject) | **Post** /atf/generate/preview | Generate an ATF project preview
[**RefreshArtifactGenerationProfileBundle**](GenerationAPI.md#RefreshArtifactGenerationProfileBundle) | **Post** /artifact-profiles/{profileId}/environments/{environmentKey}/bundle/refresh | Capture or refresh an environment baseline
[**StartAtfProjectValidation**](GenerationAPI.md#StartAtfProjectValidation) | **Post** /atf/generate/validate/start | Start asynchronous ATF compile validation
[**UpdateArtifactGenerationProfile**](GenerationAPI.md#UpdateArtifactGenerationProfile) | **Put** /artifact-profiles/{profileId} | Update a CI export profile
[**ValidateAtfProject**](GenerationAPI.md#ValidateAtfProject) | **Post** /atf/generate/validate | Validate that an ATF project compiles



## CreateArtifactGenerationProfile

> ArtifactGenerationProfile CreateArtifactGenerationProfile(ctx).ArtifactGenerationProfileInput(artifactGenerationProfileInput).IdempotencyKey(idempotencyKey).Execute()

Create a CI export profile

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
	artifactGenerationProfileInput := *openapiclient.NewArtifactGenerationProfileInput("Name_example", "ArtifactType_example", *openapiclient.NewArtifactSelection([]openapiclient.ArtifactSpecRef{*openapiclient.NewArtifactSpecRef("0197f0ab-42e7-7a31-8a9c-591a8ee54c12", "SpecType_example")}, []string{"0197f0ab-42e7-7a31-8a9c-591a8ee54c12"}, []string{"0197f0ab-42e7-7a31-8a9c-591a8ee54c12"}), *openapiclient.NewAtfProjectConfig("ProjectName_example", "PackageName_example", "TargetFramework_example", "ExportMode_example", "BuildTool_example", int32(123), openapiclient.AtfBaseUrlMode("KEEP_ABSOLUTE_URLS"), false, false, "CiProvider_example", "UnsupportedFeatureMode_example"), []openapiclient.ArtifactGenerationProfileEnvironmentInput{*openapiclient.NewArtifactGenerationProfileEnvironmentInput("EnvironmentKey_example", "ResolutionMode_example")}) // ArtifactGenerationProfileInput |
	idempotencyKey := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | A caller-generated UUID retained for safe write retries where supported. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GenerationAPI.CreateArtifactGenerationProfile(context.Background()).ArtifactGenerationProfileInput(artifactGenerationProfileInput).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.CreateArtifactGenerationProfile``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateArtifactGenerationProfile`: ArtifactGenerationProfile
	fmt.Fprintf(os.Stdout, "Response from `GenerationAPI.CreateArtifactGenerationProfile`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateArtifactGenerationProfileRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactGenerationProfileInput** | [**ArtifactGenerationProfileInput**](ArtifactGenerationProfileInput.md) |  |
 **idempotencyKey** | **string** | A caller-generated UUID retained for safe write retries where supported. |

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteArtifactGenerationProfile

> DeleteArtifactGenerationProfile(ctx, profileId).Execute()

Delete a CI export profile

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
	profileId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of a CI export profile.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.GenerationAPI.DeleteArtifactGenerationProfile(context.Background(), profileId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.DeleteArtifactGenerationProfile``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**profileId** | **string** | UUIDv7 identifier of a CI export profile. |

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteArtifactGenerationProfileRequest struct via the builder pattern


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


## DownloadArtifactGenerationProfileArchive

> *os.File DownloadArtifactGenerationProfileArchive(ctx, profileId, environmentKey).Execute()

Validate and download a CI profile archive



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
	profileId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of a CI export profile.
	environmentKey := "environmentKey_example" // string | Stable profile environment key such as test, staging, or production.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GenerationAPI.DownloadArtifactGenerationProfileArchive(context.Background(), profileId, environmentKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.DownloadArtifactGenerationProfileArchive``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadArtifactGenerationProfileArchive`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `GenerationAPI.DownloadArtifactGenerationProfileArchive`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**profileId** | **string** | UUIDv7 identifier of a CI export profile. |
**environmentKey** | **string** | Stable profile environment key such as test, staging, or production. |

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadArtifactGenerationProfileArchiveRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[***os.File**](*os.File.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadAtfProject

> *os.File DownloadAtfProject(ctx).AtfGenerationInput(atfGenerationInput).Execute()

Download a generated ATF project

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
	atfGenerationInput := *openapiclient.NewAtfGenerationInput("ProjectName_example", "PackageName_example") // AtfGenerationInput |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GenerationAPI.DownloadAtfProject(context.Background()).AtfGenerationInput(atfGenerationInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.DownloadAtfProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadAtfProject`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `GenerationAPI.DownloadAtfProject`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDownloadAtfProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **atfGenerationInput** | [**AtfGenerationInput**](AtfGenerationInput.md) |  |

### Return type

[***os.File**](*os.File.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GenerateFromOpenApiContent

> OpenApiGenerationResult GenerateFromOpenApiContent(ctx).ContentFormat(contentFormat).Body(body).IncludeNegativeTests(includeNegativeTests).GenerateFlowScenarios(generateFlowScenarios).GenerationStrategy(generationStrategy).NegativeTestGenerationMode(negativeTestGenerationMode).Execute()

Generate specifications and flows from OpenAPI content

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
	contentFormat := openapiclient.ContentFormat("JSON") // ContentFormat |  (default to "JSON")
	body := "body_example" // string |
	includeNegativeTests := true // bool |  (optional) (default to false)
	generateFlowScenarios := true // bool |  (optional) (default to false)
	generationStrategy := "generationStrategy_example" // string |  (optional) (default to "SCHEMA_BASED")
	negativeTestGenerationMode := "negativeTestGenerationMode_example" // string |  (optional) (default to "EXTENDED")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GenerationAPI.GenerateFromOpenApiContent(context.Background()).ContentFormat(contentFormat).Body(body).IncludeNegativeTests(includeNegativeTests).GenerateFlowScenarios(generateFlowScenarios).GenerationStrategy(generationStrategy).NegativeTestGenerationMode(negativeTestGenerationMode).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.GenerateFromOpenApiContent``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GenerateFromOpenApiContent`: OpenApiGenerationResult
	fmt.Fprintf(os.Stdout, "Response from `GenerationAPI.GenerateFromOpenApiContent`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGenerateFromOpenApiContentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentFormat** | [**ContentFormat**](ContentFormat.md) |  | [default to &quot;JSON&quot;]
 **body** | **string** |  |
 **includeNegativeTests** | **bool** |  | [default to false]
 **generateFlowScenarios** | **bool** |  | [default to false]
 **generationStrategy** | **string** |  | [default to &quot;SCHEMA_BASED&quot;]
 **negativeTestGenerationMode** | **string** |  | [default to &quot;EXTENDED&quot;]

### Return type

[**OpenApiGenerationResult**](OpenApiGenerationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GenerateSpecification

> []SpecGenerationResult GenerateSpecification(ctx).RequestBody(requestBody).Mode(mode).Format(format).SpecGenerationTypes(specGenerationTypes).Execute()

Generate an executable specification from concrete request evidence



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
	requestBody := map[string]interface{}{"key": interface{}(123)} // map[string]interface{} |
	mode := "mode_example" // string |  (optional) (default to "FULL")
	format := openapiclient.ContentFormat("JSON") // ContentFormat |  (optional) (default to "JSON")
	specGenerationTypes := []string{"SpecGenerationTypes_example"} // []string | Comma-separated generation variants. Streaming currently accepts POSITIVE only. (optional) (default to {"POSITIVE"})

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GenerationAPI.GenerateSpecification(context.Background()).RequestBody(requestBody).Mode(mode).Format(format).SpecGenerationTypes(specGenerationTypes).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.GenerateSpecification``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GenerateSpecification`: []SpecGenerationResult
	fmt.Fprintf(os.Stdout, "Response from `GenerationAPI.GenerateSpecification`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGenerateSpecificationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | **map[string]interface{}** |  |
 **mode** | **string** |  | [default to &quot;FULL&quot;]
 **format** | [**ContentFormat**](ContentFormat.md) |  | [default to &quot;JSON&quot;]
 **specGenerationTypes** | **[]string** | Comma-separated generation variants. Streaming currently accepts POSITIVE only. | [default to {&quot;POSITIVE&quot;}]

### Return type

[**[]SpecGenerationResult**](SpecGenerationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetArtifactGenerationProfile

> ArtifactGenerationProfile GetArtifactGenerationProfile(ctx, profileId).Execute()

Get a CI export profile

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
	profileId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of a CI export profile.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GenerationAPI.GetArtifactGenerationProfile(context.Background(), profileId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.GetArtifactGenerationProfile``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetArtifactGenerationProfile`: ArtifactGenerationProfile
	fmt.Fprintf(os.Stdout, "Response from `GenerationAPI.GetArtifactGenerationProfile`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**profileId** | **string** | UUIDv7 identifier of a CI export profile. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetArtifactGenerationProfileRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAtfProjectValidationResult

> AtfValidationResult GetAtfProjectValidationResult(ctx, validationId).Execute()

Get ATF validation status or result

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
	validationId := "validationId_example" // string | Opaque identifier of a bounded asynchronous ATF validation job.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GenerationAPI.GetAtfProjectValidationResult(context.Background(), validationId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.GetAtfProjectValidationResult``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAtfProjectValidationResult`: AtfValidationResult
	fmt.Fprintf(os.Stdout, "Response from `GenerationAPI.GetAtfProjectValidationResult`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**validationId** | **string** | Opaque identifier of a bounded asynchronous ATF validation job. |

### Other Parameters

Other parameters are passed through a pointer to a apiGetAtfProjectValidationResultRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**AtfValidationResult**](AtfValidationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListArtifactGenerationProfiles

> []ArtifactGenerationProfile ListArtifactGenerationProfiles(ctx).Execute()

List CI export profiles



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
	resp, r, err := apiClient.GenerationAPI.ListArtifactGenerationProfiles(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.ListArtifactGenerationProfiles``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListArtifactGenerationProfiles`: []ArtifactGenerationProfile
	fmt.Fprintf(os.Stdout, "Response from `GenerationAPI.ListArtifactGenerationProfiles`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiListArtifactGenerationProfilesRequest struct via the builder pattern


### Return type

[**[]ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ObserveAtfProjectValidation

> string ObserveAtfProjectValidation(ctx, validationId).Execute()

Observe ATF validation progress

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
	validationId := "validationId_example" // string | Opaque identifier of a bounded asynchronous ATF validation job.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GenerationAPI.ObserveAtfProjectValidation(context.Background(), validationId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.ObserveAtfProjectValidation``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ObserveAtfProjectValidation`: string
	fmt.Fprintf(os.Stdout, "Response from `GenerationAPI.ObserveAtfProjectValidation`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**validationId** | **string** | Opaque identifier of a bounded asynchronous ATF validation job. |

### Other Parameters

Other parameters are passed through a pointer to a apiObserveAtfProjectValidationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

**string**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PreviewAtfProject

> AtfGenerationResult PreviewAtfProject(ctx).AtfGenerationInput(atfGenerationInput).Execute()

Generate an ATF project preview

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
	atfGenerationInput := *openapiclient.NewAtfGenerationInput("ProjectName_example", "PackageName_example") // AtfGenerationInput |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GenerationAPI.PreviewAtfProject(context.Background()).AtfGenerationInput(atfGenerationInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.PreviewAtfProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PreviewAtfProject`: AtfGenerationResult
	fmt.Fprintf(os.Stdout, "Response from `GenerationAPI.PreviewAtfProject`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPreviewAtfProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **atfGenerationInput** | [**AtfGenerationInput**](AtfGenerationInput.md) |  |

### Return type

[**AtfGenerationResult**](AtfGenerationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RefreshArtifactGenerationProfileBundle

> ArtifactGenerationProfile RefreshArtifactGenerationProfileBundle(ctx, profileId, environmentKey).Execute()

Capture or refresh an environment baseline



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
	profileId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of a CI export profile.
	environmentKey := "environmentKey_example" // string | Stable profile environment key such as test, staging, or production.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GenerationAPI.RefreshArtifactGenerationProfileBundle(context.Background(), profileId, environmentKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.RefreshArtifactGenerationProfileBundle``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RefreshArtifactGenerationProfileBundle`: ArtifactGenerationProfile
	fmt.Fprintf(os.Stdout, "Response from `GenerationAPI.RefreshArtifactGenerationProfileBundle`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**profileId** | **string** | UUIDv7 identifier of a CI export profile. |
**environmentKey** | **string** | Stable profile environment key such as test, staging, or production. |

### Other Parameters

Other parameters are passed through a pointer to a apiRefreshArtifactGenerationProfileBundleRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StartAtfProjectValidation

> AtfValidationStart StartAtfProjectValidation(ctx).AtfGenerationInput(atfGenerationInput).Execute()

Start asynchronous ATF compile validation

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
	atfGenerationInput := *openapiclient.NewAtfGenerationInput("ProjectName_example", "PackageName_example") // AtfGenerationInput |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GenerationAPI.StartAtfProjectValidation(context.Background()).AtfGenerationInput(atfGenerationInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.StartAtfProjectValidation``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StartAtfProjectValidation`: AtfValidationStart
	fmt.Fprintf(os.Stdout, "Response from `GenerationAPI.StartAtfProjectValidation`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiStartAtfProjectValidationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **atfGenerationInput** | [**AtfGenerationInput**](AtfGenerationInput.md) |  |

### Return type

[**AtfValidationStart**](AtfValidationStart.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateArtifactGenerationProfile

> ArtifactGenerationProfile UpdateArtifactGenerationProfile(ctx, profileId).ArtifactGenerationProfileInput(artifactGenerationProfileInput).Execute()

Update a CI export profile



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
	profileId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUIDv7 identifier of a CI export profile.
	artifactGenerationProfileInput := *openapiclient.NewArtifactGenerationProfileInput("Name_example", "ArtifactType_example", *openapiclient.NewArtifactSelection([]openapiclient.ArtifactSpecRef{*openapiclient.NewArtifactSpecRef("0197f0ab-42e7-7a31-8a9c-591a8ee54c12", "SpecType_example")}, []string{"0197f0ab-42e7-7a31-8a9c-591a8ee54c12"}, []string{"0197f0ab-42e7-7a31-8a9c-591a8ee54c12"}), *openapiclient.NewAtfProjectConfig("ProjectName_example", "PackageName_example", "TargetFramework_example", "ExportMode_example", "BuildTool_example", int32(123), openapiclient.AtfBaseUrlMode("KEEP_ABSOLUTE_URLS"), false, false, "CiProvider_example", "UnsupportedFeatureMode_example"), []openapiclient.ArtifactGenerationProfileEnvironmentInput{*openapiclient.NewArtifactGenerationProfileEnvironmentInput("EnvironmentKey_example", "ResolutionMode_example")}) // ArtifactGenerationProfileInput |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GenerationAPI.UpdateArtifactGenerationProfile(context.Background(), profileId).ArtifactGenerationProfileInput(artifactGenerationProfileInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.UpdateArtifactGenerationProfile``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateArtifactGenerationProfile`: ArtifactGenerationProfile
	fmt.Fprintf(os.Stdout, "Response from `GenerationAPI.UpdateArtifactGenerationProfile`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**profileId** | **string** | UUIDv7 identifier of a CI export profile. |

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateArtifactGenerationProfileRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **artifactGenerationProfileInput** | [**ArtifactGenerationProfileInput**](ArtifactGenerationProfileInput.md) |  |

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ValidateAtfProject

> AtfValidationResult ValidateAtfProject(ctx).AtfGenerationInput(atfGenerationInput).Execute()

Validate that an ATF project compiles



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
	atfGenerationInput := *openapiclient.NewAtfGenerationInput("ProjectName_example", "PackageName_example") // AtfGenerationInput |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GenerationAPI.ValidateAtfProject(context.Background()).AtfGenerationInput(atfGenerationInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GenerationAPI.ValidateAtfProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ValidateAtfProject`: AtfValidationResult
	fmt.Fprintf(os.Stdout, "Response from `GenerationAPI.ValidateAtfProject`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiValidateAtfProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **atfGenerationInput** | [**AtfGenerationInput**](AtfGenerationInput.md) |  |

### Return type

[**AtfValidationResult**](AtfValidationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

