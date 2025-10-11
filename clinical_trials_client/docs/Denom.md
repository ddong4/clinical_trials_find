# Denom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | **str** |  | [optional] 
**counts** | [**List[DenomCount]**](DenomCount.md) |  | [optional] 

## Example

```python
from openapi_client.models.denom import Denom

# TODO update the JSON string below
json = "{}"
# create an instance of Denom from a JSON string
denom_instance = Denom.from_json(json)
# print the JSON string representation of the object
print(Denom.to_json())

# convert the object into a dict
denom_dict = denom_instance.to_dict()
# create an instance of Denom from a dict
denom_from_dict = Denom.from_dict(denom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


