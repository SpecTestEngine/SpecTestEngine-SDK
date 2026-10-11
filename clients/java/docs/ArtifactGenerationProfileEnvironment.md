

# ArtifactGenerationProfileEnvironment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**environmentKey** | **String** |  |  |
|**resolutionMode** | [**ResolutionModeEnum**](#ResolutionModeEnum) |  |  |
|**baseUrlMode** | **AtfBaseUrlMode** |  |  [optional] |
|**baseUrlVariableName** | **String** |  |  [optional] |
|**snapshotBundleHash** | **String** |  |  [optional] |
|**snapshotAt** | **OffsetDateTime** |  |  [optional] |
|**cachedBundleHash** | **String** |  |  [optional] |
|**cachedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: ResolutionModeEnum

| Name | Value |
|---- | -----|
| LATEST | &quot;LATEST&quot; |
| CACHED | &quot;CACHED&quot; |
| PINNED | &quot;PINNED&quot; |
| FAIL_ON_DRIFT | &quot;FAIL_ON_DRIFT&quot; |
