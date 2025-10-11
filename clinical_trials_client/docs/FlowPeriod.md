# FlowPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**milestones** | [**List[FlowMilestone]**](FlowMilestone.md) |  | [optional] 
**drop_withdraws** | [**List[DropWithdraw]**](DropWithdraw.md) |  | [optional] 

## Example

```python
from openapi_client.models.flow_period import FlowPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of FlowPeriod from a JSON string
flow_period_instance = FlowPeriod.from_json(json)
# print the JSON string representation of the object
print(FlowPeriod.to_json())

# convert the object into a dict
flow_period_dict = flow_period_instance.to_dict()
# create an instance of FlowPeriod from a dict
flow_period_from_dict = FlowPeriod.from_dict(flow_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


