# spectestengine_sdk.GraphQLSpecificationsApi

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capture_graphql_specification_attachment_visual_diff**](GraphQLSpecificationsApi.md#capture_graphql_specification_attachment_visual_diff) | **POST** /test/graphql-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed GraphQL attachment assertion
[**create_graphql_specification**](GraphQLSpecificationsApi.md#create_graphql_specification) | **POST** /test/graphql-spec/create | Create a GraphQL specification
[**delete_graphql_specification**](GraphQLSpecificationsApi.md#delete_graphql_specification) | **DELETE** /test/graphql-spec/by-id | Delete a GraphQL specification
[**get_graphql_preparation**](GraphQLSpecificationsApi.md#get_graphql_preparation) | **GET** /test/graphql-spec/preparations/by-ref/{ref} | Read eligible GRAPHQL Prepare request metadata by stable key
[**get_graphql_specification**](GraphQLSpecificationsApi.md#get_graphql_specification) | **GET** /test/graphql-spec/by-id | Get a GraphQL specification
[**get_graphql_specification_run**](GraphQLSpecificationsApi.md#get_graphql_specification_run) | **GET** /test/graphql-spec/run/history/by-run-id/{runId} | Get saved GraphQL run evidence
[**list_graphql_preparations**](GraphQLSpecificationsApi.md#list_graphql_preparations) | **GET** /test/graphql-spec/preparations | List eligible Prepare requests and output declarations
[**list_graphql_specification_runs**](GraphQLSpecificationsApi.md#list_graphql_specification_runs) | **GET** /test/graphql-spec/run/page/by-spec-id/{specId} | List saved GraphQL runs
[**list_graphql_specifications**](GraphQLSpecificationsApi.md#list_graphql_specifications) | **GET** /test/graphql-spec/page | List GraphQL specifications
[**preview_graphql_specification_recovery**](GraphQLSpecificationsApi.md#preview_graphql_specification_recovery) | **POST** /test/graphql-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a GraphQL specification version
[**restore_graphql_specification_from_run**](GraphQLSpecificationsApi.md#restore_graphql_specification_from_run) | **PUT** /test/graphql-spec/recovery/{specId}/from-run/{runId}/restore | Restore a GraphQL specification version
[**run_graphql_specification**](GraphQLSpecificationsApi.md#run_graphql_specification) | **POST** /test/graphql-spec/run/by-id | Run a saved GraphQL specification
[**test_graphql_specification_recovery_version**](GraphQLSpecificationsApi.md#test_graphql_specification_recovery_version) | **POST** /test/graphql-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous GraphQL specification version
[**update_graphql_specification**](GraphQLSpecificationsApi.md#update_graphql_specification) | **PUT** /test/graphql-spec/by-id | Replace a GraphQL specification definition


# **capture_graphql_specification_attachment_visual_diff**
> SpecificationRun capture_graphql_specification_attachment_visual_diff(spec_id, document_visual_diff_capture_run_request)

Create a visual diff from a failed GraphQL attachment assertion

Explicitly reruns the saved GraphQL specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status.

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
    api_instance = spectestengine_sdk.GraphQLSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    document_visual_diff_capture_run_request = spectestengine_sdk.DocumentVisualDiffCaptureRunRequest() # DocumentVisualDiffCaptureRunRequest |

    try:
        # Create a visual diff from a failed GraphQL attachment assertion
        api_response = api_instance.capture_graphql_specification_attachment_visual_diff(spec_id, document_visual_diff_capture_run_request)
        print("The response of GraphQLSpecificationsApi->capture_graphql_specification_attachment_visual_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLSpecificationsApi->capture_graphql_specification_attachment_visual_diff: %s\n" % e)
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

# **create_graphql_specification**
> Specification create_graphql_specification(spec_name, body, description=description, idempotency_key=idempotency_key)

Create a GraphQL specification

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
    api_instance = spectestengine_sdk.GraphQLSpecificationsApi(api_client)
    spec_name = 'spec_name_example' # str | User-facing specification name within the active project.
    body = 'body_example' # str |
    description = 'description_example' # str | Optional user-facing description stored with the asset. (optional)
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A caller-generated UUID retained for safe write retries where supported. (optional)

    try:
        # Create a GraphQL specification
        api_response = api_instance.create_graphql_specification(spec_name, body, description=description, idempotency_key=idempotency_key)
        print("The response of GraphQLSpecificationsApi->create_graphql_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLSpecificationsApi->create_graphql_specification: %s\n" % e)
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
**200** | The stored GraphQL specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_graphql_specification**
> Specification delete_graphql_specification(spec_id)

Delete a GraphQL specification

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
    api_instance = spectestengine_sdk.GraphQLSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.

    try:
        # Delete a GraphQL specification
        api_response = api_instance.delete_graphql_specification(spec_id)
        print("The response of GraphQLSpecificationsApi->delete_graphql_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLSpecificationsApi->delete_graphql_specification: %s\n" % e)
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
**200** | The deleted GraphQL specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_graphql_preparation**
> PreparationSummary get_graphql_preparation(ref)

Read eligible GRAPHQL Prepare request metadata by stable key

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
    api_instance = spectestengine_sdk.GraphQLSpecificationsApi(api_client)
    ref = 'ref_example' # str |

    try:
        # Read eligible GRAPHQL Prepare request metadata by stable key
        api_response = api_instance.get_graphql_preparation(ref)
        print("The response of GraphQLSpecificationsApi->get_graphql_preparation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLSpecificationsApi->get_graphql_preparation: %s\n" % e)
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

# **get_graphql_specification**
> Specification get_graphql_specification(spec_id)

Get a GraphQL specification

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
    api_instance = spectestengine_sdk.GraphQLSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.

    try:
        # Get a GraphQL specification
        api_response = api_instance.get_graphql_specification(spec_id)
        print("The response of GraphQLSpecificationsApi->get_graphql_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLSpecificationsApi->get_graphql_specification: %s\n" % e)
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
**200** | The requested GraphQL specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_graphql_specification_run**
> SpecificationRun get_graphql_specification_run(run_id)

Get saved GraphQL run evidence

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
    api_instance = spectestengine_sdk.GraphQLSpecificationsApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Get saved GraphQL run evidence
        api_response = api_instance.get_graphql_specification_run(run_id)
        print("The response of GraphQLSpecificationsApi->get_graphql_specification_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLSpecificationsApi->get_graphql_specification_run: %s\n" % e)
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

# **list_graphql_preparations**
> PreparationPage list_graphql_preparations(page=page, size=size, search=search)

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
    api_instance = spectestengine_sdk.GraphQLSpecificationsApi(api_client)
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int |  (optional) (default to 20)
    search = 'search_example' # str | Case-insensitive server-side search within the active project. (optional)

    try:
        # List eligible Prepare requests and output declarations
        api_response = api_instance.list_graphql_preparations(page=page, size=size, search=search)
        print("The response of GraphQLSpecificationsApi->list_graphql_preparations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLSpecificationsApi->list_graphql_preparations: %s\n" % e)
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
**200** | A page of eligible GRAPHQL preparation sources. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_graphql_specification_runs**
> SpecificationRunPage list_graphql_specification_runs(spec_id, page=page, size=size)

List saved GraphQL runs

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
    api_instance = spectestengine_sdk.GraphQLSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)

    try:
        # List saved GraphQL runs
        api_response = api_instance.list_graphql_specification_runs(spec_id, page=page, size=size)
        print("The response of GraphQLSpecificationsApi->list_graphql_specification_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLSpecificationsApi->list_graphql_specification_runs: %s\n" % e)
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

# **list_graphql_specifications**
> SpecificationPage list_graphql_specifications(page=page, size=size, search=search)

List GraphQL specifications

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
    api_instance = spectestengine_sdk.GraphQLSpecificationsApi(api_client)
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)
    search = 'search_example' # str | Case-insensitive server-side search within the active project. (optional)

    try:
        # List GraphQL specifications
        api_response = api_instance.list_graphql_specifications(page=page, size=size, search=search)
        print("The response of GraphQLSpecificationsApi->list_graphql_specifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLSpecificationsApi->list_graphql_specifications: %s\n" % e)
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
**200** | A page of GraphQL specifications. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_graphql_specification_recovery**
> SpecificationRecoveryPreview preview_graphql_specification_recovery(spec_id, run_id)

Preview restoring a GraphQL specification version

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
    api_instance = spectestengine_sdk.GraphQLSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Preview restoring a GraphQL specification version
        api_response = api_instance.preview_graphql_specification_recovery(spec_id, run_id)
        print("The response of GraphQLSpecificationsApi->preview_graphql_specification_recovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLSpecificationsApi->preview_graphql_specification_recovery: %s\n" % e)
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

# **restore_graphql_specification_from_run**
> Specification restore_graphql_specification_from_run(spec_id, run_id)

Restore a GraphQL specification version

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
    api_instance = spectestengine_sdk.GraphQLSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Restore a GraphQL specification version
        api_response = api_instance.restore_graphql_specification_from_run(spec_id, run_id)
        print("The response of GraphQLSpecificationsApi->restore_graphql_specification_from_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLSpecificationsApi->restore_graphql_specification_from_run: %s\n" % e)
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

# **run_graphql_specification**
> SpecificationRun run_graphql_specification(spec_id)

Run a saved GraphQL specification

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
    api_instance = spectestengine_sdk.GraphQLSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.

    try:
        # Run a saved GraphQL specification
        api_response = api_instance.run_graphql_specification(spec_id)
        print("The response of GraphQLSpecificationsApi->run_graphql_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLSpecificationsApi->run_graphql_specification: %s\n" % e)
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

# **test_graphql_specification_recovery_version**
> SpecificationRun test_graphql_specification_recovery_version(spec_id, run_id)

Test a previous GraphQL specification version

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
    api_instance = spectestengine_sdk.GraphQLSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Test a previous GraphQL specification version
        api_response = api_instance.test_graphql_specification_recovery_version(spec_id, run_id)
        print("The response of GraphQLSpecificationsApi->test_graphql_specification_recovery_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLSpecificationsApi->test_graphql_specification_recovery_version: %s\n" % e)
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

# **update_graphql_specification**
> Specification update_graphql_specification(spec_id, body, description=description)

Replace a GraphQL specification definition

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
    api_instance = spectestengine_sdk.GraphQLSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    body = 'body_example' # str |
    description = 'description_example' # str | Optional user-facing description stored with the asset. (optional)

    try:
        # Replace a GraphQL specification definition
        api_response = api_instance.update_graphql_specification(spec_id, body, description=description)
        print("The response of GraphQLSpecificationsApi->update_graphql_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLSpecificationsApi->update_graphql_specification: %s\n" % e)
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
**200** | The updated GraphQL specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
