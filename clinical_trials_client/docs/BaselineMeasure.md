# BaselineMeasure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**population_description** | **str** |  | [optional] 
**param_type** | [**MeasureParam**](MeasureParam.md) |  | [optional] 
**dispersion_type** | [**MeasureDispersionType**](MeasureDispersionType.md) |  | [optional] 
**unit_of_measure** | **str** |  | [optional] 
**calculate_pct** | **bool** |  | [optional] 
**denom_units_selected** | **str** |  | [optional] 
**denoms** | [**List[Denom]**](Denom.md) |  | [optional] 
**classes** | [**List[MeasureClass]**](MeasureClass.md) |  | [optional] 

## Example

```python
from openapi_client.models.baseline_measure import BaselineMeasure

# TODO update the JSON string below
json = "{}"
# create an instance of BaselineMeasure from a JSON string
baseline_measure_instance = BaselineMeasure.from_json(json)
# print the JSON string representation of the object
print(BaselineMeasure.to_json())

# convert the object into a dict
baseline_measure_dict = baseline_measure_instance.to_dict()
# create an instance of BaselineMeasure from a dict
baseline_measure_from_dict = BaselineMeasure.from_dict(baseline_measure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


