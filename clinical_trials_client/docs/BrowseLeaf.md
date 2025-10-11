# BrowseLeaf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**as_found** | **str** |  | [optional] 
**relevance** | [**BrowseLeafRelevance**](BrowseLeafRelevance.md) |  | [optional] 

## Example

```python
from openapi_client.models.browse_leaf import BrowseLeaf

# TODO update the JSON string below
json = "{}"
# create an instance of BrowseLeaf from a JSON string
browse_leaf_instance = BrowseLeaf.from_json(json)
# print the JSON string representation of the object
print(BrowseLeaf.to_json())

# convert the object into a dict
browse_leaf_dict = browse_leaf_instance.to_dict()
# create an instance of BrowseLeaf from a dict
browse_leaf_from_dict = BrowseLeaf.from_dict(browse_leaf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


