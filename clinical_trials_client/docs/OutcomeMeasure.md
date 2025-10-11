# OutcomeMeasure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**OutcomeMeasureType**](OutcomeMeasureType.md) |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**population_description** | **str** |  | [optional] 
**reporting_status** | [**ReportingStatus**](ReportingStatus.md) |  | [optional] 
**anticipated_posting_date** | **str** | Date in &#x60;yyyy&#x60;, &#x60;yyyy-MM&#x60;, or &#x60;yyyy-MM-dd&#x60; format | [optional] 
**param_type** | [**MeasureParam**](MeasureParam.md) |  | [optional] 
**dispersion_type** | **str** |  | [optional] 
**unit_of_measure** | **str** |  | [optional] 
**calculate_pct** | **bool** |  | [optional] 
**time_frame** | **str** |  | [optional] 
**type_units_analyzed** | **str** |  | [optional] 
**denom_units_selected** | **str** |  | [optional] 
**groups** | [**List[MeasureGroup]**](MeasureGroup.md) |  | [optional] 
**denoms** | [**List[Denom]**](Denom.md) |  | [optional] 
**classes** | [**List[MeasureClass]**](MeasureClass.md) |  | [optional] 
**analyses** | [**List[MeasureAnalysis]**](MeasureAnalysis.md) |  | [optional] 

## Example

```python
from openapi_client.models.outcome_measure import OutcomeMeasure

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeMeasure from a JSON string
outcome_measure_instance = OutcomeMeasure.from_json(json)
# print the JSON string representation of the object
print(OutcomeMeasure.to_json())

# convert the object into a dict
outcome_measure_dict = outcome_measure_instance.to_dict()
# create an instance of OutcomeMeasure from a dict
outcome_measure_from_dict = OutcomeMeasure.from_dict(outcome_measure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


