# ServiceBodyCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | 
**admin_user_id** | **int** |  | 
**assigned_user_ids** | **List[int]** |  | 
**url** | **str** |  | [optional] 
**helpline** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**world_id** | **str** |  | [optional] 

## Example

```python
from bmlt_client.models.service_body_create import ServiceBodyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceBodyCreate from a JSON string
service_body_create_instance = ServiceBodyCreate.from_json(json)
# print the JSON string representation of the object
print ServiceBodyCreate.to_json()

# convert the object into a dict
service_body_create_dict = service_body_create_instance.to_dict()
# create an instance of ServiceBodyCreate from a dict
service_body_create_form_dict = service_body_create.from_dict(service_body_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


