# spectestengine_sdk.DocumentVisualDiffsApi

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_document_visual_diff**](DocumentVisualDiffsApi.md#get_document_visual_diff) | **GET** /browser/visual/document-diffs/{visualDiffId} | Get a visual document diff
[**get_document_visual_diff_artifact**](DocumentVisualDiffsApi.md#get_document_visual_diff_artifact) | **GET** /browser/visual/document-diffs/{visualDiffId}/artifacts/{artifactId} | Download a rendered visual diff page
[**prepare_document_visual_diff_baseline**](DocumentVisualDiffsApi.md#prepare_document_visual_diff_baseline) | **POST** /browser/visual/document-diffs/{visualDiffId}/baseline | Preview or create an attachment baseline update draft
[**regenerate_document_visual_diff**](DocumentVisualDiffsApi.md#regenerate_document_visual_diff) | **POST** /browser/visual/document-diffs/{visualDiffId}/regenerate | Regenerate a visual document diff
[**upload_document_visual_diff_expected**](DocumentVisualDiffsApi.md#upload_document_visual_diff_expected) | **POST** /browser/visual/document-diffs/{visualDiffId}/expected | Upload a reference document and create a diff generation


# **get_document_visual_diff**
> DocumentVisualDiff get_document_visual_diff(visual_diff_id)

Get a visual document diff

Returns the protected viewer URL, TTL, immutable generations, and page-level artifact references.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.document_visual_diff import DocumentVisualDiff
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
    api_instance = spectestengine_sdk.DocumentVisualDiffsApi(api_client)
    visual_diff_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of an organization-scoped visual document diff session.

    try:
        # Get a visual document diff
        api_response = api_instance.get_document_visual_diff(visual_diff_id)
        print("The response of DocumentVisualDiffsApi->get_document_visual_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentVisualDiffsApi->get_document_visual_diff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visual_diff_id** | **UUID**| UUIDv7 identifier of an organization-scoped visual document diff session. |

### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Visual diff metadata scoped to the token company and active project. |  -  |
**410** | Derived visual artifacts expired; source run metadata remains available. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_visual_diff_artifact**
> bytes get_document_visual_diff_artifact(visual_diff_id, artifact_id)

Download a rendered visual diff page

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
    api_instance = spectestengine_sdk.DocumentVisualDiffsApi(api_client)
    visual_diff_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of an organization-scoped visual document diff session.
    artifact_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        # Download a rendered visual diff page
        api_response = api_instance.get_document_visual_diff_artifact(visual_diff_id, artifact_id)
        print("The response of DocumentVisualDiffsApi->get_document_visual_diff_artifact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentVisualDiffsApi->get_document_visual_diff_artifact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visual_diff_id** | **UUID**| UUIDv7 identifier of an organization-scoped visual document diff session. |
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
**200** | Decrypted PNG page. The encrypted derivative remains subject to the diagnostic TTL. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prepare_document_visual_diff_baseline**
> DocumentVisualDiffBaselinePreview prepare_document_visual_diff_baseline(visual_diff_id, document_visual_diff_baseline_request)

Preview or create an attachment baseline update draft

Never silently overwrites a specification. Send confirm=false first, then confirm=true only after review.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.document_visual_diff_baseline_preview import DocumentVisualDiffBaselinePreview
from spectestengine_sdk.models.document_visual_diff_baseline_request import DocumentVisualDiffBaselineRequest
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
    api_instance = spectestengine_sdk.DocumentVisualDiffsApi(api_client)
    visual_diff_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of an organization-scoped visual document diff session.
    document_visual_diff_baseline_request = spectestengine_sdk.DocumentVisualDiffBaselineRequest() # DocumentVisualDiffBaselineRequest |

    try:
        # Preview or create an attachment baseline update draft
        api_response = api_instance.prepare_document_visual_diff_baseline(visual_diff_id, document_visual_diff_baseline_request)
        print("The response of DocumentVisualDiffsApi->prepare_document_visual_diff_baseline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentVisualDiffsApi->prepare_document_visual_diff_baseline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visual_diff_id** | **UUID**| UUIDv7 identifier of an organization-scoped visual document diff session. |
 **document_visual_diff_baseline_request** | [**DocumentVisualDiffBaselineRequest**](DocumentVisualDiffBaselineRequest.md)|  |

### Return type

[**DocumentVisualDiffBaselinePreview**](DocumentVisualDiffBaselinePreview.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Baseline hash/fingerprint preview or confirmed update draft. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_document_visual_diff**
> DocumentVisualDiff regenerate_document_visual_diff(visual_diff_id, document_visual_diff_regenerate_request=document_visual_diff_regenerate_request)

Regenerate a visual document diff

Creates an immutable generation from the existing rendered pages with new comparison settings and normalized visual exclusion regions.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.document_visual_diff import DocumentVisualDiff
from spectestengine_sdk.models.document_visual_diff_regenerate_request import DocumentVisualDiffRegenerateRequest
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
    api_instance = spectestengine_sdk.DocumentVisualDiffsApi(api_client)
    visual_diff_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of an organization-scoped visual document diff session.
    document_visual_diff_regenerate_request = spectestengine_sdk.DocumentVisualDiffRegenerateRequest() # DocumentVisualDiffRegenerateRequest |  (optional)

    try:
        # Regenerate a visual document diff
        api_response = api_instance.regenerate_document_visual_diff(visual_diff_id, document_visual_diff_regenerate_request=document_visual_diff_regenerate_request)
        print("The response of DocumentVisualDiffsApi->regenerate_document_visual_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentVisualDiffsApi->regenerate_document_visual_diff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visual_diff_id** | **UUID**| UUIDv7 identifier of an organization-scoped visual document diff session. |
 **document_visual_diff_regenerate_request** | [**DocumentVisualDiffRegenerateRequest**](DocumentVisualDiffRegenerateRequest.md)|  | [optional]

### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Visual diff with a new current generation. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document_visual_diff_expected**
> DocumentVisualDiff upload_document_visual_diff_expected(visual_diff_id, expected, color_threshold=color_threshold)

Upload a reference document and create a diff generation

The uploaded PDF or image is rendered in memory and discarded. Only encrypted page images and diff metadata remain until TTL expiry.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.document_visual_diff import DocumentVisualDiff
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
    api_instance = spectestengine_sdk.DocumentVisualDiffsApi(api_client)
    visual_diff_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of an organization-scoped visual document diff session.
    expected = None # bytes |
    color_threshold = 24 # float |  (optional) (default to 24)

    try:
        # Upload a reference document and create a diff generation
        api_response = api_instance.upload_document_visual_diff_expected(visual_diff_id, expected, color_threshold=color_threshold)
        print("The response of DocumentVisualDiffsApi->upload_document_visual_diff_expected:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentVisualDiffsApi->upload_document_visual_diff_expected: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visual_diff_id** | **UUID**| UUIDv7 identifier of an organization-scoped visual document diff session. |
 **expected** | **bytes**|  |
 **color_threshold** | **float**|  | [optional] [default to 24]

### Return type

[**DocumentVisualDiff**](DocumentVisualDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The visual diff with a new current generation. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

