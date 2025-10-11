# StatusModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_verified_date** | **str** | Date in &#x60;yyyy&#x60;, &#x60;yyyy-MM&#x60;, or &#x60;yyyy-MM-dd&#x60; format | [optional] 
**overall_status** | [**Status**](Status.md) |  | [optional] 
**last_known_status** | [**Status**](Status.md) |  | [optional] 
**delayed_posting** | **bool** |  | [optional] 
**why_stopped** | **str** |  | [optional] 
**expanded_access_info** | [**ExpandedAccessInfo**](ExpandedAccessInfo.md) |  | [optional] 
**start_date_struct** | [**PartialDateStruct**](PartialDateStruct.md) |  | [optional] 
**primary_completion_date_struct** | [**PartialDateStruct**](PartialDateStruct.md) |  | [optional] 
**completion_date_struct** | [**PartialDateStruct**](PartialDateStruct.md) |  | [optional] 
**study_first_submit_date** | **date** |  | [optional] 
**study_first_submit_qc_date** | **date** |  | [optional] 
**study_first_post_date_struct** | [**DateStruct**](DateStruct.md) |  | [optional] 
**results_waived** | **bool** |  | [optional] 
**results_first_submit_date** | **date** |  | [optional] 
**results_first_submit_qc_date** | **date** |  | [optional] 
**results_first_post_date_struct** | [**DateStruct**](DateStruct.md) |  | [optional] 
**disp_first_submit_date** | **date** |  | [optional] 
**disp_first_submit_qc_date** | **date** |  | [optional] 
**disp_first_post_date_struct** | [**DateStruct**](DateStruct.md) |  | [optional] 
**last_update_submit_date** | **date** |  | [optional] 
**last_update_post_date_struct** | [**DateStruct**](DateStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.status_module import StatusModule

# TODO update the JSON string below
json = "{}"
# create an instance of StatusModule from a JSON string
status_module_instance = StatusModule.from_json(json)
# print the JSON string representation of the object
print(StatusModule.to_json())

# convert the object into a dict
status_module_dict = status_module_instance.to_dict()
# create an instance of StatusModule from a dict
status_module_from_dict = StatusModule.from_dict(status_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


