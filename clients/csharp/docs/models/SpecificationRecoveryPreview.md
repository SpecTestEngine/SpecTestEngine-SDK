# SpecTestEngine.Sdk.Model.SpecificationRecoveryPreview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SpecId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SpecName** | **string** |  |
**SpecType** | **SpecType** |  |
**CurrentSpec** | **Dictionary&lt;string, Object&gt;** |  |
**RecoveredSpec** | **Dictionary&lt;string, Object&gt;** |  |
**CurrentRawSpec** | **string** |  |
**RecoveredRawSpec** | **string** |  |
**SourceRunId** | **Guid** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SourceRunStatus** | **string** | Completed passing or assertion-failing status as retained by the owning engine. |
**Changes** | [**List&lt;SpecificationRecoveryChange&gt;**](SpecificationRecoveryChange.md) |  |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

