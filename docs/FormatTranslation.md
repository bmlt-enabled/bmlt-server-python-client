# FormatTranslation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**language** | **str** |  | 

## Example

```python
from bmlt_client.models.format_translation import FormatTranslation

# TODO update the JSON string below
json = "{}"
# create an instance of FormatTranslation from a JSON string
format_translation_instance = FormatTranslation.from_json(json)
# print the JSON string representation of the object
print(FormatTranslation.to_json())

# convert the object into a dict
format_translation_dict = format_translation_instance.to_dict()
# create an instance of FormatTranslation from a dict
format_translation_from_dict = FormatTranslation.from_dict(format_translation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


