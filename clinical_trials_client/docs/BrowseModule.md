# BrowseModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meshes** | [**List[Mesh]**](Mesh.md) |  | [optional] 
**ancestors** | [**List[Mesh]**](Mesh.md) |  | [optional] 
**browse_leaves** | [**List[BrowseLeaf]**](BrowseLeaf.md) |  | [optional] 
**browse_branches** | [**List[BrowseBranch]**](BrowseBranch.md) |  | [optional] 

## Example

```python
from openapi_client.models.browse_module import BrowseModule

# TODO update the JSON string below
json = "{}"
# create an instance of BrowseModule from a JSON string
browse_module_instance = BrowseModule.from_json(json)
# print the JSON string representation of the object
print(BrowseModule.to_json())

# convert the object into a dict
browse_module_dict = browse_module_instance.to_dict()
# create an instance of BrowseModule from a dict
browse_module_from_dict = BrowseModule.from_dict(browse_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


