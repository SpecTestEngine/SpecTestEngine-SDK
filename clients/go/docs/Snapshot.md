# Snapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**Sprint** | **string** |  |
**SourceBatchId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**ParentSnapshotId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**SelectionPolicy** | [**SnapshotSelectionPolicy**](SnapshotSelectionPolicy.md) |  |
**BatchItemIds** | Pointer to **[]string** |  | [optional]
**Environment** | **string** |  |
**BranchName** | Pointer to **NullableString** |  | [optional]
**BackendCommit** | Pointer to **NullableString** |  | [optional]
**FrontendCommit** | Pointer to **NullableString** |  | [optional]
**CreatedBy** | Pointer to **NullableString** |  | [optional]
**SnapshotId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Status** | [**SnapshotStatus**](SnapshotStatus.md) |  |
**Flows** | [**[]SnapshotItem**](SnapshotItem.md) | Captured specification, UI macro, and flow evidence retained by the snapshot. |
**CreatedAt** | **time.Time** |  |
**ApprovedAt** | Pointer to **NullableTime** |  | [optional]

## Methods

### NewSnapshot

`func NewSnapshot(name string, sprint string, sourceBatchId string, selectionPolicy SnapshotSelectionPolicy, environment string, snapshotId string, status SnapshotStatus, flows []SnapshotItem, createdAt time.Time, ) *Snapshot`

NewSnapshot instantiates a new Snapshot object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSnapshotWithDefaults

`func NewSnapshotWithDefaults() *Snapshot`

NewSnapshotWithDefaults instantiates a new Snapshot object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *Snapshot) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Snapshot) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Snapshot) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *Snapshot) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Snapshot) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Snapshot) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Snapshot) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *Snapshot) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *Snapshot) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetSprint

`func (o *Snapshot) GetSprint() string`

GetSprint returns the Sprint field if non-nil, zero value otherwise.

### GetSprintOk

`func (o *Snapshot) GetSprintOk() (*string, bool)`

GetSprintOk returns a tuple with the Sprint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSprint

`func (o *Snapshot) SetSprint(v string)`

SetSprint sets Sprint field to given value.


### GetSourceBatchId

`func (o *Snapshot) GetSourceBatchId() string`

GetSourceBatchId returns the SourceBatchId field if non-nil, zero value otherwise.

### GetSourceBatchIdOk

`func (o *Snapshot) GetSourceBatchIdOk() (*string, bool)`

GetSourceBatchIdOk returns a tuple with the SourceBatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceBatchId

`func (o *Snapshot) SetSourceBatchId(v string)`

SetSourceBatchId sets SourceBatchId field to given value.


### GetParentSnapshotId

`func (o *Snapshot) GetParentSnapshotId() string`

GetParentSnapshotId returns the ParentSnapshotId field if non-nil, zero value otherwise.

### GetParentSnapshotIdOk

`func (o *Snapshot) GetParentSnapshotIdOk() (*string, bool)`

GetParentSnapshotIdOk returns a tuple with the ParentSnapshotId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentSnapshotId

`func (o *Snapshot) SetParentSnapshotId(v string)`

SetParentSnapshotId sets ParentSnapshotId field to given value.

### HasParentSnapshotId

`func (o *Snapshot) HasParentSnapshotId() bool`

HasParentSnapshotId returns a boolean if a field has been set.

### SetParentSnapshotIdNil

`func (o *Snapshot) SetParentSnapshotIdNil(b bool)`

 SetParentSnapshotIdNil sets the value for ParentSnapshotId to be an explicit nil

### UnsetParentSnapshotId
`func (o *Snapshot) UnsetParentSnapshotId()`

UnsetParentSnapshotId ensures that no value is present for ParentSnapshotId, not even an explicit nil
### GetSelectionPolicy

`func (o *Snapshot) GetSelectionPolicy() SnapshotSelectionPolicy`

GetSelectionPolicy returns the SelectionPolicy field if non-nil, zero value otherwise.

### GetSelectionPolicyOk

`func (o *Snapshot) GetSelectionPolicyOk() (*SnapshotSelectionPolicy, bool)`

GetSelectionPolicyOk returns a tuple with the SelectionPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelectionPolicy

`func (o *Snapshot) SetSelectionPolicy(v SnapshotSelectionPolicy)`

SetSelectionPolicy sets SelectionPolicy field to given value.


### GetBatchItemIds

`func (o *Snapshot) GetBatchItemIds() []string`

GetBatchItemIds returns the BatchItemIds field if non-nil, zero value otherwise.

### GetBatchItemIdsOk

`func (o *Snapshot) GetBatchItemIdsOk() (*[]string, bool)`

GetBatchItemIdsOk returns a tuple with the BatchItemIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBatchItemIds

`func (o *Snapshot) SetBatchItemIds(v []string)`

SetBatchItemIds sets BatchItemIds field to given value.

### HasBatchItemIds

`func (o *Snapshot) HasBatchItemIds() bool`

HasBatchItemIds returns a boolean if a field has been set.

### GetEnvironment

