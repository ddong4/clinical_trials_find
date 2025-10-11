# MaskingBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**masking** | [**DesignMasking**](DesignMasking.md) |  | [optional] 
**masking_description** | **str** |  | [optional] 
**who_masked** | [**List[WhoMasked]**](WhoMasked.md) |  | [optional] 

## Example

```python
from openapi_client.models.masking_block import MaskingBlock

# TODO update the JSON string below
json = "{}"
# create an instance of MaskingBlock from a JSON string
masking_block_instance = MaskingBlock.from_json(json)
# print the JSON string representation of the object
print(MaskingBlock.to_json())

# convert the object into a dict
masking_block_dict = masking_block_instance.to_dict()
# create an instance of MaskingBlock from a dict
masking_block_from_dict = MaskingBlock.from_dict(masking_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


