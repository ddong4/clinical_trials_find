# MeasureClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**denoms** | [**List[Denom]**](Denom.md) |  | [optional] 
**categories** | [**List[MeasureCategory]**](MeasureCategory.md) |  | [optional] 

## Example

```python
from openapi_client.models.measure_class import MeasureClass

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureClass from a JSON string
measure_class_instance = MeasureClass.from_json(json)
# print the JSON string representation of the object
print(MeasureClass.to_json())

# convert the object into a dict
measure_class_dict = measure_class_instance.to_dict()
# create an instance of MeasureClass from a dict
measure_class_from_dict = MeasureClass.from_dict(measure_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