`func (o *Snapshot) GetEnvironment() string`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *Snapshot) GetEnvironmentOk() (*string, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *Snapshot) SetEnvironment(v string)`

SetEnvironment sets Environment field to given value.


### GetBranchName

`func (o *Snapshot) GetBranchName() string`

GetBranchName returns the BranchName field if non-nil, zero value otherwise.

### GetBranchNameOk

`func (o *Snapshot) GetBranchNameOk() (*string, bool)`

GetBranchNameOk returns a tuple with the BranchName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBranchName

`func (o *Snapshot) SetBranchName(v string)`

SetBranchName sets BranchName field to given value.

### HasBranchName

`func (o *Snapshot) HasBranchName() bool`

HasBranchName returns a boolean if a field has been set.

### SetBranchNameNil

`func (o *Snapshot) SetBranchNameNil(b bool)`

 SetBranchNameNil sets the value for BranchName to be an explicit nil

### UnsetBranchName
`func (o *Snapshot) UnsetBranchName()`

UnsetBranchName ensures that no value is present for BranchName, not even an explicit nil
### GetBackendCommit

`func (o *Snapshot) GetBackendCommit() string`

GetBackendCommit returns the BackendCommit field if non-nil, zero value otherwise.

### GetBackendCommitOk

`func (o *Snapshot) GetBackendCommitOk() (*string, bool)`

GetBackendCommitOk returns a tuple with the BackendCommit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBackendCommit

`func (o *Snapshot) SetBackendCommit(v string)`

SetBackendCommit sets BackendCommit field to given value.

### HasBackendCommit

`func (o *Snapshot) HasBackendCommit() bool`

HasBackendCommit returns a boolean if a field has been set.

### SetBackendCommitNil

`func (o *Snapshot) SetBackendCommitNil(b bool)`

 SetBackendCommitNil sets the value for BackendCommit to be an explicit nil

### UnsetBackendCommit
`func (o *Snapshot) UnsetBackendCommit()`

UnsetBackendCommit ensures that no value is present for BackendCommit, not even an explicit nil
### GetFrontendCommit

`func (o *Snapshot) GetFrontendCommit() string`

GetFrontendCommit returns the FrontendCommit field if non-nil, zero value otherwise.

### GetFrontendCommitOk

`func (o *Snapshot) GetFrontendCommitOk() (*string, bool)`

GetFrontendCommitOk returns a tuple with the FrontendCommit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrontendCommit

`func (o *Snapshot) SetFrontendCommit(v string)`

SetFrontendCommit sets FrontendCommit field to given value.

### HasFrontendCommit

`func (o *Snapshot) HasFrontendCommit() bool`

HasFrontendCommit returns a boolean if a field has been set.

### SetFrontendCommitNil

`func (o *Snapshot) SetFrontendCommitNil(b bool)`

 SetFrontendCommitNil sets the value for FrontendCommit to be an explicit nil

### UnsetFrontendCommit
`func (o *Snapshot) UnsetFrontendCommit()`

UnsetFrontendCommit ensures that no value is present for FrontendCommit, not even an explicit nil
### GetCreatedBy

`func (o *Snapshot) GetCreatedBy() string`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *Snapshot) GetCreatedByOk() (*string, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *Snapshot) SetCreatedBy(v string)`

SetCreatedBy sets CreatedBy field to given value.

### HasCreatedBy

`func (o *Snapshot) HasCreatedBy() bool`

HasCreatedBy returns a boolean if a field has been set.

### SetCreatedByNil

`func (o *Snapshot) SetCreatedByNil(b bool)`

 SetCreatedByNil sets the value for CreatedBy to be an explicit nil

### UnsetCreatedBy
`func (o *Snapshot) UnsetCreatedBy()`

UnsetCreatedBy ensures that no value is present for CreatedBy, not even an explicit nil
### GetSnapshotId

`func (o *Snapshot) GetSnapshotId() string`

GetSnapshotId returns the SnapshotId field if non-nil, zero value otherwise.

### GetSnapshotIdOk

`func (o *Snapshot) GetSnapshotIdOk() (*string, bool)`

GetSnapshotIdOk returns a tuple with the SnapshotId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSnapshotId

`func (o *Snapshot) SetSnapshotId(v string)`

SetSnapshotId sets SnapshotId field to given value.


### GetStatus

`func (o *Snapshot) GetStatus() SnapshotStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *Snapshot) GetStatusOk() (*SnapshotStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *Snapshot) SetStatus(v SnapshotStatus)`

SetStatus sets Status field to given value.


### GetFlows

`func (o *Snapshot) GetFlows() []SnapshotItem`

GetFlows returns the Flows field if non-nil, zero value otherwise.

### GetFlowsOk

`func (o *Snapshot) GetFlowsOk() (*[]SnapshotItem, bool)`

GetFlowsOk returns a tuple with the Flows field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlows

`func (o *Snapshot) SetFlows(v []SnapshotItem)`

SetFlows sets Flows field to given value.


### GetCreatedAt

`func (o *Snapshot) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Snapshot) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Snapshot) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetApprovedAt

`func (o *Snapshot) GetApprovedAt() time.Time`

GetApprovedAt returns the ApprovedAt field if non-nil, zero value otherwise.

### GetApprovedAtOk

`func (o *Snapshot) GetApprovedAtOk() (*time.Time, bool)`

GetApprovedAtOk returns a tuple with the ApprovedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApprovedAt

`func (o *Snapshot) SetApprovedAt(v time.Time)`

SetApprovedAt sets ApprovedAt field to given value.

### HasApprovedAt

`func (o *Snapshot) HasApprovedAt() bool`

HasApprovedAt returns a boolean if a field has been set.

### SetApprovedAtNil

`func (o *Snapshot) SetApprovedAtNil(b bool)`

 SetApprovedAtNil sets the value for ApprovedAt to be an explicit nil

### UnsetApprovedAt
`func (o *Snapshot) UnsetApprovedAt()`

UnsetApprovedAt ensures that no value is present for ApprovedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


