

# SpecificationRecoveryPreview


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**specId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**specName** | **String** |  |  |
|**specType** | **SpecType** |  |  |
|**currentSpec** | **Map&lt;String, Object&gt;** |  |  |
|**recoveredSpec** | **Map&lt;String, Object&gt;** |  |  |
|**currentRawSpec** | **String** |  |  |
|**recoveredRawSpec** | **String** |  |  |
|**sourceRunId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**sourceRunStatus** | **String** | Completed passing or assertion-failing status as retained by the owning engine. |  |
|**changes** | [**List&lt;SpecificationRecoveryChange&gt;**](SpecificationRecoveryChange.md) |  |  |



