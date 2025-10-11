# OutcomesModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_outcomes** | [**List[Outcome]**](Outcome.md) |  | [optional] 
**secondary_outcomes** | [**List[Outcome]**](Outcome.md) |  | [optional] 
**other_outcomes** | [**List[Outcome]**](Outcome.md) |  | [optional] 

## Example

```python
from openapi_client.models.outcomes_module import OutcomesModule

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomesModule from a JSON string
outcomes_module_instance = OutcomesModule.from_json(json)
# print the JSON string representation of the object
print(OutcomesModule.to_json())

# convert the object into a dict
outcomes_module_dict = outcomes_module_instance.to_dict()
# create an instance of OutcomesModule from a dict
outcomes_module_from_dict = OutcomesModule.from_dict(outcomes_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


