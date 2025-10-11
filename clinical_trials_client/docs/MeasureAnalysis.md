# MeasureAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**param_type** | **str** |  | [optional] 
**param_value** | **str** |  | [optional] 
**dispersion_type** | [**AnalysisDispersionType**](AnalysisDispersionType.md) |  | [optional] 
**dispersion_value** | **str** |  | [optional] 
**statistical_method** | **str** |  | [optional] 
**statistical_comment** | **str** |  | [optional] 
**p_value** | **str** |  | [optional] 
**p_value_comment** | **str** |  | [optional] 
**ci_num_sides** | [**ConfidenceIntervalNumSides**](ConfidenceIntervalNumSides.md) |  | [optional] 
**ci_pct_value** | **str** |  | [optional] 
**ci_lower_limit** | **str** |  | [optional] 
**ci_upper_limit** | **str** |  | [optional] 
**ci_lower_limit_comment** | **str** |  | [optional] 
**ci_upper_limit_comment** | **str** |  | [optional] 
**estimate_comment** | **str** |  | [optional] 
**tested_non_inferiority** | **bool** |  | [optional] 
**non_inferiority_type** | [**NonInferiorityType**](NonInferiorityType.md) |  | [optional] 
**non_inferiority_comment** | **str** |  | [optional] 
**other_analysis_description** | **str** |  | [optional] 
**group_description** | **str** |  | [optional] 
**group_ids** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.measure_analysis import MeasureAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureAnalysis from a JSON string
measure_analysis_instance = MeasureAnalysis.from_json(json)
# print the JSON string representation of the object
print(MeasureAnalysis.to_json())

# convert the object into a dict
measure_analysis_dict = measure_analysis_instance.to_dict()
# create an instance of MeasureAnalysis from a dict
measure_analysis_from_dict = MeasureAnalysis.from_dict(measure_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


