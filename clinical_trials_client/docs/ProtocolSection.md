# ProtocolSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identification_module** | [**IdentificationModule**](IdentificationModule.md) |  | [optional] 
**status_module** | [**StatusModule**](StatusModule.md) |  | [optional] 
**sponsor_collaborators_module** | [**SponsorCollaboratorsModule**](SponsorCollaboratorsModule.md) |  | [optional] 
**oversight_module** | [**OversightModule**](OversightModule.md) |  | [optional] 
**description_module** | [**DescriptionModule**](DescriptionModule.md) |  | [optional] 
**conditions_module** | [**ConditionsModule**](ConditionsModule.md) |  | [optional] 
**design_module** | [**DesignModule**](DesignModule.md) |  | [optional] 
**arms_interventions_module** | [**ArmsInterventionsModule**](ArmsInterventionsModule.md) |  | [optional] 
**outcomes_module** | [**OutcomesModule**](OutcomesModule.md) |  | [optional] 
**eligibility_module** | [**EligibilityModule**](EligibilityModule.md) |  | [optional] 
**contacts_locations_module** | [**ContactsLocationsModule**](ContactsLocationsModule.md) |  | [optional] 
**references_module** | [**ReferencesModule**](ReferencesModule.md) |  | [optional] 
**ipd_sharing_statement_module** | [**IpdSharingStatementModule**](IpdSharingStatementModule.md) |  | [optional] 

## Example

```python
from openapi_client.models.protocol_section import ProtocolSection

# TODO update the JSON string below
json = "{}"
# create an instance of ProtocolSection from a JSON string
protocol_section_instance = ProtocolSection.from_json(json)
# print the JSON string representation of the object
print(ProtocolSection.to_json())

# convert the object into a dict
protocol_section_dict = protocol_section_instance.to_dict()
# create an instance of ProtocolSection from a dict
protocol_section_from_dict = ProtocolSection.from_dict(protocol_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


