# FormatCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**world_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**translations** | [**List[FormatTranslation]**](FormatTranslation.md) |  | 

## Example

```python
from bmlt_client.models.format_create import FormatCreate

# TODO update the JSON string below
json = "{}"
# create an instance of FormatCreate from a JSON string
format_create_instance = FormatCreate.from_json(json)
# print the JSON string representation of the object
print(FormatCreate.to_json())

# convert the object into a dict
format_create_dict = format_create_instance.to_dict()
# create an instance of FormatCreate from a dict
format_create_from_dict = FormatCreate.from_dict(format_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


