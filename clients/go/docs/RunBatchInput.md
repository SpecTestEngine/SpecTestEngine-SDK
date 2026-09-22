# RunBatchInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**Environment** | **string** |  |
**Sprint** | Pointer to **NullableString** |  | [optional]
**BackendCommit** | Pointer to **NullableString** |  | [optional]
**FrontendCommit** | Pointer to **NullableString** |  | [optional]
**BranchName** | Pointer to **NullableString** |  | [optional]
**TriggeredBy** | Pointer to **NullableString** |  | [optional]
**TriggerType** | Pointer to **NullableString** |  | [optional]
**Notes** | Pointer to **NullableString** |  | [optional]
**SpecRunIds** | Pointer to **[]string** |  | [optional]
**UiMacroRunIds** | Pointer to **[]string** |  | [optional]
**FlowRunIds** | Pointer to **[]string** |  | [optional]

## Methods

### NewRunBatchInput

`func NewRunBatchInput(name string, environment string, ) *RunBatchInput`

NewRunBatchInput instantiates a new RunBatchInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRunBatchInputWithDefaults

`func NewRunBatchInputWithDefaults() *RunBatchInput`

NewRunBatchInputWithDefaults instantiates a new RunBatchInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *RunBatchInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RunBatchInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *RunBatchInput) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *RunBatchInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *RunBatchInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *RunBatchInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *RunBatchInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *RunBatchInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *RunBatchInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetEnvironment

`func (o *RunBatchInput) GetEnvironment() string`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *RunBatchInput) GetEnvironmentOk() (*string, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *RunBatchInput) SetEnvironment(v string)`

SetEnvironment sets Environment field to given value.


### GetSprint

`func (o *RunBatchInput) GetSprint() string`

GetSprint returns the Sprint field if non-nil, zero value otherwise.

### GetSprintOk

`func (o *RunBatchInput) GetSprintOk() (*string, bool)`

GetSprintOk returns a tuple with the Sprint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSprint

`func (o *RunBatchInput) SetSprint(v string)`

SetSprint sets Sprint field to given value.

### HasSprint

`func (o *RunBatchInput) HasSprint() bool`

HasSprint returns a boolean if a field has been set.

### SetSprintNil

`func (o *RunBatchInput) SetSprintNil(b bool)`

 SetSprintNil sets the value for Sprint to be an explicit nil

### UnsetSprint
`func (o *RunBatchInput) UnsetSprint()`

UnsetSprint ensures that no value is present for Sprint, not even an explicit nil
### GetBackendCommit

`func (o *RunBatchInput) GetBackendCommit() string`

GetBackendCommit returns the BackendCommit field if non-nil, zero value otherwise.

### GetBackendCommitOk

`func (o *RunBatchInput) GetBackendCommitOk() (*string, bool)`

GetBackendCommitOk returns a tuple with the BackendCommit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBackendCommit

`func (o *RunBatchInput) SetBackendCommit(v string)`

SetBackendCommit sets BackendCommit field to given value.

### HasBackendCommit

`func (o *RunBatchInput) HasBackendCommit() bool`

HasBackendCommit returns a boolean if a field has been set.

### SetBackendCommitNil

`func (o *RunBatchInput) SetBackendCommitNil(b bool)`

 SetBackendCommitNil sets the value for BackendCommit to be an explicit nil

### UnsetBackendCommit
`func (o *RunBatchInput) UnsetBackendCommit()`

UnsetBackendCommit ensures that no value is present for BackendCommit, not even an explicit nil
### GetFrontendCommit

`func (o *RunBatchInput) GetFrontendCommit() string`

GetFrontendCommit returns the FrontendCommit field if non-nil, zero value otherwise.

### GetFrontendCommitOk

`func (o *RunBatchInput) GetFrontendCommitOk() (*string, bool)`

GetFrontendCommitOk returns a tuple with the FrontendCommit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrontendCommit

`func (o *RunBatchInput) SetFrontendCommit(v string)`

SetFrontendCommit sets FrontendCommit field to given value.

### HasFrontendCommit

`func (o *RunBatchInput) HasFrontendCommit() bool`

HasFrontendCommit returns a boolean if a field has been set.

### SetFrontendCommitNil

`func (o *RunBatchInput) SetFrontendCommitNil(b bool)`

 SetFrontendCommitNil sets the value for FrontendCommit to be an explicit nil

### UnsetFrontendCommit
`func (o *RunBatchInput) UnsetFrontendCommit()`

UnsetFrontendCommit ensures that no value is present for FrontendCommit, not even an explicit nil
### GetBranchName

`func (o *RunBatchInput) GetBranchName() string`

GetBranchName returns the BranchName field if non-nil, zero value otherwise.

### GetBranchNameOk

`func (o *RunBatchInput) GetBranchNameOk() (*string, bool)`

GetBranchNameOk returns a tuple with the BranchName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBranchName

`func (o *RunBatchInput) SetBranchName(v string)`

SetBranchName sets BranchName field to given value.

### HasBranchName

`func (o *RunBatchInput) HasBranchName() bool`

HasBranchName returns a boolean if a field has been set.

### SetBranchNameNil

`func (o *RunBatchInput) SetBranchNameNil(b bool)`

 SetBranchNameNil sets the value for BranchName to be an explicit nil

### UnsetBranchName
`func (o *RunBatchInput) UnsetBranchName()`

UnsetBranchName ensures that no value is present for BranchName, not even an explicit nil
### GetTriggeredBy

`func (o *RunBatchInput) GetTriggeredBy() string`

GetTriggeredBy returns the TriggeredBy field if non-nil, zero value otherwise.

### GetTriggeredByOk

`func (o *RunBatchInput) GetTriggeredByOk() (*string, bool)`

GetTriggeredByOk returns a tuple with the TriggeredBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTriggeredBy

`func (o *RunBatchInput) SetTriggeredBy(v string)`

SetTriggeredBy sets TriggeredBy field to given value.

### HasTriggeredBy

`func (o *RunBatchInput) HasTriggeredBy() bool`

HasTriggeredBy returns a boolean if a field has been set.

### SetTriggeredByNil

`func (o *RunBatchInput) SetTriggeredByNil(b bool)`

 SetTriggeredByNil sets the value for TriggeredBy to be an explicit nil

### UnsetTriggeredBy
`func (o *RunBatchInput) UnsetTriggeredBy()`

UnsetTriggeredBy ensures that no value is present for TriggeredBy, not even an explicit nil
### GetTriggerType

`func (o *RunBatchInput) GetTriggerType() string`

GetTriggerType returns the TriggerType field if non-nil, zero value otherwise.

### GetTriggerTypeOk

`func (o *RunBatchInput) GetTriggerTypeOk() (*string, bool)`

GetTriggerTypeOk returns a tuple with the TriggerType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTriggerType

`func (o *RunBatchInput) SetTriggerType(v string)`

SetTriggerType sets TriggerType field to given value.

### HasTriggerType

`func (o *RunBatchInput) HasTriggerType() bool`

HasTriggerType returns a boolean if a field has been set.

### SetTriggerTypeNil

`func (o *RunBatchInput) SetTriggerTypeNil(b bool)`

 SetTriggerTypeNil sets the value for TriggerType to be an explicit nil

### UnsetTriggerType
`func (o *RunBatchInput) UnsetTriggerType()`

UnsetTriggerType ensures that no value is present for TriggerType, not even an explicit nil
### GetNotes

`func (o *RunBatchInput) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *RunBatchInput) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *RunBatchInput) SetNotes(v string)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *RunBatchInput) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotesNil

