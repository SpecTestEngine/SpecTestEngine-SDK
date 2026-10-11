# AtfGenerationInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectName** | **string** |  |
**PackageName** | **string** |  |
**TargetFramework** | Pointer to **string** |  | [optional]
**ExportMode** | Pointer to **string** |  | [optional]
**BuildTool** | Pointer to **string** |  | [optional]
**JavaVersion** | Pointer to **int32** |  | [optional]
**BaseUrlMode** | Pointer to [**AtfBaseUrlMode**](AtfBaseUrlMode.md) |  | [optional]
**BaseUrlVariableName** | Pointer to **string** |  | [optional]
**Specs** | Pointer to [**[]ArtifactSpecRef**](ArtifactSpecRef.md) |  | [optional]
**FlowIds** | Pointer to **[]string** |  | [optional]
**UiMacroIds** | Pointer to **[]string** |  | [optional]
**IncludeSupportFiles** | Pointer to **bool** |  | [optional]
**IncludeCoverage** | Pointer to **bool** |  | [optional]
**CiProvider** | Pointer to **string** |  | [optional]
**UnsupportedFeatureMode** | Pointer to **string** | FAIL is recommended for CI because unsupported flow steps must not silently disappear from an export. | [optional] [default to "FAIL"]

## Methods

### NewAtfGenerationInput

`func NewAtfGenerationInput(projectName string, packageName string, ) *AtfGenerationInput`

NewAtfGenerationInput instantiates a new AtfGenerationInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAtfGenerationInputWithDefaults

`func NewAtfGenerationInputWithDefaults() *AtfGenerationInput`

NewAtfGenerationInputWithDefaults instantiates a new AtfGenerationInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProjectName

`func (o *AtfGenerationInput) GetProjectName() string`

GetProjectName returns the ProjectName field if non-nil, zero value otherwise.

### GetProjectNameOk

`func (o *AtfGenerationInput) GetProjectNameOk() (*string, bool)`

GetProjectNameOk returns a tuple with the ProjectName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectName

`func (o *AtfGenerationInput) SetProjectName(v string)`

SetProjectName sets ProjectName field to given value.


### GetPackageName

`func (o *AtfGenerationInput) GetPackageName() string`

GetPackageName returns the PackageName field if non-nil, zero value otherwise.

### GetPackageNameOk

`func (o *AtfGenerationInput) GetPackageNameOk() (*string, bool)`

GetPackageNameOk returns a tuple with the PackageName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPackageName

`func (o *AtfGenerationInput) SetPackageName(v string)`

SetPackageName sets PackageName field to given value.


### GetTargetFramework

`func (o *AtfGenerationInput) GetTargetFramework() string`

GetTargetFramework returns the TargetFramework field if non-nil, zero value otherwise.

### GetTargetFrameworkOk

`func (o *AtfGenerationInput) GetTargetFrameworkOk() (*string, bool)`

GetTargetFrameworkOk returns a tuple with the TargetFramework field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetFramework

`func (o *AtfGenerationInput) SetTargetFramework(v string)`

SetTargetFramework sets TargetFramework field to given value.

### HasTargetFramework

`func (o *AtfGenerationInput) HasTargetFramework() bool`

HasTargetFramework returns a boolean if a field has been set.

### GetExportMode

`func (o *AtfGenerationInput) GetExportMode() string`

GetExportMode returns the ExportMode field if non-nil, zero value otherwise.

### GetExportModeOk

`func (o *AtfGenerationInput) GetExportModeOk() (*string, bool)`

GetExportModeOk returns a tuple with the ExportMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExportMode

`func (o *AtfGenerationInput) SetExportMode(v string)`

SetExportMode sets ExportMode field to given value.

### HasExportMode

`func (o *AtfGenerationInput) HasExportMode() bool`

HasExportMode returns a boolean if a field has been set.

### GetBuildTool

`func (o *AtfGenerationInput) GetBuildTool() string`

