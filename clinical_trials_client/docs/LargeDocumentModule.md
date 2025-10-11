# LargeDocumentModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_sap** | **bool** |  | [optional] 
**large_docs** | [**List[LargeDoc]**](LargeDoc.md) |  | [optional] 

## Example

```python
from openapi_client.models.large_document_module import LargeDocumentModule

# TODO update the JSON string below
json = "{}"
# create an instance of LargeDocumentModule from a JSON string
large_document_module_instance = LargeDocumentModule.from_json(json)
# print the JSON string representation of the object
print(LargeDocumentModule.to_json())

# convert the object into a dict
large_document_module_dict = large_document_module_instance.to_dict()
# create an instance of LargeDocumentModule from a dict
large_document_module_from_dict = LargeDocumentModule.from_dict(large_document_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


