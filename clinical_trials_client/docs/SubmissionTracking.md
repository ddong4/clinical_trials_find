# SubmissionTracking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_results_first_submit_date** | **date** |  | [optional] 
**first_mcp_info** | [**FirstMcpInfo**](FirstMcpInfo.md) |  | [optional] 
**submission_infos** | [**List[SubmissionInfo]**](SubmissionInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.submission_tracking import SubmissionTracking

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionTracking from a JSON string
submission_tracking_instance = SubmissionTracking.from_json(json)
# print the JSON string representation of the object
print(SubmissionTracking.to_json())

# convert the object into a dict
submission_tracking_dict = submission_tracking_instance.to_dict()
# create an instance of SubmissionTracking from a dict
submission_tracking_from_dict = SubmissionTracking.from_dict(submission_tracking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


