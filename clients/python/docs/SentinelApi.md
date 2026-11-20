# spectestengine_sdk.SentinelApi

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sentinel_check**](SentinelApi.md#create_sentinel_check) | **POST** /sentinel/checks | Create a Sentinel check
[**delete_sentinel_check**](SentinelApi.md#delete_sentinel_check) | **DELETE** /sentinel/checks/{checkId} | Delete a Sentinel check
[**enqueue_sentinel_run**](SentinelApi.md#enqueue_sentinel_run) | **POST** /sentinel/checks/{checkId}/run | Queue a Sentinel run
[**get_sentinel_check**](SentinelApi.md#get_sentinel_check) | **GET** /sentinel/checks/{checkId} | Get a Sentinel check
[**get_sentinel_dashboard_summary**](SentinelApi.md#get_sentinel_dashboard_summary) | **GET** /sentinel/dashboard/summary | Get Sentinel dashboard summary
[**get_sentinel_run**](SentinelApi.md#get_sentinel_run) | **GET** /sentinel/runs/{runId} | Get Sentinel run evidence
[**list_latest_sentinel_runs**](SentinelApi.md#list_latest_sentinel_runs) | **GET** /sentinel/runs | List latest Sentinel runs
[**list_sentinel_checks**](SentinelApi.md#list_sentinel_checks) | **GET** /sentinel/checks/page | List Sentinel checks
[**list_sentinel_dashboard_incidents**](SentinelApi.md#list_sentinel_dashboard_incidents) | **GET** /sentinel/dashboard/incidents | List recent Sentinel incidents
[**list_sentinel_linked_assets**](SentinelApi.md#list_sentinel_linked_assets) | **GET** /sentinel/checks/spec-links/page | List compact Sentinel links for one Automation asset type
[**list_sentinel_runs**](SentinelApi.md#list_sentinel_runs) | **GET** /sentinel/runs/page | List Sentinel runs
[**sample_sentinel_runs**](SentinelApi.md#sample_sentinel_runs) | **GET** /sentinel/runs/sample | Sample Sentinel runs
[**update_sentinel_check**](SentinelApi.md#update_sentinel_check) | **PUT** /sentinel/checks/{checkId} | Replace a Sentinel check configuration


# **create_sentinel_check**
> SentinelCheck create_sentinel_check(sentinel_check_input, idempotency_key=idempotency_key)

Create a Sentinel check

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.sentinel_check import SentinelCheck
from spectestengine_sdk.models.sentinel_check_input import SentinelCheckInput
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
    api_instance = spectestengine_sdk.SentinelApi(api_client)
    sentinel_check_input = spectestengine_sdk.SentinelCheckInput() # SentinelCheckInput |
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A caller-generated UUID retained for safe write retries where supported. (optional)

    try:
        # Create a Sentinel check
        api_response = api_instance.create_sentinel_check(sentinel_check_input, idempotency_key=idempotency_key)
        print("The response of SentinelApi->create_sentinel_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SentinelApi->create_sentinel_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sentinel_check_input** | [**SentinelCheckInput**](SentinelCheckInput.md)|  |
 **idempotency_key** | **UUID**| A caller-generated UUID retained for safe write retries where supported. | [optional]

### Return type

[**SentinelCheck**](SentinelCheck.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created check. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sentinel_check**
> delete_sentinel_check(check_id)

Delete a Sentinel check

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
    api_instance = spectestengine_sdk.SentinelApi(api_client)
    check_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the Sentinel check.

    try:
        # Delete a Sentinel check
        api_instance.delete_sentinel_check(check_id)
    except Exception as e:
        print("Exception when calling SentinelApi->delete_sentinel_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **UUID**| UUIDv7 identifier of the Sentinel check. |

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
**204** | Check deleted. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enqueue_sentinel_run**
> RunEnqueueResponse enqueue_sentinel_run(check_id, idempotency_key=idempotency_key, region=region)

Queue a Sentinel run

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.run_enqueue_response import RunEnqueueResponse
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
    api_instance = spectestengine_sdk.SentinelApi(api_client)
    check_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the Sentinel check.
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A caller-generated UUID retained for safe write retries where supported. (optional)
    region = 'local' # str |  (optional) (default to 'local')

    try:
        # Queue a Sentinel run
        api_response = api_instance.enqueue_sentinel_run(check_id, idempotency_key=idempotency_key, region=region)
        print("The response of SentinelApi->enqueue_sentinel_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SentinelApi->enqueue_sentinel_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **UUID**| UUIDv7 identifier of the Sentinel check. |
 **idempotency_key** | **UUID**| A caller-generated UUID retained for safe write retries where supported. | [optional]
 **region** | **str**|  | [optional] [default to &#39;local&#39;]

### Return type

[**RunEnqueueResponse**](RunEnqueueResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Queue acknowledgement and execution id. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sentinel_check**
> SentinelCheck get_sentinel_check(check_id)

Get a Sentinel check

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.sentinel_check import SentinelCheck
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
    api_instance = spectestengine_sdk.SentinelApi(api_client)
    check_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the Sentinel check.

    try:
        # Get a Sentinel check
        api_response = api_instance.get_sentinel_check(check_id)
        print("The response of SentinelApi->get_sentinel_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SentinelApi->get_sentinel_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **UUID**| UUIDv7 identifier of the Sentinel check. |

### Return type

[**SentinelCheck**](SentinelCheck.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested check. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sentinel_dashboard_summary**
> SentinelDashboardSummary get_sentinel_dashboard_summary(environment)

Get Sentinel dashboard summary

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.sentinel_dashboard_summary import SentinelDashboardSummary
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
    api_instance = spectestengine_sdk.SentinelApi(api_client)
    environment = 'environment_example' # str | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.

    try:
        # Get Sentinel dashboard summary
        api_response = api_instance.get_sentinel_dashboard_summary(environment)
        print("The response of SentinelApi->get_sentinel_dashboard_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SentinelApi->get_sentinel_dashboard_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |

### Return type

[**SentinelDashboardSummary**](SentinelDashboardSummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Environment-scoped Sentinel dashboard counters and latency summary. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sentinel_run**
> SentinelRun get_sentinel_run(run_id)

Get Sentinel run evidence

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.sentinel_run import SentinelRun
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
    api_instance = spectestengine_sdk.SentinelApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the stored run evidence.

    try:
        # Get Sentinel run evidence
        api_response = api_instance.get_sentinel_run(run_id)
        print("The response of SentinelApi->get_sentinel_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SentinelApi->get_sentinel_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**| UUIDv7 identifier of the stored run evidence. |

### Return type

[**SentinelRun**](SentinelRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run, retry attempts, response preview, and baseline evidence. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_latest_sentinel_runs**
> List[SentinelRun] list_latest_sentinel_runs(environment, size=size)

List latest Sentinel runs

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.sentinel_run import SentinelRun
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
    api_instance = spectestengine_sdk.SentinelApi(api_client)
    environment = 'environment_example' # str | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)

    try:
        # List latest Sentinel runs
        api_response = api_instance.list_latest_sentinel_runs(environment, size=size)
        print("The response of SentinelApi->list_latest_sentinel_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SentinelApi->list_latest_sentinel_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]

### Return type

[**List[SentinelRun]**](SentinelRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The latest Sentinel runs for the selected environment. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sentinel_checks**
> SentinelCheckPage list_sentinel_checks(environment, page=page, size=size, search=search)

List Sentinel checks

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.sentinel_check_page import SentinelCheckPage
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
    api_instance = spectestengine_sdk.SentinelApi(api_client)
    environment = 'environment_example' # str | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)
    search = 'search_example' # str | Case-insensitive server-side search within the active project. (optional)

    try:
        # List Sentinel checks
        api_response = api_instance.list_sentinel_checks(environment, page=page, size=size, search=search)
        print("The response of SentinelApi->list_sentinel_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SentinelApi->list_sentinel_checks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]
 **search** | **str**| Case-insensitive server-side search within the active project. | [optional]

### Return type

[**SentinelCheckPage**](SentinelCheckPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of Sentinel checks. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sentinel_dashboard_incidents**
> List[SentinelIncident] list_sentinel_dashboard_incidents(environment)

List recent Sentinel incidents

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.sentinel_incident import SentinelIncident
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
    api_instance = spectestengine_sdk.SentinelApi(api_client)
    environment = 'environment_example' # str | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.

    try:
        # List recent Sentinel incidents
        api_response = api_instance.list_sentinel_dashboard_incidents(environment)
        print("The response of SentinelApi->list_sentinel_dashboard_incidents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SentinelApi->list_sentinel_dashboard_incidents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |

### Return type

[**List[SentinelIncident]**](SentinelIncident.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recent incidents for the selected Sentinel environment. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sentinel_linked_assets**
> SentinelLinkSummaryPage list_sentinel_linked_assets(environment, check_type, page=page, size=size)

List compact Sentinel links for one Automation asset type

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.sentinel_link_summary_page import SentinelLinkSummaryPage
from spectestengine_sdk.models.sentinel_linked_asset_check_type import SentinelLinkedAssetCheckType
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
    api_instance = spectestengine_sdk.SentinelApi(api_client)
    environment = 'environment_example' # str | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
    check_type = spectestengine_sdk.SentinelLinkedAssetCheckType() # SentinelLinkedAssetCheckType | Exact Automation asset type whose Sentinel links should be returned.
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)

    try:
        # List compact Sentinel links for one Automation asset type
        api_response = api_instance.list_sentinel_linked_assets(environment, check_type, page=page, size=size)
        print("The response of SentinelApi->list_sentinel_linked_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SentinelApi->list_sentinel_linked_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |
 **check_type** | [**SentinelLinkedAssetCheckType**](.md)| Exact Automation asset type whose Sentinel links should be returned. |
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]

### Return type

[**SentinelLinkSummaryPage**](SentinelLinkSummaryPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of normalized asset names and their Sentinel link counts. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sentinel_runs**
> SentinelRunPage list_sentinel_runs(environment, page=page, size=size, check_id=check_id, status=status, sort_by=sort_by, sort_direction=sort_direction)

List Sentinel runs

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.run_status_code import RunStatusCode
from spectestengine_sdk.models.sentinel_run_page import SentinelRunPage
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
    api_instance = spectestengine_sdk.SentinelApi(api_client)
    environment = 'environment_example' # str | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)
    check_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    status = spectestengine_sdk.RunStatusCode() # RunStatusCode |  (optional)
    sort_by = 'queuedAt' # str |  (optional) (default to 'queuedAt')
    sort_direction = desc # str |  (optional) (default to desc)

    try:
        # List Sentinel runs
        api_response = api_instance.list_sentinel_runs(environment, page=page, size=size, check_id=check_id, status=status, sort_by=sort_by, sort_direction=sort_direction)
        print("The response of SentinelApi->list_sentinel_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SentinelApi->list_sentinel_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]
 **check_id** | **UUID**|  | [optional]
 **status** | [**RunStatusCode**](.md)|  | [optional]
 **sort_by** | **str**|  | [optional] [default to &#39;queuedAt&#39;]
 **sort_direction** | **str**|  | [optional] [default to desc]

### Return type

[**SentinelRunPage**](SentinelRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of Sentinel runs. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_sentinel_runs**
> List[SentinelRun] sample_sentinel_runs(environment, days=days, size=size)

Sample Sentinel runs

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.sentinel_run import SentinelRun
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
    api_instance = spectestengine_sdk.SentinelApi(api_client)
    environment = 'environment_example' # str | Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents.
    days = 30 # int |  (optional) (default to 30)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)

    try:
        # Sample Sentinel runs
        api_response = api_instance.sample_sentinel_runs(environment, days=days, size=size)
        print("The response of SentinelApi->sample_sentinel_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SentinelApi->sample_sentinel_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Environment scope used to isolate Sentinel checks, runs, dashboard metrics, and incidents. |
 **days** | **int**|  | [optional] [default to 30]
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]

### Return type

[**List[SentinelRun]**](SentinelRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A bounded sample of Sentinel runs for the selected environment. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sentinel_check**
> SentinelCheck update_sentinel_check(check_id, sentinel_check_input)

Replace a Sentinel check configuration

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.sentinel_check import SentinelCheck
from spectestengine_sdk.models.sentinel_check_input import SentinelCheckInput
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
    api_instance = spectestengine_sdk.SentinelApi(api_client)
    check_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the Sentinel check.
    sentinel_check_input = spectestengine_sdk.SentinelCheckInput() # SentinelCheckInput |

    try:
        # Replace a Sentinel check configuration
        api_response = api_instance.update_sentinel_check(check_id, sentinel_check_input)
        print("The response of SentinelApi->update_sentinel_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SentinelApi->update_sentinel_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **UUID**| UUIDv7 identifier of the Sentinel check. |
 **sentinel_check_input** | [**SentinelCheckInput**](SentinelCheckInput.md)|  |

### Return type

[**SentinelCheck**](SentinelCheck.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated check. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
