# DateStruct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**type** | [**DateType**](DateType.md) |  | [optional] 

## Example

```python
from openapi_client.models.date_struct import DateStruct

# TODO update the JSON string below
json = "{}"
# create an instance of DateStruct from a JSON string
date_struct_instance = DateStruct.from_json(json)
# print the JSON string representation of the object
print(DateStruct.to_json())

# convert the object into a dict
date_struct_dict = date_struct_instance.to_dict()
# create an instance of DateStruct from a dict
date_struct_from_dict = DateStruct.from_dict(date_struct_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


