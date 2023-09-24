# RootServerBaseStatistics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_bodies** | [**RootServerBaseStatisticsServiceBodies**](RootServerBaseStatisticsServiceBodies.md) |  | 
**meetings** | [**RootServerBaseStatisticsMeetings**](RootServerBaseStatisticsMeetings.md) |  | 

## Example

```python
from bmlt_client.models.root_server_base_statistics import RootServerBaseStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of RootServerBaseStatistics from a JSON string
root_server_base_statistics_instance = RootServerBaseStatistics.from_json(json)
# print the JSON string representation of the object
print RootServerBaseStatistics.to_json()

# convert the object into a dict
root_server_base_statistics_dict = root_server_base_statistics_instance.to_dict()
# create an instance of RootServerBaseStatistics from a dict
root_server_base_statistics_form_dict = root_server_base_statistics.from_dict(root_server_base_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


