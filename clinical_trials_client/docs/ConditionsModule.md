# ConditionsModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | **List[str]** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.conditions_module import ConditionsModule

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionsModule from a JSON string
conditions_module_instance = ConditionsModule.from_json(json)
# print the JSON string representation of the object
print(ConditionsModule.to_json())

# convert the object into a dict
conditions_module_dict = conditions_module_instance.to_dict()
# create an instance of ConditionsModule from a dict
conditions_module_from_dict = ConditionsModule.from_dict(conditions_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


