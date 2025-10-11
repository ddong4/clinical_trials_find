# SecondaryIdInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**SecondaryIdType**](SecondaryIdType.md) |  | [optional] 
**domain** | **str** |  | [optional] 
**link** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.secondary_id_info import SecondaryIdInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryIdInfo from a JSON string
secondary_id_info_instance = SecondaryIdInfo.from_json(json)
# print the JSON string representation of the object
print(SecondaryIdInfo.to_json())

# convert the object into a dict
secondary_id_info_dict = secondary_id_info_instance.to_dict()
# create an instance of SecondaryIdInfo from a dict
secondary_id_info_from_dict = SecondaryIdInfo.from_dict(secondary_id_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


