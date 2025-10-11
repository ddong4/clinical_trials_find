# ResultsSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant_flow_module** | [**ParticipantFlowModule**](ParticipantFlowModule.md) |  | [optional] 
**baseline_characteristics_module** | [**BaselineCharacteristicsModule**](BaselineCharacteristicsModule.md) |  | [optional] 
**outcome_measures_module** | [**OutcomeMeasuresModule**](OutcomeMeasuresModule.md) |  | [optional] 
**adverse_events_module** | [**AdverseEventsModule**](AdverseEventsModule.md) |  | [optional] 
**more_info_module** | [**MoreInfoModule**](MoreInfoModule.md) |  | [optional] 

## Example

```python
from openapi_client.models.results_section import ResultsSection

# TODO update the JSON string below
json = "{}"
# create an instance of ResultsSection from a JSON string
results_section_instance = ResultsSection.from_json(json)
# print the JSON string representation of the object
print(ResultsSection.to_json())

# convert the object into a dict
results_section_dict = results_section_instance.to_dict()
# create an instance of ResultsSection from a dict
results_section_from_dict = ResultsSection.from_dict(results_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


