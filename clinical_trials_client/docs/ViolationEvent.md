# ViolationEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ViolationEventType**](ViolationEventType.md) |  | [optional] 
**description** | **str** |  | [optional] 
**creation_date** | **date** |  | [optional] 
**issued_date** | **date** |  | [optional] 
**release_date** | **date** |  | [optional] 
**posted_date** | **date** |  | [optional] 

## Example

```python
from openapi_client.models.violation_event import ViolationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ViolationEvent from a JSON string
violation_event_instance = ViolationEvent.from_json(json)
# print the JSON string representation of the object
print(ViolationEvent.to_json())

# convert the object into a dict
violation_event_dict = violation_event_instance.to_dict()
# create an instance of ViolationEvent from a dict
violation_event_from_dict = ViolationEvent.from_dict(violation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


