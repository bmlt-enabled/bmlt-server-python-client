# MeetingPartialUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_body_id** | **int** |  | [optional] 
**format_ids** | **List[int]** |  | [optional] 
**venue_type** | **int** |  | [optional] 
**temporarily_virtual** | **bool** |  | [optional] 
**day** | **int** |  | [optional] 
**start_time** | **str** |  | [optional] 
**duration** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**published** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**world_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**location_text** | **str** |  | [optional] 
**location_info** | **str** |  | [optional] 
**location_street** | **str** |  | [optional] 
**location_neighborhood** | **str** |  | [optional] 
**location_city_subsection** | **str** |  | [optional] 
**location_municipality** | **str** |  | [optional] 
**location_sub_province** | **str** |  | [optional] 
**location_province** | **str** |  | [optional] 
**location_postal_code_1** | **str** |  | [optional] 
**location_nation** | **str** |  | [optional] 
**phone_meeting_number** | **str** |  | [optional] 
**virtual_meeting_link** | **str** |  | [optional] 
**virtual_meeting_additional_info** | **str** |  | [optional] 
**contact_name_1** | **str** |  | [optional] 
**contact_name_2** | **str** |  | [optional] 
**contact_phone_1** | **str** |  | [optional] 
**contact_phone_2** | **str** |  | [optional] 
**contact_email_1** | **str** |  | [optional] 
**contact_email_2** | **str** |  | [optional] 
**bus_lines** | **str** |  | [optional] 
**train_lines** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**custom_fields** | **Dict[str, str]** |  | [optional] 

## Example

```python
from bmlt_client.models.meeting_partial_update import MeetingPartialUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MeetingPartialUpdate from a JSON string
meeting_partial_update_instance = MeetingPartialUpdate.from_json(json)
# print the JSON string representation of the object
print(MeetingPartialUpdate.to_json())

# convert the object into a dict
meeting_partial_update_dict = meeting_partial_update_instance.to_dict()
# create an instance of MeetingPartialUpdate from a dict
meeting_partial_update_from_dict = MeetingPartialUpdate.from_dict(meeting_partial_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


