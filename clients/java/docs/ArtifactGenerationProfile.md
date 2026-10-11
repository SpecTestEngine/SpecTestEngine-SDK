

# ArtifactGenerationProfile


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**revision** | **Long** |  |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**artifactType** | [**ArtifactTypeEnum**](#ArtifactTypeEnum) |  |  |
|**selection** | [**ArtifactSelection**](ArtifactSelection.md) |  |  |
|**atf** | [**AtfProjectConfig**](AtfProjectConfig.md) |  |  |
|**environments** | [**List&lt;ArtifactGenerationProfileEnvironment&gt;**](ArtifactGenerationProfileEnvironment.md) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |



## Enum: ArtifactTypeEnum

| Name | Value |
|---- | -----|
| ATF_PROJECT | &quot;ATF_PROJECT&quot; |
