

# DocumentVisualDiff


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**visualDiffId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**viewerUrl** | **URI** |  |  |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) |  |  |
|**sourceRunId** | **String** |  |  [optional] |
|**sourceStepId** | **String** |  |  [optional] |
|**attachmentId** | **String** |  |  |
|**actualContentType** | **String** |  |  |
|**actualSha256** | **String** |  |  |
|**expectedSha256** | **String** |  |  [optional] |
|**status** | **DocumentVisualDiffStatus** |  |  |
|**decision** | **DocumentVisualDiffDecision** |  |  |
|**actualPageCount** | **Integer** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**expiresAt** | **OffsetDateTime** |  |  |
|**actualAvailable** | **Boolean** |  |  |
|**expectedUploadRequired** | **Boolean** |  |  |
|**regenerateAvailable** | **Boolean** |  |  |
|**generations** | [**List&lt;DocumentVisualDiffGeneration&gt;**](DocumentVisualDiffGeneration.md) |  |  |
|**currentGeneration** | [**DocumentVisualDiffGeneration**](DocumentVisualDiffGeneration.md) |  |  [optional] |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| REST_SPEC_RUN | &quot;REST_SPEC_RUN&quot; |
| SOAP_SPEC_RUN | &quot;SOAP_SPEC_RUN&quot; |
| GRAPHQL_SPEC_RUN | &quot;GRAPHQL_SPEC_RUN&quot; |
| FLOW_RUN | &quot;FLOW_RUN&quot; |
| SPECIFICATION_RUN | &quot;SPECIFICATION_RUN&quot; |



