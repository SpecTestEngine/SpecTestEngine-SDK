# spectestengine_sdk.RunBatchesApi

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_run_batch**](RunBatchesApi.md#create_run_batch) | **POST** /test/run-batch/create | Create a run batch
[**get_run_batch**](RunBatchesApi.md#get_run_batch) | **GET** /test/run-batch/by-id/{batchId} | Get a run batch
[**list_run_batches**](RunBatchesApi.md#list_run_batches) | **GET** /test/run-batch/page | List run batches


# **create_run_batch**
> RunBatch create_run_batch(run_batch_input, idempotency_key=idempotency_key)

Create a run batch

Collect completed specification, UI macro, and flow runs into one immutable evidence set that can later become a snapshot baseline.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.run_batch import RunBatch
from spectestengine_sdk.models.run_batch_input import RunBatchInput
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
    api_instance = spectestengine_sdk.RunBatchesApi(api_client)
    run_batch_input = spectestengine_sdk.RunBatchInput() # RunBatchInput |
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A caller-generated UUID retained for safe write retries where supported. (optional)

    try:
        # Create a run batch
        api_response = api_instance.create_run_batch(run_batch_input, idempotency_key=idempotency_key)
        print("The response of RunBatchesApi->create_run_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunBatchesApi->create_run_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_batch_input** | [**RunBatchInput**](RunBatchInput.md)|  |
 **idempotency_key** | **UUID**| A caller-generated UUID retained for safe write retries where supported. | [optional]

### Return type

[**RunBatch**](RunBatch.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created run batch and its captured evidence items. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_batch**
> RunBatch get_run_batch(batch_id)

Get a run batch

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.run_batch import RunBatch
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
    api_instance = spectestengine_sdk.RunBatchesApi(api_client)
    batch_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved run batch.

    try:
        # Get a run batch
        api_response = api_instance.get_run_batch(batch_id)
        print("The response of RunBatchesApi->get_run_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunBatchesApi->get_run_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **UUID**| UUIDv7 identifier of the saved run batch. |

### Return type

[**RunBatch**](RunBatch.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested run batch with its captured evidence items. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_run_batches**
> RunBatchPage list_run_batches(page=page, size=size, search=search)

List run batches

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.run_batch_page import RunBatchPage
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
    api_instance = spectestengine_sdk.RunBatchesApi(api_client)
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)
    search = 'search_example' # str | Case-insensitive server-side search within the active project. (optional)

    try:
        # List run batches
        api_response = api_instance.list_run_batches(page=page, size=size, search=search)
        print("The response of RunBatchesApi->list_run_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunBatchesApi->list_run_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]
 **search** | **str**| Case-insensitive server-side search within the active project. | [optional]

### Return type

[**RunBatchPage**](RunBatchPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of run batches in the active project. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
