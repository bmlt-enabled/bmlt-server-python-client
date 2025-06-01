# ServiceBodyPartialUpdate


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
from bmlt_client.models.service_body_partial_update import ServiceBodyPartialUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceBodyPartialUpdate from a JSON string
service_body_partial_update_instance = ServiceBodyPartialUpdate.from_json(json)
# print the JSON string representation of the object
print(ServiceBodyPartialUpdate.to_json())

# convert the object into a dict
service_body_partial_update_dict = service_body_partial_update_instance.to_dict()
# create an instance of ServiceBodyPartialUpdate from a dict
service_body_partial_update_from_dict = ServiceBodyPartialUpdate.from_dict(service_body_partial_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


