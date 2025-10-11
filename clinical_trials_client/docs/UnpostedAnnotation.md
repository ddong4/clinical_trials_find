# UnpostedAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unposted_responsible_party** | **str** |  | [optional] 
**unposted_events** | [**List[UnpostedEvent]**](UnpostedEvent.md) |  | [optional] 

## Example

```python
from openapi_client.models.unposted_annotation import UnpostedAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of UnpostedAnnotation from a JSON string
unposted_annotation_instance = UnpostedAnnotation.from_json(json)
# print the JSON string representation of the object
print(UnpostedAnnotation.to_json())

# convert the object into a dict
unposted_annotation_dict = unposted_annotation_instance.to_dict()
# create an instance of UnpostedAnnotation from a dict
unposted_annotation_from_dict = UnpostedAnnotation.from_dict(unposted_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


