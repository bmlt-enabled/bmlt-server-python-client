# ServiceBodyBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**admin_user_id** | **int** |  | [optional] 
**assigned_user_ids** | **List[int]** |  | [optional] 
**url** | **str** |  | [optional] 
**helpline** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**world_id** | **str** |  | [optional] 

## Example

```python
from bmlt_client.models.service_body_base import ServiceBodyBase

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceBodyBase from a JSON string
service_body_base_instance = ServiceBodyBase.from_json(json)
# print the JSON string representation of the object
print(ServiceBodyBase.to_json())

# convert the object into a dict
service_body_base_dict = service_body_base_instance.to_dict()
# create an instance of ServiceBodyBase from a dict
service_body_base_from_dict = ServiceBodyBase.from_dict(service_body_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


