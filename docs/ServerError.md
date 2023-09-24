# ServerError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from bmlt_client.models.server_error import ServerError

# TODO update the JSON string below
json = "{}"
# create an instance of ServerError from a JSON string
server_error_instance = ServerError.from_json(json)
# print the JSON string representation of the object
print ServerError.to_json()

# convert the object into a dict
server_error_dict = server_error_instance.to_dict()
# create an instance of ServerError from a dict
server_error_form_dict = server_error.from_dict(server_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


