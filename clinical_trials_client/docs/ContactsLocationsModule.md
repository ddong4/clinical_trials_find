# ContactsLocationsModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**central_contacts** | [**List[Contact]**](Contact.md) |  | [optional] 
**overall_officials** | [**List[Official]**](Official.md) |  | [optional] 
**locations** | [**List[Location]**](Location.md) |  | [optional] 

## Example

```python
from openapi_client.models.contacts_locations_module import ContactsLocationsModule

# TODO update the JSON string below
json = "{}"
# create an instance of ContactsLocationsModule from a JSON string
contacts_locations_module_instance = ContactsLocationsModule.from_json(json)
# print the JSON string representation of the object
print(ContactsLocationsModule.to_json())

# convert the object into a dict
contacts_locations_module_dict = contacts_locations_module_instance.to_dict()
# create an instance of ContactsLocationsModule from a dict
contacts_locations_module_from_dict = ContactsLocationsModule.from_dict(contacts_locations_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


