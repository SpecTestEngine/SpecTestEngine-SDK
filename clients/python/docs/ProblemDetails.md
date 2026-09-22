# ProblemDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  |
**status** | **int** |  |
**error** | **str** |  |
**message** | **str** |  |
**path** | **str** |  |
**error_code** | **str** |  |
**translation_key** | **str** |  | [optional]
**request_id** | **str** |  | [optional]
**violations** | **List[Dict[str, object]]** |  | [optional]

## Example

```python
from spectestengine_sdk.models.problem_details import ProblemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemDetails from a JSON string
problem_details_instance = ProblemDetails.from_json(json)
# print the JSON string representation of the object
print(ProblemDetails.to_json())

# convert the object into a dict
problem_details_dict = problem_details_instance.to_dict()
# create an instance of ProblemDetails from a dict
problem_details_from_dict = ProblemDetails.from_dict(problem_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


