# AtfValidationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectName** | **string** |  |
**ExportMode** | **string** |  |
**BuildTool** | **string** |  |
**ValidationPassed** | **bool** |  |
**SuggestedCommand** | **string** |  |
**Steps** | [**[]AtfValidationStep**](AtfValidationStep.md) |  |

## Methods

### NewAtfValidationResult

`func NewAtfValidationResult(projectName string, exportMode string, buildTool string, validationPassed bool, suggestedCommand string, steps []AtfValidationStep, ) *AtfValidationResult`

NewAtfValidationResult instantiates a new AtfValidationResult object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAtfValidationResultWithDefaults

`func NewAtfValidationResultWithDefaults() *AtfValidationResult`

NewAtfValidationResultWithDefaults instantiates a new AtfValidationResult object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProjectName

`func (o *AtfValidationResult) GetProjectName() string`

GetProjectName returns the ProjectName field if non-nil, zero value otherwise.

### GetProjectNameOk

`func (o *AtfValidationResult) GetProjectNameOk() (*string, bool)`

GetProjectNameOk returns a tuple with the ProjectName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectName

`func (o *AtfValidationResult) SetProjectName(v string)`

SetProjectName sets ProjectName field to given value.


### GetExportMode

`func (o *AtfValidationResult) GetExportMode() string`

GetExportMode returns the ExportMode field if non-nil, zero value otherwise.

### GetExportModeOk

`func (o *AtfValidationResult) GetExportModeOk() (*string, bool)`

GetExportModeOk returns a tuple with the ExportMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExportMode

`func (o *AtfValidationResult) SetExportMode(v string)`

SetExportMode sets ExportMode field to given value.


### GetBuildTool

`func (o *AtfValidationResult) GetBuildTool() string`

GetBuildTool returns the BuildTool field if non-nil, zero value otherwise.

### GetBuildToolOk

`func (o *AtfValidationResult) GetBuildToolOk() (*string, bool)`

GetBuildToolOk returns a tuple with the BuildTool field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuildTool

`func (o *AtfValidationResult) SetBuildTool(v string)`

SetBuildTool sets BuildTool field to given value.


### GetValidationPassed

`func (o *AtfValidationResult) GetValidationPassed() bool`

GetValidationPassed returns the ValidationPassed field if non-nil, zero value otherwise.

### GetValidationPassedOk

`func (o *AtfValidationResult) GetValidationPassedOk() (*bool, bool)`

GetValidationPassedOk returns a tuple with the ValidationPassed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValidationPassed

`func (o *AtfValidationResult) SetValidationPassed(v bool)`

SetValidationPassed sets ValidationPassed field to given value.


### GetSuggestedCommand

`func (o *AtfValidationResult) GetSuggestedCommand() string`

GetSuggestedCommand returns the SuggestedCommand field if non-nil, zero value otherwise.

### GetSuggestedCommandOk

`func (o *AtfValidationResult) GetSuggestedCommandOk() (*string, bool)`

GetSuggestedCommandOk returns a tuple with the SuggestedCommand field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuggestedCommand

`func (o *AtfValidationResult) SetSuggestedCommand(v string)`

SetSuggestedCommand sets SuggestedCommand field to given value.


### GetSteps

`func (o *AtfValidationResult) GetSteps() []AtfValidationStep`

GetSteps returns the Steps field if non-nil, zero value otherwise.

### GetStepsOk

`func (o *AtfValidationResult) GetStepsOk() (*[]AtfValidationStep, bool)`

GetStepsOk returns a tuple with the Steps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteps

`func (o *AtfValidationResult) SetSteps(v []AtfValidationStep)`

SetSteps sets Steps field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


