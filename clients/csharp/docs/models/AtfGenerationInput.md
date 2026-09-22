# SpecTestEngine.Sdk.Model.AtfGenerationInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectName** | **string** |  |
**PackageName** | **string** |  |
**TargetFramework** | **string** |  | [optional]
**ExportMode** | **string** |  | [optional]
**BuildTool** | **string** |  | [optional]
**JavaVersion** | **int** |  | [optional]
**BaseUrlMode** | **AtfBaseUrlMode** |  | [optional]
**BaseUrlVariableName** | **string** |  | [optional]
**Specs** | [**List&lt;ArtifactSpecRef&gt;**](ArtifactSpecRef.md) |  | [optional]
**FlowIds** | **List&lt;Guid&gt;** |  | [optional]
**UiMacroIds** | **List&lt;Guid&gt;** |  | [optional]
**IncludeSupportFiles** | **bool** |  | [optional]
**IncludeCoverage** | **bool** |  | [optional]
**CiProvider** | **string** |  | [optional]
**UnsupportedFeatureMode** | **string** | FAIL is recommended for CI because unsupported flow steps must not silently disappear from an export. | [optional] [default to UnsupportedFeatureModeEnum.FAIL]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

