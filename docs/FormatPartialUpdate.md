# FormatPartialUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**world_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**translations** | [**List[FormatTranslation]**](FormatTranslation.md) |  | [optional] 

## Example

```python
from bmlt_client.models.format_partial_update import FormatPartialUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of FormatPartialUpdate from a JSON string
format_partial_update_instance = FormatPartialUpdate.from_json(json)
# print the JSON string representation of the object
print FormatPartialUpdate.to_json()

# convert the object into a dict
format_partial_update_dict = format_partial_update_instance.to_dict()
# create an instance of FormatPartialUpdate from a dict
format_partial_update_form_dict = format_partial_update.from_dict(format_partial_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


