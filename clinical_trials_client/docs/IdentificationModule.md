# IdentificationModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nct_id** | **str** | NCT number | [optional] 
**nct_id_aliases** | **List[str]** |  | [optional] 
**org_study_id_info** | [**OrgStudyIdInfo**](OrgStudyIdInfo.md) |  | [optional] 
**secondary_id_infos** | [**List[SecondaryIdInfo]**](SecondaryIdInfo.md) |  | [optional] 
**brief_title** | **str** |  | [optional] 
**official_title** | **str** |  | [optional] 
**acronym** | **str** |  | [optional] 
**organization** | [**Organization**](Organization.md) |  | [optional] 

## Example

```python
from openapi_client.models.identification_module import IdentificationModule

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationModule from a JSON string
identification_module_instance = IdentificationModule.from_json(json)
# print the JSON string representation of the object
print(IdentificationModule.to_json())

# convert the object into a dict
identification_module_dict = identification_module_instance.to_dict()
# create an instance of IdentificationModule from a dict
identification_module_from_dict = IdentificationModule.from_dict(identification_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


