# SnapshotInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**Sprint** | **string** |  |
**SourceBatchId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**ParentSnapshotId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**SelectionPolicy** | Pointer to [**SnapshotSelectionPolicy**](SnapshotSelectionPolicy.md) |  | [optional]
**BatchItemIds** | Pointer to **[]string** |  | [optional]
**Environment** | **string** |  |
**BranchName** | Pointer to **NullableString** |  | [optional]
**BackendCommit** | Pointer to **NullableString** |  | [optional]
**FrontendCommit** | Pointer to **NullableString** |  | [optional]
**CreatedBy** | Pointer to **NullableString** |  | [optional]

## Methods

### NewSnapshotInput

`func NewSnapshotInput(name string, sprint string, sourceBatchId string, environment string, ) *SnapshotInput`

NewSnapshotInput instantiates a new SnapshotInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSnapshotInputWithDefaults

`func NewSnapshotInputWithDefaults() *SnapshotInput`

NewSnapshotInputWithDefaults instantiates a new SnapshotInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *SnapshotInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SnapshotInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SnapshotInput) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *SnapshotInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *SnapshotInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *SnapshotInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *SnapshotInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *SnapshotInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *SnapshotInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetSprint

`func (o *SnapshotInput) GetSprint() string`

GetSprint returns the Sprint field if non-nil, zero value otherwise.

### GetSprintOk

`func (o *SnapshotInput) GetSprintOk() (*string, bool)`

GetSprintOk returns a tuple with the Sprint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSprint

`func (o *SnapshotInput) SetSprint(v string)`

SetSprint sets Sprint field to given value.


### GetSourceBatchId

`func (o *SnapshotInput) GetSourceBatchId() string`

GetSourceBatchId returns the SourceBatchId field if non-nil, zero value otherwise.

### GetSourceBatchIdOk

`func (o *SnapshotInput) GetSourceBatchIdOk() (*string, bool)`

GetSourceBatchIdOk returns a tuple with the SourceBatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceBatchId

`func (o *SnapshotInput) SetSourceBatchId(v string)`

SetSourceBatchId sets SourceBatchId field to given value.


### GetParentSnapshotId

`func (o *SnapshotInput) GetParentSnapshotId() string`

GetParentSnapshotId returns the ParentSnapshotId field if non-nil, zero value otherwise.

### GetParentSnapshotIdOk

`func (o *SnapshotInput) GetParentSnapshotIdOk() (*string, bool)`

GetParentSnapshotIdOk returns a tuple with the ParentSnapshotId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentSnapshotId

`func (o *SnapshotInput) SetParentSnapshotId(v string)`

SetParentSnapshotId sets ParentSnapshotId field to given value.

### HasParentSnapshotId

`func (o *SnapshotInput) HasParentSnapshotId() bool`

HasParentSnapshotId returns a boolean if a field has been set.

### SetParentSnapshotIdNil

`func (o *SnapshotInput) SetParentSnapshotIdNil(b bool)`

 SetParentSnapshotIdNil sets the value for ParentSnapshotId to be an explicit nil

### UnsetParentSnapshotId
`func (o *SnapshotInput) UnsetParentSnapshotId()`

UnsetParentSnapshotId ensures that no value is present for ParentSnapshotId, not even an explicit nil
### GetSelectionPolicy

`func (o *SnapshotInput) GetSelectionPolicy() SnapshotSelectionPolicy`

GetSelectionPolicy returns the SelectionPolicy field if non-nil, zero value otherwise.

### GetSelectionPolicyOk

`func (o *SnapshotInput) GetSelectionPolicyOk() (*SnapshotSelectionPolicy, bool)`

GetSelectionPolicyOk returns a tuple with the SelectionPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelectionPolicy

`func (o *SnapshotInput) SetSelectionPolicy(v SnapshotSelectionPolicy)`

SetSelectionPolicy sets SelectionPolicy field to given value.

### HasSelectionPolicy

`func (o *SnapshotInput) HasSelectionPolicy() bool`

HasSelectionPolicy returns a boolean if a field has been set.

### GetBatchItemIds

`func (o *SnapshotInput) GetBatchItemIds() []string`

GetBatchItemIds returns the BatchItemIds field if non-nil, zero value otherwise.

### GetBatchItemIdsOk

`func (o *SnapshotInput) GetBatchItemIdsOk() (*[]string, bool)`

