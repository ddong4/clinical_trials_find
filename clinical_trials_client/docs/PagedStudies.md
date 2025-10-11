# PagedStudies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** |  | [optional] 
**studies** | [**List[Study]**](Study.md) | &#x60;study&#x60; field values of type &#x60;markup&#x60; are in markdown format.  | 
**total_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.paged_studies import PagedStudies

# TODO update the JSON string below
json = "{}"
# create an instance of PagedStudies from a JSON string
paged_studies_instance = PagedStudies.from_json(json)
# print the JSON string representation of the object
print(PagedStudies.to_json())

# convert the object into a dict
paged_studies_dict = paged_studies_instance.to_dict()
# create an instance of PagedStudies from a dict
paged_studies_from_dict = PagedStudies.from_dict(paged_studies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


