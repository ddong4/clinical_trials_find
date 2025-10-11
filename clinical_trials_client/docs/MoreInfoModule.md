# MoreInfoModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limitations_and_caveats** | [**LimitationsAndCaveats**](LimitationsAndCaveats.md) |  | [optional] 
**certain_agreement** | [**CertainAgreement**](CertainAgreement.md) |  | [optional] 
**point_of_contact** | [**PointOfContact**](PointOfContact.md) |  | [optional] 

## Example

```python
from openapi_client.models.more_info_module import MoreInfoModule

# TODO update the JSON string below
json = "{}"
# create an instance of MoreInfoModule from a JSON string
more_info_module_instance = MoreInfoModule.from_json(json)
# print the JSON string representation of the object
print(MoreInfoModule.to_json())

# convert the object into a dict
more_info_module_dict = more_info_module_instance.to_dict()
# create an instance of MoreInfoModule from a dict
more_info_module_from_dict = MoreInfoModule.from_dict(more_info_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


