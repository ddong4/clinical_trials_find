# DesignModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**study_type** | [**StudyType**](StudyType.md) |  | [optional] 
**n_ptrs_to_this_exp_acc_nct_id** | **int** |  | [optional] 
**expanded_access_types** | [**ExpandedAccessTypes**](ExpandedAccessTypes.md) |  | [optional] 
**patient_registry** | **bool** |  | [optional] 
**target_duration** | **str** |  | [optional] 
**phases** | [**List[Phase]**](Phase.md) |  | [optional] 
**design_info** | [**DesignInfo**](DesignInfo.md) |  | [optional] 
**bio_spec** | [**BioSpec**](BioSpec.md) |  | [optional] 
**enrollment_info** | [**EnrollmentInfo**](EnrollmentInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.design_module import DesignModule

# TODO update the JSON string below
json = "{}"
# create an instance of DesignModule from a JSON string
design_module_instance = DesignModule.from_json(json)
# print the JSON string representation of the object
print(DesignModule.to_json())

# convert the object into a dict
design_module_dict = design_module_instance.to_dict()
# create an instance of DesignModule from a dict
design_module_from_dict = DesignModule.from_dict(design_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


