

# AtfValidationResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**projectName** | **String** |  |  |
|**exportMode** | [**ExportModeEnum**](#ExportModeEnum) |  |  |
|**buildTool** | [**BuildToolEnum**](#BuildToolEnum) |  |  |
|**validationPassed** | **Boolean** |  |  |
|**suggestedCommand** | **String** |  |  |
|**steps** | [**List&lt;AtfValidationStep&gt;**](AtfValidationStep.md) |  |  |



## Enum: ExportModeEnum

| Name | Value |
|---- | -----|
| STANDALONE_PROJECT | &quot;STANDALONE_PROJECT&quot; |
| IN_PROJECT_HTTP_TESTS | &quot;IN_PROJECT_HTTP_TESTS&quot; |
| SPRING_BOOT_COMPONENT_TESTS | &quot;SPRING_BOOT_COMPONENT_TESTS&quot; |



## Enum: BuildToolEnum

| Name | Value |
|---- | -----|
| GRADLE | &quot;GRADLE&quot; |
| MAVEN | &quot;MAVEN&quot; |



