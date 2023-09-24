# RootServerBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**statistics** | [**RootServerBaseStatistics**](RootServerBaseStatistics.md) |  | [optional] 
**server_info** | **str** |  | [optional] 
**last_successful_import** | **datetime** |  | [optional] 

## Example

```python
from bmlt_client.models.root_server_base import RootServerBase

# TODO update the JSON string below
json = "{}"
# create an instance of RootServerBase from a JSON string
root_server_base_instance = RootServerBase.from_json(json)
# print the JSON string representation of the object
print RootServerBase.to_json()

# convert the object into a dict
root_server_base_dict = root_server_base_instance.to_dict()
# create an instance of RootServerBase from a dict
root_server_base_form_dict = root_server_base.from_dict(root_server_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


