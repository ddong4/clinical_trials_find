# CertainAgreement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pi_sponsor_employee** | **bool** |  | [optional] 
**restriction_type** | [**AgreementRestrictionType**](AgreementRestrictionType.md) |  | [optional] 
**restrictive_agreement** | **bool** |  | [optional] 
**other_details** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.certain_agreement import CertainAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of CertainAgreement from a JSON string
certain_agreement_instance = CertainAgreement.from_json(json)
# print the JSON string representation of the object
print(CertainAgreement.to_json())

# convert the object into a dict
certain_agreement_dict = certain_agreement_instance.to_dict()
# create an instance of CertainAgreement from a dict
certain_agreement_from_dict = CertainAgreement.from_dict(certain_agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


