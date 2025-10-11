# AdverseEventsModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency_threshold** | **str** |  | [optional] 
**time_frame** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**all_cause_mortality_comment** | **str** |  | [optional] 
**event_groups** | [**List[EventGroup]**](EventGroup.md) |  | [optional] 
**serious_events** | [**List[AdverseEvent]**](AdverseEvent.md) |  | [optional] 
**other_events** | [**List[AdverseEvent]**](AdverseEvent.md) |  | [optional] 

## Example

```python
from openapi_client.models.adverse_events_module import AdverseEventsModule

# TODO update the JSON string below
json = "{}"
# create an instance of AdverseEventsModule from a JSON string
adverse_events_module_instance = AdverseEventsModule.from_json(json)
# print the JSON string representation of the object
print(AdverseEventsModule.to_json())

# convert the object into a dict
adverse_events_module_dict = adverse_events_module_instance.to_dict()
# create an instance of AdverseEventsModule from a dict
adverse_events_module_from_dict = AdverseEventsModule.from_dict(adverse_events_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


