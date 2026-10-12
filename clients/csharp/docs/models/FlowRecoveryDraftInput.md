# SpecTestEngine.Sdk.Model.FlowRecoveryDraftInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ManifestHash** | **string** |  |
**Mode** | **string** |  |
**Draft** | **Dictionary&lt;string, Object&gt;** | Ordinary Flow create/update authoring shape, up to 16 MiB. Preserve retained visual references for owner validation. |
**ExpectedFlowRevision** | **long** |  |
**SourceStepIds** | **List&lt;Guid&gt;** | One original occurrence UUID per ordered draft step, or null for an added step. Identity does not grant authority. |
**DependencyRevisions** | **Dictionary&lt;string, long&gt;** |  |
**Bindings** | **Dictionary&lt;string, Object&gt;** | Exactly required selected bindings. Preserve scalar types; never invent old literal inputs. Not retained in the journal. |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
