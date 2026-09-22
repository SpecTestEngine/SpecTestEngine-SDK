# AtfProjectConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectName** | **string** |  |
**PackageName** | **string** |  |
**TargetFramework** | **string** |  |
**ExportMode** | **string** |  |
**BuildTool** | **string** |  |
**JavaVersion** | **int32** |  |
**BaseUrlMode** | [**AtfBaseUrlMode**](AtfBaseUrlMode.md) |  |
**BaseUrlVariableName** | Pointer to **string** |  | [optional]
**IncludeSupportFiles** | **bool** |  |
**IncludeCoverage** | **bool** |  |
**CiProvider** | **string** |  |
**UnsupportedFeatureMode** | **string** |  | [default to "FAIL"]

## Methods

### NewAtfProjectConfig

`func NewAtfProjectConfig(projectName string, packageName string, targetFramework string, exportMode string, buildTool string, javaVersion int32, baseUrlMode AtfBaseUrlMode, includeSupportFiles bool, includeCoverage bool, ciProvider string, unsupportedFeatureMode string, ) *AtfProjectConfig`

NewAtfProjectConfig instantiates a new AtfProjectConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAtfProjectConfigWithDefaults

`func NewAtfProjectConfigWithDefaults() *AtfProjectConfig`

NewAtfProjectConfigWithDefaults instantiates a new AtfProjectConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProjectName

`func (o *AtfProjectConfig) GetProjectName() string`

GetProjectName returns the ProjectName field if non-nil, zero value otherwise.

### GetProjectNameOk

`func (o *AtfProjectConfig) GetProjectNameOk() (*string, bool)`

GetProjectNameOk returns a tuple with the ProjectName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectName

`func (o *AtfProjectConfig) SetProjectName(v string)`

SetProjectName sets ProjectName field to given value.


### GetPackageName

`func (o *AtfProjectConfig) GetPackageName() string`

GetPackageName returns the PackageName field if non-nil, zero value otherwise.

### GetPackageNameOk

`func (o *AtfProjectConfig) GetPackageNameOk() (*string, bool)`

GetPackageNameOk returns a tuple with the PackageName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPackageName

`func (o *AtfProjectConfig) SetPackageName(v string)`

SetPackageName sets PackageName field to given value.


### GetTargetFramework

`func (o *AtfProjectConfig) GetTargetFramework() string`

GetTargetFramework returns the TargetFramework field if non-nil, zero value otherwise.

### GetTargetFrameworkOk

`func (o *AtfProjectConfig) GetTargetFrameworkOk() (*string, bool)`

GetTargetFrameworkOk returns a tuple with the TargetFramework field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetFramework

`func (o *AtfProjectConfig) SetTargetFramework(v string)`

SetTargetFramework sets TargetFramework field to given value.


### GetExportMode

`func (o *AtfProjectConfig) GetExportMode() string`

GetExportMode returns the ExportMode field if non-nil, zero value otherwise.

### GetExportModeOk

`func (o *AtfProjectConfig) GetExportModeOk() (*string, bool)`

GetExportModeOk returns a tuple with the ExportMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExportMode

`func (o *AtfProjectConfig) SetExportMode(v string)`

SetExportMode sets ExportMode field to given value.


### GetBuildTool

`func (o *AtfProjectConfig) GetBuildTool() string`

GetBuildTool returns the BuildTool field if non-nil, zero value otherwise.

### GetBuildToolOk

`func (o *AtfProjectConfig) GetBuildToolOk() (*string, bool)`

GetBuildToolOk returns a tuple with the BuildTool field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuildTool

`func (o *AtfProjectConfig) SetBuildTool(v string)`

SetBuildTool sets BuildTool field to given value.


### GetJavaVersion

`func (o *AtfProjectConfig) GetJavaVersion() int32`

GetJavaVersion returns the JavaVersion field if non-nil, zero value otherwise.

### GetJavaVersionOk

`func (o *AtfProjectConfig) GetJavaVersionOk() (*int32, bool)`

