# ReferencesModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**references** | [**List[Reference]**](Reference.md) |  | [optional] 
**see_also_links** | [**List[SeeAlsoLink]**](SeeAlsoLink.md) |  | [optional] 
**avail_ipds** | [**List[AvailIpd]**](AvailIpd.md) |  | [optional] 

## Example

```python
from openapi_client.models.references_module import ReferencesModule

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencesModule from a JSON string
references_module_instance = ReferencesModule.from_json(json)
# print the JSON string representation of the object
print(ReferencesModule.to_json())

# convert the object into a dict
references_module_dict = references_module_instance.to_dict()
# create an instance of ReferencesModule from a dict
references_module_from_dict = ReferencesModule.from_dict(references_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


