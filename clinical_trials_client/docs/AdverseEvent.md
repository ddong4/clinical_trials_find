# AdverseEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | **str** |  | [optional] 
**organ_system** | **str** |  | [optional] 
**source_vocabulary** | **str** |  | [optional] 
**assessment_type** | [**EventAssessment**](EventAssessment.md) |  | [optional] 
**notes** | **str** |  | [optional] 
**stats** | [**List[EventStats]**](EventStats.md) |  | [optional] 

## Example

```python
from openapi_client.models.adverse_event import AdverseEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AdverseEvent from a JSON string
adverse_event_instance = AdverseEvent.from_json(json)
# print the JSON string representation of the object
print(AdverseEvent.to_json())

# convert the object into a dict
adverse_event_dict = adverse_event_instance.to_dict()
# create an instance of AdverseEvent from a dict
adverse_event_from_dict = AdverseEvent.from_dict(adverse_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


