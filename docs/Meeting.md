# Meeting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_body_id** | **int** |  | 
**format_ids** | **List[int]** |  | 
**venue_type** | **int** |  | 
**temporarily_virtual** | **bool** |  | 
**day** | **int** |  | 
**start_time** | **str** |  | 
**duration** | **str** |  | 
**time_zone** | **str** |  | 
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**published** | **bool** |  | 
**email** | **str** |  | 
**world_id** | **str** |  | 
**name** | **str** |  | 
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
**id** | **int** |  | 

## Example

```python
from bmlt_client.models.meeting import Meeting

# TODO update the JSON string below
json = "{}"
# create an instance of Meeting from a JSON string
meeting_instance = Meeting.from_json(json)
# print the JSON string representation of the object
print(Meeting.to_json())

# convert the object into a dict
meeting_dict = meeting_instance.to_dict()
# create an instance of Meeting from a dict
meeting_from_dict = Meeting.from_dict(meeting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