GetBuildTool returns the BuildTool field if non-nil, zero value otherwise.

### GetBuildToolOk

`func (o *AtfGenerationInput) GetBuildToolOk() (*string, bool)`

GetBuildToolOk returns a tuple with the BuildTool field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuildTool

`func (o *AtfGenerationInput) SetBuildTool(v string)`

SetBuildTool sets BuildTool field to given value.

### HasBuildTool

`func (o *AtfGenerationInput) HasBuildTool() bool`

HasBuildTool returns a boolean if a field has been set.

### GetJavaVersion

`func (o *AtfGenerationInput) GetJavaVersion() int32`

GetJavaVersion returns the JavaVersion field if non-nil, zero value otherwise.

### GetJavaVersionOk

`func (o *AtfGenerationInput) GetJavaVersionOk() (*int32, bool)`

GetJavaVersionOk returns a tuple with the JavaVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJavaVersion

`func (o *AtfGenerationInput) SetJavaVersion(v int32)`

SetJavaVersion sets JavaVersion field to given value.

### HasJavaVersion

`func (o *AtfGenerationInput) HasJavaVersion() bool`

HasJavaVersion returns a boolean if a field has been set.

### GetBaseUrlMode

`func (o *AtfGenerationInput) GetBaseUrlMode() AtfBaseUrlMode`

GetBaseUrlMode returns the BaseUrlMode field if non-nil, zero value otherwise.

### GetBaseUrlModeOk

`func (o *AtfGenerationInput) GetBaseUrlModeOk() (*AtfBaseUrlMode, bool)`

GetBaseUrlModeOk returns a tuple with the BaseUrlMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseUrlMode

`func (o *AtfGenerationInput) SetBaseUrlMode(v AtfBaseUrlMode)`

SetBaseUrlMode sets BaseUrlMode field to given value.

### HasBaseUrlMode

`func (o *AtfGenerationInput) HasBaseUrlMode() bool`

HasBaseUrlMode returns a boolean if a field has been set.

### GetBaseUrlVariableName

`func (o *AtfGenerationInput) GetBaseUrlVariableName() string`

GetBaseUrlVariableName returns the BaseUrlVariableName field if non-nil, zero value otherwise.

### GetBaseUrlVariableNameOk

`func (o *AtfGenerationInput) GetBaseUrlVariableNameOk() (*string, bool)`

GetBaseUrlVariableNameOk returns a tuple with the BaseUrlVariableName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseUrlVariableName

`func (o *AtfGenerationInput) SetBaseUrlVariableName(v string)`

SetBaseUrlVariableName sets BaseUrlVariableName field to given value.

### HasBaseUrlVariableName

`func (o *AtfGenerationInput) HasBaseUrlVariableName() bool`

HasBaseUrlVariableName returns a boolean if a field has been set.

### GetSpecs

`func (o *AtfGenerationInput) GetSpecs() []ArtifactSpecRef`

GetSpecs returns the Specs field if non-nil, zero value otherwise.

### GetSpecsOk

`func (o *AtfGenerationInput) GetSpecsOk() (*[]ArtifactSpecRef, bool)`

GetSpecsOk returns a tuple with the Specs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecs

`func (o *AtfGenerationInput) SetSpecs(v []ArtifactSpecRef)`

SetSpecs sets Specs field to given value.

### HasSpecs

`func (o *AtfGenerationInput) HasSpecs() bool`

HasSpecs returns a boolean if a field has been set.

### GetFlowIds

`func (o *AtfGenerationInput) GetFlowIds() []string`

GetFlowIds returns the FlowIds field if non-nil, zero value otherwise.

### GetFlowIdsOk

`func (o *AtfGenerationInput) GetFlowIdsOk() (*[]string, bool)`

GetFlowIdsOk returns a tuple with the FlowIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlowIds

`func (o *AtfGenerationInput) SetFlowIds(v []string)`

