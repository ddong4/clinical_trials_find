# DerivedSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**misc_info_module** | [**MiscInfoModule**](MiscInfoModule.md) |  | [optional] 
**condition_browse_module** | [**BrowseModule**](BrowseModule.md) |  | [optional] 
**intervention_browse_module** | [**BrowseModule**](BrowseModule.md) |  | [optional] 

## Example

```python
from openapi_client.models.derived_section import DerivedSection

# TODO update the JSON string below
json = "{}"
# create an instance of DerivedSection from a JSON string
derived_section_instance = DerivedSection.from_json(json)
# print the JSON string representation of the object
print(DerivedSection.to_json())

# convert the object into a dict
derived_section_dict = derived_section_instance.to_dict()
# create an instance of DerivedSection from a dict
derived_section_from_dict = DerivedSection.from_dict(derived_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


