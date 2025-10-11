# ViolationAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**violation_events** | [**List[ViolationEvent]**](ViolationEvent.md) |  | [optional] 

## Example

```python
from openapi_client.models.violation_annotation import ViolationAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of ViolationAnnotation from a JSON string
violation_annotation_instance = ViolationAnnotation.from_json(json)
# print the JSON string representation of the object
print(ViolationAnnotation.to_json())

# convert the object into a dict
violation_annotation_dict = violation_annotation_instance.to_dict()
# create an instance of ViolationAnnotation from a dict
violation_annotation_from_dict = ViolationAnnotation.from_dict(violation_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


