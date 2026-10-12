# FlowRecoveryDraftInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manifest_hash** | **str** |  |
**mode** | **str** |  |
**draft** | **Dict[str, object]** | Ordinary Flow create/update authoring shape, up to 16 MiB. Preserve retained visual references for owner validation. |
**expected_flow_revision** | **int** |  |
**source_step_ids** | **List[Optional[UUID]]** | One original occurrence UUID per ordered draft step, or null for an added step. Identity does not grant authority. |
**dependency_revisions** | **Dict[str, int]** |  |
**bindings** | **Dict[str, object]** | Exactly required selected bindings. Preserve scalar types; never invent old literal inputs. Not retained in the journal. |

## Example

```python
from spectestengine_sdk.models.flow_recovery_draft_input import FlowRecoveryDraftInput

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRecoveryDraftInput from a JSON string
flow_recovery_draft_input_instance = FlowRecoveryDraftInput.from_json(json)
# print the JSON string representation of the object
print(FlowRecoveryDraftInput.to_json())

# convert the object into a dict
flow_recovery_draft_input_dict = flow_recovery_draft_input_instance.to_dict()
# create an instance of FlowRecoveryDraftInput from a dict
flow_recovery_draft_input_from_dict = FlowRecoveryDraftInput.from_dict(flow_recovery_draft_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
