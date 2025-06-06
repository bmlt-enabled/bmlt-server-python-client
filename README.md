# bmlt-server-client
BMLT Admin API Documentation

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.14.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/bmlt-enabled/bmlt-server-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/bmlt-enabled/bmlt-server-python-client.git`)

Then import the package:
```python
import bmlt_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import bmlt_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    except ApiException as e:
        print("Exception when calling RootServerApi->auth_logout: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8000/main_server*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RootServerApi* | [**auth_logout**](docs/RootServerApi.md#auth_logout) | **POST** /api/v1/auth/logout | Revokes a token
*RootServerApi* | [**auth_refresh**](docs/RootServerApi.md#auth_refresh) | **POST** /api/v1/auth/refresh | Revokes and issues a new token
*RootServerApi* | [**auth_token**](docs/RootServerApi.md#auth_token) | **POST** /api/v1/auth/token | Creates a token
*RootServerApi* | [**create_error_test**](docs/RootServerApi.md#create_error_test) | **POST** /api/v1/errortest | Tests some errors
*RootServerApi* | [**create_format**](docs/RootServerApi.md#create_format) | **POST** /api/v1/formats | Creates a format
*RootServerApi* | [**create_meeting**](docs/RootServerApi.md#create_meeting) | **POST** /api/v1/meetings | Creates a meeting
*RootServerApi* | [**create_service_body**](docs/RootServerApi.md#create_service_body) | **POST** /api/v1/servicebodies | Creates a service body
*RootServerApi* | [**create_user**](docs/RootServerApi.md#create_user) | **POST** /api/v1/users | Creates a user
*RootServerApi* | [**delete_format**](docs/RootServerApi.md#delete_format) | **DELETE** /api/v1/formats/{formatId} | Deletes a format
*RootServerApi* | [**delete_meeting**](docs/RootServerApi.md#delete_meeting) | **DELETE** /api/v1/meetings/{meetingId} | Deletes a meeting
*RootServerApi* | [**delete_service_body**](docs/RootServerApi.md#delete_service_body) | **DELETE** /api/v1/servicebodies/{serviceBodyId} | Deletes a service body
*RootServerApi* | [**delete_user**](docs/RootServerApi.md#delete_user) | **DELETE** /api/v1/users/{userId} | Deletes a user
*RootServerApi* | [**get_format**](docs/RootServerApi.md#get_format) | **GET** /api/v1/formats/{formatId} | Retrieves a format
*RootServerApi* | [**get_formats**](docs/RootServerApi.md#get_formats) | **GET** /api/v1/formats | Retrieves formats
*RootServerApi* | [**get_laravel_log**](docs/RootServerApi.md#get_laravel_log) | **GET** /api/v1/logs/laravel | Retrieves laravel log
*RootServerApi* | [**get_meeting**](docs/RootServerApi.md#get_meeting) | **GET** /api/v1/meetings/{meetingId} | Retrieves a meeting
*RootServerApi* | [**get_meeting_changes**](docs/RootServerApi.md#get_meeting_changes) | **GET** /api/v1/meetings/{meetingId}/changes | Retrieve changes for a meeting
*RootServerApi* | [**get_meetings**](docs/RootServerApi.md#get_meetings) | **GET** /api/v1/meetings | Retrieves meetings
*RootServerApi* | [**get_root_server**](docs/RootServerApi.md#get_root_server) | **GET** /api/v1/rootservers/{rootServerId} | Retrieves a root server
*RootServerApi* | [**get_root_servers**](docs/RootServerApi.md#get_root_servers) | **GET** /api/v1/rootservers | Retrieves root servers
*RootServerApi* | [**get_service_bodies**](docs/RootServerApi.md#get_service_bodies) | **GET** /api/v1/servicebodies | Retrieves service bodies
*RootServerApi* | [**get_service_body**](docs/RootServerApi.md#get_service_body) | **GET** /api/v1/servicebodies/{serviceBodyId} | Retrieves a service body
*RootServerApi* | [**get_user**](docs/RootServerApi.md#get_user) | **GET** /api/v1/users/{userId} | Retrieves a single user
*RootServerApi* | [**get_users**](docs/RootServerApi.md#get_users) | **GET** /api/v1/users | Retrieves users
*RootServerApi* | [**partial_update_user**](docs/RootServerApi.md#partial_update_user) | **PATCH** /api/v1/users/{userId} | Patches a user
*RootServerApi* | [**patch_format**](docs/RootServerApi.md#patch_format) | **PATCH** /api/v1/formats/{formatId} | Patches a format
*RootServerApi* | [**patch_meeting**](docs/RootServerApi.md#patch_meeting) | **PATCH** /api/v1/meetings/{meetingId} | Patches a meeting
*RootServerApi* | [**patch_service_body**](docs/RootServerApi.md#patch_service_body) | **PATCH** /api/v1/servicebodies/{serviceBodyId} | Patches a service body
*RootServerApi* | [**update_format**](docs/RootServerApi.md#update_format) | **PUT** /api/v1/formats/{formatId} | Updates a format
*RootServerApi* | [**update_meeting**](docs/RootServerApi.md#update_meeting) | **PUT** /api/v1/meetings/{meetingId} | Updates a meeting
*RootServerApi* | [**update_service_body**](docs/RootServerApi.md#update_service_body) | **PUT** /api/v1/servicebodies/{serviceBodyId} | Updates a Service Body
*RootServerApi* | [**update_user**](docs/RootServerApi.md#update_user) | **PUT** /api/v1/users/{userId} | Update single user


## Documentation For Models

 - [AuthenticationError](docs/AuthenticationError.md)
 - [AuthorizationError](docs/AuthorizationError.md)
 - [ConflictError](docs/ConflictError.md)
 - [ErrorTest](docs/ErrorTest.md)
 - [Format](docs/Format.md)
 - [FormatBase](docs/FormatBase.md)
 - [FormatCreate](docs/FormatCreate.md)
 - [FormatPartialUpdate](docs/FormatPartialUpdate.md)
 - [FormatTranslation](docs/FormatTranslation.md)
 - [FormatUpdate](docs/FormatUpdate.md)
 - [Meeting](docs/Meeting.md)
 - [MeetingBase](docs/MeetingBase.md)
 - [MeetingChangeResource](docs/MeetingChangeResource.md)
 - [MeetingCreate](docs/MeetingCreate.md)
 - [MeetingPartialUpdate](docs/MeetingPartialUpdate.md)
 - [MeetingUpdate](docs/MeetingUpdate.md)
 - [NotFoundError](docs/NotFoundError.md)
 - [RootServer](docs/RootServer.md)
 - [RootServerBase](docs/RootServerBase.md)
 - [RootServerBaseStatistics](docs/RootServerBaseStatistics.md)
 - [RootServerBaseStatisticsMeetings](docs/RootServerBaseStatisticsMeetings.md)
 - [RootServerBaseStatisticsServiceBodies](docs/RootServerBaseStatisticsServiceBodies.md)
 - [ServerError](docs/ServerError.md)
 - [ServiceBody](docs/ServiceBody.md)
 - [ServiceBodyBase](docs/ServiceBodyBase.md)
 - [ServiceBodyCreate](docs/ServiceBodyCreate.md)
 - [ServiceBodyPartialUpdate](docs/ServiceBodyPartialUpdate.md)
 - [ServiceBodyUpdate](docs/ServiceBodyUpdate.md)
 - [Token](docs/Token.md)
 - [TokenCredentials](docs/TokenCredentials.md)
 - [User](docs/User.md)
 - [UserBase](docs/UserBase.md)
 - [UserCreate](docs/UserCreate.md)
 - [UserPartialUpdate](docs/UserPartialUpdate.md)
 - [UserUpdate](docs/UserUpdate.md)
 - [ValidationError](docs/ValidationError.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bmltToken"></a>
### bmltToken

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: N/A


## Author




