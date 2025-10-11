# DesignInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation** | [**DesignAllocation**](DesignAllocation.md) |  | [optional] 
**intervention_model** | [**InterventionalAssignment**](InterventionalAssignment.md) |  | [optional] 
**intervention_model_description** | **str** |  | [optional] 
**primary_purpose** | [**PrimaryPurpose**](PrimaryPurpose.md) |  | [optional] 
**observational_model** | [**ObservationalModel**](ObservationalModel.md) |  | [optional] 
**time_perspective** | [**DesignTimePerspective**](DesignTimePerspective.md) |  | [optional] 
**masking_info** | [**MaskingBlock**](MaskingBlock.md) |  | [optional] 

## Example

```python
from openapi_client.models.design_info import DesignInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DesignInfo from a JSON string
design_info_instance = DesignInfo.from_json(json)
# print the JSON string representation of the object
print(DesignInfo.to_json())

# convert the object into a dict
design_info_dict = design_info_instance.to_dict()
# create an instance of DesignInfo from a dict
design_info_from_dict = DesignInfo.from_dict(design_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


