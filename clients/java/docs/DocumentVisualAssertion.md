

# DocumentVisualAssertion

Persistent masked-render assertion. Protocol engines contact Browser Engine only when excludedRegions is non-empty and the local attachment hash or fingerprint failed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**version** | [**VersionEnum**](#VersionEnum) |  |  |
|**algorithm** | [**AlgorithmEnum**](#AlgorithmEnum) |  |  |
|**renderProfile** | **String** |  |  |
|**pages** | [**List&lt;DocumentVisualAssertionPage&gt;**](DocumentVisualAssertionPage.md) |  |  |
|**excludedRegions** | [**List&lt;DocumentVisualExcludedRegion&gt;**](DocumentVisualExcludedRegion.md) |  |  |



## Enum: VersionEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |



## Enum: AlgorithmEnum

| Name | Value |
|---- | -----|
| MASKED_RENDER_SHA256_V1 | &quot;MASKED_RENDER_SHA256_V1&quot; |



