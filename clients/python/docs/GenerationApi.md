# spectestengine_sdk.GenerationApi

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_artifact_generation_profile**](GenerationApi.md#create_artifact_generation_profile) | **POST** /artifact-profiles | Create a CI export profile
[**delete_artifact_generation_profile**](GenerationApi.md#delete_artifact_generation_profile) | **DELETE** /artifact-profiles/{profileId} | Delete a CI export profile
[**download_artifact_generation_profile_archive**](GenerationApi.md#download_artifact_generation_profile_archive) | **POST** /artifact-profiles/{profileId}/environments/{environmentKey}/atf/archive | Validate and download a CI profile archive
[**download_atf_project**](GenerationApi.md#download_atf_project) | **POST** /atf/generate/download | Download a generated ATF project
[**generate_from_open_api_content**](GenerationApi.md#generate_from_open_api_content) | **POST** /openapi/generate-from-content | Generate specifications and flows from OpenAPI content
[**generate_specification**](GenerationApi.md#generate_specification) | **POST** /spec/generate | Generate an executable specification from concrete request evidence
[**get_artifact_generation_profile**](GenerationApi.md#get_artifact_generation_profile) | **GET** /artifact-profiles/{profileId} | Get a CI export profile
[**get_atf_project_validation_result**](GenerationApi.md#get_atf_project_validation_result) | **GET** /atf/generate/validate/result/{validationId} | Get ATF validation status or result
[**list_artifact_generation_profiles**](GenerationApi.md#list_artifact_generation_profiles) | **GET** /artifact-profiles | List CI export profiles
[**observe_atf_project_validation**](GenerationApi.md#observe_atf_project_validation) | **GET** /atf/generate/validate/events/{validationId} | Observe ATF validation progress
[**preview_atf_project**](GenerationApi.md#preview_atf_project) | **POST** /atf/generate/preview | Generate an ATF project preview
[**refresh_artifact_generation_profile_bundle**](GenerationApi.md#refresh_artifact_generation_profile_bundle) | **POST** /artifact-profiles/{profileId}/environments/{environmentKey}/bundle/refresh | Capture or refresh an environment baseline
[**start_atf_project_validation**](GenerationApi.md#start_atf_project_validation) | **POST** /atf/generate/validate/start | Start asynchronous ATF compile validation
[**update_artifact_generation_profile**](GenerationApi.md#update_artifact_generation_profile) | **PUT** /artifact-profiles/{profileId} | Update a CI export profile
[**validate_atf_project**](GenerationApi.md#validate_atf_project) | **POST** /atf/generate/validate | Validate that an ATF project compiles


# **create_artifact_generation_profile**
> ArtifactGenerationProfile create_artifact_generation_profile(artifact_generation_profile_input, idempotency_key=idempotency_key)

Create a CI export profile

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.artifact_generation_profile import ArtifactGenerationProfile
from spectestengine_sdk.models.artifact_generation_profile_input import ArtifactGenerationProfileInput
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
    api_instance = spectestengine_sdk.GenerationApi(api_client)
    artifact_generation_profile_input = spectestengine_sdk.ArtifactGenerationProfileInput() # ArtifactGenerationProfileInput |
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A caller-generated UUID retained for safe write retries where supported. (optional)

    try:
        # Create a CI export profile
        api_response = api_instance.create_artifact_generation_profile(artifact_generation_profile_input, idempotency_key=idempotency_key)
        print("The response of GenerationApi->create_artifact_generation_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->create_artifact_generation_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_generation_profile_input** | [**ArtifactGenerationProfileInput**](ArtifactGenerationProfileInput.md)|  |
 **idempotency_key** | **UUID**| A caller-generated UUID retained for safe write retries where supported. | [optional]

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The stored CI export profile. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact_generation_profile**
> delete_artifact_generation_profile(profile_id)

Delete a CI export profile

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
    api_instance = spectestengine_sdk.GenerationApi(api_client)
    profile_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of a CI export profile.

    try:
        # Delete a CI export profile
        api_instance.delete_artifact_generation_profile(profile_id)
    except Exception as e:
        print("Exception when calling GenerationApi->delete_artifact_generation_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **UUID**| UUIDv7 identifier of a CI export profile. |

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
**204** | The profile was deleted. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_artifact_generation_profile_archive**
> bytes download_artifact_generation_profile_archive(profile_id, environment_key)

Validate and download a CI profile archive

Resolves the environment policy, enforces drift rules, then returns an archive only after the generated project passes compile validation.

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
    api_instance = spectestengine_sdk.GenerationApi(api_client)
    profile_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of a CI export profile.
    environment_key = 'environment_key_example' # str | Stable profile environment key such as test, staging, or production.

    try:
        # Validate and download a CI profile archive
        api_response = api_instance.download_artifact_generation_profile_archive(profile_id, environment_key)
        print("The response of GenerationApi->download_artifact_generation_profile_archive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->download_artifact_generation_profile_archive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **UUID**| UUIDv7 identifier of a CI export profile. |
 **environment_key** | **str**| Stable profile environment key such as test, staging, or production. |

### Return type

**bytes**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A compile-validated ATF project archive. |  * Content-Disposition -  <br>  |
**422** | The generated project did not pass readiness validation; no archive was returned. |  -  |
**429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_atf_project**
> bytes download_atf_project(atf_generation_input)

Download a generated ATF project

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.atf_generation_input import AtfGenerationInput
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
    api_instance = spectestengine_sdk.GenerationApi(api_client)
    atf_generation_input = spectestengine_sdk.AtfGenerationInput() # AtfGenerationInput |

    try:
        # Download a generated ATF project
        api_response = api_instance.download_atf_project(atf_generation_input)
        print("The response of GenerationApi->download_atf_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->download_atf_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **atf_generation_input** | [**AtfGenerationInput**](AtfGenerationInput.md)|  |

### Return type

**bytes**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A portable ATF project archive. |  * Content-Disposition -  <br>  |
**422** | The generated project did not pass readiness validation; no archive was returned. |  -  |
**429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_from_open_api_content**
> OpenApiGenerationResult generate_from_open_api_content(content_format, body, include_negative_tests=include_negative_tests, generate_flow_scenarios=generate_flow_scenarios, generation_strategy=generation_strategy, negative_test_generation_mode=negative_test_generation_mode)

Generate specifications and flows from OpenAPI content

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.content_format import ContentFormat
from spectestengine_sdk.models.open_api_generation_result import OpenApiGenerationResult
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
    api_instance = spectestengine_sdk.GenerationApi(api_client)
    content_format = JSON # ContentFormat |  (default to JSON)
    body = 'body_example' # str |
    include_negative_tests = False # bool |  (optional) (default to False)
    generate_flow_scenarios = False # bool |  (optional) (default to False)
    generation_strategy = SCHEMA_BASED # str |  (optional) (default to SCHEMA_BASED)
    negative_test_generation_mode = EXTENDED # str |  (optional) (default to EXTENDED)

    try:
        # Generate specifications and flows from OpenAPI content
        api_response = api_instance.generate_from_open_api_content(content_format, body, include_negative_tests=include_negative_tests, generate_flow_scenarios=generate_flow_scenarios, generation_strategy=generation_strategy, negative_test_generation_mode=negative_test_generation_mode)
        print("The response of GenerationApi->generate_from_open_api_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->generate_from_open_api_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_format** | [**ContentFormat**](.md)|  | [default to JSON]
 **body** | **str**|  |
 **include_negative_tests** | **bool**|  | [optional] [default to False]
 **generate_flow_scenarios** | **bool**|  | [optional] [default to False]
 **generation_strategy** | **str**|  | [optional] [default to SCHEMA_BASED]
 **negative_test_generation_mode** | **str**|  | [optional] [default to EXTENDED]

### Return type

[**OpenApiGenerationResult**](OpenApiGenerationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generated specification drafts, flow drafts, and operation coverage. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_specification**
> List[SpecGenerationResult] generate_specification(request_body, mode=mode, format=format, spec_generation_types=spec_generation_types)

Generate an executable specification from concrete request evidence

Generates a REST, SOAP, GraphQL, or Streaming specification. Streaming input may
contain observedEvidence from a completed Craftsman session; generation derives
expectations from that transcript and never opens a second connection. Workflow
placeholders must be materialized before this endpoint is called.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.content_format import ContentFormat
from spectestengine_sdk.models.spec_generation_result import SpecGenerationResult
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
    api_instance = spectestengine_sdk.GenerationApi(api_client)
    request_body = None # Dict[str, object] |
    mode = FULL # str |  (optional) (default to FULL)
    format = JSON # ContentFormat |  (optional) (default to JSON)
    spec_generation_types = ["POSITIVE"] # List[str] | Comma-separated generation variants. Streaming currently accepts POSITIVE only. (optional) (default to ["POSITIVE"])

    try:
        # Generate an executable specification from concrete request evidence
        api_response = api_instance.generate_specification(request_body, mode=mode, format=format, spec_generation_types=spec_generation_types)
        print("The response of GenerationApi->generate_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->generate_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  |
 **mode** | **str**|  | [optional] [default to FULL]
 **format** | [**ContentFormat**](.md)|  | [optional] [default to JSON]
 **spec_generation_types** | [**List[str]**](str.md)| Comma-separated generation variants. Streaming currently accepts POSITIVE only. | [optional] [default to [&quot;POSITIVE&quot;]]

### Return type

[**List[SpecGenerationResult]**](SpecGenerationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generated executable specification variants. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_generation_profile**
> ArtifactGenerationProfile get_artifact_generation_profile(profile_id)

Get a CI export profile

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.artifact_generation_profile import ArtifactGenerationProfile
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
    api_instance = spectestengine_sdk.GenerationApi(api_client)
    profile_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of a CI export profile.

    try:
        # Get a CI export profile
        api_response = api_instance.get_artifact_generation_profile(profile_id)
        print("The response of GenerationApi->get_artifact_generation_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->get_artifact_generation_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **UUID**| UUIDv7 identifier of a CI export profile. |

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested profile. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_atf_project_validation_result**
> AtfValidationResult get_atf_project_validation_result(validation_id)

Get ATF validation status or result

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.atf_validation_result import AtfValidationResult
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
    api_instance = spectestengine_sdk.GenerationApi(api_client)
    validation_id = 'validation_id_example' # str | Opaque identifier of a bounded asynchronous ATF validation job.

    try:
        # Get ATF validation status or result
        api_response = api_instance.get_atf_project_validation_result(validation_id)
        print("The response of GenerationApi->get_atf_project_validation_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->get_atf_project_validation_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_id** | **str**| Opaque identifier of a bounded asynchronous ATF validation job. |

### Return type

[**AtfValidationResult**](AtfValidationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current or terminal validation result. |  -  |
**409** | The validation job is still running. Retry with the same identifier. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_artifact_generation_profiles**
> List[ArtifactGenerationProfile] list_artifact_generation_profiles()

List CI export profiles

Lists reusable export definitions used by CI to resolve an environment-specific source bundle and download a compile-validated ATF archive.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.artifact_generation_profile import ArtifactGenerationProfile
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
    api_instance = spectestengine_sdk.GenerationApi(api_client)

    try:
        # List CI export profiles
        api_response = api_instance.list_artifact_generation_profiles()
        print("The response of GenerationApi->list_artifact_generation_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->list_artifact_generation_profiles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ArtifactGenerationProfile]**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CI export profiles in the active project. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **observe_atf_project_validation**
> str observe_atf_project_validation(validation_id)

Observe ATF validation progress

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
    api_instance = spectestengine_sdk.GenerationApi(api_client)
    validation_id = 'validation_id_example' # str | Opaque identifier of a bounded asynchronous ATF validation job.

    try:
        # Observe ATF validation progress
        api_response = api_instance.observe_atf_project_validation(validation_id)
        print("The response of GenerationApi->observe_atf_project_validation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->observe_atf_project_validation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_id** | **str**| Opaque identifier of a bounded asynchronous ATF validation job. |

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server-sent validation lifecycle events. If the stream is interrupted, fetch the result endpoint with the same identifier. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_atf_project**
> AtfGenerationResult preview_atf_project(atf_generation_input)

Generate an ATF project preview

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.atf_generation_input import AtfGenerationInput
from spectestengine_sdk.models.atf_generation_result import AtfGenerationResult
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
    api_instance = spectestengine_sdk.GenerationApi(api_client)
    atf_generation_input = spectestengine_sdk.AtfGenerationInput() # AtfGenerationInput |

    try:
        # Generate an ATF project preview
        api_response = api_instance.preview_atf_project(atf_generation_input)
        print("The response of GenerationApi->preview_atf_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->preview_atf_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **atf_generation_input** | [**AtfGenerationInput**](AtfGenerationInput.md)|  |

### Return type

[**AtfGenerationResult**](AtfGenerationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generated files, manifest, and compatibility notes. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_artifact_generation_profile_bundle**
> ArtifactGenerationProfile refresh_artifact_generation_profile_bundle(profile_id, environment_key)

Capture or refresh an environment baseline

Resolves current selected assets and atomically stores the bundle plus its hash for PINNED or FAIL_ON_DRIFT downloads.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.artifact_generation_profile import ArtifactGenerationProfile
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
    api_instance = spectestengine_sdk.GenerationApi(api_client)
    profile_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of a CI export profile.
    environment_key = 'environment_key_example' # str | Stable profile environment key such as test, staging, or production.

    try:
        # Capture or refresh an environment baseline
        api_response = api_instance.refresh_artifact_generation_profile_bundle(profile_id, environment_key)
        print("The response of GenerationApi->refresh_artifact_generation_profile_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->refresh_artifact_generation_profile_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **UUID**| UUIDv7 identifier of a CI export profile. |
 **environment_key** | **str**| Stable profile environment key such as test, staging, or production. |

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The refreshed profile. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_atf_project_validation**
> AtfValidationStart start_atf_project_validation(atf_generation_input)

Start asynchronous ATF compile validation

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.atf_generation_input import AtfGenerationInput
from spectestengine_sdk.models.atf_validation_start import AtfValidationStart
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
    api_instance = spectestengine_sdk.GenerationApi(api_client)
    atf_generation_input = spectestengine_sdk.AtfGenerationInput() # AtfGenerationInput |

    try:
        # Start asynchronous ATF compile validation
        api_response = api_instance.start_atf_project_validation(atf_generation_input)
        print("The response of GenerationApi->start_atf_project_validation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->start_atf_project_validation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **atf_generation_input** | [**AtfGenerationInput**](AtfGenerationInput.md)|  |

### Return type

[**AtfValidationStart**](AtfValidationStart.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Identifier used to observe the bounded validation job. |  -  |
**429** | The company or global validation capacity is currently in use. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_artifact_generation_profile**
> ArtifactGenerationProfile update_artifact_generation_profile(profile_id, artifact_generation_profile_input)

Update a CI export profile

Send the revision returned by the latest read. A stale revision is rejected instead of overwriting a teammate's changes.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.artifact_generation_profile import ArtifactGenerationProfile
from spectestengine_sdk.models.artifact_generation_profile_input import ArtifactGenerationProfileInput
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
    api_instance = spectestengine_sdk.GenerationApi(api_client)
    profile_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | UUIDv7 identifier of a CI export profile.
    artifact_generation_profile_input = spectestengine_sdk.ArtifactGenerationProfileInput() # ArtifactGenerationProfileInput |

    try:
        # Update a CI export profile
        api_response = api_instance.update_artifact_generation_profile(profile_id, artifact_generation_profile_input)
        print("The response of GenerationApi->update_artifact_generation_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->update_artifact_generation_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **UUID**| UUIDv7 identifier of a CI export profile. |
 **artifact_generation_profile_input** | [**ArtifactGenerationProfileInput**](ArtifactGenerationProfileInput.md)|  |

### Return type

[**ArtifactGenerationProfile**](ArtifactGenerationProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated profile and its next revision. |  -  |
**409** | The profile was updated after the supplied revision was read. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_atf_project**
> AtfValidationResult validate_atf_project(atf_generation_input)

Validate that an ATF project compiles

Resolves the selected assets, generates the project, and runs a bounded compile validation without creating an archive.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.atf_generation_input import AtfGenerationInput
from spectestengine_sdk.models.atf_validation_result import AtfValidationResult
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
    api_instance = spectestengine_sdk.GenerationApi(api_client)
    atf_generation_input = spectestengine_sdk.AtfGenerationInput() # AtfGenerationInput |

    try:
        # Validate that an ATF project compiles
        api_response = api_instance.validate_atf_project(atf_generation_input)
        print("The response of GenerationApi->validate_atf_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->validate_atf_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **atf_generation_input** | [**AtfGenerationInput**](AtfGenerationInput.md)|  |

### Return type

[**AtfValidationResult**](AtfValidationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Structural and compile readiness for the generated project. |  -  |
**429** | The bounded validation capacity is currently in use. Retry after another validation completes. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

