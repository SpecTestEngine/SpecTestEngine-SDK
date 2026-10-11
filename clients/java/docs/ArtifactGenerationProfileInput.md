

# ArtifactGenerationProfileInput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**revision** | **Long** | Omit when creating. Send the last returned revision when updating. |  [optional] |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**artifactType** | [**ArtifactTypeEnum**](#ArtifactTypeEnum) |  |  |
|**selection** | [**ArtifactSelection**](ArtifactSelection.md) |  |  |
|**atf** | [**AtfProjectConfig**](AtfProjectConfig.md) |  |  |
|**environments** | [**List&lt;ArtifactGenerationProfileEnvironmentInput&gt;**](ArtifactGenerationProfileEnvironmentInput.md) |  |  |



## Enum: ArtifactTypeEnum

| Name | Value |
|---- | -----|
| ATF_PROJECT | &quot;ATF_PROJECT&quot; |
