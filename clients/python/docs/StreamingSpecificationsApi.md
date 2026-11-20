# spectestengine_sdk.StreamingSpecificationsApi

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_streaming_specification_run**](StreamingSpecificationsApi.md#cancel_streaming_specification_run) | **POST** /test/streaming-spec/run/history/by-run-id/{runId}/cancel | Cancel an active streaming run
[**create_streaming_specification**](StreamingSpecificationsApi.md#create_streaming_specification) | **POST** /test/streaming-spec/create | Create a streaming specification
[**delete_streaming_specification**](StreamingSpecificationsApi.md#delete_streaming_specification) | **DELETE** /test/streaming-spec/by-id | Delete a streaming specification
[**get_streaming_capabilities**](StreamingSpecificationsApi.md#get_streaming_capabilities) | **GET** /engine/streaming/capabilities | Get streaming engine capabilities and enforced limits
[**get_streaming_preparation**](StreamingSpecificationsApi.md#get_streaming_preparation) | **GET** /test/streaming-spec/preparations/by-ref/{ref} | Read eligible STREAMING Prepare request metadata by stable key
[**get_streaming_specification**](StreamingSpecificationsApi.md#get_streaming_specification) | **GET** /test/streaming-spec/by-id | Get a streaming specification
[**get_streaming_specification_run**](StreamingSpecificationsApi.md#get_streaming_specification_run) | **GET** /test/streaming-spec/run/history/by-run-id/{runId} | Get streaming run state and bounded semantic evidence
[**get_streaming_specification_run_transcript**](StreamingSpecificationsApi.md#get_streaming_specification_run_transcript) | **GET** /test/streaming-spec/run/history/by-run-id/{runId}/transcript | Page a bounded streaming run transcript
[**list_streaming_preparations**](StreamingSpecificationsApi.md#list_streaming_preparations) | **GET** /test/streaming-spec/preparations | List eligible Prepare requests and output declarations
[**list_streaming_specification_runs**](StreamingSpecificationsApi.md#list_streaming_specification_runs) | **GET** /test/streaming-spec/run/page/by-spec-id/{specId} | List runs for a saved streaming specification
[**list_streaming_specifications**](StreamingSpecificationsApi.md#list_streaming_specifications) | **GET** /test/streaming-spec/page | List streaming specifications
[**preview_streaming_specification_recovery**](StreamingSpecificationsApi.md#preview_streaming_specification_recovery) | **POST** /test/streaming-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a Streaming specification version
[**restore_streaming_specification_from_run**](StreamingSpecificationsApi.md#restore_streaming_specification_from_run) | **PUT** /test/streaming-spec/recovery/{specId}/from-run/{runId}/restore | Restore a Streaming specification version
[**run_streaming_specification**](StreamingSpecificationsApi.md#run_streaming_specification) | **POST** /test/streaming-spec/run/by-id/{specId} | Queue a saved streaming specification run
[**run_streaming_specification_draft**](StreamingSpecificationsApi.md#run_streaming_specification_draft) | **POST** /test/streaming-spec/run/draft | Queue a bounded streaming specification draft run
[**test_streaming_specification_recovery_version**](StreamingSpecificationsApi.md#test_streaming_specification_recovery_version) | **POST** /test/streaming-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous Streaming specification version
[**update_streaming_specification**](StreamingSpecificationsApi.md#update_streaming_specification) | **PUT** /test/streaming-spec/by-id | Replace a streaming specification definition
[**validate_streaming_specification_draft**](StreamingSpecificationsApi.md#validate_streaming_specification_draft) | **POST** /test/streaming-spec/validate-draft | Validate and detect the transport of a streaming specification draft


# **cancel_streaming_specification_run**
> StreamingRun cancel_streaming_specification_run(run_id)

Cancel an active streaming run

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_run import StreamingRun
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Cancel an active streaming run
        api_response = api_instance.cancel_streaming_specification_run(run_id)
        print("The response of StreamingSpecificationsApi->cancel_streaming_specification_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->cancel_streaming_specification_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**| UUIDv7 identifier of the stored run evidence. |

### Return type

[**StreamingRun**](StreamingRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cancelled run, or the unchanged result when it was already terminal. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_streaming_specification**
> StreamingSpecification create_streaming_specification(spec_name, body, description=description, idempotency_key=idempotency_key)

Create a streaming specification

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_specification import StreamingSpecification
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    spec_name = 'spec_name_example' # str | User-facing specification name within the active project.
    body = 'body_example' # str |
    description = 'description_example' # str | Optional user-facing description stored with the asset. (optional)
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A caller-generated UUID retained for safe write retries where supported. (optional)

    try:
        # Create a streaming specification
        api_response = api_instance.create_streaming_specification(spec_name, body, description=description, idempotency_key=idempotency_key)
        print("The response of StreamingSpecificationsApi->create_streaming_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->create_streaming_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_name** | **str**| User-facing specification name within the active project. |
 **body** | **str**|  |
 **description** | **str**| Optional user-facing description stored with the asset. | [optional]
 **idempotency_key** | **UUID**| A caller-generated UUID retained for safe write retries where supported. | [optional]

### Return type

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The stored streaming specification and detected transport. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_streaming_specification**
> StreamingSpecification delete_streaming_specification(spec_id)

Delete a streaming specification

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_specification import StreamingSpecification
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.

    try:
        # Delete a streaming specification
        api_response = api_instance.delete_streaming_specification(spec_id)
        print("The response of StreamingSpecificationsApi->delete_streaming_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->delete_streaming_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |

### Return type

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted streaming specification. Existing run evidence remains detached and readable. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_streaming_capabilities**
> StreamingCapabilities get_streaming_capabilities()

Get streaming engine capabilities and enforced limits

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_capabilities import StreamingCapabilities
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)

    try:
        # Get streaming engine capabilities and enforced limits
        api_response = api_instance.get_streaming_capabilities()
        print("The response of StreamingSpecificationsApi->get_streaming_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->get_streaming_capabilities: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StreamingCapabilities**](StreamingCapabilities.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Supported transports, codecs, actions, expected* assertion fields, endpoint schemes, and hard limits. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_streaming_preparation**
> PreparationSummary get_streaming_preparation(ref)

Read eligible STREAMING Prepare request metadata by stable key

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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    ref = 'ref_example' # str |

    try:
        # Read eligible STREAMING Prepare request metadata by stable key
        api_response = api_instance.get_streaming_preparation(ref)
        print("The response of StreamingSpecificationsApi->get_streaming_preparation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->get_streaming_preparation: %s\n" % e)
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

# **get_streaming_specification**
> StreamingSpecification get_streaming_specification(spec_id)

Get a streaming specification

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_specification import StreamingSpecification
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.

    try:
        # Get a streaming specification
        api_response = api_instance.get_streaming_specification(spec_id)
        print("The response of StreamingSpecificationsApi->get_streaming_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->get_streaming_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |

### Return type

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested streaming specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_streaming_specification_run**
> StreamingRun get_streaming_specification_run(run_id)

Get streaming run state and bounded semantic evidence

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_run import StreamingRun
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Get streaming run state and bounded semantic evidence
        api_response = api_instance.get_streaming_specification_run(run_id)
        print("The response of StreamingSpecificationsApi->get_streaming_specification_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->get_streaming_specification_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**| UUIDv7 identifier of the stored run evidence. |

### Return type

[**StreamingRun**](StreamingRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current or terminal run metadata and evidence summary. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_streaming_specification_run_transcript**
> StreamingTranscriptPage get_streaming_specification_run_transcript(run_id, page=page, size=size)

Page a bounded streaming run transcript

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_transcript_page import StreamingTranscriptPage
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 100 # int |  (optional) (default to 100)

    try:
        # Page a bounded streaming run transcript
        api_response = api_instance.get_streaming_specification_run_transcript(run_id, page=page, size=size)
        print("The response of StreamingSpecificationsApi->get_streaming_specification_run_transcript:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->get_streaming_specification_run_transcript: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**| UUIDv7 identifier of the stored run evidence. |
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 100]

### Return type

[**StreamingTranscriptPage**](StreamingTranscriptPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One transcript page. Payload exclusions and redactions are already applied. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_streaming_preparations**
> PreparationPage list_streaming_preparations(page=page, size=size, search=search)

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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int |  (optional) (default to 20)
    search = 'search_example' # str | Case-insensitive server-side search within the active project. (optional)

    try:
        # List eligible Prepare requests and output declarations
        api_response = api_instance.list_streaming_preparations(page=page, size=size, search=search)
        print("The response of StreamingSpecificationsApi->list_streaming_preparations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->list_streaming_preparations: %s\n" % e)
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
**200** | A page of eligible STREAMING preparation sources. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_streaming_specification_runs**
> StreamingRunPage list_streaming_specification_runs(spec_id, page=page, size=size)

List runs for a saved streaming specification

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_run_page import StreamingRunPage
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)

    try:
        # List runs for a saved streaming specification
        api_response = api_instance.list_streaming_specification_runs(spec_id, page=page, size=size)
        print("The response of StreamingSpecificationsApi->list_streaming_specification_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->list_streaming_specification_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]

### Return type

[**StreamingRunPage**](StreamingRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of current and terminal streaming runs. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_streaming_specifications**
> StreamingSpecificationPage list_streaming_specifications(page=page, size=size, search=search, transport=transport)

List streaming specifications

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_specification_page import StreamingSpecificationPage
from spectestengine_sdk.models.streaming_transport import StreamingTransport
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)
    search = 'search_example' # str | Case-insensitive server-side search within the active project. (optional)
    transport = spectestengine_sdk.StreamingTransport() # StreamingTransport | Filter by streaming transport. (optional)

    try:
        # List streaming specifications
        api_response = api_instance.list_streaming_specifications(page=page, size=size, search=search, transport=transport)
        print("The response of StreamingSpecificationsApi->list_streaming_specifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->list_streaming_specifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]
 **search** | **str**| Case-insensitive server-side search within the active project. | [optional]
 **transport** | [**StreamingTransport**](.md)| Filter by streaming transport. | [optional]

### Return type

[**StreamingSpecificationPage**](StreamingSpecificationPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of WebSocket/WSS, SSE, gRPC Streaming, and MQTT specifications. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_streaming_specification_recovery**
> SpecificationRecoveryPreview preview_streaming_specification_recovery(spec_id, run_id)

Preview restoring a Streaming specification version

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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Preview restoring a Streaming specification version
        api_response = api_instance.preview_streaming_specification_recovery(spec_id, run_id)
        print("The response of StreamingSpecificationsApi->preview_streaming_specification_recovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->preview_streaming_specification_recovery: %s\n" % e)
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

# **restore_streaming_specification_from_run**
> StreamingSpecification restore_streaming_specification_from_run(spec_id, run_id)

Restore a Streaming specification version

Replaces only the current DSL content with the exact snapshot retained by a completed PASS or FAIL run. The specification id, name, description, and stable identity are preserved.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_specification import StreamingSpecification
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Restore a Streaming specification version
        api_response = api_instance.restore_streaming_specification_from_run(spec_id, run_id)
        print("The response of StreamingSpecificationsApi->restore_streaming_specification_from_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->restore_streaming_specification_from_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |
 **run_id** | **UUID**| UUIDv7 identifier of the stored run evidence. |

### Return type

[**StreamingSpecification**](StreamingSpecification.md)

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

# **run_streaming_specification**
> StreamingRunAccepted run_streaming_specification(spec_id)

Queue a saved streaming specification run

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_run_accepted import StreamingRunAccepted
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.

    try:
        # Queue a saved streaming specification run
        api_response = api_instance.run_streaming_specification(spec_id)
        print("The response of StreamingSpecificationsApi->run_streaming_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->run_streaming_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |

### Return type

[**StreamingRunAccepted**](StreamingRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Run accepted. Poll the returned status URL until the state is terminal. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_streaming_specification_draft**
> StreamingRunAccepted run_streaming_specification_draft(body, spec_name=spec_name)

Queue a bounded streaming specification draft run

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_run_accepted import StreamingRunAccepted
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    body = 'body_example' # str |
    spec_name = 'spec_name_example' # str |  (optional)

    try:
        # Queue a bounded streaming specification draft run
        api_response = api_instance.run_streaming_specification_draft(body, spec_name=spec_name)
        print("The response of StreamingSpecificationsApi->run_streaming_specification_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->run_streaming_specification_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  |
 **spec_name** | **str**|  | [optional]

### Return type

[**StreamingRunAccepted**](StreamingRunAccepted.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Run accepted. Poll statusUrl, page transcriptUrl, or POST cancelUrl. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_streaming_specification_recovery_version**
> StreamingRun test_streaming_specification_recovery_version(spec_id, run_id)

Test a previous Streaming specification version

Executes the exact DSL snapshot retained by the selected completed PASS or FAIL run against the current API without changing the saved specification.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_run import StreamingRun
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Test a previous Streaming specification version
        api_response = api_instance.test_streaming_specification_recovery_version(spec_id, run_id)
        print("The response of StreamingSpecificationsApi->test_streaming_specification_recovery_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->test_streaming_specification_recovery_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |
 **run_id** | **UUID**| UUIDv7 identifier of the stored run evidence. |

### Return type

[**StreamingRun**](StreamingRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete terminal test-run evidence for the selected version. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_streaming_specification**
> StreamingSpecification update_streaming_specification(spec_id, body, description=description)

Replace a streaming specification definition

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_specification import StreamingSpecification
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    spec_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved specification.
    body = 'body_example' # str |
    description = 'description_example' # str | Optional user-facing description stored with the asset. (optional)

    try:
        # Replace a streaming specification definition
        api_response = api_instance.update_streaming_specification(spec_id, body, description=description)
        print("The response of StreamingSpecificationsApi->update_streaming_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->update_streaming_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **UUID**| UUIDv7 identifier of the saved specification. |
 **body** | **str**|  |
 **description** | **str**| Optional user-facing description stored with the asset. | [optional]

### Return type

[**StreamingSpecification**](StreamingSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated streaming specification and newly detected transport. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_streaming_specification_draft**
> StreamingDraftValidation validate_streaming_specification_draft(body)

Validate and detect the transport of a streaming specification draft

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.streaming_draft_validation import StreamingDraftValidation
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
    api_instance = spectestengine_sdk.StreamingSpecificationsApi(api_client)
    body = 'body_example' # str |

    try:
        # Validate and detect the transport of a streaming specification draft
        api_response = api_instance.validate_streaming_specification_draft(body)
        print("The response of StreamingSpecificationsApi->validate_streaming_specification_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingSpecificationsApi->validate_streaming_specification_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  |

### Return type

[**StreamingDraftValidation**](StreamingDraftValidation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Valid draft with its detected streaming transport. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
