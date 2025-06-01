# TokenCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from bmlt_client.models.token_credentials import TokenCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of TokenCredentials from a JSON string
token_credentials_instance = TokenCredentials.from_json(json)
# print the JSON string representation of the object
print(TokenCredentials.to_json())

# convert the object into a dict
token_credentials_dict = token_credentials_instance.to_dict()
# create an instance of TokenCredentials from a dict
token_credentials_from_dict = TokenCredentials.from_dict(token_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


