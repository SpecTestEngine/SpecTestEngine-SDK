# spectestengine_sdk.RESTSpecificationsApi

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capture_rest_specification_attachment_visual_diff**](RESTSpecificationsApi.md#capture_rest_specification_attachment_visual_diff) | **POST** /test/rest-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed REST attachment assertion
[**create_rest_specification**](RESTSpecificationsApi.md#create_rest_specification) | **POST** /test/rest-spec/create | Create a REST specification
[**delete_rest_specification**](RESTSpecificationsApi.md#delete_rest_specification) | **DELETE** /test/rest-spec/by-id | Delete a REST specification
[**get_rest_specification**](RESTSpecificationsApi.md#get_rest_specification) | **GET** /test/rest-spec/by-id | Get a REST specification
[**get_rest_specification_run**](RESTSpecificationsApi.md#get_rest_specification_run) | **GET** /test/rest-spec/run/history/by-run-id/{runId} | Get saved REST run evidence
[**list_rest_specification_runs**](RESTSpecificationsApi.md#list_rest_specification_runs) | **GET** /test/rest-spec/run/page/by-spec-id/{specId} | List saved REST runs
[**list_rest_specifications**](RESTSpecificationsApi.md#list_rest_specifications) | **GET** /test/rest-spec/page | List REST specifications
[**preview_rest_specification_recovery**](RESTSpecificationsApi.md#preview_rest_specification_recovery) | **POST** /test/rest-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a REST specification version
[**restore_rest_specification_from_run**](RESTSpecificationsApi.md#restore_rest_specification_from_run) | **PUT** /test/rest-spec/recovery/{specId}/from-run/{runId}/restore | Restore a REST specification version
[**run_rest_specification**](RESTSpecificationsApi.md#run_rest_specification) | **POST** /test/rest-spec/run/by-id | Run a saved REST specification
[**test_rest_specification_recovery_version**](RESTSpecificationsApi.md#test_rest_specification_recovery_version) | **POST** /test/rest-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous REST specification version
[**update_rest_specification**](RESTSpecificationsApi.md#update_rest_specification) | **PUT** /test/rest-spec/by-id | Replace a REST specification definition


# **capture_rest_specification_attachment_visual_diff**
> SpecificationRun capture_rest_specification_attachment_visual_diff(spec_id, document_visual_diff_capture_run_request)

Create a visual diff from a failed REST attachment assertion

Explicitly reruns the saved REST specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status; no visual-diff fallback changes the test result.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.document_visual_diff_capture_run_request import DocumentVisualDiffCaptureRunRequest
from spectestengine_sdk.models.specification_run import SpecificationRun
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
    api_instance = spectestengine_sdk.RESTSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    document_visual_diff_capture_run_request = spectestengine_sdk.DocumentVisualDiffCaptureRunRequest() # DocumentVisualDiffCaptureRunRequest |

    try:
        # Create a visual diff from a failed REST attachment assertion
        api_response = api_instance.capture_rest_specification_attachment_visual_diff(spec_id, document_visual_diff_capture_run_request)
        print("The response of RESTSpecificationsApi->capture_rest_specification_attachment_visual_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RESTSpecificationsApi->capture_rest_specification_attachment_visual_diff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |
 **document_visual_diff_capture_run_request** | [**DocumentVisualDiffCaptureRunRequest**](DocumentVisualDiffCaptureRunRequest.md)|  |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete failed run evidence containing the temporary visual diff link. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rest_specification**
> Specification create_rest_specification(spec_name, body, description=description, idempotency_key=idempotency_key)

Create a REST specification

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.specification import Specification
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
    api_instance = spectestengine_sdk.RESTSpecificationsApi(api_client)
    spec_name = 'spec_name_example' # str | User-facing specification name within the active project.
    body = 'body_example' # str |
    description = 'description_example' # str | Optional user-facing description stored with the asset. (optional)
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A caller-generated UUID retained for safe write retries where supported. (optional)

    try:
        # Create a REST specification
        api_response = api_instance.create_rest_specification(spec_name, body, description=description, idempotency_key=idempotency_key)
        print("The response of RESTSpecificationsApi->create_rest_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RESTSpecificationsApi->create_rest_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_name** | **str**| User-facing specification name within the active project. |
 **body** | **str**|  |
 **description** | **str**| Optional user-facing description stored with the asset. | [optional]
 **idempotency_key** | **UUID**| A caller-generated UUID retained for safe write retries where supported. | [optional]

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The stored REST specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rest_specification**
> Specification delete_rest_specification(spec_id)

Delete a REST specification

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.specification import Specification
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
    api_instance = spectestengine_sdk.RESTSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.

    try:
        # Delete a REST specification
        api_response = api_instance.delete_rest_specification(spec_id)
        print("The response of RESTSpecificationsApi->delete_rest_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RESTSpecificationsApi->delete_rest_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted REST specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rest_specification**
> Specification get_rest_specification(spec_id)

Get a REST specification

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.specification import Specification
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
    api_instance = spectestengine_sdk.RESTSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.

    try:
        # Get a REST specification
        api_response = api_instance.get_rest_specification(spec_id)
        print("The response of RESTSpecificationsApi->get_rest_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RESTSpecificationsApi->get_rest_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested REST specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rest_specification_run**
> SpecificationRun get_rest_specification_run(run_id)

Get saved REST run evidence

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.specification_run import SpecificationRun
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
    api_instance = spectestengine_sdk.RESTSpecificationsApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Get saved REST run evidence
        api_response = api_instance.get_rest_specification_run(run_id)
        print("The response of RESTSpecificationsApi->get_rest_specification_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RESTSpecificationsApi->get_rest_specification_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**| UUIDv7 identifier of the stored run evidence. |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete saved run evidence. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rest_specification_runs**
> SpecificationRunPage list_rest_specification_runs(spec_id, page=page, size=size)

List saved REST runs

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.specification_run_page import SpecificationRunPage
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
    api_instance = spectestengine_sdk.RESTSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)

    try:
        # List saved REST runs
        api_response = api_instance.list_rest_specification_runs(spec_id, page=page, size=size)
        print("The response of RESTSpecificationsApi->list_rest_specification_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RESTSpecificationsApi->list_rest_specification_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]

### Return type

[**SpecificationRunPage**](SpecificationRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of run summaries. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rest_specifications**
> SpecificationPage list_rest_specifications(page=page, size=size, search=search)

List REST specifications

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.specification_page import SpecificationPage
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
    api_instance = spectestengine_sdk.RESTSpecificationsApi(api_client)
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)
    search = 'search_example' # str | Case-insensitive server-side search within the active project. (optional)

    try:
        # List REST specifications
        api_response = api_instance.list_rest_specifications(page=page, size=size, search=search)
        print("The response of RESTSpecificationsApi->list_rest_specifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RESTSpecificationsApi->list_rest_specifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]
 **search** | **str**| Case-insensitive server-side search within the active project. | [optional]

### Return type

[**SpecificationPage**](SpecificationPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of REST specifications. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_rest_specification_recovery**
> SpecificationRecoveryPreview preview_rest_specification_recovery(spec_id, run_id)

Preview restoring a REST specification version

Compares the current specification with the exact DSL snapshot retained by a completed PASS or FAIL run. No expectations are regenerated.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.specification_recovery_preview import SpecificationRecoveryPreview
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
    api_instance = spectestengine_sdk.RESTSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Preview restoring a REST specification version
        api_response = api_instance.preview_rest_specification_recovery(spec_id, run_id)
        print("The response of RESTSpecificationsApi->preview_rest_specification_recovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RESTSpecificationsApi->preview_rest_specification_recovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |
 **run_id** | **UUID**| UUIDv7 identifier of the stored run evidence. |

### Return type

[**SpecificationRecoveryPreview**](SpecificationRecoveryPreview.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Definition-only recovery preview. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_rest_specification_from_run**
> Specification restore_rest_specification_from_run(spec_id, run_id)

Restore a REST specification version

Replaces only the current DSL content with the exact snapshot retained by a completed PASS or FAIL run. The specification id, name, description, and stable identity are preserved.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.specification import Specification
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
    api_instance = spectestengine_sdk.RESTSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Restore a REST specification version
        api_response = api_instance.restore_rest_specification_from_run(spec_id, run_id)
        print("The response of RESTSpecificationsApi->restore_rest_specification_from_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RESTSpecificationsApi->restore_rest_specification_from_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |
 **run_id** | **UUID**| UUIDv7 identifier of the stored run evidence. |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Restored specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_rest_specification**
> SpecificationRun run_rest_specification(spec_id)

Run a saved REST specification

Starts and completes one synchronous specification execution.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.specification_run import SpecificationRun
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
    api_instance = spectestengine_sdk.RESTSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.

    try:
        # Run a saved REST specification
        api_response = api_instance.run_rest_specification(spec_id)
        print("The response of RESTSpecificationsApi->run_rest_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RESTSpecificationsApi->run_rest_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete run evidence. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_rest_specification_recovery_version**
> SpecificationRun test_rest_specification_recovery_version(spec_id, run_id)

Test a previous REST specification version

Executes the exact DSL snapshot retained by the selected completed PASS or FAIL run against the current API without changing the saved specification.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.specification_run import SpecificationRun
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
    api_instance = spectestengine_sdk.RESTSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Test a previous REST specification version
        api_response = api_instance.test_rest_specification_recovery_version(spec_id, run_id)
        print("The response of RESTSpecificationsApi->test_rest_specification_recovery_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RESTSpecificationsApi->test_rest_specification_recovery_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |
 **run_id** | **UUID**| UUIDv7 identifier of the stored run evidence. |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete test-run evidence for the selected version. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rest_specification**
> Specification update_rest_specification(spec_id, body, description=description)

Replace a REST specification definition

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.specification import Specification
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
    api_instance = spectestengine_sdk.RESTSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    body = 'body_example' # str |
    description = 'description_example' # str | Optional user-facing description stored with the asset. (optional)

    try:
        # Replace a REST specification definition
        api_response = api_instance.update_rest_specification(spec_id, body, description=description)
        print("The response of RESTSpecificationsApi->update_rest_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RESTSpecificationsApi->update_rest_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |
 **body** | **str**|  |
 **description** | **str**| Optional user-facing description stored with the asset. | [optional]

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated REST specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
