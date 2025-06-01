# ServiceBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | 
**admin_user_id** | **int** |  | 
**assigned_user_ids** | **List[int]** |  | 
**url** | **str** |  | 
**helpline** | **str** |  | 
**email** | **str** |  | 
**world_id** | **str** |  | 
**id** | **int** |  | 

## Example

```python
from bmlt_client.models.service_body import ServiceBody

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceBody from a JSON string
service_body_instance = ServiceBody.from_json(json)
# print the JSON string representation of the object
print(ServiceBody.to_json())

# convert the object into a dict
service_body_dict = service_body_instance.to_dict()
# create an instance of ServiceBody from a dict
service_body_from_dict = ServiceBody.from_dict(service_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


