# spectestengine_sdk.CraftsmanApi

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_craftsman_run**](CraftsmanApi.md#cancel_craftsman_run) | **POST** /sentinel/request-workspaces/runs/{runId}/cancel | Cancel a queued or active Craftsman run
[**create_request_node**](CraftsmanApi.md#create_request_node) | **POST** /sentinel/request-workspaces/{workspaceId}/nodes | Add a folder or saved request
[**create_request_workspace**](CraftsmanApi.md#create_request_workspace) | **POST** /sentinel/request-workspaces | Create a request workspace
[**delete_request_node**](CraftsmanApi.md#delete_request_node) | **DELETE** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId} | Delete a folder or saved request
[**delete_request_workspace**](CraftsmanApi.md#delete_request_workspace) | **DELETE** /sentinel/request-workspaces/{workspaceId} | Delete a request workspace
[**get_craftsman_run**](CraftsmanApi.md#get_craftsman_run) | **GET** /sentinel/request-workspaces/runs/{runId} | Get Craftsman run lifecycle and evidence
[**get_craftsman_run_transcript**](CraftsmanApi.md#get_craftsman_run_transcript) | **GET** /sentinel/request-workspaces/runs/{runId}/transcript | Get a Craftsman Streaming semantic transcript
[**get_document_asset**](CraftsmanApi.md#get_document_asset) | **GET** /sentinel/document-assets/{assetId} | Resolve request attachment metadata
[**get_request_workspace**](CraftsmanApi.md#get_request_workspace) | **GET** /sentinel/request-workspaces/{workspaceId} | Get a request workspace
[**list_request_workspaces**](CraftsmanApi.md#list_request_workspaces) | **GET** /sentinel/request-workspaces/page | List request workspaces
[**queue_craftsman_streaming_run**](CraftsmanApi.md#queue_craftsman_streaming_run) | **POST** /sentinel/request-workspaces/runs/streaming | Queue a standalone bounded Streaming session
[**queue_craftsman_workflow_run**](CraftsmanApi.md#queue_craftsman_workflow_run) | **POST** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId}/runs | Queue a saved request or mixed-protocol Workflow run
[**update_request_node**](CraftsmanApi.md#update_request_node) | **PUT** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId} | Update a folder or saved request
[**update_request_workspace**](CraftsmanApi.md#update_request_workspace) | **PUT** /sentinel/request-workspaces/{workspaceId} | Replace request workspace metadata and variables
[**upload_document_asset**](CraftsmanApi.md#upload_document_asset) | **POST** /sentinel/document-assets | Upload a reusable request attachment


# **cancel_craftsman_run**
> CraftsmanRun cancel_craftsman_run(run_id)

Cancel a queued or active Craftsman run

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.craftsman_run import CraftsmanRun
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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Cancel a queued or active Craftsman run
        api_response = api_instance.cancel_craftsman_run(run_id)
        print("The response of CraftsmanApi->cancel_craftsman_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CraftsmanApi->cancel_craftsman_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**| UUIDv7 identifier of the stored run evidence. |

### Return type

[**CraftsmanRun**](CraftsmanRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated lifecycle after cooperative cancellation was requested. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_request_node**
> RequestNode create_request_node(workspace_id, request_node_input, idempotency_key=idempotency_key)

Add a folder or saved request

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.request_node import RequestNode
from spectestengine_sdk.models.request_node_input import RequestNodeInput
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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the Craftsman request workspace.
    request_node_input = spectestengine_sdk.RequestNodeInput() # RequestNodeInput |
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A caller-generated UUID retained for safe write retries where supported. (optional)

    try:
        # Add a folder or saved request
        api_response = api_instance.create_request_node(workspace_id, request_node_input, idempotency_key=idempotency_key)
        print("The response of CraftsmanApi->create_request_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CraftsmanApi->create_request_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| UUIDv7 identifier of the Craftsman request workspace. |
 **request_node_input** | [**RequestNodeInput**](RequestNodeInput.md)|  |
 **idempotency_key** | **UUID**| A caller-generated UUID retained for safe write retries where supported. | [optional]

### Return type

[**RequestNode**](RequestNode.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created workspace node. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_request_workspace**
> RequestWorkspace create_request_workspace(request_workspace_input, idempotency_key=idempotency_key)

Create a request workspace

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.request_workspace import RequestWorkspace
from spectestengine_sdk.models.request_workspace_input import RequestWorkspaceInput
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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    request_workspace_input = spectestengine_sdk.RequestWorkspaceInput() # RequestWorkspaceInput |
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A caller-generated UUID retained for safe write retries where supported. (optional)

    try:
        # Create a request workspace
        api_response = api_instance.create_request_workspace(request_workspace_input, idempotency_key=idempotency_key)
        print("The response of CraftsmanApi->create_request_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CraftsmanApi->create_request_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_workspace_input** | [**RequestWorkspaceInput**](RequestWorkspaceInput.md)|  |
 **idempotency_key** | **UUID**| A caller-generated UUID retained for safe write retries where supported. | [optional]

### Return type

[**RequestWorkspace**](RequestWorkspace.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created workspace. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_request_node**
> delete_request_node(workspace_id, node_id)

Delete a folder or saved request

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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the Craftsman request workspace.
    node_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        # Delete a folder or saved request
        api_instance.delete_request_node(workspace_id, node_id)
    except Exception as e:
        print("Exception when calling CraftsmanApi->delete_request_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| UUIDv7 identifier of the Craftsman request workspace. |
 **node_id** | **UUID**|  |

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
**204** | Workspace node deleted. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_request_workspace**
> delete_request_workspace(workspace_id)

Delete a request workspace

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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the Craftsman request workspace.

    try:
        # Delete a request workspace
        api_instance.delete_request_workspace(workspace_id)
    except Exception as e:
        print("Exception when calling CraftsmanApi->delete_request_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| UUIDv7 identifier of the Craftsman request workspace. |

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
**204** | Workspace deleted. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_craftsman_run**
> CraftsmanRun get_craftsman_run(run_id)

Get Craftsman run lifecycle and evidence

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.craftsman_run import CraftsmanRun
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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Get Craftsman run lifecycle and evidence
        api_response = api_instance.get_craftsman_run(run_id)
        print("The response of CraftsmanApi->get_craftsman_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CraftsmanApi->get_craftsman_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**| UUIDv7 identifier of the stored run evidence. |

### Return type

[**CraftsmanRun**](CraftsmanRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current lifecycle and terminal result when available. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_craftsman_run_transcript**
> object get_craftsman_run_transcript(run_id)

Get a Craftsman Streaming semantic transcript

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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Get a Craftsman Streaming semantic transcript
        api_response = api_instance.get_craftsman_run_transcript(run_id)
        print("The response of CraftsmanApi->get_craftsman_run_transcript:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CraftsmanApi->get_craftsman_run_transcript: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**| UUIDv7 identifier of the stored run evidence. |

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bounded semantic event transcript captured by Sentinel. Use the completed run result for connection, assertion, and termination evidence required by Generate Spec. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_asset**
> DocumentAssetReference get_document_asset(asset_id, field_name=field_name, content_id=content_id)

Resolve request attachment metadata

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.document_asset_reference import DocumentAssetReference
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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    asset_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    field_name = 'file' # str |  (optional) (default to 'file')
    content_id = 'content_id_example' # str |  (optional)

    try:
        # Resolve request attachment metadata
        api_response = api_instance.get_document_asset(asset_id, field_name=field_name, content_id=content_id)
        print("The response of CraftsmanApi->get_document_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CraftsmanApi->get_document_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**|  |
 **field_name** | **str**|  | [optional] [default to &#39;file&#39;]
 **content_id** | **str**|  | [optional]

### Return type

[**DocumentAssetReference**](DocumentAssetReference.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment metadata suitable for reuse in a saved request or specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_workspace**
> RequestWorkspace get_request_workspace(workspace_id)

Get a request workspace

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.request_workspace import RequestWorkspace
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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the Craftsman request workspace.

    try:
        # Get a request workspace
        api_response = api_instance.get_request_workspace(workspace_id)
        print("The response of CraftsmanApi->get_request_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CraftsmanApi->get_request_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| UUIDv7 identifier of the Craftsman request workspace. |

### Return type

[**RequestWorkspace**](RequestWorkspace.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The complete workspace tree. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_request_workspaces**
> RequestWorkspacePage list_request_workspaces(page=page, size=size, search=search)

List request workspaces

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.request_workspace_page import RequestWorkspacePage
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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)
    search = 'search_example' # str | Case-insensitive server-side search within the active project. (optional)

    try:
        # List request workspaces
        api_response = api_instance.list_request_workspaces(page=page, size=size, search=search)
        print("The response of CraftsmanApi->list_request_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CraftsmanApi->list_request_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]
 **search** | **str**| Case-insensitive server-side search within the active project. | [optional]

### Return type

[**RequestWorkspacePage**](RequestWorkspacePage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of request workspaces. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **queue_craftsman_streaming_run**
> CraftsmanRunAccepted queue_craftsman_streaming_run(craftsman_streaming_run_input)

Queue a standalone bounded Streaming session

Standalone sessions require concrete values and do not inherit Workflow variables.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.craftsman_run_accepted import CraftsmanRunAccepted
from spectestengine_sdk.models.craftsman_streaming_run_input import CraftsmanStreamingRunInput
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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    craftsman_streaming_run_input = spectestengine_sdk.CraftsmanStreamingRunInput() # CraftsmanStreamingRunInput |

    try:
        # Queue a standalone bounded Streaming session
        api_response = api_instance.queue_craftsman_streaming_run(craftsman_streaming_run_input)
        print("The response of CraftsmanApi->queue_craftsman_streaming_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CraftsmanApi->queue_craftsman_streaming_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **craftsman_streaming_run_input** | [**CraftsmanStreamingRunInput**](CraftsmanStreamingRunInput.md)|  |

### Return type

[**CraftsmanRunAccepted**](CraftsmanRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The bounded session was accepted. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **queue_craftsman_workflow_run**
> CraftsmanRunAccepted queue_craftsman_workflow_run(workspace_id, node_id, request_chain_run_input=request_chain_run_input)

Queue a saved request or mixed-protocol Workflow run

Supports REST, SOAP, GraphQL, WebSocket/WSS, SSE, gRPC Streaming, and MQTT nodes. Poll the returned run id.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.craftsman_run_accepted import CraftsmanRunAccepted
from spectestengine_sdk.models.request_chain_run_input import RequestChainRunInput
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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the Craftsman request workspace.
    node_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    request_chain_run_input = spectestengine_sdk.RequestChainRunInput() # RequestChainRunInput |  (optional)

    try:
        # Queue a saved request or mixed-protocol Workflow run
        api_response = api_instance.queue_craftsman_workflow_run(workspace_id, node_id, request_chain_run_input=request_chain_run_input)
        print("The response of CraftsmanApi->queue_craftsman_workflow_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CraftsmanApi->queue_craftsman_workflow_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| UUIDv7 identifier of the Craftsman request workspace. |
 **node_id** | **UUID**|  |
 **request_chain_run_input** | [**RequestChainRunInput**](RequestChainRunInput.md)|  | [optional]

### Return type

[**CraftsmanRunAccepted**](CraftsmanRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The bounded Craftsman run was accepted. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_request_node**
> RequestNode update_request_node(workspace_id, node_id, request_node_input)

Update a folder or saved request

Replaces the selected node definition. STREAMING requests use streamingSpec and do not accept HTTP request fields.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.request_node import RequestNode
from spectestengine_sdk.models.request_node_input import RequestNodeInput
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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the Craftsman request workspace.
    node_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    request_node_input = spectestengine_sdk.RequestNodeInput() # RequestNodeInput |

    try:
        # Update a folder or saved request
        api_response = api_instance.update_request_node(workspace_id, node_id, request_node_input)
        print("The response of CraftsmanApi->update_request_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CraftsmanApi->update_request_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| UUIDv7 identifier of the Craftsman request workspace. |
 **node_id** | **UUID**|  |
 **request_node_input** | [**RequestNodeInput**](RequestNodeInput.md)|  |

### Return type

[**RequestNode**](RequestNode.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated workspace node. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_request_workspace**
> RequestWorkspace update_request_workspace(workspace_id, request_workspace_input)

Replace request workspace metadata and variables

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.request_workspace import RequestWorkspace
from spectestengine_sdk.models.request_workspace_input import RequestWorkspaceInput
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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the Craftsman request workspace.
    request_workspace_input = spectestengine_sdk.RequestWorkspaceInput() # RequestWorkspaceInput |

    try:
        # Replace request workspace metadata and variables
        api_response = api_instance.update_request_workspace(workspace_id, request_workspace_input)
        print("The response of CraftsmanApi->update_request_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CraftsmanApi->update_request_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| UUIDv7 identifier of the Craftsman request workspace. |
 **request_workspace_input** | [**RequestWorkspaceInput**](RequestWorkspaceInput.md)|  |

### Return type

[**RequestWorkspace**](RequestWorkspace.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated workspace. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document_asset**
> DocumentAssetReference upload_document_asset(file, field_name=field_name, content_id=content_id)

Upload a reusable request attachment

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.document_asset_reference import DocumentAssetReference
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
    api_instance = spectestengine_sdk.CraftsmanApi(api_client)
    file = None # bytes |
    field_name = 'file' # str |  (optional) (default to 'file')
    content_id = 'content_id_example' # str |  (optional)

    try:
        # Upload a reusable request attachment
        api_response = api_instance.upload_document_asset(file, field_name=field_name, content_id=content_id)
        print("The response of CraftsmanApi->upload_document_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CraftsmanApi->upload_document_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytes**|  |
 **field_name** | **str**|  | [optional] [default to &#39;file&#39;]
 **content_id** | **str**|  | [optional]

### Return type

[**DocumentAssetReference**](DocumentAssetReference.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Immutable content-addressed attachment reference. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