GetBatchItemIdsOk returns a tuple with the BatchItemIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBatchItemIds

`func (o *SnapshotInput) SetBatchItemIds(v []string)`

SetBatchItemIds sets BatchItemIds field to given value.

### HasBatchItemIds

`func (o *SnapshotInput) HasBatchItemIds() bool`

HasBatchItemIds returns a boolean if a field has been set.

### GetEnvironment

`func (o *SnapshotInput) GetEnvironment() string`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *SnapshotInput) GetEnvironmentOk() (*string, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *SnapshotInput) SetEnvironment(v string)`

SetEnvironment sets Environment field to given value.


### GetBranchName

`func (o *SnapshotInput) GetBranchName() string`

GetBranchName returns the BranchName field if non-nil, zero value otherwise.

### GetBranchNameOk

`func (o *SnapshotInput) GetBranchNameOk() (*string, bool)`

GetBranchNameOk returns a tuple with the BranchName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBranchName

`func (o *SnapshotInput) SetBranchName(v string)`

SetBranchName sets BranchName field to given value.

### HasBranchName

`func (o *SnapshotInput) HasBranchName() bool`

HasBranchName returns a boolean if a field has been set.

### SetBranchNameNil

`func (o *SnapshotInput) SetBranchNameNil(b bool)`

 SetBranchNameNil sets the value for BranchName to be an explicit nil

### UnsetBranchName
`func (o *SnapshotInput) UnsetBranchName()`

UnsetBranchName ensures that no value is present for BranchName, not even an explicit nil
### GetBackendCommit

`func (o *SnapshotInput) GetBackendCommit() string`

GetBackendCommit returns the BackendCommit field if non-nil, zero value otherwise.

### GetBackendCommitOk

`func (o *SnapshotInput) GetBackendCommitOk() (*string, bool)`

GetBackendCommitOk returns a tuple with the BackendCommit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBackendCommit

`func (o *SnapshotInput) SetBackendCommit(v string)`

SetBackendCommit sets BackendCommit field to given value.

### HasBackendCommit

`func (o *SnapshotInput) HasBackendCommit() bool`

HasBackendCommit returns a boolean if a field has been set.

### SetBackendCommitNil

`func (o *SnapshotInput) SetBackendCommitNil(b bool)`

 SetBackendCommitNil sets the value for BackendCommit to be an explicit nil

### UnsetBackendCommit
`func (o *SnapshotInput) UnsetBackendCommit()`

UnsetBackendCommit ensures that no value is present for BackendCommit, not even an explicit nil
### GetFrontendCommit

`func (o *SnapshotInput) GetFrontendCommit() string`

GetFrontendCommit returns the FrontendCommit field if non-nil, zero value otherwise.

### GetFrontendCommitOk

`func (o *SnapshotInput) GetFrontendCommitOk() (*string, bool)`

GetFrontendCommitOk returns a tuple with the FrontendCommit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrontendCommit

`func (o *SnapshotInput) SetFrontendCommit(v string)`

SetFrontendCommit sets FrontendCommit field to given value.

### HasFrontendCommit

`func (o *SnapshotInput) HasFrontendCommit() bool`

HasFrontendCommit returns a boolean if a field has been set.

### SetFrontendCommitNil

`func (o *SnapshotInput) SetFrontendCommitNil(b bool)`

 SetFrontendCommitNil sets the value for FrontendCommit to be an explicit nil

### UnsetFrontendCommit
`func (o *SnapshotInput) UnsetFrontendCommit()`

UnsetFrontendCommit ensures that no value is present for FrontendCommit, not even an explicit nil
### GetCreatedBy

`func (o *SnapshotInput) GetCreatedBy() string`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *SnapshotInput) GetCreatedByOk() (*string, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *SnapshotInput) SetCreatedBy(v string)`

SetCreatedBy sets CreatedBy field to given value.

### HasCreatedBy

`func (o *SnapshotInput) HasCreatedBy() bool`

HasCreatedBy returns a boolean if a field has been set.

### SetCreatedByNil

`func (o *SnapshotInput) SetCreatedByNil(b bool)`

 SetCreatedByNil sets the value for CreatedBy to be an explicit nil

### UnsetCreatedBy
`func (o *SnapshotInput) UnsetCreatedBy()`

UnsetCreatedBy ensures that no value is present for CreatedBy, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


