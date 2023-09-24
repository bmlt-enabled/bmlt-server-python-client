# FormatBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**world_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**translations** | [**List[FormatTranslation]**](FormatTranslation.md) |  | [optional] 

## Example

```python
from bmlt_client.models.format_base import FormatBase

# TODO update the JSON string below
json = "{}"
# create an instance of FormatBase from a JSON string
format_base_instance = FormatBase.from_json(json)
# print the JSON string representation of the object
print FormatBase.to_json()

# convert the object into a dict
format_base_dict = format_base_instance.to_dict()
# create an instance of FormatBase from a dict
format_base_form_dict = format_base.from_dict(format_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


