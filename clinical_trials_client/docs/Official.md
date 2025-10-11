# Official


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**affiliation** | **str** |  | [optional] 
**role** | [**OfficialRole**](OfficialRole.md) |  | [optional] 

## Example

```python
from openapi_client.models.official import Official

# TODO update the JSON string below
json = "{}"
# create an instance of Official from a JSON string
official_instance = Official.from_json(json)
# print the JSON string representation of the object
print(Official.to_json())

# convert the object into a dict
official_dict = official_instance.to_dict()
# create an instance of Official from a dict
official_from_dict = Official.from_dict(official_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


