# FlowMilestone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**achievements** | [**List[FlowStats]**](FlowStats.md) |  | [optional] 

## Example

```python
from openapi_client.models.flow_milestone import FlowMilestone

# TODO update the JSON string below
json = "{}"
# create an instance of FlowMilestone from a JSON string
flow_milestone_instance = FlowMilestone.from_json(json)
# print the JSON string representation of the object
print(FlowMilestone.to_json())

# convert the object into a dict
flow_milestone_dict = flow_milestone_instance.to_dict()
# create an instance of FlowMilestone from a dict
flow_milestone_from_dict = FlowMilestone.from_dict(flow_milestone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


