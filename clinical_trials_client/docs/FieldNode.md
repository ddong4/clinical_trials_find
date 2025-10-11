# FieldNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_piece_names** | **List[str]** |  | [optional] 
**children** | [**List[FieldNode]**](FieldNode.md) |  | [optional] 
**ded_link** | [**WebLink**](WebLink.md) |  | [optional] 
**description** | **str** |  | [optional] 
**historic_only** | **bool** |  | [optional] 
**indexed_only** | **bool** |  | [optional] 
**is_enum** | **bool** |  | [optional] 
**max_chars** | **int** |  | [optional] 
**name** | **str** |  | 
**nested** | **bool** |  | [optional] 
**piece** | **str** |  | 
**rules** | **str** |  | [optional] 
**source_type** | **str** |  | 
**synonyms** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.field_node import FieldNode

# TODO update the JSON string below
json = "{}"
# create an instance of FieldNode from a JSON string
field_node_instance = FieldNode.from_json(json)
# print the JSON string representation of the object
print(FieldNode.to_json())

# convert the object into a dict
field_node_dict = field_node_instance.to_dict()
# create an instance of FieldNode from a dict
field_node_from_dict = FieldNode.from_dict(field_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


