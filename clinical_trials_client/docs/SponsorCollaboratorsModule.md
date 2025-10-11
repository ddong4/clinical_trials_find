# SponsorCollaboratorsModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responsible_party** | [**ResponsibleParty**](ResponsibleParty.md) |  | [optional] 
**lead_sponsor** | [**Sponsor**](Sponsor.md) |  | [optional] 
**collaborators** | [**List[Sponsor]**](Sponsor.md) |  | [optional] 

## Example

```python
from openapi_client.models.sponsor_collaborators_module import SponsorCollaboratorsModule

# TODO update the JSON string below
json = "{}"
# create an instance of SponsorCollaboratorsModule from a JSON string
sponsor_collaborators_module_instance = SponsorCollaboratorsModule.from_json(json)
# print the JSON string representation of the object
print(SponsorCollaboratorsModule.to_json())

# convert the object into a dict
sponsor_collaborators_module_dict = sponsor_collaborators_module_instance.to_dict()
# create an instance of SponsorCollaboratorsModule from a dict
sponsor_collaborators_module_from_dict = SponsorCollaboratorsModule.from_dict(sponsor_collaborators_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


