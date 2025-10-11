# BioSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retention** | [**BioSpecRetention**](BioSpecRetention.md) |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bio_spec import BioSpec

# TODO update the JSON string below
json = "{}"
# create an instance of BioSpec from a JSON string
bio_spec_instance = BioSpec.from_json(json)
# print the JSON string representation of the object
print(BioSpec.to_json())

# convert the object into a dict
bio_spec_dict = bio_spec_instance.to_dict()
# create an instance of BioSpec from a dict
bio_spec_from_dict = BioSpec.from_dict(bio_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


