# DropWithdraw


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**reasons** | [**List[FlowStats]**](FlowStats.md) |  | [optional] 

## Example

```python
from openapi_client.models.drop_withdraw import DropWithdraw

# TODO update the JSON string below
json = "{}"
# create an instance of DropWithdraw from a JSON string
drop_withdraw_instance = DropWithdraw.from_json(json)
# print the JSON string representation of the object
print(DropWithdraw.to_json())

# convert the object into a dict
drop_withdraw_dict = drop_withdraw_instance.to_dict()
# create an instance of DropWithdraw from a dict
drop_withdraw_from_dict = DropWithdraw.from_dict(drop_withdraw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


