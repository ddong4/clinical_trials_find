# SubmissionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_date** | **date** |  | [optional] 
**unrelease_date** | **date** |  | [optional] 
**unrelease_date_unknown** | **bool** |  | [optional] 
**reset_date** | **date** |  | [optional] 
**mcp_release_n** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.submission_info import SubmissionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionInfo from a JSON string
submission_info_instance = SubmissionInfo.from_json(json)
# print the JSON string representation of the object
print(SubmissionInfo.to_json())

# convert the object into a dict
submission_info_dict = submission_info_instance.to_dict()
# create an instance of SubmissionInfo from a dict
submission_info_from_dict = SubmissionInfo.from_dict(submission_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


