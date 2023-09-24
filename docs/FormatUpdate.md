# FormatUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**world_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**translations** | [**List[FormatTranslation]**](FormatTranslation.md) |  | 

## Example

```python
from bmlt_client.models.format_update import FormatUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of FormatUpdate from a JSON string
format_update_instance = FormatUpdate.from_json(json)
# print the JSON string representation of the object
print FormatUpdate.to_json()

# convert the object into a dict
format_update_dict = format_update_instance.to_dict()
# create an instance of FormatUpdate from a dict
format_update_form_dict = format_update.from_dict(format_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


