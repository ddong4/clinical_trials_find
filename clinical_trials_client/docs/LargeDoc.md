# LargeDoc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_abbrev** | **str** |  | [optional] 
**has_protocol** | **bool** |  | [optional] 
**has_sap** | **bool** |  | [optional] 
**has_icf** | **bool** |  | [optional] 
**label** | **str** |  | [optional] 
**var_date** | **date** |  | [optional] 
**upload_date** | **str** | Date and time in &#x60;yyyy-MM-dd&#39;T&#39;HH:mm&#x60; format | [optional] 
**filename** | **str** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.large_doc import LargeDoc

# TODO update the JSON string below
json = "{}"
# create an instance of LargeDoc from a JSON string
large_doc_instance = LargeDoc.from_json(json)
# print the JSON string representation of the object
print(LargeDoc.to_json())

# convert the object into a dict
large_doc_dict = large_doc_instance.to_dict()
# create an instance of LargeDoc from a dict
large_doc_from_dict = LargeDoc.from_dict(large_doc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


