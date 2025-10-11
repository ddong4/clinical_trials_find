# MeasureCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**measurements** | [**List[Measurement]**](Measurement.md) |  | [optional] 

## Example

```python
from openapi_client.models.measure_category import MeasureCategory

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureCategory from a JSON string
measure_category_instance = MeasureCategory.from_json(json)
# print the JSON string representation of the object
print(MeasureCategory.to_json())

# convert the object into a dict
measure_category_dict = measure_category_instance.to_dict()
# create an instance of MeasureCategory from a dict
measure_category_from_dict = MeasureCategory.from_dict(measure_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