SetFlowIds sets FlowIds field to given value.

### HasFlowIds

`func (o *AtfGenerationInput) HasFlowIds() bool`

HasFlowIds returns a boolean if a field has been set.

### GetUiMacroIds

`func (o *AtfGenerationInput) GetUiMacroIds() []string`

GetUiMacroIds returns the UiMacroIds field if non-nil, zero value otherwise.

### GetUiMacroIdsOk

`func (o *AtfGenerationInput) GetUiMacroIdsOk() (*[]string, bool)`

GetUiMacroIdsOk returns a tuple with the UiMacroIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiMacroIds

`func (o *AtfGenerationInput) SetUiMacroIds(v []string)`

SetUiMacroIds sets UiMacroIds field to given value.

### HasUiMacroIds

`func (o *AtfGenerationInput) HasUiMacroIds() bool`

HasUiMacroIds returns a boolean if a field has been set.

### GetIncludeSupportFiles

`func (o *AtfGenerationInput) GetIncludeSupportFiles() bool`

GetIncludeSupportFiles returns the IncludeSupportFiles field if non-nil, zero value otherwise.

### GetIncludeSupportFilesOk

`func (o *AtfGenerationInput) GetIncludeSupportFilesOk() (*bool, bool)`

GetIncludeSupportFilesOk returns a tuple with the IncludeSupportFiles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeSupportFiles

`func (o *AtfGenerationInput) SetIncludeSupportFiles(v bool)`

SetIncludeSupportFiles sets IncludeSupportFiles field to given value.

### HasIncludeSupportFiles

`func (o *AtfGenerationInput) HasIncludeSupportFiles() bool`

HasIncludeSupportFiles returns a boolean if a field has been set.

### GetIncludeCoverage

`func (o *AtfGenerationInput) GetIncludeCoverage() bool`

GetIncludeCoverage returns the IncludeCoverage field if non-nil, zero value otherwise.

### GetIncludeCoverageOk

`func (o *AtfGenerationInput) GetIncludeCoverageOk() (*bool, bool)`

GetIncludeCoverageOk returns a tuple with the IncludeCoverage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeCoverage

`func (o *AtfGenerationInput) SetIncludeCoverage(v bool)`

SetIncludeCoverage sets IncludeCoverage field to given value.

### HasIncludeCoverage

`func (o *AtfGenerationInput) HasIncludeCoverage() bool`

HasIncludeCoverage returns a boolean if a field has been set.

### GetCiProvider

`func (o *AtfGenerationInput) GetCiProvider() string`

GetCiProvider returns the CiProvider field if non-nil, zero value otherwise.

### GetCiProviderOk

`func (o *AtfGenerationInput) GetCiProviderOk() (*string, bool)`

GetCiProviderOk returns a tuple with the CiProvider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCiProvider

`func (o *AtfGenerationInput) SetCiProvider(v string)`

SetCiProvider sets CiProvider field to given value.

### HasCiProvider

`func (o *AtfGenerationInput) HasCiProvider() bool`

HasCiProvider returns a boolean if a field has been set.

### GetUnsupportedFeatureMode

`func (o *AtfGenerationInput) GetUnsupportedFeatureMode() string`

GetUnsupportedFeatureMode returns the UnsupportedFeatureMode field if non-nil, zero value otherwise.

### GetUnsupportedFeatureModeOk

`func (o *AtfGenerationInput) GetUnsupportedFeatureModeOk() (*string, bool)`

GetUnsupportedFeatureModeOk returns a tuple with the UnsupportedFeatureMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnsupportedFeatureMode

`func (o *AtfGenerationInput) SetUnsupportedFeatureMode(v string)`

SetUnsupportedFeatureMode sets UnsupportedFeatureMode field to given value.

### HasUnsupportedFeatureMode

`func (o *AtfGenerationInput) HasUnsupportedFeatureMode() bool`

HasUnsupportedFeatureMode returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
