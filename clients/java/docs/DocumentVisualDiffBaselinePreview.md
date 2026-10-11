

# DocumentVisualDiffBaselinePreview


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**visualDiffId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**sourceType** | **String** |  |  |
|**sourceRunId** | **String** |  |  [optional] |
|**sourceStepId** | **String** |  |  [optional] |
|**attachmentId** | **String** |  |  |
|**expectedAttachmentHash** | **String** |  |  |
|**expectedAttachmentFingerprint** | **String** | Serialized deterministic fingerprint for a new specification revision. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) |  |  |
|**proposedAssertion** | [**DocumentAttachmentAssertionBaseline**](DocumentAttachmentAssertionBaseline.md) |  |  |
|**confirmed** | **Boolean** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**message** | **String** |  |  |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| EXACT | &quot;EXACT&quot; |
| VISUAL_EXCLUSIONS | &quot;VISUAL_EXCLUSIONS&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PREVIEW | &quot;PREVIEW&quot; |
| DRAFT_READY | &quot;DRAFT_READY&quot; |
