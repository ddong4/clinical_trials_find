# MiscInfoModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_holder** | **date** |  | [optional] 
**removed_countries** | **List[str]** |  | [optional] 
**submission_tracking** | [**SubmissionTracking**](SubmissionTracking.md) |  | [optional] 

## Example

```python
from openapi_client.models.misc_info_module import MiscInfoModule

# TODO update the JSON string below
json = "{}"
# create an instance of MiscInfoModule from a JSON string
misc_info_module_instance = MiscInfoModule.from_json(json)
# print the JSON string representation of the object
print(MiscInfoModule.to_json())

# convert the object into a dict
misc_info_module_dict = misc_info_module_instance.to_dict()
# create an instance of MiscInfoModule from a dict
misc_info_module_from_dict = MiscInfoModule.from_dict(misc_info_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


