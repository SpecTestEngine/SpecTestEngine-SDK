

# AtfProjectConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**projectName** | **String** |  |  |
|**packageName** | **String** |  |  |
|**targetFramework** | [**TargetFrameworkEnum**](#TargetFrameworkEnum) |  |  |
|**exportMode** | [**ExportModeEnum**](#ExportModeEnum) |  |  |
|**buildTool** | [**BuildToolEnum**](#BuildToolEnum) |  |  |
|**javaVersion** | [**JavaVersionEnum**](#JavaVersionEnum) |  |  |
|**baseUrlMode** | **AtfBaseUrlMode** |  |  |
|**baseUrlVariableName** | **String** |  |  [optional] |
|**includeSupportFiles** | **Boolean** |  |  |
|**includeCoverage** | **Boolean** |  |  |
|**ciProvider** | [**CiProviderEnum**](#CiProviderEnum) |  |  |
|**unsupportedFeatureMode** | [**UnsupportedFeatureModeEnum**](#UnsupportedFeatureModeEnum) |  |  |



## Enum: TargetFrameworkEnum

| Name | Value |
|---- | -----|
| REST_ASSURED_JUNIT5 | &quot;REST_ASSURED_JUNIT5&quot; |
| REST_ASSURED_PLAYWRIGHT_JUNIT5 | &quot;REST_ASSURED_PLAYWRIGHT_JUNIT5&quot; |
| CUCUMBER_REST_ASSURED_PLAYWRIGHT | &quot;CUCUMBER_REST_ASSURED_PLAYWRIGHT&quot; |



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



## Enum: JavaVersionEnum

| Name | Value |
|---- | -----|
| NUMBER_17 | 17 |
| NUMBER_21 | 21 |
| NUMBER_25 | 25 |



## Enum: CiProviderEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| GITHUB_ACTIONS | &quot;GITHUB_ACTIONS&quot; |
| GITLAB_CI | &quot;GITLAB_CI&quot; |
| JENKINS | &quot;JENKINS&quot; |



## Enum: UnsupportedFeatureModeEnum

| Name | Value |
|---- | -----|
| WARN | &quot;WARN&quot; |
| FAIL | &quot;FAIL&quot; |



