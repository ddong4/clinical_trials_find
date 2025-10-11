# ResponsibleParty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ResponsiblePartyType**](ResponsiblePartyType.md) |  | [optional] 
**investigator_full_name** | **str** |  | [optional] 
**investigator_title** | **str** |  | [optional] 
**investigator_affiliation** | **str** |  | [optional] 
**old_name_title** | **str** |  | [optional] 
**old_organization** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.responsible_party import ResponsibleParty

# TODO update the JSON string below
json = "{}"
# create an instance of ResponsibleParty from a JSON string
responsible_party_instance = ResponsibleParty.from_json(json)
# print the JSON string representation of the object
print(ResponsibleParty.to_json())

# convert the object into a dict
responsible_party_dict = responsible_party_instance.to_dict()
# create an instance of ResponsibleParty from a dict
responsible_party_from_dict = ResponsibleParty.from_dict(responsible_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


