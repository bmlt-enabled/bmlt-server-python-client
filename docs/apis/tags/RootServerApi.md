<a name="__pageTop"></a>
# bmlt_client.apis.tags.root_server_api.RootServerApi

All URIs are relative to *http://localhost:8000/main_server*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_logout**](#auth_logout) | **post** /api/v1/auth/logout | Revokes a token
[**auth_refresh**](#auth_refresh) | **post** /api/v1/auth/refresh | Revokes and issues a new token
[**auth_token**](#auth_token) | **post** /api/v1/auth/token | Creates a token
[**create_format**](#create_format) | **post** /api/v1/formats | Creates a format
[**create_meeting**](#create_meeting) | **post** /api/v1/meetings | Creates a meeting
[**create_service_body**](#create_service_body) | **post** /api/v1/servicebodies | Creates a service body
[**create_user**](#create_user) | **post** /api/v1/users | Creates a user
[**delete_format**](#delete_format) | **delete** /api/v1/formats/{formatId} | Deletes a format
[**delete_meeting**](#delete_meeting) | **delete** /api/v1/meetings/{meetingId} | Deletes a meeting
[**delete_service_body**](#delete_service_body) | **delete** /api/v1/servicebodies/{serviceBodyId} | Deletes a service body
[**delete_user**](#delete_user) | **delete** /api/v1/users/{userId} | Deletes a user
[**get_format**](#get_format) | **get** /api/v1/formats/{formatId} | Retrieves a format
[**get_formats**](#get_formats) | **get** /api/v1/formats | Retrieves formats
[**get_meeting**](#get_meeting) | **get** /api/v1/meetings/{meetingId} | Retrieves a meeting
[**get_meetings**](#get_meetings) | **get** /api/v1/meetings | Retrieves meetings
[**get_service_bodies**](#get_service_bodies) | **get** /api/v1/servicebodies | Retrieves service bodies
[**get_service_body**](#get_service_body) | **get** /api/v1/servicebodies/{serviceBodyId} | Retrieves a service body
[**get_user**](#get_user) | **get** /api/v1/users/{userId} | Retrieves a single user
[**get_users**](#get_users) | **get** /api/v1/users | Retrieves users
[**partial_update_user**](#partial_update_user) | **patch** /api/v1/users/{userId} | Patches a user
[**patch_format**](#patch_format) | **patch** /api/v1/formats/{formatId} | Patches a format
[**patch_meeting**](#patch_meeting) | **patch** /api/v1/meetings/{meetingId} | Patches a meeting
[**patch_service_body**](#patch_service_body) | **patch** /api/v1/servicebodies/{serviceBodyId} | Patches a service body
[**update_format**](#update_format) | **put** /api/v1/formats/{formatId} | Updates a format
[**update_meeting**](#update_meeting) | **put** /api/v1/meetings/{meetingId} | Updates a meeting
[**update_service_body**](#update_service_body) | **put** /api/v1/servicebodies/{serviceBodyId} | Updates a Service Body
[**update_user**](#update_user) | **put** /api/v1/users/{userId} | Update single user

# **auth_logout**
<a name="auth_logout"></a>
> auth_logout()

Revokes a token

Revoke token and logout.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Revokes a token
        api_response = api_instance.auth_logout()
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->auth_logout: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#auth_logout.ApiResponseFor200) | Returns when token was logged out.
401 | [ApiResponseFor401](#auth_logout.ApiResponseFor401) | Returns when request is unauthenticated.

#### auth_logout.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### auth_logout.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **auth_refresh**
<a name="auth_refresh"></a>
> Token auth_refresh()

Revokes and issues a new token

Refresh token.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.token import Token
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Revokes and issues a new token
        api_response = api_instance.auth_refresh()
        pprint(api_response)
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->auth_refresh: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#auth_refresh.ApiResponseFor200) | Returns when refresh is successful.
401 | [ApiResponseFor401](#auth_refresh.ApiResponseFor401) | Returns when request is unauthenticated.

#### auth_refresh.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Token**](../../models/Token.md) |  | 


#### auth_refresh.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **auth_token**
<a name="auth_token"></a>
> Token auth_token(token_credentials)

Creates a token

Exchange credentials for a new token

### Example

```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.token_credentials import TokenCredentials
from bmlt_client.model.token import Token
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    body = TokenCredentials(
        password="PassWord12345",
        username="MyUsername",
    )
    try:
        # Creates a token
        api_response = api_instance.auth_token(
            body=body,
        )
        pprint(api_response)
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->auth_token: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TokenCredentials**](../../models/TokenCredentials.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#auth_token.ApiResponseFor201) | Returns when POST is successful.
401 | [ApiResponseFor401](#auth_token.ApiResponseFor401) | Returns when credentials are incorrect.
422 | [ApiResponseFor422](#auth_token.ApiResponseFor422) | Validation error.

#### auth_token.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Token**](../../models/Token.md) |  | 


#### auth_token.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### auth_token.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_format**
<a name="create_format"></a>
> Format create_format(format_create)

Creates a format

Creates a format.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.format import Format
from bmlt_client.model.format_create import FormatCreate
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    body = FormatCreate(None)
    try:
        # Creates a format
        api_response = api_instance.create_format(
            body=body,
        )
        pprint(api_response)
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->create_format: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FormatCreate**](../../models/FormatCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_format.ApiResponseFor201) | Returns when POST is successful.
401 | [ApiResponseFor401](#create_format.ApiResponseFor401) | Returns when user is not authenticated.
403 | [ApiResponseFor403](#create_format.ApiResponseFor403) | Returns when user is unauthorized to perform action.
404 | [ApiResponseFor404](#create_format.ApiResponseFor404) | Returns when no format exists.
422 | [ApiResponseFor422](#create_format.ApiResponseFor422) | Validation error.

#### create_format.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Format**](../../models/Format.md) |  | 


#### create_format.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### create_format.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### create_format.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


#### create_format.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_meeting**
<a name="create_meeting"></a>
> Meeting create_meeting(meeting_create)

Creates a meeting

Creates a meeting.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.meeting_create import MeetingCreate
from bmlt_client.model.authorization_error import AuthorizationError
from bmlt_client.model.not_found_error import NotFoundError
from bmlt_client.model.meeting import Meeting
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    body = MeetingCreate(None)
    try:
        # Creates a meeting
        api_response = api_instance.create_meeting(
            body=body,
        )
        pprint(api_response)
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->create_meeting: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MeetingCreate**](../../models/MeetingCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_meeting.ApiResponseFor201) | Returns when POST is successful.
401 | [ApiResponseFor401](#create_meeting.ApiResponseFor401) | Returns when user is not authenticated.
403 | [ApiResponseFor403](#create_meeting.ApiResponseFor403) | Returns when user is unauthorized to perform action.
404 | [ApiResponseFor404](#create_meeting.ApiResponseFor404) | Returns when no meeting body exists.
422 | [ApiResponseFor422](#create_meeting.ApiResponseFor422) | Validation error.

#### create_meeting.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Meeting**](../../models/Meeting.md) |  | 


#### create_meeting.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### create_meeting.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizationError**](../../models/AuthorizationError.md) |  | 


#### create_meeting.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


#### create_meeting.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_service_body**
<a name="create_service_body"></a>
> ServiceBody create_service_body(service_body_create)

Creates a service body

Creates a service body.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.service_body_create import ServiceBodyCreate
from bmlt_client.model.service_body import ServiceBody
from bmlt_client.model.authorization_error import AuthorizationError
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    body = ServiceBodyCreate(None)
    try:
        # Creates a service body
        api_response = api_instance.create_service_body(
            body=body,
        )
        pprint(api_response)
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->create_service_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceBodyCreate**](../../models/ServiceBodyCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_service_body.ApiResponseFor201) | Returns when POST is successful.
401 | [ApiResponseFor401](#create_service_body.ApiResponseFor401) | Returns when user is not authenticated.
403 | [ApiResponseFor403](#create_service_body.ApiResponseFor403) | Returns when user is unauthorized to perform action.
404 | [ApiResponseFor404](#create_service_body.ApiResponseFor404) | Returns when no service body exists.
422 | [ApiResponseFor422](#create_service_body.ApiResponseFor422) | Validation error.

#### create_service_body.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceBody**](../../models/ServiceBody.md) |  | 


#### create_service_body.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### create_service_body.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizationError**](../../models/AuthorizationError.md) |  | 


#### create_service_body.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


#### create_service_body.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_user**
<a name="create_user"></a>
> User create_user(user_create)

Creates a user

Creates a user.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.user_create import UserCreate
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.user import User
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    body = UserCreate()
    try:
        # Creates a user
        api_response = api_instance.create_user(
            body=body,
        )
        pprint(api_response)
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->create_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserCreate**](../../models/UserCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_user.ApiResponseFor201) | Returns when POST is successful.
401 | [ApiResponseFor401](#create_user.ApiResponseFor401) | Returns when user is not authenticated.
403 | [ApiResponseFor403](#create_user.ApiResponseFor403) | Returns when user is unauthorized to perform action.
404 | [ApiResponseFor404](#create_user.ApiResponseFor404) | Returns when no user exists.
422 | [ApiResponseFor422](#create_user.ApiResponseFor422) | Validation error.

#### create_user.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**User**](../../models/User.md) |  | 


#### create_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### create_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### create_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


#### create_user.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_format**
<a name="delete_format"></a>
> delete_format(format_id)

Deletes a format

Deletes a format by id.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.authorization_error import AuthorizationError
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'formatId': 1,
    }
    try:
        # Deletes a format
        api_response = api_instance.delete_format(
            path_params=path_params,
        )
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->delete_format: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
formatId | FormatIdSchema | | 

# FormatIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_format.ApiResponseFor204) | Success.
401 | [ApiResponseFor401](#delete_format.ApiResponseFor401) | Returns when not authenticated
403 | [ApiResponseFor403](#delete_format.ApiResponseFor403) | Returns when unauthorized
404 | [ApiResponseFor404](#delete_format.ApiResponseFor404) | Returns when no format exists.
422 | [ApiResponseFor422](#delete_format.ApiResponseFor422) | Validation error.

#### delete_format.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_format.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### delete_format.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizationError**](../../models/AuthorizationError.md) |  | 


#### delete_format.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


#### delete_format.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_meeting**
<a name="delete_meeting"></a>
> delete_meeting(meeting_id)

Deletes a meeting

Deletes a meeting by id.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.authorization_error import AuthorizationError
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'meetingId': 1,
    }
    try:
        # Deletes a meeting
        api_response = api_instance.delete_meeting(
            path_params=path_params,
        )
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->delete_meeting: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
meetingId | MeetingIdSchema | | 

# MeetingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_meeting.ApiResponseFor204) | Success.
401 | [ApiResponseFor401](#delete_meeting.ApiResponseFor401) | Returns when user is not authenticated.
403 | [ApiResponseFor403](#delete_meeting.ApiResponseFor403) | Returns when user is unauthorized to perform action.
404 | [ApiResponseFor404](#delete_meeting.ApiResponseFor404) | Returns when no meeting exists.

#### delete_meeting.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_meeting.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### delete_meeting.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizationError**](../../models/AuthorizationError.md) |  | 


#### delete_meeting.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_service_body**
<a name="delete_service_body"></a>
> delete_service_body(service_body_id)

Deletes a service body

Deletes a service body by id.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.authorization_error import AuthorizationError
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serviceBodyId': 1,
    }
    try:
        # Deletes a service body
        api_response = api_instance.delete_service_body(
            path_params=path_params,
        )
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->delete_service_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
serviceBodyId | ServiceBodyIdSchema | | 

# ServiceBodyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_service_body.ApiResponseFor204) | Success.
401 | [ApiResponseFor401](#delete_service_body.ApiResponseFor401) | Returns when user is not authenticated.
403 | [ApiResponseFor403](#delete_service_body.ApiResponseFor403) | Returns when user is unauthorized to perform action.
404 | [ApiResponseFor404](#delete_service_body.ApiResponseFor404) | Returns when no service body exists.

#### delete_service_body.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_service_body.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### delete_service_body.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizationError**](../../models/AuthorizationError.md) |  | 


#### delete_service_body.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_user**
<a name="delete_user"></a>
> delete_user(user_id)

Deletes a user

Deletes a user by id

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.authorization_error import AuthorizationError
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': 1,
    }
    try:
        # Deletes a user
        api_response = api_instance.delete_user(
            path_params=path_params,
        )
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->delete_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_user.ApiResponseFor204) | Success.
401 | [ApiResponseFor401](#delete_user.ApiResponseFor401) | Returns when not authenticated
403 | [ApiResponseFor403](#delete_user.ApiResponseFor403) | Returns when unauthorized
404 | [ApiResponseFor404](#delete_user.ApiResponseFor404) | Returns when no user exists.
422 | [ApiResponseFor422](#delete_user.ApiResponseFor422) | Validation error.

#### delete_user.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### delete_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizationError**](../../models/AuthorizationError.md) |  | 


#### delete_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


#### delete_user.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_format**
<a name="get_format"></a>
> Format get_format(format_id)

Retrieves a format

Retrieve a format

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.format import Format
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'formatId': 1,
    }
    try:
        # Retrieves a format
        api_response = api_instance.get_format(
            path_params=path_params,
        )
        pprint(api_response)
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->get_format: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
formatId | FormatIdSchema | | 

# FormatIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_format.ApiResponseFor200) | Returns when user is authenticated.
401 | [ApiResponseFor401](#get_format.ApiResponseFor401) | Returns when not authenticated.
404 | [ApiResponseFor404](#get_format.ApiResponseFor404) | Returns when no format exists.

#### get_format.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Format**](../../models/Format.md) |  | 


#### get_format.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### get_format.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_formats**
<a name="get_formats"></a>
> FormatCollection get_formats()

Retrieves formats

Retrieve formats

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.format_collection import FormatCollection
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieves formats
        api_response = api_instance.get_formats()
        pprint(api_response)
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->get_formats: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_formats.ApiResponseFor200) | Returns when user is authenticated.
401 | [ApiResponseFor401](#get_formats.ApiResponseFor401) | Returns when not authenticated

#### get_formats.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FormatCollection**](../../models/FormatCollection.md) |  | 


#### get_formats.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_meeting**
<a name="get_meeting"></a>
> Meeting get_meeting(meeting_id)

Retrieves a meeting

Retrieve a meeting.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.not_found_error import NotFoundError
from bmlt_client.model.meeting import Meeting
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'meetingId': 1,
    }
    try:
        # Retrieves a meeting
        api_response = api_instance.get_meeting(
            path_params=path_params,
        )
        pprint(api_response)
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->get_meeting: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
meetingId | MeetingIdSchema | | 

# MeetingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_meeting.ApiResponseFor200) | Returns when user is authenticated.
401 | [ApiResponseFor401](#get_meeting.ApiResponseFor401) | Returns when user is not authenticated.
404 | [ApiResponseFor404](#get_meeting.ApiResponseFor404) | Returns when no meeting exists.

#### get_meeting.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Meeting**](../../models/Meeting.md) |  | 


#### get_meeting.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### get_meeting.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_meetings**
<a name="get_meetings"></a>
> MeetingCollection get_meetings()

Retrieves meetings

Retrieve meetings for authenticated user.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.meeting_collection import MeetingCollection
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only optional values
    query_params = {
        'meetingIds': "1,2",
        'days': "0,1",
        'serviceBodyIds': "3,4",
        'searchString': "Just for Today",
    }
    try:
        # Retrieves meetings
        api_response = api_instance.get_meetings(
            query_params=query_params,
        )
        pprint(api_response)
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->get_meetings: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
meetingIds | MeetingIdsSchema | | optional
days | DaysSchema | | optional
serviceBodyIds | ServiceBodyIdsSchema | | optional
searchString | SearchStringSchema | | optional


# MeetingIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DaysSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServiceBodyIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SearchStringSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_meetings.ApiResponseFor200) | List of meetings.
401 | [ApiResponseFor401](#get_meetings.ApiResponseFor401) | Returns when user is not authenticated.
422 | [ApiResponseFor422](#get_meetings.ApiResponseFor422) | Validation error.

#### get_meetings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MeetingCollection**](../../models/MeetingCollection.md) |  | 


#### get_meetings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### get_meetings.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_service_bodies**
<a name="get_service_bodies"></a>
> ServiceBodyCollection get_service_bodies()

Retrieves service bodies

Retrieve service bodies for authenticated user.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.service_body_collection import ServiceBodyCollection
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieves service bodies
        api_response = api_instance.get_service_bodies()
        pprint(api_response)
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->get_service_bodies: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_service_bodies.ApiResponseFor200) | Returns when user is authenticated.
401 | [ApiResponseFor401](#get_service_bodies.ApiResponseFor401) | Returns when not authenticated.

#### get_service_bodies.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceBodyCollection**](../../models/ServiceBodyCollection.md) |  | 


#### get_service_bodies.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_service_body**
<a name="get_service_body"></a>
> ServiceBody get_service_body(service_body_id)

Retrieves a service body

Retrieve a single service body by id.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.service_body import ServiceBody
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serviceBodyId': 1,
    }
    try:
        # Retrieves a service body
        api_response = api_instance.get_service_body(
            path_params=path_params,
        )
        pprint(api_response)
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->get_service_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
serviceBodyId | ServiceBodyIdSchema | | 

# ServiceBodyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_service_body.ApiResponseFor200) | Returns when user is authenticated.
401 | [ApiResponseFor401](#get_service_body.ApiResponseFor401) | Returns when user is not authenticated.
404 | [ApiResponseFor404](#get_service_body.ApiResponseFor404) | Returns when no service body exists.

#### get_service_body.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceBody**](../../models/ServiceBody.md) |  | 


#### get_service_body.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### get_service_body.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_user**
<a name="get_user"></a>
> User get_user(user_id)

Retrieves a single user

Retrieve single user.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.user import User
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': 1,
    }
    try:
        # Retrieves a single user
        api_response = api_instance.get_user(
            path_params=path_params,
        )
        pprint(api_response)
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->get_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user.ApiResponseFor200) | Returns when user is authenticated.
401 | [ApiResponseFor401](#get_user.ApiResponseFor401) | Returns when not authenticated.
404 | [ApiResponseFor404](#get_user.ApiResponseFor404) | Returns when no user exists.

#### get_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**User**](../../models/User.md) |  | 


#### get_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### get_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_users**
<a name="get_users"></a>
> UserCollection get_users()

Retrieves users

Retrieve users for authenticated user.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.user_collection import UserCollection
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieves users
        api_response = api_instance.get_users()
        pprint(api_response)
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->get_users: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_users.ApiResponseFor200) | Returns when user is authenticated.
401 | [ApiResponseFor401](#get_users.ApiResponseFor401) | Returns when not authenticated

#### get_users.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserCollection**](../../models/UserCollection.md) |  | 


#### get_users.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **partial_update_user**
<a name="partial_update_user"></a>
> partial_update_user(user_iduser_partial_update)

Patches a user

Patches a user by id.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.authorization_error import AuthorizationError
from bmlt_client.model.not_found_error import NotFoundError
from bmlt_client.model.user_partial_update import UserPartialUpdate
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': 1,
    }
    body = UserPartialUpdate()
    try:
        # Patches a user
        api_response = api_instance.partial_update_user(
            path_params=path_params,
            body=body,
        )
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->partial_update_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserPartialUpdate**](../../models/UserPartialUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#partial_update_user.ApiResponseFor204) | Success.
401 | [ApiResponseFor401](#partial_update_user.ApiResponseFor401) | Returns when not authenticated
403 | [ApiResponseFor403](#partial_update_user.ApiResponseFor403) | Returns when unauthorized
404 | [ApiResponseFor404](#partial_update_user.ApiResponseFor404) | Returns when no user exists.
422 | [ApiResponseFor422](#partial_update_user.ApiResponseFor422) | Validation error.

#### partial_update_user.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### partial_update_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### partial_update_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizationError**](../../models/AuthorizationError.md) |  | 


#### partial_update_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


#### partial_update_user.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_format**
<a name="patch_format"></a>
> patch_format(format_idformat_partial_update)

Patches a format

Patches a single format by id.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.format_partial_update import FormatPartialUpdate
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.authorization_error import AuthorizationError
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'formatId': 1,
    }
    body = FormatPartialUpdate(None)
    try:
        # Patches a format
        api_response = api_instance.patch_format(
            path_params=path_params,
            body=body,
        )
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->patch_format: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FormatPartialUpdate**](../../models/FormatPartialUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
formatId | FormatIdSchema | | 

# FormatIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#patch_format.ApiResponseFor204) | Success.
401 | [ApiResponseFor401](#patch_format.ApiResponseFor401) | Returns when not authenticated
403 | [ApiResponseFor403](#patch_format.ApiResponseFor403) | Returns when unauthorized
404 | [ApiResponseFor404](#patch_format.ApiResponseFor404) | Returns when no format exists.
422 | [ApiResponseFor422](#patch_format.ApiResponseFor422) | Validation error.

#### patch_format.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### patch_format.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### patch_format.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizationError**](../../models/AuthorizationError.md) |  | 


#### patch_format.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


#### patch_format.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_meeting**
<a name="patch_meeting"></a>
> patch_meeting(meeting_idmeeting_partial_update)

Patches a meeting

Patches a meeting by id

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.meeting_partial_update import MeetingPartialUpdate
from bmlt_client.model.authorization_error import AuthorizationError
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'meetingId': 1,
    }
    body = MeetingPartialUpdate(None)
    try:
        # Patches a meeting
        api_response = api_instance.patch_meeting(
            path_params=path_params,
            body=body,
        )
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->patch_meeting: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MeetingPartialUpdate**](../../models/MeetingPartialUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
meetingId | MeetingIdSchema | | 

# MeetingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#patch_meeting.ApiResponseFor204) | Success.
401 | [ApiResponseFor401](#patch_meeting.ApiResponseFor401) | Returns when user is not authenticated.
403 | [ApiResponseFor403](#patch_meeting.ApiResponseFor403) | Returns when user is unauthorized to perform action.
404 | [ApiResponseFor404](#patch_meeting.ApiResponseFor404) | Returns when no meeting exists.
422 | [ApiResponseFor422](#patch_meeting.ApiResponseFor422) | Validation error.

#### patch_meeting.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### patch_meeting.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### patch_meeting.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizationError**](../../models/AuthorizationError.md) |  | 


#### patch_meeting.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


#### patch_meeting.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_service_body**
<a name="patch_service_body"></a>
> patch_service_body(service_body_idservice_body_partial_update)

Patches a service body

Patches a single service body by id.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.authorization_error import AuthorizationError
from bmlt_client.model.service_body_partial_update import ServiceBodyPartialUpdate
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serviceBodyId': 1,
    }
    body = ServiceBodyPartialUpdate(None)
    try:
        # Patches a service body
        api_response = api_instance.patch_service_body(
            path_params=path_params,
            body=body,
        )
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->patch_service_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceBodyPartialUpdate**](../../models/ServiceBodyPartialUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
serviceBodyId | ServiceBodyIdSchema | | 

# ServiceBodyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#patch_service_body.ApiResponseFor204) | Success.
401 | [ApiResponseFor401](#patch_service_body.ApiResponseFor401) | Returns when user is not authenticated.
403 | [ApiResponseFor403](#patch_service_body.ApiResponseFor403) | Returns when user is unauthorized to perform action.
404 | [ApiResponseFor404](#patch_service_body.ApiResponseFor404) | Returns when no service body exists.
422 | [ApiResponseFor422](#patch_service_body.ApiResponseFor422) | Validation error.

#### patch_service_body.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### patch_service_body.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### patch_service_body.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizationError**](../../models/AuthorizationError.md) |  | 


#### patch_service_body.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


#### patch_service_body.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_format**
<a name="update_format"></a>
> update_format(format_idformat_update)

Updates a format

Updates a format.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.not_found_error import NotFoundError
from bmlt_client.model.format_update import FormatUpdate
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'formatId': 1,
    }
    body = FormatUpdate(None)
    try:
        # Updates a format
        api_response = api_instance.update_format(
            path_params=path_params,
            body=body,
        )
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->update_format: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FormatUpdate**](../../models/FormatUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
formatId | FormatIdSchema | | 

# FormatIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_format.ApiResponseFor204) | Success.
401 | [ApiResponseFor401](#update_format.ApiResponseFor401) | Returns when user is not authenticated.
403 | [ApiResponseFor403](#update_format.ApiResponseFor403) | Returns when user is unauthorized to perform action.
404 | [ApiResponseFor404](#update_format.ApiResponseFor404) | Returns when no format exists.
422 | [ApiResponseFor422](#update_format.ApiResponseFor422) | Validation error.

#### update_format.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_format.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### update_format.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### update_format.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


#### update_format.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_meeting**
<a name="update_meeting"></a>
> update_meeting(meeting_idmeeting_update)

Updates a meeting

Updates a meeting.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.meeting_update import MeetingUpdate
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.authorization_error import AuthorizationError
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'meetingId': 1,
    }
    body = MeetingUpdate(None)
    try:
        # Updates a meeting
        api_response = api_instance.update_meeting(
            path_params=path_params,
            body=body,
        )
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->update_meeting: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MeetingUpdate**](../../models/MeetingUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
meetingId | MeetingIdSchema | | 

# MeetingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_meeting.ApiResponseFor204) | Success.
401 | [ApiResponseFor401](#update_meeting.ApiResponseFor401) | Returns when user is not authenticated.
403 | [ApiResponseFor403](#update_meeting.ApiResponseFor403) | Returns when user is unauthorized to perform action.
404 | [ApiResponseFor404](#update_meeting.ApiResponseFor404) | Returns when no meeting exists.
422 | [ApiResponseFor422](#update_meeting.ApiResponseFor422) | Validation error.

#### update_meeting.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_meeting.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### update_meeting.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizationError**](../../models/AuthorizationError.md) |  | 


#### update_meeting.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


#### update_meeting.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_service_body**
<a name="update_service_body"></a>
> update_service_body(service_body_idservice_body_update)

Updates a Service Body

Updates a single service body.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.service_body_update import ServiceBodyUpdate
from bmlt_client.model.authorization_error import AuthorizationError
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'serviceBodyId': 1,
    }
    body = ServiceBodyUpdate(None)
    try:
        # Updates a Service Body
        api_response = api_instance.update_service_body(
            path_params=path_params,
            body=body,
        )
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->update_service_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceBodyUpdate**](../../models/ServiceBodyUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
serviceBodyId | ServiceBodyIdSchema | | 

# ServiceBodyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_service_body.ApiResponseFor204) | Success.
401 | [ApiResponseFor401](#update_service_body.ApiResponseFor401) | Returns when user is not authenticated.
403 | [ApiResponseFor403](#update_service_body.ApiResponseFor403) | Returns when user is unauthorized to perform action.
404 | [ApiResponseFor404](#update_service_body.ApiResponseFor404) | Returns when no service body exists.
422 | [ApiResponseFor422](#update_service_body.ApiResponseFor422) | Validation error.

#### update_service_body.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_service_body.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### update_service_body.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizationError**](../../models/AuthorizationError.md) |  | 


#### update_service_body.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


#### update_service_body.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_user**
<a name="update_user"></a>
> update_user(user_iduser_update)

Update single user

Updates a user.

### Example

* OAuth Authentication (bmltToken):
```python
import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.authentication_error import AuthenticationError
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.user_update import UserUpdate
from bmlt_client.model.not_found_error import NotFoundError
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

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': 1,
    }
    body = UserUpdate()
    try:
        # Update single user
        api_response = api_instance.update_user(
            path_params=path_params,
            body=body,
        )
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->update_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserUpdate**](../../models/UserUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_user.ApiResponseFor204) | Success.
401 | [ApiResponseFor401](#update_user.ApiResponseFor401) | Returns when user is not authenticated.
403 | [ApiResponseFor403](#update_user.ApiResponseFor403) | Returns when user is unauthorized to perform action.
404 | [ApiResponseFor404](#update_user.ApiResponseFor404) | Returns when no user exists.
422 | [ApiResponseFor422](#update_user.ApiResponseFor422) | Validation error.

#### update_user.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### update_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationError**](../../models/AuthenticationError.md) |  | 


#### update_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundError**](../../models/NotFoundError.md) |  | 


#### update_user.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


### Authorization

[bmltToken](../../../README.md#bmltToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

