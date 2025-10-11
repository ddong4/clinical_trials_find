# UnpostedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**UnpostedEventType**](UnpostedEventType.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**date_unknown** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.unposted_event import UnpostedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UnpostedEvent from a JSON string
unposted_event_instance = UnpostedEvent.from_json(json)
# print the JSON string representation of the object
print(UnpostedEvent.to_json())

# convert the object into a dict
unposted_event_dict = unposted_event_instance.to_dict()
# create an instance of UnpostedEvent from a dict
unposted_event_from_dict = UnpostedEvent.from_dict(unposted_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