`func (o *RunBatchInput) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *RunBatchInput) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil
### GetSpecRunIds

`func (o *RunBatchInput) GetSpecRunIds() []string`

GetSpecRunIds returns the SpecRunIds field if non-nil, zero value otherwise.

### GetSpecRunIdsOk

`func (o *RunBatchInput) GetSpecRunIdsOk() (*[]string, bool)`

GetSpecRunIdsOk returns a tuple with the SpecRunIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecRunIds

`func (o *RunBatchInput) SetSpecRunIds(v []string)`

SetSpecRunIds sets SpecRunIds field to given value.

### HasSpecRunIds

`func (o *RunBatchInput) HasSpecRunIds() bool`

HasSpecRunIds returns a boolean if a field has been set.

### GetUiMacroRunIds

`func (o *RunBatchInput) GetUiMacroRunIds() []string`

GetUiMacroRunIds returns the UiMacroRunIds field if non-nil, zero value otherwise.

### GetUiMacroRunIdsOk

`func (o *RunBatchInput) GetUiMacroRunIdsOk() (*[]string, bool)`

GetUiMacroRunIdsOk returns a tuple with the UiMacroRunIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiMacroRunIds

`func (o *RunBatchInput) SetUiMacroRunIds(v []string)`

SetUiMacroRunIds sets UiMacroRunIds field to given value.

### HasUiMacroRunIds

`func (o *RunBatchInput) HasUiMacroRunIds() bool`

HasUiMacroRunIds returns a boolean if a field has been set.

### GetFlowRunIds

`func (o *RunBatchInput) GetFlowRunIds() []string`

GetFlowRunIds returns the FlowRunIds field if non-nil, zero value otherwise.

### GetFlowRunIdsOk

`func (o *RunBatchInput) GetFlowRunIdsOk() (*[]string, bool)`

GetFlowRunIdsOk returns a tuple with the FlowRunIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlowRunIds

`func (o *RunBatchInput) SetFlowRunIds(v []string)`

SetFlowRunIds sets FlowRunIds field to given value.

### HasFlowRunIds

`func (o *RunBatchInput) HasFlowRunIds() bool`

HasFlowRunIds returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


