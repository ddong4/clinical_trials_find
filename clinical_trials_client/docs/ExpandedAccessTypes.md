# ExpandedAccessTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**individual** | **bool** |  | [optional] 
**intermediate** | **bool** |  | [optional] 
**treatment** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.expanded_access_types import ExpandedAccessTypes

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedAccessTypes from a JSON string
expanded_access_types_instance = ExpandedAccessTypes.from_json(json)
# print the JSON string representation of the object
print(ExpandedAccessTypes.to_json())

# convert the object into a dict
expanded_access_types_dict = expanded_access_types_instance.to_dict()
# create an instance of ExpandedAccessTypes from a dict
expanded_access_types_from_dict = ExpandedAccessTypes.from_dict(expanded_access_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


