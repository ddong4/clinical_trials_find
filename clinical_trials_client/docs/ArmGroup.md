# ArmGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | [**ArmGroupType**](ArmGroupType.md) |  | [optional] 
**description** | **str** |  | [optional] 
**intervention_names** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.arm_group import ArmGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ArmGroup from a JSON string
arm_group_instance = ArmGroup.from_json(json)
# print the JSON string representation of the object
print(ArmGroup.to_json())

# convert the object into a dict
arm_group_dict = arm_group_instance.to_dict()
# create an instance of ArmGroup from a dict
arm_group_from_dict = ArmGroup.from_dict(arm_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


