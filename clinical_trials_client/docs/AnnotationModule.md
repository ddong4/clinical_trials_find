# AnnotationModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unposted_annotation** | [**UnpostedAnnotation**](UnpostedAnnotation.md) |  | [optional] 
**violation_annotation** | [**ViolationAnnotation**](ViolationAnnotation.md) |  | [optional] 

## Example

```python
from openapi_client.models.annotation_module import AnnotationModule

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationModule from a JSON string
annotation_module_instance = AnnotationModule.from_json(json)
# print the JSON string representation of the object
print(AnnotationModule.to_json())

# convert the object into a dict
annotation_module_dict = annotation_module_instance.to_dict()
# create an instance of AnnotationModule from a dict
annotation_module_from_dict = AnnotationModule.from_dict(annotation_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


