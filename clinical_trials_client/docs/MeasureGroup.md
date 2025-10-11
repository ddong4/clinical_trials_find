# MeasureGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.measure_group import MeasureGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureGroup from a JSON string
measure_group_instance = MeasureGroup.from_json(json)
# print the JSON string representation of the object
print(MeasureGroup.to_json())

# convert the object into a dict
measure_group_dict = measure_group_instance.to_dict()
# create an instance of MeasureGroup from a dict
measure_group_from_dict = MeasureGroup.from_dict(measure_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


