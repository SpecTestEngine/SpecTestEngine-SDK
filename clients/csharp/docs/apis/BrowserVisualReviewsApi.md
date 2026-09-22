# SpecTestEngine.Sdk.Api.BrowserVisualReviewsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ExcludeBrowserVisualAreaAndRecompare**](BrowserVisualReviewsApi.md#excludebrowservisualareaandrecompare) | **POST** /browser/visual/comparisons/{comparisonId}/exclude-and-recompare | Exclude area and recompare |
| [**GetBrowserVisualArtifactContent**](BrowserVisualReviewsApi.md#getbrowservisualartifactcontent) | **GET** /browser/visual/artifacts/{artifactId}/content | Download Browser visual evidence |
| [**GetBrowserVisualComparison**](BrowserVisualReviewsApi.md#getbrowservisualcomparison) | **GET** /browser/visual/comparisons/{comparisonId} | Get a Browser visual comparison |
| [**KeepBrowserVisualAsRegression**](BrowserVisualReviewsApi.md#keepbrowservisualasregression) | **POST** /browser/visual/comparisons/{comparisonId}/keep-as-regression | Keep as regression |
| [**UseCurrentBrowserVisualAsNewBaseline**](BrowserVisualReviewsApi.md#usecurrentbrowservisualasnewbaseline) | **POST** /browser/visual/comparisons/{comparisonId}/use-current-as-new-baseline | Use current as new baseline |

<a id="excludebrowservisualareaandrecompare"></a>
# **ExcludeBrowserVisualAreaAndRecompare**
> BrowserVisualComparison ExcludeBrowserVisualAreaAndRecompare (Guid comparisonId, BrowserVisualExcludeAndRecompareRequest browserVisualExcludeAndRecompareRequest)

Exclude area and recompare

Saves normalized exclusion masks in a new assertion revision and creates a child comparison generation with the existing Browser comparator.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **comparisonId** | **Guid** | Identifier of an immutable Browser visual comparison generation. |  |
| **browserVisualExcludeAndRecompareRequest** | [**BrowserVisualExcludeAndRecompareRequest**](BrowserVisualExcludeAndRecompareRequest.md) |  |  |

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New comparison generation linked to the source and root comparisons. |  -  |
| **409** | The expected assertion revision is stale or the action id conflicts with another command. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getbrowservisualartifactcontent"></a>
# **GetBrowserVisualArtifactContent**
> System.IO.Stream GetBrowserVisualArtifactContent (Guid artifactId)

Download Browser visual evidence

Returns a retained PNG baseline, current, or diff artifact after company and project authorization.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **artifactId** | **Guid** |  |  |

### Return type

**System.IO.Stream**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PNG visual evidence subject to the configured artifact retention policy. |  -  |
| **410** | The artifact expired; comparison metadata and lineage remain available. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getbrowservisualcomparison"></a>
# **GetBrowserVisualComparison**
> BrowserVisualComparison GetBrowserVisualComparison (Guid comparisonId)

Get a Browser visual comparison

Returns one immutable comparison generation, its evidence lineage, normalized exclusions, and currently available review actions.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **comparisonId** | **Guid** | Identifier of an immutable Browser visual comparison generation. |  |

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Browser visual comparison scoped to the token company and active project. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="keepbrowservisualasregression"></a>
# **KeepBrowserVisualAsRegression**
> BrowserVisualComparison KeepBrowserVisualAsRegression (Guid comparisonId, BrowserVisualKeepRegressionRequest browserVisualKeepRegressionRequest)

Keep as regression

Confirms the mismatch as a regression without changing the active baseline or assertion exclusions.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **comparisonId** | **Guid** | Identifier of an immutable Browser visual comparison generation. |  |
| **browserVisualKeepRegressionRequest** | [**BrowserVisualKeepRegressionRequest**](BrowserVisualKeepRegressionRequest.md) |  |  |

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comparison marked as a confirmed regression. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="usecurrentbrowservisualasnewbaseline"></a>
# **UseCurrentBrowserVisualAsNewBaseline**
> BrowserVisualComparison UseCurrentBrowserVisualAsNewBaseline (Guid comparisonId, BrowserVisualPromoteBaselineRequest browserVisualPromoteBaselineRequest)

Use current as new baseline

Creates and activates a new immutable baseline revision. Historical comparison and baseline evidence remains addressable by Snapshot Timeline.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **comparisonId** | **Guid** | Identifier of an immutable Browser visual comparison generation. |  |
| **browserVisualPromoteBaselineRequest** | [**BrowserVisualPromoteBaselineRequest**](BrowserVisualPromoteBaselineRequest.md) |  |  |

### Return type

[**BrowserVisualComparison**](BrowserVisualComparison.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reviewed comparison with the applied baseline revision. |  -  |
| **409** | The expected assertion revision is stale or the action id conflicts with another command. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

