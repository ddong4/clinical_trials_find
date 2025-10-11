# ExpandedAccessInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_expanded_access** | **bool** |  | [optional] 
**nct_id** | **str** | NCT number | [optional] 
**status_for_nct_id** | [**ExpandedAccessStatus**](ExpandedAccessStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.expanded_access_info import ExpandedAccessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedAccessInfo from a JSON string
expanded_access_info_instance = ExpandedAccessInfo.from_json(json)
# print the JSON string representation of the object
print(ExpandedAccessInfo.to_json())

# convert the object into a dict
expanded_access_info_dict = expanded_access_info_instance.to_dict()
# create an instance of ExpandedAccessInfo from a dict
expanded_access_info_from_dict = ExpandedAccessInfo.from_dict(expanded_access_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


