# RootServerBaseStatisticsMeetings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_total** | **int** |  | 
**num_in_person** | **int** |  | 
**num_virtual** | **int** |  | 
**num_hybrid** | **int** |  | 
**num_unknown** | **int** |  | 

## Example

```python
from bmlt_client.models.root_server_base_statistics_meetings import RootServerBaseStatisticsMeetings

# TODO update the JSON string below
json = "{}"
# create an instance of RootServerBaseStatisticsMeetings from a JSON string
root_server_base_statistics_meetings_instance = RootServerBaseStatisticsMeetings.from_json(json)
# print the JSON string representation of the object
print RootServerBaseStatisticsMeetings.to_json()

# convert the object into a dict
root_server_base_statistics_meetings_dict = root_server_base_statistics_meetings_instance.to_dict()
# create an instance of RootServerBaseStatisticsMeetings from a dict
root_server_base_statistics_meetings_form_dict = root_server_base_statistics_meetings.from_dict(root_server_base_statistics_meetings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


