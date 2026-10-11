# RunBatch

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
**BatchId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Items** | [**[]RunBatchItem**](RunBatchItem.md) |  |
**CreatedAt** | **time.Time** |  |
**FinishedAt** | Pointer to **NullableTime** |  | [optional]

## Methods

### NewRunBatch

`func NewRunBatch(name string, environment string, batchId string, items []RunBatchItem, createdAt time.Time, ) *RunBatch`

NewRunBatch instantiates a new RunBatch object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRunBatchWithDefaults

`func NewRunBatchWithDefaults() *RunBatch`

NewRunBatchWithDefaults instantiates a new RunBatch object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *RunBatch) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RunBatch) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *RunBatch) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *RunBatch) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *RunBatch) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *RunBatch) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *RunBatch) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *RunBatch) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *RunBatch) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetEnvironment

`func (o *RunBatch) GetEnvironment() string`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *RunBatch) GetEnvironmentOk() (*string, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *RunBatch) SetEnvironment(v string)`

SetEnvironment sets Environment field to given value.


### GetSprint

`func (o *RunBatch) GetSprint() string`

GetSprint returns the Sprint field if non-nil, zero value otherwise.

### GetSprintOk

`func (o *RunBatch) GetSprintOk() (*string, bool)`

GetSprintOk returns a tuple with the Sprint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSprint

`func (o *RunBatch) SetSprint(v string)`

SetSprint sets Sprint field to given value.

### HasSprint

`func (o *RunBatch) HasSprint() bool`

HasSprint returns a boolean if a field has been set.

### SetSprintNil

`func (o *RunBatch) SetSprintNil(b bool)`

 SetSprintNil sets the value for Sprint to be an explicit nil

### UnsetSprint
`func (o *RunBatch) UnsetSprint()`

UnsetSprint ensures that no value is present for Sprint, not even an explicit nil
### GetBackendCommit

`func (o *RunBatch) GetBackendCommit() string`

GetBackendCommit returns the BackendCommit field if non-nil, zero value otherwise.

### GetBackendCommitOk

`func (o *RunBatch) GetBackendCommitOk() (*string, bool)`

GetBackendCommitOk returns a tuple with the BackendCommit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBackendCommit

`func (o *RunBatch) SetBackendCommit(v string)`

SetBackendCommit sets BackendCommit field to given value.

### HasBackendCommit

`func (o *RunBatch) HasBackendCommit() bool`

HasBackendCommit returns a boolean if a field has been set.

### SetBackendCommitNil

`func (o *RunBatch) SetBackendCommitNil(b bool)`

 SetBackendCommitNil sets the value for BackendCommit to be an explicit nil

### UnsetBackendCommit
`func (o *RunBatch) UnsetBackendCommit()`

UnsetBackendCommit ensures that no value is present for BackendCommit, not even an explicit nil
### GetFrontendCommit

`func (o *RunBatch) GetFrontendCommit() string`

GetFrontendCommit returns the FrontendCommit field if non-nil, zero value otherwise.

### GetFrontendCommitOk

`func (o *RunBatch) GetFrontendCommitOk() (*string, bool)`

GetFrontendCommitOk returns a tuple with the FrontendCommit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrontendCommit

`func (o *RunBatch) SetFrontendCommit(v string)`

SetFrontendCommit sets FrontendCommit field to given value.

### HasFrontendCommit

`func (o *RunBatch) HasFrontendCommit() bool`

HasFrontendCommit returns a boolean if a field has been set.

### SetFrontendCommitNil

`func (o *RunBatch) SetFrontendCommitNil(b bool)`

 SetFrontendCommitNil sets the value for FrontendCommit to be an explicit nil

### UnsetFrontendCommit
`func (o *RunBatch) UnsetFrontendCommit()`

UnsetFrontendCommit ensures that no value is present for FrontendCommit, not even an explicit nil
### GetBranchName

`func (o *RunBatch) GetBranchName() string`

GetBranchName returns the BranchName field if non-nil, zero value otherwise.

### GetBranchNameOk

`func (o *RunBatch) GetBranchNameOk() (*string, bool)`

GetBranchNameOk returns a tuple with the BranchName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBranchName

`func (o *RunBatch) SetBranchName(v string)`

SetBranchName sets BranchName field to given value.

### HasBranchName

`func (o *RunBatch) HasBranchName() bool`

HasBranchName returns a boolean if a field has been set.

### SetBranchNameNil

`func (o *RunBatch) SetBranchNameNil(b bool)`

 SetBranchNameNil sets the value for BranchName to be an explicit nil

### UnsetBranchName
`func (o *RunBatch) UnsetBranchName()`

UnsetBranchName ensures that no value is present for BranchName, not even an explicit nil
### GetTriggeredBy

`func (o *RunBatch) GetTriggeredBy() string`

GetTriggeredBy returns the TriggeredBy field if non-nil, zero value otherwise.

### GetTriggeredByOk

`func (o *RunBatch) GetTriggeredByOk() (*string, bool)`

GetTriggeredByOk returns a tuple with the TriggeredBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTriggeredBy

`func (o *RunBatch) SetTriggeredBy(v string)`

SetTriggeredBy sets TriggeredBy field to given value.

### HasTriggeredBy

`func (o *RunBatch) HasTriggeredBy() bool`

HasTriggeredBy returns a boolean if a field has been set.

### SetTriggeredByNil

`func (o *RunBatch) SetTriggeredByNil(b bool)`

 SetTriggeredByNil sets the value for TriggeredBy to be an explicit nil

### UnsetTriggeredBy
`func (o *RunBatch) UnsetTriggeredBy()`

UnsetTriggeredBy ensures that no value is present for TriggeredBy, not even an explicit nil
### GetTriggerType

`func (o *RunBatch) GetTriggerType() string`

GetTriggerType returns the TriggerType field if non-nil, zero value otherwise.

### GetTriggerTypeOk

`func (o *RunBatch) GetTriggerTypeOk() (*string, bool)`

GetTriggerTypeOk returns a tuple with the TriggerType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTriggerType

`func (o *RunBatch) SetTriggerType(v string)`

SetTriggerType sets TriggerType field to given value.

### HasTriggerType

`func (o *RunBatch) HasTriggerType() bool`

HasTriggerType returns a boolean if a field has been set.

### SetTriggerTypeNil

`func (o *RunBatch) SetTriggerTypeNil(b bool)`

 SetTriggerTypeNil sets the value for TriggerType to be an explicit nil

### UnsetTriggerType
`func (o *RunBatch) UnsetTriggerType()`

UnsetTriggerType ensures that no value is present for TriggerType, not even an explicit nil
### GetNotes

`func (o *RunBatch) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *RunBatch) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *RunBatch) SetNotes(v string)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *RunBatch) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotesNil

