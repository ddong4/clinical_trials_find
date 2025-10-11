# EventGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**deaths_num_affected** | **int** |  | [optional] 
**deaths_num_at_risk** | **int** |  | [optional] 
**serious_num_affected** | **int** |  | [optional] 
**serious_num_at_risk** | **int** |  | [optional] 
**other_num_affected** | **int** |  | [optional] 
**other_num_at_risk** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.event_group import EventGroup

# TODO update the JSON string below
json = "{}"
# create an instance of EventGroup from a JSON string
event_group_instance = EventGroup.from_json(json)
# print the JSON string representation of the object
print(EventGroup.to_json())

# convert the object into a dict
event_group_dict = event_group_instance.to_dict()
# create an instance of EventGroup from a dict
event_group_from_dict = EventGroup.from_dict(event_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


