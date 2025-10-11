# EligibilityModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligibility_criteria** | **str** |  | [optional] 
**healthy_volunteers** | **bool** |  | [optional] 
**sex** | [**Sex**](Sex.md) |  | [optional] 
**gender_based** | **bool** |  | [optional] 
**gender_description** | **str** |  | [optional] 
**minimum_age** | **str** |  | [optional] 
**maximum_age** | **str** |  | [optional] 
**std_ages** | [**List[StandardAge]**](StandardAge.md) |  | [optional] 
**study_population** | **str** |  | [optional] 
**sampling_method** | [**SamplingMethod**](SamplingMethod.md) |  | [optional] 

## Example

```python
from openapi_client.models.eligibility_module import EligibilityModule

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityModule from a JSON string
eligibility_module_instance = EligibilityModule.from_json(json)
# print the JSON string representation of the object
print(EligibilityModule.to_json())

# convert the object into a dict
eligibility_module_dict = eligibility_module_instance.to_dict()
# create an instance of EligibilityModule from a dict
eligibility_module_from_dict = EligibilityModule.from_dict(eligibility_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


