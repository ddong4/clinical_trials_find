# EventStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | [optional] 
**num_events** | **int** |  | [optional] 
**num_affected** | **int** |  | [optional] 
**num_at_risk** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.event_stats import EventStats

# TODO update the JSON string below
json = "{}"
# create an instance of EventStats from a JSON string
event_stats_instance = EventStats.from_json(json)
# print the JSON string representation of the object
print(EventStats.to_json())

# convert the object into a dict
event_stats_dict = event_stats_instance.to_dict()
# create an instance of EventStats from a dict
event_stats_from_dict = EventStats.from_dict(event_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


