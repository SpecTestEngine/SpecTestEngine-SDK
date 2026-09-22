# spectestengine_sdk.FragmentsApi

All URIs are relative to *https://app.ste.software*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compile_draft_fragments**](FragmentsApi.md#compile_draft_fragments) | **POST** /test/spec/fragment/compile-draft | Compile inline fragment DSL into a specification draft
[**compile_fragments**](FragmentsApi.md#compile_fragments) | **POST** /test/spec/fragment/compile | Compile fragments into a specification draft
[**create_fragment**](FragmentsApi.md#create_fragment) | **POST** /test/spec/fragment/create | Create a specification fragment
[**delete_fragment**](FragmentsApi.md#delete_fragment) | **DELETE** /test/spec/fragment/by-id | Delete a fragment
[**get_fragment**](FragmentsApi.md#get_fragment) | **GET** /test/spec/fragment/by-id/{fragmentId} | Get a fragment
[**get_fragment_catalog**](FragmentsApi.md#get_fragment_catalog) | **GET** /test/spec/fragment/catalog | Get the fragment DSL catalog for an API type
[**get_fragment_summary**](FragmentsApi.md#get_fragment_summary) | **GET** /test/spec/fragment/summary | Count fragments by API type
[**list_fragments**](FragmentsApi.md#list_fragments) | **GET** /test/spec/fragment/page | List specification fragments
[**save_fragments_as_specification**](FragmentsApi.md#save_fragments_as_specification) | **POST** /test/spec/fragment/save-as-spec | Compile saved fragments and persist the result in the matching protocol engine
[**update_fragment**](FragmentsApi.md#update_fragment) | **PUT** /test/spec/fragment/by-id | Replace a fragment


# **compile_draft_fragments**
> CompiledSpecification compile_draft_fragments(fragment_draft_assembly, format=format)

Compile inline fragment DSL into a specification draft

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.compiled_specification import CompiledSpecification
from spectestengine_sdk.models.content_format import ContentFormat
from spectestengine_sdk.models.fragment_draft_assembly import FragmentDraftAssembly
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
    api_instance = spectestengine_sdk.FragmentsApi(api_client)
    fragment_draft_assembly = spectestengine_sdk.FragmentDraftAssembly() # FragmentDraftAssembly |
    format = JSON # ContentFormat | Serialization format used for the returned specification source. (optional) (default to JSON)

    try:
        # Compile inline fragment DSL into a specification draft
        api_response = api_instance.compile_draft_fragments(fragment_draft_assembly, format=format)
        print("The response of FragmentsApi->compile_draft_fragments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FragmentsApi->compile_draft_fragments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fragment_draft_assembly** | [**FragmentDraftAssembly**](FragmentDraftAssembly.md)|  |
 **format** | [**ContentFormat**](.md)| Serialization format used for the returned specification source. | [optional] [default to JSON]

### Return type

[**CompiledSpecification**](CompiledSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The compiled and protocol-validated specification draft. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compile_fragments**
> CompiledSpecification compile_fragments(fragment_assembly, format=format)

Compile fragments into a specification draft

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.compiled_specification import CompiledSpecification
from spectestengine_sdk.models.content_format import ContentFormat
from spectestengine_sdk.models.fragment_assembly import FragmentAssembly
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
    api_instance = spectestengine_sdk.FragmentsApi(api_client)
    fragment_assembly = spectestengine_sdk.FragmentAssembly() # FragmentAssembly |
    format = JSON # ContentFormat | Serialization format used for the returned specification source. (optional) (default to JSON)

    try:
        # Compile fragments into a specification draft
        api_response = api_instance.compile_fragments(fragment_assembly, format=format)
        print("The response of FragmentsApi->compile_fragments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FragmentsApi->compile_fragments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fragment_assembly** | [**FragmentAssembly**](FragmentAssembly.md)|  |
 **format** | [**ContentFormat**](.md)| Serialization format used for the returned specification source. | [optional] [default to JSON]

### Return type

[**CompiledSpecification**](CompiledSpecification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The compiled specification draft. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fragment**
> Fragment create_fragment(fragment_input, idempotency_key=idempotency_key)

Create a specification fragment

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.fragment import Fragment
from spectestengine_sdk.models.fragment_input import FragmentInput
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
    api_instance = spectestengine_sdk.FragmentsApi(api_client)
    fragment_input = spectestengine_sdk.FragmentInput() # FragmentInput |
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A caller-generated UUID retained for safe write retries where supported. (optional)

    try:
        # Create a specification fragment
        api_response = api_instance.create_fragment(fragment_input, idempotency_key=idempotency_key)
        print("The response of FragmentsApi->create_fragment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FragmentsApi->create_fragment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fragment_input** | [**FragmentInput**](FragmentInput.md)|  |
 **idempotency_key** | **UUID**| A caller-generated UUID retained for safe write retries where supported. | [optional]

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The stored fragment. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fragment**
> Fragment delete_fragment(fragment_id)

Delete a fragment

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.fragment import Fragment
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
    api_instance = spectestengine_sdk.FragmentsApi(api_client)
    fragment_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        # Delete a fragment
        api_response = api_instance.delete_fragment(fragment_id)
        print("The response of FragmentsApi->delete_fragment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FragmentsApi->delete_fragment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fragment_id** | **UUID**|  |

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted fragment. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fragment**
> Fragment get_fragment(fragment_id)

Get a fragment

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.fragment import Fragment
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
    api_instance = spectestengine_sdk.FragmentsApi(api_client)
    fragment_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        # Get a fragment
        api_response = api_instance.get_fragment(fragment_id)
        print("The response of FragmentsApi->get_fragment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FragmentsApi->get_fragment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fragment_id** | **UUID**|  |

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested fragment. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fragment_catalog**
> FragmentCatalog get_fragment_catalog(spec_type)

Get the fragment DSL catalog for an API type

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.fragment_catalog import FragmentCatalog
from spectestengine_sdk.models.spec_type import SpecType
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
    api_instance = spectestengine_sdk.FragmentsApi(api_client)
    spec_type = spectestengine_sdk.SpecType() # SpecType |

    try:
        # Get the fragment DSL catalog for an API type
        api_response = api_instance.get_fragment_catalog(spec_type)
        print("The response of FragmentsApi->get_fragment_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FragmentsApi->get_fragment_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_type** | [**SpecType**](.md)|  |

### Return type

[**FragmentCatalog**](FragmentCatalog.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compatible fragment types, fields, editor modes, and starter templates. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fragment_summary**
> FragmentSummary get_fragment_summary()

Count fragments by API type

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.fragment_summary import FragmentSummary
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
    api_instance = spectestengine_sdk.FragmentsApi(api_client)

    try:
        # Count fragments by API type
        api_response = api_instance.get_fragment_summary()
        print("The response of FragmentsApi->get_fragment_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FragmentsApi->get_fragment_summary: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FragmentSummary**](FragmentSummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | REST, SOAP, and GraphQL fragment counts. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fragments**
> FragmentPage list_fragments(page=page, size=size, search=search, spec_type=spec_type, type=type)

List specification fragments

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.fragment_page import FragmentPage
from spectestengine_sdk.models.fragment_type import FragmentType
from spectestengine_sdk.models.spec_type import SpecType
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
    api_instance = spectestengine_sdk.FragmentsApi(api_client)
    page = 0 # int | Zero-based page index. (optional) (default to 0)
    size = 20 # int | Maximum number of results returned in one page. (optional) (default to 20)
    search = 'search_example' # str | Case-insensitive server-side search within the active project. (optional)
    spec_type = spectestengine_sdk.SpecType() # SpecType | Filter the library to one API protocol. (optional)
    type = spectestengine_sdk.FragmentType() # FragmentType |  (optional)

    try:
        # List specification fragments
        api_response = api_instance.list_fragments(page=page, size=size, search=search, spec_type=spec_type, type=type)
        print("The response of FragmentsApi->list_fragments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FragmentsApi->list_fragments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index. | [optional] [default to 0]
 **size** | **int**| Maximum number of results returned in one page. | [optional] [default to 20]
 **search** | **str**| Case-insensitive server-side search within the active project. | [optional]
 **spec_type** | [**SpecType**](.md)| Filter the library to one API protocol. | [optional]
 **type** | [**FragmentType**](.md)|  | [optional]

### Return type

[**FragmentPage**](FragmentPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of reusable fragments. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_fragments_as_specification**
> Specification save_fragments_as_specification(spec_name, fragment_assembly, description=description, format=format, idempotency_key=idempotency_key)

Compile saved fragments and persist the result in the matching protocol engine

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.content_format import ContentFormat
from spectestengine_sdk.models.fragment_assembly import FragmentAssembly
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
    api_instance = spectestengine_sdk.FragmentsApi(api_client)
    spec_name = 'spec_name_example' # str |
    fragment_assembly = spectestengine_sdk.FragmentAssembly() # FragmentAssembly |
    description = 'description_example' # str |  (optional)
    format = JSON # ContentFormat | Serialization format used for the returned specification source. (optional) (default to JSON)
    idempotency_key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A caller-generated UUID retained for safe write retries where supported. (optional)

    try:
        # Compile saved fragments and persist the result in the matching protocol engine
        api_response = api_instance.save_fragments_as_specification(spec_name, fragment_assembly, description=description, format=format, idempotency_key=idempotency_key)
        print("The response of FragmentsApi->save_fragments_as_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FragmentsApi->save_fragments_as_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_name** | **str**|  |
 **fragment_assembly** | [**FragmentAssembly**](FragmentAssembly.md)|  |
 **description** | **str**|  | [optional]
 **format** | [**ContentFormat**](.md)| Serialization format used for the returned specification source. | [optional] [default to JSON]
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
**200** | The persisted REST, SOAP, or GraphQL specification. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fragment**
> Fragment update_fragment(fragment_id, fragment_input)

Replace a fragment

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import spectestengine_sdk
from spectestengine_sdk.models.fragment import Fragment
from spectestengine_sdk.models.fragment_input import FragmentInput
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
    api_instance = spectestengine_sdk.FragmentsApi(api_client)
    fragment_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    fragment_input = spectestengine_sdk.FragmentInput() # FragmentInput |

    try:
        # Replace a fragment
        api_response = api_instance.update_fragment(fragment_id, fragment_input)
        print("The response of FragmentsApi->update_fragment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FragmentsApi->update_fragment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fragment_id** | **UUID**|  |
 **fragment_input** | [**FragmentInput**](FragmentInput.md)|  |

### Return type

[**Fragment**](Fragment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated fragment. |  -  |
**0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

