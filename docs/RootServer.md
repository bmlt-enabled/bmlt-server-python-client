# RootServer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **int** |  | 
**name** | **str** |  | 
**url** | **str** |  | 
**statistics** | [**RootServerBaseStatistics**](RootServerBaseStatistics.md) |  | [optional] 
**server_info** | **str** |  | [optional] 
**last_successful_import** | **datetime** |  | 
**id** | **int** |  | 

## Example

```python
from bmlt_client.models.root_server import RootServer

# TODO update the JSON string below
json = "{}"
# create an instance of RootServer from a JSON string
root_server_instance = RootServer.from_json(json)
# print the JSON string representation of the object
print RootServer.to_json()

# convert the object into a dict
root_server_dict = root_server_instance.to_dict()
# create an instance of RootServer from a dict
root_server_form_dict = root_server.from_dict(root_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


