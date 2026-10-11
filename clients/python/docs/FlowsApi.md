# spectestengine_sdk.FlowsApi

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capture_flow_step_attachment_visual_diff**](FlowsApi.md#capture_flow_step_attachment_visual_diff) | **POST** /test/flow/run/by-id/{flowId}/visual-diff-captures | Create a visual diff from a failed flow-step attachment assertion
[**create_flow**](FlowsApi.md#create_flow) | **POST** /test/flow/create | Create a test flow
[**create_flow_recovery**](FlowsApi.md#create_flow_recovery) | **POST** /test/flow/run/saved/{runId}/recovery | Recover a saved run as a new Flow and new dependency copies
[**delete_flow**](FlowsApi.md#delete_flow) | **DELETE** /test/flow/by-id | Delete a test flow
[**get_flow**](FlowsApi.md#get_flow) | **GET** /test/flow/by-id/{flowId} | Get a test flow
[**get_flow_recovery_dependency**](FlowsApi.md#get_flow_recovery_dependency) | **GET** /test/flow/run/saved/{runId}/recovery/dependencies/{dependencyKey} | Inspect one retained safe dependency definition
[**get_flow_recovery_operation**](FlowsApi.md#get_flow_recovery_operation) | **GET** /test/flow/run/recovery-operations/{operationId} | Read a Flow recovery outcome without performing writes
[**get_flow_run**](FlowsApi.md#get_flow_run) | **GET** /test/flow/run/saved/{runId} | Get a saved flow run
[**list_flow_recovery_dependencies**](FlowsApi.md#list_flow_recovery_dependencies) | **GET** /test/flow/run/saved/{runId}/recovery/dependencies | List historical dependency versions for Flow recovery
[**list_flow_runs**](FlowsApi.md#list_flow_runs) | **GET** /test/flow/run/by-flow-id/{flowId}/page | List saved runs for a flow
[**list_flows**](FlowsApi.md#list_flows) | **GET** /test/flow/page | List test flows
[**preview_flow_recovery**](FlowsApi.md#preview_flow_recovery) | **GET** /test/flow/run/saved/{runId}/recovery/preview | Preview an independent Flow recovery from a saved run
[**run_flow**](FlowsApi.md#run_flow) | **POST** /test/flow/run/by-id/{flowId} | Run a saved flow
[**run_flow_batch**](FlowsApi.md#run_flow_batch) | **POST** /test/flow/run/batch | Run multiple saved flows
[**update_flow**](FlowsApi.md#update_flow) | **PUT** /test/flow/by-id | Replace a test flow


# **capture_flow_step_attachment_visual_diff**
> FlowRun capture_flow_step_attachment_visual_diff(flow_id, flow_document_visual_diff_capture_run_request)

Create a visual diff from a failed flow-step attachment assertion

Explicitly reruns the saved flow and captures one failed PDF or image response from the selected API step. The flow and attachment assertion retain their real status.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.flow_document_visual_diff_capture_run_request import FlowDocumentVisualDiffCaptureRunRequest
from spectestengine_sdk.models.flow_run import FlowRun
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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    flow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved test flow.
    flow_document_visual_diff_capture_run_request = spectestengine_sdk.FlowDocumentVisualDiffCaptureRunRequest() # FlowDocumentVisualDiffCaptureRunRequest |

    try:
        # Create a visual diff from a failed flow-step attachment assertion
        api_response = api_instance.capture_flow_step_attachment_visual_diff(flow_id, flow_document_visual_diff_capture_run_request)
        print("The response of FlowsApi->capture_flow_step_attachment_visual_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->capture_flow_step_attachment_visual_diff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **UUID**| UUIDv7 identifier of the saved test flow. |
 **flow_document_visual_diff_capture_run_request** | [**FlowDocumentVisualDiffCaptureRunRequest**](FlowDocumentVisualDiffCaptureRunRequest.md)|  |

### Return type

[**FlowRun**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete flow run evidence containing the temporary visual diff link in the selected step. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_flow**
> Flow create_flow(flow_input, format=format, idempotency_key=idempotency_key)

Create a test flow

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.content_format import ContentFormat
from spectestengine_sdk.models.flow import Flow
from spectestengine_sdk.models.flow_input import FlowInput
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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    flow_input = spectestengine_sdk.FlowInput() # FlowInput |
    format = JSON # ContentFormat | Serialization format used for the returned specification source. (optional) (default to JSON)
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A caller-generated UUID retained for safe write retries where supported. (optional)

    try:
        # Create a test flow
        api_response = api_instance.create_flow(flow_input, format=format, idempotency_key=idempotency_key)
        print("The response of FlowsApi->create_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->create_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_input** | [**FlowInput**](FlowInput.md)|  |
 **format** | [**ContentFormat**](.md)| Serialization format used for the returned specification source. | [optional] [default to JSON]
 **idempotency_key** | **UUID**| A caller-generated UUID retained for safe write retries where supported. | [optional]

### Return type

[**Flow**](Flow.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The stored flow. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_flow_recovery**
> FlowRecoveryOperation create_flow_recovery(run_id, idempotency_key, flow_recovery_input)

Recover a saved run as a new Flow and new dependency copies

Explicitly creates independent owned artifacts. Originals, snapshots and scheduled bindings are unchanged; tests are not executed. Requires current Flow create and owning specification/macro create permissions and entitlements. Keep the same key and identical body after an ambiguous response; GET status never resumes writes. Partial copies remain tracked. Agent-delegated grants are not supported.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.flow_recovery_input import FlowRecoveryInput
from spectestengine_sdk.models.flow_recovery_operation import FlowRecoveryOperation
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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    flow_recovery_input = spectestengine_sdk.FlowRecoveryInput() # FlowRecoveryInput |

    try:
        # Recover a saved run as a new Flow and new dependency copies
        api_response = api_instance.create_flow_recovery(run_id, idempotency_key, flow_recovery_input)
        print("The response of FlowsApi->create_flow_recovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->create_flow_recovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**|  |
 **idempotency_key** | **UUID**|  |
 **flow_recovery_input** | [**FlowRecoveryInput**](FlowRecoveryInput.md)|  |

### Return type

[**FlowRecoveryOperation**](FlowRecoveryOperation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmed completed operation; retries reuse its result identities. |  -  |
**202** | Accepted or unconfirmed operation. Read its status; resume only this same intent explicitly. |  * Location -  <br>  |
**409** | The request failed. |  -  |
**422** | The request failed. |  -  |
**429** | The request failed. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_flow**
> delete_flow(flow_id)

Delete a test flow

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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    flow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        # Delete a test flow
        api_instance.delete_flow(flow_id)
    except Exception as e:
        print("Exception when calling FlowsApi->delete_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **UUID**|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Flow deleted. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow**
> Flow get_flow(flow_id)

Get a test flow

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.flow import Flow
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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    flow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved test flow.

    try:
        # Get a test flow
        api_response = api_instance.get_flow(flow_id)
        print("The response of FlowsApi->get_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->get_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **UUID**| UUIDv7 identifier of the saved test flow. |

### Return type

[**Flow**](Flow.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested flow. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_recovery_dependency**
> FlowRecoveryDependencyDetail get_flow_recovery_dependency(run_id, dependency_key)

Inspect one retained safe dependency definition

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.flow_recovery_dependency_detail import FlowRecoveryDependencyDetail
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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    dependency_key = 'dependency_key_example' # str |

    try:
        # Inspect one retained safe dependency definition
        api_response = api_instance.get_flow_recovery_dependency(run_id, dependency_key)
        print("The response of FlowsApi->get_flow_recovery_dependency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->get_flow_recovery_dependency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**|  |
 **dependency_key** | **str**|  |

### Return type

[**FlowRecoveryDependencyDetail**](FlowRecoveryDependencyDetail.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Exact historical safe authoring projection, up to 4 MiB, scoped to this manifest. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_recovery_operation**
> FlowRecoveryOperation get_flow_recovery_operation(operation_id)

Read a Flow recovery outcome without performing writes

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.flow_recovery_operation import FlowRecoveryOperation
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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    operation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        # Read a Flow recovery outcome without performing writes
        api_response = api_instance.get_flow_recovery_operation(operation_id)
        print("The response of FlowsApi->get_flow_recovery_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->get_flow_recovery_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_id** | **UUID**|  |

### Return type

[**FlowRecoveryOperation**](FlowRecoveryOperation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current initiating-principal and project-scoped outcome, with no request bindings or raw dependency bodies. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_run**
> FlowRun get_flow_run(run_id)

Get a saved flow run

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.flow_run import FlowRun
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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        # Get a saved flow run
        api_response = api_instance.get_flow_run(run_id)
        print("The response of FlowsApi->get_flow_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->get_flow_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**|  |

### Return type

[**FlowRun**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete persisted flow run evidence. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_flow_recovery_dependencies**
> FlowRecoveryDependencyPage list_flow_recovery_dependencies(run_id, page=page, size=size)

List historical dependency versions for Flow recovery

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.flow_recovery_dependency_page import FlowRecoveryDependencyPage
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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int |  (optional) (default to 20)

    try:
        # List historical dependency versions for Flow recovery
        api_response = api_instance.list_flow_recovery_dependencies(run_id, page=page, size=size)
        print("The response of FlowsApi->list_flow_recovery_dependencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->list_flow_recovery_dependencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**|  |
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 20]

### Return type

[**FlowRecoveryDependencyPage**](FlowRecoveryDependencyPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary-shaped page, without nested DSL, binaries or worker authority. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_flow_runs**
> FlowRunPage list_flow_runs(flow_id, page=page, size=size)

List saved runs for a flow

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.flow_run_page import FlowRunPage
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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    flow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved test flow.
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)

    try:
        # List saved runs for a flow
        api_response = api_instance.list_flow_runs(flow_id, page=page, size=size)
        print("The response of FlowsApi->list_flow_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->list_flow_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **UUID**| UUIDv7 identifier of the saved test flow. |
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]

### Return type

[**FlowRunPage**](FlowRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of lightweight persisted flow run summaries. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_flows**
> FlowPage list_flows(page=page, size=size, search=search)

List test flows

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.flow_page import FlowPage
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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)
    search = 'search_example' # str | Case-insensitive server-side search within the active project. (optional)

    try:
        # List test flows
        api_response = api_instance.list_flows(page=page, size=size, search=search)
        print("The response of FlowsApi->list_flows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->list_flows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]
 **search** | **str**| Case-insensitive server-side search within the active project. | [optional]

### Return type

[**FlowPage**](FlowPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of flow summaries. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_flow_recovery**
> FlowRecoveryPreview preview_flow_recovery(run_id)

Preview an independent Flow recovery from a saved run

Read-only historical authoring preview. Requires current source Flow/project and dependency read access. Legacy or incomplete evidence is explicitly unavailable. Does not execute tests or create artifacts.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.flow_recovery_preview import FlowRecoveryPreview
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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        # Preview an independent Flow recovery from a saved run
        api_response = api_instance.preview_flow_recovery(run_id)
        print("The response of FlowsApi->preview_flow_recovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->preview_flow_recovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**|  |

### Return type

[**FlowRecoveryPreview**](FlowRecoveryPreview.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Eligibility, historical definition, binding requirements and bounded dependency summaries. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_flow**
> FlowRun run_flow(flow_id, watch=watch)

Run a saved flow

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.flow_run import FlowRun
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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    flow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved test flow.
    watch = False # bool | Create a browser watch token when the flow contains visible browser steps. (optional) (default to False)

    try:
        # Run a saved flow
        api_response = api_instance.run_flow(flow_id, watch=watch)
        print("The response of FlowsApi->run_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->run_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **UUID**| UUIDv7 identifier of the saved test flow. |
 **watch** | **bool**| Create a browser watch token when the flow contains visible browser steps. | [optional] [default to False]

### Return type

[**FlowRun**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete flow run evidence. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_flow_batch**
> List[FlowRun] run_flow_batch(run_flow_batch_request)

Run multiple saved flows

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.flow_run import FlowRun
from spectestengine_sdk.models.run_flow_batch_request import RunFlowBatchRequest
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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    run_flow_batch_request = spectestengine_sdk.RunFlowBatchRequest() # RunFlowBatchRequest |

    try:
        # Run multiple saved flows
        api_response = api_instance.run_flow_batch(run_flow_batch_request)
        print("The response of FlowsApi->run_flow_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->run_flow_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_flow_batch_request** | [**RunFlowBatchRequest**](RunFlowBatchRequest.md)|  |

### Return type

[**List[FlowRun]**](FlowRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete evidence for every requested flow. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flow**
> Flow update_flow(flow_id, flow_input, format=format)

Replace a test flow

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.content_format import ContentFormat
from spectestengine_sdk.models.flow import Flow
from spectestengine_sdk.models.flow_input import FlowInput
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
    api_instance = spectestengine_sdk.FlowsApi(api_client)
    flow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    flow_input = spectestengine_sdk.FlowInput() # FlowInput |
    format = JSON # ContentFormat | Serialization format used for the returned specification source. (optional) (default to JSON)

    try:
        # Replace a test flow
        api_response = api_instance.update_flow(flow_id, flow_input, format=format)
        print("The response of FlowsApi->update_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->update_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **UUID**|  |
 **flow_input** | [**FlowInput**](FlowInput.md)|  |
 **format** | [**ContentFormat**](.md)| Serialization format used for the returned specification source. | [optional] [default to JSON]

### Return type

[**Flow**](Flow.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated flow. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
