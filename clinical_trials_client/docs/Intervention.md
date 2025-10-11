# Intervention


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InterventionType**](InterventionType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**arm_group_labels** | **List[str]** |  | [optional] 
**other_names** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.intervention import Intervention

# TODO update the JSON string below
json = "{}"
# create an instance of Intervention from a JSON string
intervention_instance = Intervention.from_json(json)
# print the JSON string representation of the object
print(Intervention.to_json())

# convert the object into a dict
intervention_dict = intervention_instance.to_dict()
# create an instance of Intervention from a dict
intervention_from_dict = Intervention.from_dict(intervention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


