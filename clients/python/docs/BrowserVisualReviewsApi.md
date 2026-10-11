# spectestengine_sdk.BrowserVisualReviewsApi

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exclude_browser_visual_area_and_recompare**](BrowserVisualReviewsApi.md#exclude_browser_visual_area_and_recompare) | **POST** /browser/visual/comparisons/{comparisonId}/exclude-and-recompare | Exclude area and recompare
[**get_browser_visual_artifact_content**](BrowserVisualReviewsApi.md#get_browser_visual_artifact_content) | **GET** /browser/visual/artifacts/{artifactId}/content | Download Browser visual evidence
[**get_browser_visual_comparison**](BrowserVisualReviewsApi.md#get_browser_visual_comparison) | **GET** /browser/visual/comparisons/{comparisonId} | Get a Browser visual comparison
[**keep_browser_visual_as_regression**](BrowserVisualReviewsApi.md#keep_browser_visual_as_regression) | **POST** /browser/visual/comparisons/{comparisonId}/keep-as-regression | Keep as regression
[**use_current_browser_visual_as_new_baseline**](BrowserVisualReviewsApi.md#use_current_browser_visual_as_new_baseline) | **POST** /browser/visual/comparisons/{comparisonId}/use-current-as-new-baseline | Use current as new baseline


# **exclude_browser_visual_area_and_recompare**
> BrowserVisualComparison exclude_browser_visual_area_and_recompare(comparison_id, browser_visual_exclude_and_recompare_request)

Exclude area and recompare

Saves normalized exclusion masks in a new assertion revision and creates a child comparison generation with the existing Browser comparator.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.browser_visual_comparison import BrowserVisualComparison
from spectestengine_sdk.models.browser_visual_exclude_and_recompare_request import BrowserVisualExcludeAndRecompareRequest
from spectestengine_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.ste.software
# See configuration.py for a list of all supported configuration parameters.
configuration = spectestengine_sdk.Configuration(
    host = "https://app.ste.software"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = spectestengine_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spectestengine_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spectestengine_sdk.BrowserVisualReviewsApi(api_client)
    comparison_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Identifier of an immutable Browser visual comparison generation.
    browser_visual_exclude_and_recompare_request = spectestengine_sdk.BrowserVisualExcludeAndRecompareRequest() # BrowserVisualExcludeAndRecompareRequest |

    try:
        # Exclude area and recompare
        api_response = api_instance.exclude_browser_visual_area_and_recompare(comparison_id, browser_visual_exclude_and_recompare_request)
        print("The response of BrowserVisualReviewsApi->exclude_browser_visual_area_and_recompare:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowserVisualReviewsApi->exclude_browser_visual_area_and_recompare: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comparison_id** | **UUID**| Identifier of an immutable Browser visual comparison generation. |
 **browser_visual_exclude_and_recompare_request** | [**BrowserVisualExcludeAndRecompareRequest**](BrowserVisualExcludeAndRecompareRequest.md)|  |

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
**200** | New comparison generation linked to the source and root comparisons. |  -  |
**409** | The expected assertion revision is stale or the action id conflicts with another command. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_browser_visual_artifact_content**
> bytes get_browser_visual_artifact_content(artifact_id)

Download Browser visual evidence

Returns a retained PNG baseline, current, or diff artifact after company and project authorization.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.ste.software
# See configuration.py for a list of all supported configuration parameters.
configuration = spectestengine_sdk.Configuration(
    host = "https://app.ste.software"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = spectestengine_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spectestengine_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spectestengine_sdk.BrowserVisualReviewsApi(api_client)
    artifact_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        # Download Browser visual evidence
        api_response = api_instance.get_browser_visual_artifact_content(artifact_id)
        print("The response of BrowserVisualReviewsApi->get_browser_visual_artifact_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowserVisualReviewsApi->get_browser_visual_artifact_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **UUID**|  |

### Return type

**bytes**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PNG visual evidence subject to the configured artifact retention policy. |  -  |
**410** | The artifact expired; comparison metadata and lineage remain available. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_browser_visual_comparison**
> BrowserVisualComparison get_browser_visual_comparison(comparison_id)

Get a Browser visual comparison

Returns one immutable comparison generation, its evidence lineage, normalized exclusions, and currently available review actions.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.browser_visual_comparison import BrowserVisualComparison
from spectestengine_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.ste.software
# See configuration.py for a list of all supported configuration parameters.
configuration = spectestengine_sdk.Configuration(
    host = "https://app.ste.software"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = spectestengine_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spectestengine_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spectestengine_sdk.BrowserVisualReviewsApi(api_client)
    comparison_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Identifier of an immutable Browser visual comparison generation.

    try:
        # Get a Browser visual comparison
        api_response = api_instance.get_browser_visual_comparison(comparison_id)
        print("The response of BrowserVisualReviewsApi->get_browser_visual_comparison:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowserVisualReviewsApi->get_browser_visual_comparison: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comparison_id** | **UUID**| Identifier of an immutable Browser visual comparison generation. |

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
**200** | Browser visual comparison scoped to the token company and active project. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keep_browser_visual_as_regression**
> BrowserVisualComparison keep_browser_visual_as_regression(comparison_id, browser_visual_keep_regression_request)

Keep as regression

Confirms the mismatch as a regression without changing the active baseline or assertion exclusions.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.browser_visual_comparison import BrowserVisualComparison
from spectestengine_sdk.models.browser_visual_keep_regression_request import BrowserVisualKeepRegressionRequest
from spectestengine_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.ste.software
# See configuration.py for a list of all supported configuration parameters.
configuration = spectestengine_sdk.Configuration(
    host = "https://app.ste.software"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = spectestengine_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spectestengine_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spectestengine_sdk.BrowserVisualReviewsApi(api_client)
    comparison_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Identifier of an immutable Browser visual comparison generation.
    browser_visual_keep_regression_request = spectestengine_sdk.BrowserVisualKeepRegressionRequest() # BrowserVisualKeepRegressionRequest |

    try:
        # Keep as regression
        api_response = api_instance.keep_browser_visual_as_regression(comparison_id, browser_visual_keep_regression_request)
        print("The response of BrowserVisualReviewsApi->keep_browser_visual_as_regression:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowserVisualReviewsApi->keep_browser_visual_as_regression: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comparison_id** | **UUID**| Identifier of an immutable Browser visual comparison generation. |
 **browser_visual_keep_regression_request** | [**BrowserVisualKeepRegressionRequest**](BrowserVisualKeepRegressionRequest.md)|  |

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
**200** | Comparison marked as a confirmed regression. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **use_current_browser_visual_as_new_baseline**
> BrowserVisualComparison use_current_browser_visual_as_new_baseline(comparison_id, browser_visual_promote_baseline_request)

Use current as new baseline

Creates and activates a new immutable baseline revision. Historical comparison and baseline evidence remains addressable by Snapshot Timeline.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.browser_visual_comparison import BrowserVisualComparison
from spectestengine_sdk.models.browser_visual_promote_baseline_request import BrowserVisualPromoteBaselineRequest
from spectestengine_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.ste.software
# See configuration.py for a list of all supported configuration parameters.
configuration = spectestengine_sdk.Configuration(
    host = "https://app.ste.software"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = spectestengine_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spectestengine_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spectestengine_sdk.BrowserVisualReviewsApi(api_client)
    comparison_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Identifier of an immutable Browser visual comparison generation.
    browser_visual_promote_baseline_request = spectestengine_sdk.BrowserVisualPromoteBaselineRequest() # BrowserVisualPromoteBaselineRequest |

    try:
        # Use current as new baseline
        api_response = api_instance.use_current_browser_visual_as_new_baseline(comparison_id, browser_visual_promote_baseline_request)
        print("The response of BrowserVisualReviewsApi->use_current_browser_visual_as_new_baseline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowserVisualReviewsApi->use_current_browser_visual_as_new_baseline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comparison_id** | **UUID**| Identifier of an immutable Browser visual comparison generation. |
 **browser_visual_promote_baseline_request** | [**BrowserVisualPromoteBaselineRequest**](BrowserVisualPromoteBaselineRequest.md)|  |

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
**200** | Reviewed comparison with the applied baseline revision. |  -  |
**409** | The expected assertion revision is stale or the action id conflicts with another command. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
