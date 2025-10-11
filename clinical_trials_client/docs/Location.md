# Location


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility** | **str** |  | [optional] 
**status** | [**RecruitmentStatus**](RecruitmentStatus.md) |  | [optional] 
**city** | **str** | State/province or city name | [optional] 
**state** | **str** | State/province or city name | [optional] 
**zip** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**contacts** | [**List[Contact]**](Contact.md) |  | [optional] 
**geo_point** | [**GeoPoint**](GeoPoint.md) |  | [optional] 

## Example

```python
from openapi_client.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print(Location.to_json())

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_from_dict = Location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


