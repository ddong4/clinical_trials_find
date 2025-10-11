# BaselineCharacteristicsModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**population_description** | **str** |  | [optional] 
**type_units_analyzed** | **str** |  | [optional] 
**groups** | [**List[MeasureGroup]**](MeasureGroup.md) |  | [optional] 
**denoms** | [**List[Denom]**](Denom.md) |  | [optional] 
**measures** | [**List[BaselineMeasure]**](BaselineMeasure.md) |  | [optional] 

## Example

```python
from openapi_client.models.baseline_characteristics_module import BaselineCharacteristicsModule

# TODO update the JSON string below
json = "{}"
# create an instance of BaselineCharacteristicsModule from a JSON string
baseline_characteristics_module_instance = BaselineCharacteristicsModule.from_json(json)
# print the JSON string representation of the object
print(BaselineCharacteristicsModule.to_json())

# convert the object into a dict
baseline_characteristics_module_dict = baseline_characteristics_module_instance.to_dict()
# create an instance of BaselineCharacteristicsModule from a dict
baseline_characteristics_module_from_dict = BaselineCharacteristicsModule.from_dict(baseline_characteristics_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


