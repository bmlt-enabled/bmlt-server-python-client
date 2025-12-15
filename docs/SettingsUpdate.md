# SettingsUpdate

Partial update object - include only the settings you want to update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google_api_key** | **str** |  | [optional] 
**change_depth_for_meetings** | **int** |  | [optional] 
**default_sort_key** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**default_duration_time** | **str** |  | [optional] 
**region_bias** | **str** |  | [optional] 
**distance_units** | **str** |  | [optional] 
**meeting_states_and_provinces** | **List[str]** |  | [optional] 
**meeting_counties_and_sub_provinces** | **List[str]** |  | [optional] 
**search_spec_map_center_longitude** | **float** |  | [optional] 
**search_spec_map_center_latitude** | **float** |  | [optional] 
**search_spec_map_center_zoom** | **int** |  | [optional] 
**number_of_meetings_for_auto** | **int** |  | [optional] 
**auto_geocoding_enabled** | **bool** |  | [optional] 
**county_auto_geocoding_enabled** | **bool** |  | [optional] 
**zip_auto_geocoding_enabled** | **bool** |  | [optional] 
**default_closed_status** | **bool** |  | [optional] 
**enable_language_selector** | **bool** |  | [optional] 
**include_service_body_email_in_semantic** | **bool** |  | [optional] 
**bmlt_title** | **str** |  | [optional] 
**bmlt_notice** | **str** |  | [optional] 
**format_lang_names** | **object** |  | [optional] 

## Example

```python
from bmlt_client.models.settings_update import SettingsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsUpdate from a JSON string
settings_update_instance = SettingsUpdate.from_json(json)
# print the JSON string representation of the object
print(SettingsUpdate.to_json())

# convert the object into a dict
settings_update_dict = settings_update_instance.to_dict()
# create an instance of SettingsUpdate from a dict
settings_update_from_dict = SettingsUpdate.from_dict(settings_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


