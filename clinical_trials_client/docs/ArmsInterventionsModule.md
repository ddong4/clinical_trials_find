# ArmsInterventionsModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arm_groups** | [**List[ArmGroup]**](ArmGroup.md) |  | [optional] 
**interventions** | [**List[Intervention]**](Intervention.md) |  | [optional] 

## Example

```python
from openapi_client.models.arms_interventions_module import ArmsInterventionsModule

# TODO update the JSON string below
json = "{}"
# create an instance of ArmsInterventionsModule from a JSON string
arms_interventions_module_instance = ArmsInterventionsModule.from_json(json)
# print the JSON string representation of the object
print(ArmsInterventionsModule.to_json())

# convert the object into a dict
arms_interventions_module_dict = arms_interventions_module_instance.to_dict()
# create an instance of ArmsInterventionsModule from a dict
arms_interventions_module_from_dict = ArmsInterventionsModule.from_dict(arms_interventions_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


