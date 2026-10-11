# StreamingSpecificationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**name** | **str** |  |
**description** | **str** |  | [optional]
**spec_type** | **str** |  |
**transport** | [**StreamingTransport**](StreamingTransport.md) |  |
**endpoint** | **str** | Streaming endpoint URI |
**codec** | **str** |  |
**created_at** | **datetime** |  |
**updated_at** | **datetime** |  |
**last_run_at** | **datetime** |  | [optional]
**last_run_status** | **str** |  | [optional]

## Example

```python
from spectestengine_sdk.models.streaming_specification_summary import StreamingSpecificationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingSpecificationSummary from a JSON string
streaming_specification_summary_instance = StreamingSpecificationSummary.from_json(json)
# print the JSON string representation of the object
print(StreamingSpecificationSummary.to_json())

# convert the object into a dict
streaming_specification_summary_dict = streaming_specification_summary_instance.to_dict()
# create an instance of StreamingSpecificationSummary from a dict
streaming_specification_summary_from_dict = StreamingSpecificationSummary.from_dict(streaming_specification_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
