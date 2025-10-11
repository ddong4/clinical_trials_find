# IpdSharingStatementModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipd_sharing** | [**IpdSharing**](IpdSharing.md) |  | [optional] 
**description** | **str** |  | [optional] 
**info_types** | [**List[IpdSharingInfoType]**](IpdSharingInfoType.md) |  | [optional] 
**time_frame** | **str** |  | [optional] 
**access_criteria** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ipd_sharing_statement_module import IpdSharingStatementModule

# TODO update the JSON string below
json = "{}"
# create an instance of IpdSharingStatementModule from a JSON string
ipd_sharing_statement_module_instance = IpdSharingStatementModule.from_json(json)
# print the JSON string representation of the object
print(IpdSharingStatementModule.to_json())

# convert the object into a dict
ipd_sharing_statement_module_dict = ipd_sharing_statement_module_instance.to_dict()
# create an instance of IpdSharingStatementModule from a dict
ipd_sharing_statement_module_from_dict = IpdSharingStatementModule.from_dict(ipd_sharing_statement_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


