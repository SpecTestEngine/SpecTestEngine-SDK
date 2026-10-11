# AtfGenerationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectName** | **string** |  |
**TargetFramework** | **string** |  |
**ExportMode** | **string** |  |
**BuildTool** | **string** |  |
**Manifest** | **map[string]interface{}** |  |
**Files** | [**[]AtfGenerationResultFilesInner**](AtfGenerationResultFilesInner.md) |  |
**Notes** | **[]map[string]interface{}** |  |

## Methods

### NewAtfGenerationResult

`func NewAtfGenerationResult(projectName string, targetFramework string, exportMode string, buildTool string, manifest map[string]interface{}, files []AtfGenerationResultFilesInner, notes []map[string]interface{}, ) *AtfGenerationResult`

NewAtfGenerationResult instantiates a new AtfGenerationResult object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAtfGenerationResultWithDefaults

`func NewAtfGenerationResultWithDefaults() *AtfGenerationResult`

NewAtfGenerationResultWithDefaults instantiates a new AtfGenerationResult object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProjectName

`func (o *AtfGenerationResult) GetProjectName() string`

GetProjectName returns the ProjectName field if non-nil, zero value otherwise.

### GetProjectNameOk

`func (o *AtfGenerationResult) GetProjectNameOk() (*string, bool)`

GetProjectNameOk returns a tuple with the ProjectName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectName

`func (o *AtfGenerationResult) SetProjectName(v string)`

SetProjectName sets ProjectName field to given value.


### GetTargetFramework

`func (o *AtfGenerationResult) GetTargetFramework() string`

GetTargetFramework returns the TargetFramework field if non-nil, zero value otherwise.

### GetTargetFrameworkOk

`func (o *AtfGenerationResult) GetTargetFrameworkOk() (*string, bool)`

GetTargetFrameworkOk returns a tuple with the TargetFramework field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetFramework

`func (o *AtfGenerationResult) SetTargetFramework(v string)`

SetTargetFramework sets TargetFramework field to given value.


### GetExportMode

`func (o *AtfGenerationResult) GetExportMode() string`

GetExportMode returns the ExportMode field if non-nil, zero value otherwise.

### GetExportModeOk

`func (o *AtfGenerationResult) GetExportModeOk() (*string, bool)`

GetExportModeOk returns a tuple with the ExportMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExportMode

`func (o *AtfGenerationResult) SetExportMode(v string)`

SetExportMode sets ExportMode field to given value.


### GetBuildTool

`func (o *AtfGenerationResult) GetBuildTool() string`

GetBuildTool returns the BuildTool field if non-nil, zero value otherwise.

### GetBuildToolOk

`func (o *AtfGenerationResult) GetBuildToolOk() (*string, bool)`

GetBuildToolOk returns a tuple with the BuildTool field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuildTool

`func (o *AtfGenerationResult) SetBuildTool(v string)`

SetBuildTool sets BuildTool field to given value.


### GetManifest

`func (o *AtfGenerationResult) GetManifest() map[string]interface{}`

GetManifest returns the Manifest field if non-nil, zero value otherwise.

### GetManifestOk

`func (o *AtfGenerationResult) GetManifestOk() (*map[string]interface{}, bool)`

GetManifestOk returns a tuple with the Manifest field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManifest

`func (o *AtfGenerationResult) SetManifest(v map[string]interface{})`

SetManifest sets Manifest field to given value.


### GetFiles

`func (o *AtfGenerationResult) GetFiles() []AtfGenerationResultFilesInner`

GetFiles returns the Files field if non-nil, zero value otherwise.

### GetFilesOk

`func (o *AtfGenerationResult) GetFilesOk() (*[]AtfGenerationResultFilesInner, bool)`

GetFilesOk returns a tuple with the Files field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFiles

`func (o *AtfGenerationResult) SetFiles(v []AtfGenerationResultFilesInner)`

SetFiles sets Files field to given value.


### GetNotes

`func (o *AtfGenerationResult) GetNotes() []map[string]interface{}`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *AtfGenerationResult) GetNotesOk() (*[]map[string]interface{}, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *AtfGenerationResult) SetNotes(v []map[string]interface{})`

SetNotes sets Notes field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
