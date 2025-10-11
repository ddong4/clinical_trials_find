# PartialDateStruct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date in &#x60;yyyy&#x60;, &#x60;yyyy-MM&#x60;, or &#x60;yyyy-MM-dd&#x60; format | [optional] 
**type** | [**DateType**](DateType.md) |  | [optional] 

## Example

```python
from openapi_client.models.partial_date_struct import PartialDateStruct

# TODO update the JSON string below
json = "{}"
# create an instance of PartialDateStruct from a JSON string
partial_date_struct_instance = PartialDateStruct.from_json(json)
# print the JSON string representation of the object
print(PartialDateStruct.to_json())

# convert the object into a dict
partial_date_struct_dict = partial_date_struct_instance.to_dict()
# create an instance of PartialDateStruct from a dict
partial_date_struct_from_dict = PartialDateStruct.from_dict(partial_date_struct_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


