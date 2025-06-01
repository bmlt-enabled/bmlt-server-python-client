# bmlt_client.RootServerApi

All URIs are relative to *http://localhost:8000/main_server*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_logout**](RootServerApi.md#auth_logout) | **POST** /api/v1/auth/logout | Revokes a token
[**auth_refresh**](RootServerApi.md#auth_refresh) | **POST** /api/v1/auth/refresh | Revokes and issues a new token
[**auth_token**](RootServerApi.md#auth_token) | **POST** /api/v1/auth/token | Creates a token
[**create_error_test**](RootServerApi.md#create_error_test) | **POST** /api/v1/errortest | Tests some errors
[**create_format**](RootServerApi.md#create_format) | **POST** /api/v1/formats | Creates a format
[**create_meeting**](RootServerApi.md#create_meeting) | **POST** /api/v1/meetings | Creates a meeting
[**create_service_body**](RootServerApi.md#create_service_body) | **POST** /api/v1/servicebodies | Creates a service body
[**create_user**](RootServerApi.md#create_user) | **POST** /api/v1/users | Creates a user
[**delete_format**](RootServerApi.md#delete_format) | **DELETE** /api/v1/formats/{formatId} | Deletes a format
[**delete_meeting**](RootServerApi.md#delete_meeting) | **DELETE** /api/v1/meetings/{meetingId} | Deletes a meeting
[**delete_service_body**](RootServerApi.md#delete_service_body) | **DELETE** /api/v1/servicebodies/{serviceBodyId} | Deletes a service body
[**delete_user**](RootServerApi.md#delete_user) | **DELETE** /api/v1/users/{userId} | Deletes a user
[**get_format**](RootServerApi.md#get_format) | **GET** /api/v1/formats/{formatId} | Retrieves a format
[**get_formats**](RootServerApi.md#get_formats) | **GET** /api/v1/formats | Retrieves formats
[**get_laravel_log**](RootServerApi.md#get_laravel_log) | **GET** /api/v1/logs/laravel | Retrieves laravel log
[**get_meeting**](RootServerApi.md#get_meeting) | **GET** /api/v1/meetings/{meetingId} | Retrieves a meeting
[**get_meeting_changes**](RootServerApi.md#get_meeting_changes) | **GET** /api/v1/meetings/{meetingId}/changes | Retrieve changes for a meeting
[**get_meetings**](RootServerApi.md#get_meetings) | **GET** /api/v1/meetings | Retrieves meetings
[**get_root_server**](RootServerApi.md#get_root_server) | **GET** /api/v1/rootservers/{rootServerId} | Retrieves a root server
[**get_root_servers**](RootServerApi.md#get_root_servers) | **GET** /api/v1/rootservers | Retrieves root servers
[**get_service_bodies**](RootServerApi.md#get_service_bodies) | **GET** /api/v1/servicebodies | Retrieves service bodies
[**get_service_body**](RootServerApi.md#get_service_body) | **GET** /api/v1/servicebodies/{serviceBodyId} | Retrieves a service body
[**get_user**](RootServerApi.md#get_user) | **GET** /api/v1/users/{userId} | Retrieves a single user
[**get_users**](RootServerApi.md#get_users) | **GET** /api/v1/users | Retrieves users
[**partial_update_user**](RootServerApi.md#partial_update_user) | **PATCH** /api/v1/users/{userId} | Patches a user
[**patch_format**](RootServerApi.md#patch_format) | **PATCH** /api/v1/formats/{formatId} | Patches a format
[**patch_meeting**](RootServerApi.md#patch_meeting) | **PATCH** /api/v1/meetings/{meetingId} | Patches a meeting
[**patch_service_body**](RootServerApi.md#patch_service_body) | **PATCH** /api/v1/servicebodies/{serviceBodyId} | Patches a service body
[**update_format**](RootServerApi.md#update_format) | **PUT** /api/v1/formats/{formatId} | Updates a format
[**update_meeting**](RootServerApi.md#update_meeting) | **PUT** /api/v1/meetings/{meetingId} | Updates a meeting
[**update_service_body**](RootServerApi.md#update_service_body) | **PUT** /api/v1/servicebodies/{serviceBodyId} | Updates a Service Body
[**update_user**](RootServerApi.md#update_user) | **PUT** /api/v1/users/{userId} | Update single user


# **auth_logout**
> auth_logout()

Revokes a token

Revoke token and logout.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)

    try:
        # Revokes a token
        api_instance.auth_logout()
    except Exception as e:
        print("Exception when calling RootServerApi->auth_logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns when token was logged out. |  -  |
**401** | Returns when request is unauthenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_refresh**
> Token auth_refresh()

Revokes and issues a new token

Refresh token.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.token import Token
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)

    try:
        # Revokes and issues a new token
        api_response = api_instance.auth_refresh()
        print("The response of RootServerApi->auth_refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->auth_refresh: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Token**](Token.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns when refresh is successful. |  -  |
**401** | Returns when request is unauthenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_token**
> Token auth_token(token_credentials)

Creates a token

Exchange credentials for a new token

### Example


```python
import bmlt_client
from bmlt_client.models.token import Token
from bmlt_client.models.token_credentials import TokenCredentials
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)


# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    token_credentials = bmlt_client.TokenCredentials() # TokenCredentials | User credentials

    try:
        # Creates a token
        api_response = api_instance.auth_token(token_credentials)
        print("The response of RootServerApi->auth_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->auth_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_credentials** | [**TokenCredentials**](TokenCredentials.md)| User credentials | 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns when POST is successful. |  -  |
**401** | Returns when credentials are incorrect. |  -  |
**403** | Returns when unauthorized. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_error_test**
> ErrorTest create_error_test(error_test)

Tests some errors

Tests some errors.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.error_test import ErrorTest
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    error_test = bmlt_client.ErrorTest() # ErrorTest | Pass in error test object.

    try:
        # Tests some errors
        api_response = api_instance.create_error_test(error_test)
        print("The response of RootServerApi->create_error_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->create_error_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_test** | [**ErrorTest**](ErrorTest.md)| Pass in error test object. | 

### Return type

[**ErrorTest**](ErrorTest.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns when POST is successful. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**422** | Validation error. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_format**
> Format create_format(format_create)

Creates a format

Creates a format.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.format import Format
from bmlt_client.models.format_create import FormatCreate
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    format_create = bmlt_client.FormatCreate() # FormatCreate | Pass in format object

    try:
        # Creates a format
        api_response = api_instance.create_format(format_create)
        print("The response of RootServerApi->create_format:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->create_format: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format_create** | [**FormatCreate**](FormatCreate.md)| Pass in format object | 

### Return type

[**Format**](Format.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns when POST is successful. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**403** | Returns when user is unauthorized to perform action. |  -  |
**404** | Returns when no format exists. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_meeting**
> Meeting create_meeting(meeting_create)

Creates a meeting

Creates a meeting.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.meeting import Meeting
from bmlt_client.models.meeting_create import MeetingCreate
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    meeting_create = bmlt_client.MeetingCreate() # MeetingCreate | Pass in meeting object

    try:
        # Creates a meeting
        api_response = api_instance.create_meeting(meeting_create)
        print("The response of RootServerApi->create_meeting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->create_meeting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_create** | [**MeetingCreate**](MeetingCreate.md)| Pass in meeting object | 

### Return type

[**Meeting**](Meeting.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns when POST is successful. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**403** | Returns when user is unauthorized to perform action. |  -  |
**404** | Returns when no meeting body exists. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_body**
> ServiceBody create_service_body(service_body_create)

Creates a service body

Creates a service body.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.service_body import ServiceBody
from bmlt_client.models.service_body_create import ServiceBodyCreate
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    service_body_create = bmlt_client.ServiceBodyCreate() # ServiceBodyCreate | Pass in service body object

    try:
        # Creates a service body
        api_response = api_instance.create_service_body(service_body_create)
        print("The response of RootServerApi->create_service_body:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->create_service_body: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_body_create** | [**ServiceBodyCreate**](ServiceBodyCreate.md)| Pass in service body object | 

### Return type

[**ServiceBody**](ServiceBody.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns when POST is successful. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**403** | Returns when user is unauthorized to perform action. |  -  |
**404** | Returns when no service body exists. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(user_create)

Creates a user

Creates a user.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.user import User
from bmlt_client.models.user_create import UserCreate
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    user_create = bmlt_client.UserCreate() # UserCreate | Pass in user object

    try:
        # Creates a user
        api_response = api_instance.create_user(user_create)
        print("The response of RootServerApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)| Pass in user object | 

### Return type

[**User**](User.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns when POST is successful. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**403** | Returns when user is unauthorized to perform action. |  -  |
**404** | Returns when no user exists. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_format**
> delete_format(format_id)

Deletes a format

Deletes a format by id.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    format_id = 1 # int | ID of format

    try:
        # Deletes a format
        api_instance.delete_format(format_id)
    except Exception as e:
        print("Exception when calling RootServerApi->delete_format: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format_id** | **int**| ID of format | 

### Return type

void (empty response body)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Returns when not authenticated |  -  |
**403** | Returns when unauthorized |  -  |
**404** | Returns when no format exists. |  -  |
**409** | Returns when format has meetings assigned. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_meeting**
> delete_meeting(meeting_id)

Deletes a meeting

Deletes a meeting by id.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    meeting_id = 1 # int | ID of meeting

    try:
        # Deletes a meeting
        api_instance.delete_meeting(meeting_id)
    except Exception as e:
        print("Exception when calling RootServerApi->delete_meeting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| ID of meeting | 

### Return type

void (empty response body)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**403** | Returns when user is unauthorized to perform action. |  -  |
**404** | Returns when no meeting exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_body**
> delete_service_body(service_body_id)

Deletes a service body

Deletes a service body by id.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    service_body_id = 1 # int | ID of service body

    try:
        # Deletes a service body
        api_instance.delete_service_body(service_body_id)
    except Exception as e:
        print("Exception when calling RootServerApi->delete_service_body: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_body_id** | **int**| ID of service body | 

### Return type

void (empty response body)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**403** | Returns when user is unauthorized to perform action. |  -  |
**404** | Returns when no service body exists. |  -  |
**409** | Returns when service body has children. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id)

Deletes a user

Deletes a user by id

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    user_id = 1 # int | ID of user

    try:
        # Deletes a user
        api_instance.delete_user(user_id)
    except Exception as e:
        print("Exception when calling RootServerApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of user | 

### Return type

void (empty response body)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Returns when not authenticated |  -  |
**403** | Returns when unauthorized |  -  |
**404** | Returns when no user exists. |  -  |
**409** | Returns when user is still referenced by service bodies. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_format**
> Format get_format(format_id)

Retrieves a format

Retrieve a format

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.format import Format
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    format_id = 1 # int | ID of format

    try:
        # Retrieves a format
        api_response = api_instance.get_format(format_id)
        print("The response of RootServerApi->get_format:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->get_format: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format_id** | **int**| ID of format | 

### Return type

[**Format**](Format.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns when user is authenticated. |  -  |
**401** | Returns when not authenticated. |  -  |
**404** | Returns when no format exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_formats**
> List[Format] get_formats()

Retrieves formats

Retrieve formats

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.format import Format
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)

    try:
        # Retrieves formats
        api_response = api_instance.get_formats()
        print("The response of RootServerApi->get_formats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->get_formats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Format]**](Format.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns when user is authenticated. |  -  |
**401** | Returns when not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_laravel_log**
> bytearray get_laravel_log()

Retrieves laravel log

Retrieve the laravel log if it exists.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)

    try:
        # Retrieves laravel log
        api_response = api_instance.get_laravel_log()
        print("The response of RootServerApi->get_laravel_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->get_laravel_log: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bytearray**

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/gzip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns when user is authenticated. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**403** | Returns when user is unauthorized to perform action. |  -  |
**404** | Returns when no laravel log file exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meeting**
> Meeting get_meeting(meeting_id)

Retrieves a meeting

Retrieve a meeting.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.meeting import Meeting
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    meeting_id = 1 # int | ID of meeting

    try:
        # Retrieves a meeting
        api_response = api_instance.get_meeting(meeting_id)
        print("The response of RootServerApi->get_meeting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->get_meeting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| ID of meeting | 

### Return type

[**Meeting**](Meeting.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns when user is authenticated. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**404** | Returns when no meeting exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meeting_changes**
> List[MeetingChangeResource] get_meeting_changes(meeting_id)

Retrieve changes for a meeting

Retrieve all changes made to a specific meeting.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.meeting_change_resource import MeetingChangeResource
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    meeting_id = 1 # int | ID of the meeting

    try:
        # Retrieve changes for a meeting
        api_response = api_instance.get_meeting_changes(meeting_id)
        print("The response of RootServerApi->get_meeting_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->get_meeting_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| ID of the meeting | 

### Return type

[**List[MeetingChangeResource]**](MeetingChangeResource.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of changes for the meeting. |  -  |
**401** | Unauthorized. |  -  |
**403** | Returns when unauthorized |  -  |
**404** | Meeting not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meetings**
> List[Meeting] get_meetings(meeting_ids=meeting_ids, days=days, service_body_ids=service_body_ids, search_string=search_string)

Retrieves meetings

Retrieve meetings for authenticated user.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.meeting import Meeting
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    meeting_ids = '1,2' # str | comma delimited meeting ids (optional)
    days = '0,1' # str | comma delimited day ids between 0-6 (optional)
    service_body_ids = '3,4' # str | comma delimited service body ids (optional)
    search_string = 'Just for Today' # str | string (optional)

    try:
        # Retrieves meetings
        api_response = api_instance.get_meetings(meeting_ids=meeting_ids, days=days, service_body_ids=service_body_ids, search_string=search_string)
        print("The response of RootServerApi->get_meetings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->get_meetings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_ids** | **str**| comma delimited meeting ids | [optional] 
 **days** | **str**| comma delimited day ids between 0-6 | [optional] 
 **service_body_ids** | **str**| comma delimited service body ids | [optional] 
 **search_string** | **str**| string | [optional] 

### Return type

[**List[Meeting]**](Meeting.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of meetings. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_server**
> RootServer get_root_server(root_server_id)

Retrieves a root server

Retrieve a single root server id.

### Example


```python
import bmlt_client
from bmlt_client.models.root_server import RootServer
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)


# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    root_server_id = 1 # int | ID of root server

    try:
        # Retrieves a root server
        api_response = api_instance.get_root_server(root_server_id)
        print("The response of RootServerApi->get_root_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->get_root_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_server_id** | **int**| ID of root server | 

### Return type

[**RootServer**](RootServer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**404** | Returns when no root server exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_servers**
> List[RootServer] get_root_servers()

Retrieves root servers

Retrieve root servers.

### Example


```python
import bmlt_client
from bmlt_client.models.root_server import RootServer
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)


# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)

    try:
        # Retrieves root servers
        api_response = api_instance.get_root_servers()
        print("The response of RootServerApi->get_root_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->get_root_servers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RootServer]**](RootServer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**404** | Returns when aggregator mode is disabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_bodies**
> List[ServiceBody] get_service_bodies()

Retrieves service bodies

Retrieve service bodies for authenticated user.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.service_body import ServiceBody
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)

    try:
        # Retrieves service bodies
        api_response = api_instance.get_service_bodies()
        print("The response of RootServerApi->get_service_bodies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->get_service_bodies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ServiceBody]**](ServiceBody.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns when user is authenticated. |  -  |
**401** | Returns when not authenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_body**
> ServiceBody get_service_body(service_body_id)

Retrieves a service body

Retrieve a single service body by id.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.service_body import ServiceBody
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    service_body_id = 1 # int | ID of service body

    try:
        # Retrieves a service body
        api_response = api_instance.get_service_body(service_body_id)
        print("The response of RootServerApi->get_service_body:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->get_service_body: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_body_id** | **int**| ID of service body | 

### Return type

[**ServiceBody**](ServiceBody.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns when user is authenticated. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**404** | Returns when no service body exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_id)

Retrieves a single user

Retrieve single user.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.user import User
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    user_id = 1 # int | ID of user

    try:
        # Retrieves a single user
        api_response = api_instance.get_user(user_id)
        print("The response of RootServerApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of user | 

### Return type

[**User**](User.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns when user is authenticated. |  -  |
**401** | Returns when not authenticated. |  -  |
**404** | Returns when no user exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> List[User] get_users()

Retrieves users

Retrieve users for authenticated user.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.user import User
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)

    try:
        # Retrieves users
        api_response = api_instance.get_users()
        print("The response of RootServerApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootServerApi->get_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[User]**](User.md)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns when user is authenticated. |  -  |
**401** | Returns when not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_user**
> partial_update_user(user_id, user_partial_update)

Patches a user

Patches a user by id.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.user_partial_update import UserPartialUpdate
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    user_id = 1 # int | ID of user
    user_partial_update = bmlt_client.UserPartialUpdate() # UserPartialUpdate | Pass in fields you want to update.

    try:
        # Patches a user
        api_instance.partial_update_user(user_id, user_partial_update)
    except Exception as e:
        print("Exception when calling RootServerApi->partial_update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of user | 
 **user_partial_update** | [**UserPartialUpdate**](UserPartialUpdate.md)| Pass in fields you want to update. | 

### Return type

void (empty response body)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Returns when not authenticated |  -  |
**403** | Returns when unauthorized |  -  |
**404** | Returns when no user exists. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_format**
> patch_format(format_id, format_partial_update)

Patches a format

Patches a single format by id.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.format_partial_update import FormatPartialUpdate
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    format_id = 1 # int | ID of format
    format_partial_update = bmlt_client.FormatPartialUpdate() # FormatPartialUpdate | Pass in fields you want to update.

    try:
        # Patches a format
        api_instance.patch_format(format_id, format_partial_update)
    except Exception as e:
        print("Exception when calling RootServerApi->patch_format: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format_id** | **int**| ID of format | 
 **format_partial_update** | [**FormatPartialUpdate**](FormatPartialUpdate.md)| Pass in fields you want to update. | 

### Return type

void (empty response body)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Returns when not authenticated |  -  |
**403** | Returns when unauthorized |  -  |
**404** | Returns when no format exists. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_meeting**
> patch_meeting(meeting_id, meeting_partial_update)

Patches a meeting

Patches a meeting by id

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.meeting_partial_update import MeetingPartialUpdate
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    meeting_id = 1 # int | ID of meeting
    meeting_partial_update = bmlt_client.MeetingPartialUpdate() # MeetingPartialUpdate | Pass in fields you want to update.

    try:
        # Patches a meeting
        api_instance.patch_meeting(meeting_id, meeting_partial_update)
    except Exception as e:
        print("Exception when calling RootServerApi->patch_meeting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| ID of meeting | 
 **meeting_partial_update** | [**MeetingPartialUpdate**](MeetingPartialUpdate.md)| Pass in fields you want to update. | 

### Return type

void (empty response body)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**403** | Returns when user is unauthorized to perform action. |  -  |
**404** | Returns when no meeting exists. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_service_body**
> patch_service_body(service_body_id, service_body_partial_update)

Patches a service body

Patches a single service body by id.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.service_body_partial_update import ServiceBodyPartialUpdate
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    service_body_id = 1 # int | ID of service body
    service_body_partial_update = bmlt_client.ServiceBodyPartialUpdate() # ServiceBodyPartialUpdate | Pass in fields you want to update.

    try:
        # Patches a service body
        api_instance.patch_service_body(service_body_id, service_body_partial_update)
    except Exception as e:
        print("Exception when calling RootServerApi->patch_service_body: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_body_id** | **int**| ID of service body | 
 **service_body_partial_update** | [**ServiceBodyPartialUpdate**](ServiceBodyPartialUpdate.md)| Pass in fields you want to update. | 

### Return type

void (empty response body)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**403** | Returns when user is unauthorized to perform action. |  -  |
**404** | Returns when no service body exists. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_format**
> update_format(format_id, format_update)

Updates a format

Updates a format.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.format_update import FormatUpdate
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    format_id = 1 # int | ID of format
    format_update = bmlt_client.FormatUpdate() # FormatUpdate | Pass in format object

    try:
        # Updates a format
        api_instance.update_format(format_id, format_update)
    except Exception as e:
        print("Exception when calling RootServerApi->update_format: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format_id** | **int**| ID of format | 
 **format_update** | [**FormatUpdate**](FormatUpdate.md)| Pass in format object | 

### Return type

void (empty response body)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**403** | Returns when user is unauthorized to perform action. |  -  |
**404** | Returns when no format exists. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_meeting**
> update_meeting(meeting_id, meeting_update)

Updates a meeting

Updates a meeting.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.meeting_update import MeetingUpdate
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    meeting_id = 1 # int | ID of meeting
    meeting_update = bmlt_client.MeetingUpdate() # MeetingUpdate | Pass in meeting object

    try:
        # Updates a meeting
        api_instance.update_meeting(meeting_id, meeting_update)
    except Exception as e:
        print("Exception when calling RootServerApi->update_meeting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| ID of meeting | 
 **meeting_update** | [**MeetingUpdate**](MeetingUpdate.md)| Pass in meeting object | 

### Return type

void (empty response body)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**403** | Returns when user is unauthorized to perform action. |  -  |
**404** | Returns when no meeting exists. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_body**
> update_service_body(service_body_id, service_body_update)

Updates a Service Body

Updates a single service body.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.service_body_update import ServiceBodyUpdate
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    service_body_id = 1 # int | ID of service body
    service_body_update = bmlt_client.ServiceBodyUpdate() # ServiceBodyUpdate | Pass in service body object

    try:
        # Updates a Service Body
        api_instance.update_service_body(service_body_id, service_body_update)
    except Exception as e:
        print("Exception when calling RootServerApi->update_service_body: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_body_id** | **int**| ID of service body | 
 **service_body_update** | [**ServiceBodyUpdate**](ServiceBodyUpdate.md)| Pass in service body object | 

### Return type

void (empty response body)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**403** | Returns when user is unauthorized to perform action. |  -  |
**404** | Returns when no service body exists. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(user_id, user_update)

Update single user

Updates a user.

### Example

* OAuth Authentication (bmltToken):

```python
import bmlt_client
from bmlt_client.models.user_update import UserUpdate
from bmlt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bmlt_client.RootServerApi(api_client)
    user_id = 1 # int | ID of user
    user_update = bmlt_client.UserUpdate() # UserUpdate | Pass in user object

    try:
        # Update single user
        api_instance.update_user(user_id, user_update)
    except Exception as e:
        print("Exception when calling RootServerApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of user | 
 **user_update** | [**UserUpdate**](UserUpdate.md)| Pass in user object | 

### Return type

void (empty response body)

### Authorization

[bmltToken](../README.md#bmltToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**401** | Returns when user is not authenticated. |  -  |
**403** | Returns when user is unauthorized to perform action. |  -  |
**404** | Returns when no user exists. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

