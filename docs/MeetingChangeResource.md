# MeetingChangeResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_string** | **str** | Human-readable date and time. | [optional] 
**user_name** | **str** | Name of the user who made the change. | [optional] 
**service_body_name** | **str** | Name of the service body related to the meeting. | [optional] 
**details** | **List[str]** | List of details about the changes. | [optional] 

## Example

```python
from bmlt_client.models.meeting_change_resource import MeetingChangeResource

# TODO update the JSON string below
json = "{}"
# create an instance of MeetingChangeResource from a JSON string
meeting_change_resource_instance = MeetingChangeResource.from_json(json)
# print the JSON string representation of the object
print(MeetingChangeResource.to_json())

# convert the object into a dict
meeting_change_resource_dict = meeting_change_resource_instance.to_dict()
# create an instance of MeetingChangeResource from a dict
meeting_change_resource_from_dict = MeetingChangeResource.from_dict(meeting_change_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


