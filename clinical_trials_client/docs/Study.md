# Study


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol_section** | [**ProtocolSection**](ProtocolSection.md) |  | [optional] 
**results_section** | [**ResultsSection**](ResultsSection.md) |  | [optional] 
**annotation_section** | [**AnnotationSection**](AnnotationSection.md) |  | [optional] 
**document_section** | [**DocumentSection**](DocumentSection.md) |  | [optional] 
**derived_section** | [**DerivedSection**](DerivedSection.md) |  | [optional] 
**has_results** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.study import Study

# TODO update the JSON string below
json = "{}"
# create an instance of Study from a JSON string
study_instance = Study.from_json(json)
# print the JSON string representation of the object
print(Study.to_json())

# convert the object into a dict
study_dict = study_instance.to_dict()
# create an instance of Study from a dict
study_from_dict = Study.from_dict(study_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


