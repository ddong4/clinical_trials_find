# PointOfContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**phone_ext** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.point_of_contact import PointOfContact

# TODO update the JSON string below
json = "{}"
# create an instance of PointOfContact from a JSON string
point_of_contact_instance = PointOfContact.from_json(json)
# print the JSON string representation of the object
print(PointOfContact.to_json())

# convert the object into a dict
point_of_contact_dict = point_of_contact_instance.to_dict()
# create an instance of PointOfContact from a dict
point_of_contact_from_dict = PointOfContact.from_dict(point_of_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


