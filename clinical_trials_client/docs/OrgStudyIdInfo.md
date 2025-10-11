# OrgStudyIdInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**OrgStudyIdType**](OrgStudyIdType.md) |  | [optional] 
**link** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.org_study_id_info import OrgStudyIdInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrgStudyIdInfo from a JSON string
org_study_id_info_instance = OrgStudyIdInfo.from_json(json)
# print the JSON string representation of the object
print(OrgStudyIdInfo.to_json())

# convert the object into a dict
org_study_id_info_dict = org_study_id_info_instance.to_dict()
# create an instance of OrgStudyIdInfo from a dict
org_study_id_info_from_dict = OrgStudyIdInfo.from_dict(org_study_id_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


