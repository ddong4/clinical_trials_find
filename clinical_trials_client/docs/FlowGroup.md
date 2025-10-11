# FlowGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.flow_group import FlowGroup

# TODO update the JSON string below
json = "{}"
# create an instance of FlowGroup from a JSON string
flow_group_instance = FlowGroup.from_json(json)
# print the JSON string representation of the object
print(FlowGroup.to_json())

# convert the object into a dict
flow_group_dict = flow_group_instance.to_dict()
# create an instance of FlowGroup from a dict
flow_group_from_dict = FlowGroup.from_dict(flow_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


