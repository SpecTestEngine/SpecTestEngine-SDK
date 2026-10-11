# spectestengine_sdk.SnapshotsApi

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compare_snapshot_step**](SnapshotsApi.md#compare_snapshot_step) | **POST** /test/snapshot/diff/step | Compare snapshot step payloads
[**compare_snapshot_to_run_batch**](SnapshotsApi.md#compare_snapshot_to_run_batch) | **GET** /test/snapshot/diff/snapshot/{snapshotId}/batch/{batchId} | Compare a snapshot with a run batch
[**compare_snapshots**](SnapshotsApi.md#compare_snapshots) | **GET** /test/snapshot/diff/snapshot/{leftSnapshotId}/snapshot/{rightSnapshotId} | Compare two snapshots
[**create_snapshot**](SnapshotsApi.md#create_snapshot) | **POST** /test/snapshot/create | Create a snapshot baseline
[**get_snapshot**](SnapshotsApi.md#get_snapshot) | **GET** /test/snapshot/by-id/{snapshotId} | Get a snapshot
[**list_snapshots**](SnapshotsApi.md#list_snapshots) | **GET** /test/snapshot/page | List snapshots


# **compare_snapshot_step**
> SnapshotStepDiff compare_snapshot_step(snapshot_step_diff_input)

Compare snapshot step payloads

Produce a field-level definition and behavior diff for one API, UI macro, or browser-action step.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.snapshot_step_diff import SnapshotStepDiff
from spectestengine_sdk.models.snapshot_step_diff_input import SnapshotStepDiffInput
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
    api_instance = spectestengine_sdk.SnapshotsApi(api_client)
    snapshot_step_diff_input = spectestengine_sdk.SnapshotStepDiffInput() # SnapshotStepDiffInput |

    try:
        # Compare snapshot step payloads
        api_response = api_instance.compare_snapshot_step(snapshot_step_diff_input)
        print("The response of SnapshotsApi->compare_snapshot_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->compare_snapshot_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_step_diff_input** | [**SnapshotStepDiffInput**](SnapshotStepDiffInput.md)|  |

### Return type

[**SnapshotStepDiff**](SnapshotStepDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A grouped, field-level step comparison suitable for a review UI. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compare_snapshot_to_run_batch**
> SnapshotDiff compare_snapshot_to_run_batch(snapshot_id, batch_id)

Compare a snapshot with a run batch

Compare a saved baseline with fresh run-batch evidence before promoting a new snapshot.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.snapshot_diff import SnapshotDiff
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
    api_instance = spectestengine_sdk.SnapshotsApi(api_client)
    snapshot_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved snapshot baseline.
    batch_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved run batch.

    try:
        # Compare a snapshot with a run batch
        api_response = api_instance.compare_snapshot_to_run_batch(snapshot_id, batch_id)
        print("The response of SnapshotsApi->compare_snapshot_to_run_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->compare_snapshot_to_run_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **UUID**| UUIDv7 identifier of the saved snapshot baseline. |
 **batch_id** | **UUID**| UUIDv7 identifier of the saved run batch. |

### Return type

[**SnapshotDiff**](SnapshotDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The classified baseline-to-batch comparison. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compare_snapshots**
> SnapshotDiff compare_snapshots(left_snapshot_id, right_snapshot_id)

Compare two snapshots

Compare two saved baselines and classify new, removed, regressed, improved, and stable subjects.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.snapshot_diff import SnapshotDiff
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
    api_instance = spectestengine_sdk.SnapshotsApi(api_client)
    left_snapshot_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the baseline side of the comparison.
    right_snapshot_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the candidate side of the comparison.

    try:
        # Compare two snapshots
        api_response = api_instance.compare_snapshots(left_snapshot_id, right_snapshot_id)
        print("The response of SnapshotsApi->compare_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->compare_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **left_snapshot_id** | **UUID**| UUIDv7 identifier of the baseline side of the comparison. |
 **right_snapshot_id** | **UUID**| UUIDv7 identifier of the candidate side of the comparison. |

### Return type

[**SnapshotDiff**](SnapshotDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The classified snapshot comparison. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot**
> Snapshot create_snapshot(snapshot_input, idempotency_key=idempotency_key)

Create a snapshot baseline

Promote all or a selected subset of one run batch into a versioned baseline for later regression comparison.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.snapshot import Snapshot
from spectestengine_sdk.models.snapshot_input import SnapshotInput
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
    api_instance = spectestengine_sdk.SnapshotsApi(api_client)
    snapshot_input = spectestengine_sdk.SnapshotInput() # SnapshotInput |
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A caller-generated UUID retained for safe write retries where supported. (optional)

    try:
        # Create a snapshot baseline
        api_response = api_instance.create_snapshot(snapshot_input, idempotency_key=idempotency_key)
        print("The response of SnapshotsApi->create_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->create_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_input** | [**SnapshotInput**](SnapshotInput.md)|  |
 **idempotency_key** | **UUID**| A caller-generated UUID retained for safe write retries where supported. | [optional]

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created snapshot baseline. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot**
> Snapshot get_snapshot(snapshot_id)

Get a snapshot

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.snapshot import Snapshot
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
    api_instance = spectestengine_sdk.SnapshotsApi(api_client)
    snapshot_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of the saved snapshot baseline.

    try:
        # Get a snapshot
        api_response = api_instance.get_snapshot(snapshot_id)
        print("The response of SnapshotsApi->get_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->get_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **UUID**| UUIDv7 identifier of the saved snapshot baseline. |

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested snapshot and its baseline evidence. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshots**
> SnapshotPage list_snapshots(page=page, size=size, search=search)

List snapshots

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.snapshot_page import SnapshotPage
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
    api_instance = spectestengine_sdk.SnapshotsApi(api_client)
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)
    search = 'search_example' # str | Case-insensitive server-side search within the active project. (optional)

    try:
        # List snapshots
        api_response = api_instance.list_snapshots(page=page, size=size, search=search)
        print("The response of SnapshotsApi->list_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->list_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]
 **search** | **str**| Case-insensitive server-side search within the active project. | [optional]

### Return type

[**SnapshotPage**](SnapshotPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of snapshot baselines in the active project. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