GetJavaVersionOk returns a tuple with the JavaVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJavaVersion

`func (o *AtfProjectConfig) SetJavaVersion(v int32)`

SetJavaVersion sets JavaVersion field to given value.


### GetBaseUrlMode

`func (o *AtfProjectConfig) GetBaseUrlMode() AtfBaseUrlMode`

GetBaseUrlMode returns the BaseUrlMode field if non-nil, zero value otherwise.

### GetBaseUrlModeOk

`func (o *AtfProjectConfig) GetBaseUrlModeOk() (*AtfBaseUrlMode, bool)`

GetBaseUrlModeOk returns a tuple with the BaseUrlMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseUrlMode

`func (o *AtfProjectConfig) SetBaseUrlMode(v AtfBaseUrlMode)`

SetBaseUrlMode sets BaseUrlMode field to given value.


### GetBaseUrlVariableName

`func (o *AtfProjectConfig) GetBaseUrlVariableName() string`

GetBaseUrlVariableName returns the BaseUrlVariableName field if non-nil, zero value otherwise.

### GetBaseUrlVariableNameOk

`func (o *AtfProjectConfig) GetBaseUrlVariableNameOk() (*string, bool)`

GetBaseUrlVariableNameOk returns a tuple with the BaseUrlVariableName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseUrlVariableName

`func (o *AtfProjectConfig) SetBaseUrlVariableName(v string)`

SetBaseUrlVariableName sets BaseUrlVariableName field to given value.

### HasBaseUrlVariableName

`func (o *AtfProjectConfig) HasBaseUrlVariableName() bool`

HasBaseUrlVariableName returns a boolean if a field has been set.

### GetIncludeSupportFiles

`func (o *AtfProjectConfig) GetIncludeSupportFiles() bool`

GetIncludeSupportFiles returns the IncludeSupportFiles field if non-nil, zero value otherwise.

### GetIncludeSupportFilesOk

`func (o *AtfProjectConfig) GetIncludeSupportFilesOk() (*bool, bool)`

GetIncludeSupportFilesOk returns a tuple with the IncludeSupportFiles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeSupportFiles

`func (o *AtfProjectConfig) SetIncludeSupportFiles(v bool)`

SetIncludeSupportFiles sets IncludeSupportFiles field to given value.


### GetIncludeCoverage

`func (o *AtfProjectConfig) GetIncludeCoverage() bool`

GetIncludeCoverage returns the IncludeCoverage field if non-nil, zero value otherwise.

### GetIncludeCoverageOk

`func (o *AtfProjectConfig) GetIncludeCoverageOk() (*bool, bool)`

GetIncludeCoverageOk returns a tuple with the IncludeCoverage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeCoverage

`func (o *AtfProjectConfig) SetIncludeCoverage(v bool)`

SetIncludeCoverage sets IncludeCoverage field to given value.


### GetCiProvider

`func (o *AtfProjectConfig) GetCiProvider() string`

GetCiProvider returns the CiProvider field if non-nil, zero value otherwise.

### GetCiProviderOk

`func (o *AtfProjectConfig) GetCiProviderOk() (*string, bool)`

GetCiProviderOk returns a tuple with the CiProvider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCiProvider

`func (o *AtfProjectConfig) SetCiProvider(v string)`

SetCiProvider sets CiProvider field to given value.


### GetUnsupportedFeatureMode

`func (o *AtfProjectConfig) GetUnsupportedFeatureMode() string`

GetUnsupportedFeatureMode returns the UnsupportedFeatureMode field if non-nil, zero value otherwise.

### GetUnsupportedFeatureModeOk

`func (o *AtfProjectConfig) GetUnsupportedFeatureModeOk() (*string, bool)`

GetUnsupportedFeatureModeOk returns a tuple with the UnsupportedFeatureMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnsupportedFeatureMode

`func (o *AtfProjectConfig) SetUnsupportedFeatureMode(v string)`

SetUnsupportedFeatureMode sets UnsupportedFeatureMode field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


