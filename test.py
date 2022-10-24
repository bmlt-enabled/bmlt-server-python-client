import bmlt_client
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.validation_error import ValidationError
from bmlt_client.model.token_credentials import TokenCredentials
from bmlt_client.model.token import Token
from bmlt_client.model.error_incorrect_credentials import ErrorIncorrectCredentials
from bmlt_client import ApiClient

from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "https://latest.aws.bmlt.app/main_server"
)

api_instance = root_server_api.RootServerApi(ApiClient(configuration))
body = TokenCredentials(
    password="",
    username="",
)
try:
    # Creates a token
    api_response = api_instance.auth_token(
        body=body,
    ).response
    print(api_response.data.decode())
except bmlt_client.ApiException as e:
    print("Exception when calling RootServerApi->auth_token: %s\n" % e)