`func (o *RunBatch) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *RunBatch) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil
### GetSpecRunIds

`func (o *RunBatch) GetSpecRunIds() []string`

GetSpecRunIds returns the SpecRunIds field if non-nil, zero value otherwise.

### GetSpecRunIdsOk

`func (o *RunBatch) GetSpecRunIdsOk() (*[]string, bool)`

GetSpecRunIdsOk returns a tuple with the SpecRunIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecRunIds

`func (o *RunBatch) SetSpecRunIds(v []string)`

SetSpecRunIds sets SpecRunIds field to given value.

### HasSpecRunIds

`func (o *RunBatch) HasSpecRunIds() bool`

HasSpecRunIds returns a boolean if a field has been set.

### GetUiMacroRunIds

`func (o *RunBatch) GetUiMacroRunIds() []string`

GetUiMacroRunIds returns the UiMacroRunIds field if non-nil, zero value otherwise.

### GetUiMacroRunIdsOk

`func (o *RunBatch) GetUiMacroRunIdsOk() (*[]string, bool)`

GetUiMacroRunIdsOk returns a tuple with the UiMacroRunIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiMacroRunIds

`func (o *RunBatch) SetUiMacroRunIds(v []string)`

SetUiMacroRunIds sets UiMacroRunIds field to given value.

### HasUiMacroRunIds

`func (o *RunBatch) HasUiMacroRunIds() bool`

HasUiMacroRunIds returns a boolean if a field has been set.

### GetFlowRunIds

`func (o *RunBatch) GetFlowRunIds() []string`

GetFlowRunIds returns the FlowRunIds field if non-nil, zero value otherwise.

### GetFlowRunIdsOk

`func (o *RunBatch) GetFlowRunIdsOk() (*[]string, bool)`

GetFlowRunIdsOk returns a tuple with the FlowRunIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlowRunIds

`func (o *RunBatch) SetFlowRunIds(v []string)`

SetFlowRunIds sets FlowRunIds field to given value.

### HasFlowRunIds

`func (o *RunBatch) HasFlowRunIds() bool`

HasFlowRunIds returns a boolean if a field has been set.

### GetBatchId

`func (o *RunBatch) GetBatchId() string`

GetBatchId returns the BatchId field if non-nil, zero value otherwise.

### GetBatchIdOk

`func (o *RunBatch) GetBatchIdOk() (*string, bool)`

GetBatchIdOk returns a tuple with the BatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBatchId

`func (o *RunBatch) SetBatchId(v string)`

SetBatchId sets BatchId field to given value.


### GetItems

`func (o *RunBatch) GetItems() []RunBatchItem`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *RunBatch) GetItemsOk() (*[]RunBatchItem, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *RunBatch) SetItems(v []RunBatchItem)`

SetItems sets Items field to given value.


### GetCreatedAt

`func (o *RunBatch) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *RunBatch) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *RunBatch) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetFinishedAt

`func (o *RunBatch) GetFinishedAt() time.Time`

GetFinishedAt returns the FinishedAt field if non-nil, zero value otherwise.

### GetFinishedAtOk

`func (o *RunBatch) GetFinishedAtOk() (*time.Time, bool)`

GetFinishedAtOk returns a tuple with the FinishedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinishedAt

`func (o *RunBatch) SetFinishedAt(v time.Time)`

SetFinishedAt sets FinishedAt field to given value.

### HasFinishedAt

`func (o *RunBatch) HasFinishedAt() bool`

HasFinishedAt returns a boolean if a field has been set.

### SetFinishedAtNil

`func (o *RunBatch) SetFinishedAtNil(b bool)`

 SetFinishedAtNil sets the value for FinishedAt to be an explicit nil

### UnsetFinishedAt
`func (o *RunBatch) UnsetFinishedAt()`

UnsetFinishedAt ensures that no value is present for FinishedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
