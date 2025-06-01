# UserPartialUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**owner_id** | **int** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from bmlt_client.models.user_partial_update import UserPartialUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UserPartialUpdate from a JSON string
user_partial_update_instance = UserPartialUpdate.from_json(json)
# print the JSON string representation of the object
print(UserPartialUpdate.to_json())

# convert the object into a dict
user_partial_update_dict = user_partial_update_instance.to_dict()
# create an instance of UserPartialUpdate from a dict
user_partial_update_from_dict = UserPartialUpdate.from_dict(user_partial_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


