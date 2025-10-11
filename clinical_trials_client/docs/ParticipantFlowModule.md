# ParticipantFlowModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pre_assignment_details** | **str** |  | [optional] 
**recruitment_details** | **str** |  | [optional] 
**type_units_analyzed** | **str** |  | [optional] 
**groups** | [**List[FlowGroup]**](FlowGroup.md) |  | [optional] 
**periods** | [**List[FlowPeriod]**](FlowPeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.participant_flow_module import ParticipantFlowModule

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantFlowModule from a JSON string
participant_flow_module_instance = ParticipantFlowModule.from_json(json)
# print the JSON string representation of the object
print(ParticipantFlowModule.to_json())

# convert the object into a dict
participant_flow_module_dict = participant_flow_module_instance.to_dict()
# create an instance of ParticipantFlowModule from a dict
participant_flow_module_from_dict = ParticipantFlowModule.from_dict(participant_flow_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


