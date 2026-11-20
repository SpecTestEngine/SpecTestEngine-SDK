# spectestengine_sdk.SOAPSpecificationsApi

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capture_soap_specification_attachment_visual_diff**](SOAPSpecificationsApi.md#capture_soap_specification_attachment_visual_diff) | **POST** /test/soap-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed SOAP attachment assertion
[**create_soap_specification**](SOAPSpecificationsApi.md#create_soap_specification) | **POST** /test/soap-spec/create | Create a SOAP specification
[**delete_soap_specification**](SOAPSpecificationsApi.md#delete_soap_specification) | **DELETE** /test/soap-spec/by-id | Delete a SOAP specification
[**get_soap_preparation**](SOAPSpecificationsApi.md#get_soap_preparation) | **GET** /test/soap-spec/preparations/by-ref/{ref} | Read eligible SOAP Prepare request metadata by stable key
[**get_soap_specification**](SOAPSpecificationsApi.md#get_soap_specification) | **GET** /test/soap-spec/by-id | Get a SOAP specification
[**get_soap_specification_run**](SOAPSpecificationsApi.md#get_soap_specification_run) | **GET** /test/soap-spec/run/history/by-run-id/{runId} | Get saved SOAP run evidence
[**list_soap_preparations**](SOAPSpecificationsApi.md#list_soap_preparations) | **GET** /test/soap-spec/preparations | List eligible Prepare requests and output declarations
[**list_soap_specification_runs**](SOAPSpecificationsApi.md#list_soap_specification_runs) | **GET** /test/soap-spec/run/page/by-spec-id/{specId} | List saved SOAP runs
[**list_soap_specifications**](SOAPSpecificationsApi.md#list_soap_specifications) | **GET** /test/soap-spec/page | List SOAP specifications
[**preview_soap_specification_recovery**](SOAPSpecificationsApi.md#preview_soap_specification_recovery) | **POST** /test/soap-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a SOAP specification version
[**restore_soap_specification_from_run**](SOAPSpecificationsApi.md#restore_soap_specification_from_run) | **PUT** /test/soap-spec/recovery/{specId}/from-run/{runId}/restore | Restore a SOAP specification version
[**run_soap_specification**](SOAPSpecificationsApi.md#run_soap_specification) | **POST** /test/soap-spec/run/by-id | Run a saved SOAP specification
[**test_soap_specification_recovery_version**](SOAPSpecificationsApi.md#test_soap_specification_recovery_version) | **POST** /test/soap-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous SOAP specification version
[**update_soap_specification**](SOAPSpecificationsApi.md#update_soap_specification) | **PUT** /test/soap-spec/by-id | Replace a SOAP specification definition


# **capture_soap_specification_attachment_visual_diff**
> SpecificationRun capture_soap_specification_attachment_visual_diff(spec_id, document_visual_diff_capture_run_request)

Create a visual diff from a failed SOAP attachment assertion

Explicitly reruns the saved SOAP specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status.

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
    api_instance = spectestengine_sdk.SOAPSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    document_visual_diff_capture_run_request = spectestengine_sdk.DocumentVisualDiffCaptureRunRequest() # DocumentVisualDiffCaptureRunRequest |

    try:
        # Create a visual diff from a failed SOAP attachment assertion
        api_response = api_instance.capture_soap_specification_attachment_visual_diff(spec_id, document_visual_diff_capture_run_request)
        print("The response of SOAPSpecificationsApi->capture_soap_specification_attachment_visual_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SOAPSpecificationsApi->capture_soap_specification_attachment_visual_diff: %s\n" % e)
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

# **create_soap_specification**
> Specification create_soap_specification(spec_name, body, description=description, idempotency_key=idempotency_key)

Create a SOAP specification

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
    api_instance = spectestengine_sdk.SOAPSpecificationsApi(api_client)
    spec_name = 'spec_name_example' # str | User-facing specification name within the active project.
    body = 'body_example' # str |
    description = 'description_example' # str | Optional user-facing description stored with the asset. (optional)
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A caller-generated UUID retained for safe write retries where supported. (optional)

    try:
        # Create a SOAP specification
        api_response = api_instance.create_soap_specification(spec_name, body, description=description, idempotency_key=idempotency_key)
        print("The response of SOAPSpecificationsApi->create_soap_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SOAPSpecificationsApi->create_soap_specification: %s\n" % e)
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
**200** | The stored SOAP specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_soap_specification**
> Specification delete_soap_specification(spec_id)

Delete a SOAP specification

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
    api_instance = spectestengine_sdk.SOAPSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.

    try:
        # Delete a SOAP specification
        api_response = api_instance.delete_soap_specification(spec_id)
        print("The response of SOAPSpecificationsApi->delete_soap_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SOAPSpecificationsApi->delete_soap_specification: %s\n" % e)
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
**200** | The deleted SOAP specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_soap_preparation**
> PreparationSummary get_soap_preparation(ref)

Read eligible SOAP Prepare request metadata by stable key

Same-company current-read metadata only; no definition or runtime values. Missing, unmarked or inaccessible sources cannot be selected.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.preparation_summary import PreparationSummary
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
    api_instance = spectestengine_sdk.SOAPSpecificationsApi(api_client)
    ref = 'ref_example' # str |

    try:
        # Read eligible SOAP Prepare request metadata by stable key
        api_response = api_instance.get_soap_preparation(ref)
        print("The response of SOAPSpecificationsApi->get_soap_preparation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SOAPSpecificationsApi->get_soap_preparation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**|  |

### Return type

[**PreparationSummary**](PreparationSummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The eligible source and its declared output variables. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_soap_specification**
> Specification get_soap_specification(spec_id)

Get a SOAP specification

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
    api_instance = spectestengine_sdk.SOAPSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.

    try:
        # Get a SOAP specification
        api_response = api_instance.get_soap_specification(spec_id)
        print("The response of SOAPSpecificationsApi->get_soap_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SOAPSpecificationsApi->get_soap_specification: %s\n" % e)
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
**200** | The requested SOAP specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_soap_specification_run**
> SpecificationRun get_soap_specification_run(run_id)

Get saved SOAP run evidence

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
    api_instance = spectestengine_sdk.SOAPSpecificationsApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Get saved SOAP run evidence
        api_response = api_instance.get_soap_specification_run(run_id)
        print("The response of SOAPSpecificationsApi->get_soap_specification_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SOAPSpecificationsApi->get_soap_specification_run: %s\n" % e)
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

# **list_soap_preparations**
> PreparationPage list_soap_preparations(page=page, size=size, search=search)

List eligible Prepare requests and output declarations

Same-company paginated metadata only. Values and full specification definitions are never included. The selected protocol and stableKey are used as preparation.protocol and preparation.ref in the consumer DSL. Any native protocol can prepare any other protocol.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.preparation_page import PreparationPage
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
    api_instance = spectestengine_sdk.SOAPSpecificationsApi(api_client)
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int |  (optional) (default to 20)
    search = 'search_example' # str | Case-insensitive server-side search within the active project. (optional)

    try:
        # List eligible Prepare requests and output declarations
        api_response = api_instance.list_soap_preparations(page=page, size=size, search=search)
        print("The response of SOAPSpecificationsApi->list_soap_preparations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SOAPSpecificationsApi->list_soap_preparations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 20]
 **search** | **str**| Case-insensitive server-side search within the active project. | [optional]

### Return type

[**PreparationPage**](PreparationPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of eligible SOAP preparation sources. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_soap_specification_runs**
> SpecificationRunPage list_soap_specification_runs(spec_id, page=page, size=size)

List saved SOAP runs

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
    api_instance = spectestengine_sdk.SOAPSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)

    try:
        # List saved SOAP runs
        api_response = api_instance.list_soap_specification_runs(spec_id, page=page, size=size)
        print("The response of SOAPSpecificationsApi->list_soap_specification_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SOAPSpecificationsApi->list_soap_specification_runs: %s\n" % e)
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

# **list_soap_specifications**
> SpecificationPage list_soap_specifications(page=page, size=size, search=search)

List SOAP specifications

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
    api_instance = spectestengine_sdk.SOAPSpecificationsApi(api_client)
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)
    search = 'search_example' # str | Case-insensitive server-side search within the active project. (optional)

    try:
        # List SOAP specifications
        api_response = api_instance.list_soap_specifications(page=page, size=size, search=search)
        print("The response of SOAPSpecificationsApi->list_soap_specifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SOAPSpecificationsApi->list_soap_specifications: %s\n" % e)
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
**200** | A page of SOAP specifications. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_soap_specification_recovery**
> SpecificationRecoveryPreview preview_soap_specification_recovery(spec_id, run_id)

Preview restoring a SOAP specification version

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
    api_instance = spectestengine_sdk.SOAPSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Preview restoring a SOAP specification version
        api_response = api_instance.preview_soap_specification_recovery(spec_id, run_id)
        print("The response of SOAPSpecificationsApi->preview_soap_specification_recovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SOAPSpecificationsApi->preview_soap_specification_recovery: %s\n" % e)
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

# **restore_soap_specification_from_run**
> Specification restore_soap_specification_from_run(spec_id, run_id)

Restore a SOAP specification version

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
    api_instance = spectestengine_sdk.SOAPSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Restore a SOAP specification version
        api_response = api_instance.restore_soap_specification_from_run(spec_id, run_id)
        print("The response of SOAPSpecificationsApi->restore_soap_specification_from_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SOAPSpecificationsApi->restore_soap_specification_from_run: %s\n" % e)
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

# **run_soap_specification**
> SpecificationRun run_soap_specification(spec_id)

Run a saved SOAP specification

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
    api_instance = spectestengine_sdk.SOAPSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.

    try:
        # Run a saved SOAP specification
        api_response = api_instance.run_soap_specification(spec_id)
        print("The response of SOAPSpecificationsApi->run_soap_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SOAPSpecificationsApi->run_soap_specification: %s\n" % e)
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

# **test_soap_specification_recovery_version**
> SpecificationRun test_soap_specification_recovery_version(spec_id, run_id)

Test a previous SOAP specification version

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
    api_instance = spectestengine_sdk.SOAPSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Test a previous SOAP specification version
        api_response = api_instance.test_soap_specification_recovery_version(spec_id, run_id)
        print("The response of SOAPSpecificationsApi->test_soap_specification_recovery_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SOAPSpecificationsApi->test_soap_specification_recovery_version: %s\n" % e)
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

# **update_soap_specification**
> Specification update_soap_specification(spec_id, body, description=description)

Replace a SOAP specification definition

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
    api_instance = spectestengine_sdk.SOAPSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    body = 'body_example' # str |
    description = 'description_example' # str | Optional user-facing description stored with the asset. (optional)

    try:
        # Replace a SOAP specification definition
        api_response = api_instance.update_soap_specification(spec_id, body, description=description)
        print("The response of SOAPSpecificationsApi->update_soap_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SOAPSpecificationsApi->update_soap_specification: %s\n" % e)
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
**200** | The updated SOAP specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
