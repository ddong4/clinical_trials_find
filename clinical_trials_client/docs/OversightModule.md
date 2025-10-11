# OversightModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oversight_has_dmc** | **bool** |  | [optional] 
**is_fda_regulated_drug** | **bool** |  | [optional] 
**is_fda_regulated_device** | **bool** |  | [optional] 
**is_unapproved_device** | **bool** |  | [optional] 
**is_ppsd** | **bool** |  | [optional] 
**is_us_export** | **bool** |  | [optional] 
**fdaaa801_violation** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.oversight_module import OversightModule

# TODO update the JSON string below
json = "{}"
# create an instance of OversightModule from a JSON string
oversight_module_instance = OversightModule.from_json(json)
# print the JSON string representation of the object
print(OversightModule.to_json())

# convert the object into a dict
oversight_module_dict = oversight_module_instance.to_dict()
# create an instance of OversightModule from a dict
oversight_module_from_dict = OversightModule.from_dict(oversight_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


