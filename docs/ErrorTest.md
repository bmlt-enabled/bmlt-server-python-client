# ErrorTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arbitrary_string** | **str** |  | [optional] 
**arbitrary_int** | **int** |  | [optional] 
**force_server_error** | **bool** |  | [optional] 

## Example

```python
from bmlt_client.models.error_test import ErrorTest

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorTest from a JSON string
error_test_instance = ErrorTest.from_json(json)
# print the JSON string representation of the object
print(ErrorTest.to_json())

# convert the object into a dict
error_test_dict = error_test_instance.to_dict()
# create an instance of ErrorTest from a dict
error_test_from_dict = ErrorTest.from_dict(error_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


