# FlowStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**num_subjects** | **str** |  | [optional] 
**num_units** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.flow_stats import FlowStats

# TODO update the JSON string below
json = "{}"
# create an instance of FlowStats from a JSON string
flow_stats_instance = FlowStats.from_json(json)
# print the JSON string representation of the object
print(FlowStats.to_json())

# convert the object into a dict
flow_stats_dict = flow_stats_instance.to_dict()
# create an instance of FlowStats from a dict
flow_stats_from_dict = FlowStats.from_dict(flow_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


