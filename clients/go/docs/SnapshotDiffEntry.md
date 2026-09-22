# SnapshotDiffEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SubjectType** | [**SnapshotSubjectType**](SnapshotSubjectType.md) |  |
**SubjectKey** | **string** |  |
**SubjectName** | **string** |  |
**ChangeType** | [**SnapshotDiffChangeType**](SnapshotDiffChangeType.md) |  |
**LeftStatus** | Pointer to **NullableString** |  | [optional]
**RightStatus** | Pointer to **NullableString** |  | [optional]
**LeftDefinitionHash** | Pointer to **NullableString** |  | [optional]
**RightDefinitionHash** | Pointer to **NullableString** |  | [optional]
**LeftBehaviorHash** | Pointer to **NullableString** |  | [optional]
**RightBehaviorHash** | Pointer to **NullableString** |  | [optional]
**Details** | Pointer to **NullableString** |  | [optional]

## Methods

### NewSnapshotDiffEntry

`func NewSnapshotDiffEntry(subjectType SnapshotSubjectType, subjectKey string, subjectName string, changeType SnapshotDiffChangeType, ) *SnapshotDiffEntry`

NewSnapshotDiffEntry instantiates a new SnapshotDiffEntry object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSnapshotDiffEntryWithDefaults

`func NewSnapshotDiffEntryWithDefaults() *SnapshotDiffEntry`

NewSnapshotDiffEntryWithDefaults instantiates a new SnapshotDiffEntry object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSubjectType

`func (o *SnapshotDiffEntry) GetSubjectType() SnapshotSubjectType`

GetSubjectType returns the SubjectType field if non-nil, zero value otherwise.

### GetSubjectTypeOk

`func (o *SnapshotDiffEntry) GetSubjectTypeOk() (*SnapshotSubjectType, bool)`

GetSubjectTypeOk returns a tuple with the SubjectType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubjectType

`func (o *SnapshotDiffEntry) SetSubjectType(v SnapshotSubjectType)`

SetSubjectType sets SubjectType field to given value.


### GetSubjectKey

`func (o *SnapshotDiffEntry) GetSubjectKey() string`

GetSubjectKey returns the SubjectKey field if non-nil, zero value otherwise.

### GetSubjectKeyOk

`func (o *SnapshotDiffEntry) GetSubjectKeyOk() (*string, bool)`

GetSubjectKeyOk returns a tuple with the SubjectKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubjectKey

`func (o *SnapshotDiffEntry) SetSubjectKey(v string)`

SetSubjectKey sets SubjectKey field to given value.


### GetSubjectName

`func (o *SnapshotDiffEntry) GetSubjectName() string`

GetSubjectName returns the SubjectName field if non-nil, zero value otherwise.

### GetSubjectNameOk

`func (o *SnapshotDiffEntry) GetSubjectNameOk() (*string, bool)`

GetSubjectNameOk returns a tuple with the SubjectName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubjectName

`func (o *SnapshotDiffEntry) SetSubjectName(v string)`

SetSubjectName sets SubjectName field to given value.


### GetChangeType

`func (o *SnapshotDiffEntry) GetChangeType() SnapshotDiffChangeType`

GetChangeType returns the ChangeType field if non-nil, zero value otherwise.

### GetChangeTypeOk

`func (o *SnapshotDiffEntry) GetChangeTypeOk() (*SnapshotDiffChangeType, bool)`

GetChangeTypeOk returns a tuple with the ChangeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangeType

`func (o *SnapshotDiffEntry) SetChangeType(v SnapshotDiffChangeType)`

SetChangeType sets ChangeType field to given value.


### GetLeftStatus

`func (o *SnapshotDiffEntry) GetLeftStatus() string`

GetLeftStatus returns the LeftStatus field if non-nil, zero value otherwise.

### GetLeftStatusOk

`func (o *SnapshotDiffEntry) GetLeftStatusOk() (*string, bool)`

GetLeftStatusOk returns a tuple with the LeftStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeftStatus

`func (o *SnapshotDiffEntry) SetLeftStatus(v string)`

SetLeftStatus sets LeftStatus field to given value.

### HasLeftStatus

`func (o *SnapshotDiffEntry) HasLeftStatus() bool`

HasLeftStatus returns a boolean if a field has been set.

### SetLeftStatusNil

`func (o *SnapshotDiffEntry) SetLeftStatusNil(b bool)`

 SetLeftStatusNil sets the value for LeftStatus to be an explicit nil

### UnsetLeftStatus
`func (o *SnapshotDiffEntry) UnsetLeftStatus()`

UnsetLeftStatus ensures that no value is present for LeftStatus, not even an explicit nil
### GetRightStatus

`func (o *SnapshotDiffEntry) GetRightStatus() string`

GetRightStatus returns the RightStatus field if non-nil, zero value otherwise.

### GetRightStatusOk

`func (o *SnapshotDiffEntry) GetRightStatusOk() (*string, bool)`

GetRightStatusOk returns a tuple with the RightStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRightStatus

`func (o *SnapshotDiffEntry) SetRightStatus(v string)`

SetRightStatus sets RightStatus field to given value.

### HasRightStatus

`func (o *SnapshotDiffEntry) HasRightStatus() bool`

HasRightStatus returns a boolean if a field has been set.

### SetRightStatusNil

`func (o *SnapshotDiffEntry) SetRightStatusNil(b bool)`

 SetRightStatusNil sets the value for RightStatus to be an explicit nil

### UnsetRightStatus
`func (o *SnapshotDiffEntry) UnsetRightStatus()`

UnsetRightStatus ensures that no value is present for RightStatus, not even an explicit nil
### GetLeftDefinitionHash

`func (o *SnapshotDiffEntry) GetLeftDefinitionHash() string`

GetLeftDefinitionHash returns the LeftDefinitionHash field if non-nil, zero value otherwise.

### GetLeftDefinitionHashOk

`func (o *SnapshotDiffEntry) GetLeftDefinitionHashOk() (*string, bool)`

GetLeftDefinitionHashOk returns a tuple with the LeftDefinitionHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeftDefinitionHash

`func (o *SnapshotDiffEntry) SetLeftDefinitionHash(v string)`

SetLeftDefinitionHash sets LeftDefinitionHash field to given value.

### HasLeftDefinitionHash

`func (o *SnapshotDiffEntry) HasLeftDefinitionHash() bool`

HasLeftDefinitionHash returns a boolean if a field has been set.

### SetLeftDefinitionHashNil

`func (o *SnapshotDiffEntry) SetLeftDefinitionHashNil(b bool)`

 SetLeftDefinitionHashNil sets the value for LeftDefinitionHash to be an explicit nil

### UnsetLeftDefinitionHash
`func (o *SnapshotDiffEntry) UnsetLeftDefinitionHash()`

UnsetLeftDefinitionHash ensures that no value is present for LeftDefinitionHash, not even an explicit nil
### GetRightDefinitionHash

`func (o *SnapshotDiffEntry) GetRightDefinitionHash() string`

GetRightDefinitionHash returns the RightDefinitionHash field if non-nil, zero value otherwise.

### GetRightDefinitionHashOk

`func (o *SnapshotDiffEntry) GetRightDefinitionHashOk() (*string, bool)`

GetRightDefinitionHashOk returns a tuple with the RightDefinitionHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRightDefinitionHash

`func (o *SnapshotDiffEntry) SetRightDefinitionHash(v string)`

SetRightDefinitionHash sets RightDefinitionHash field to given value.

### HasRightDefinitionHash

`func (o *SnapshotDiffEntry) HasRightDefinitionHash() bool`

HasRightDefinitionHash returns a boolean if a field has been set.

### SetRightDefinitionHashNil

`func (o *SnapshotDiffEntry) SetRightDefinitionHashNil(b bool)`

 SetRightDefinitionHashNil sets the value for RightDefinitionHash to be an explicit nil

### UnsetRightDefinitionHash
`func (o *SnapshotDiffEntry) UnsetRightDefinitionHash()`

UnsetRightDefinitionHash ensures that no value is present for RightDefinitionHash, not even an explicit nil
### GetLeftBehaviorHash

`func (o *SnapshotDiffEntry) GetLeftBehaviorHash() string`

GetLeftBehaviorHash returns the LeftBehaviorHash field if non-nil, zero value otherwise.

### GetLeftBehaviorHashOk

`func (o *SnapshotDiffEntry) GetLeftBehaviorHashOk() (*string, bool)`

GetLeftBehaviorHashOk returns a tuple with the LeftBehaviorHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeftBehaviorHash

`func (o *SnapshotDiffEntry) SetLeftBehaviorHash(v string)`

SetLeftBehaviorHash sets LeftBehaviorHash field to given value.

### HasLeftBehaviorHash

`func (o *SnapshotDiffEntry) HasLeftBehaviorHash() bool`

HasLeftBehaviorHash returns a boolean if a field has been set.

### SetLeftBehaviorHashNil

`func (o *SnapshotDiffEntry) SetLeftBehaviorHashNil(b bool)`

 SetLeftBehaviorHashNil sets the value for LeftBehaviorHash to be an explicit nil

### UnsetLeftBehaviorHash
`func (o *SnapshotDiffEntry) UnsetLeftBehaviorHash()`

UnsetLeftBehaviorHash ensures that no value is present for LeftBehaviorHash, not even an explicit nil
### GetRightBehaviorHash

`func (o *SnapshotDiffEntry) GetRightBehaviorHash() string`

GetRightBehaviorHash returns the RightBehaviorHash field if non-nil, zero value otherwise.

### GetRightBehaviorHashOk

`func (o *SnapshotDiffEntry) GetRightBehaviorHashOk() (*string, bool)`

GetRightBehaviorHashOk returns a tuple with the RightBehaviorHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRightBehaviorHash

`func (o *SnapshotDiffEntry) SetRightBehaviorHash(v string)`

SetRightBehaviorHash sets RightBehaviorHash field to given value.

### HasRightBehaviorHash

`func (o *SnapshotDiffEntry) HasRightBehaviorHash() bool`

HasRightBehaviorHash returns a boolean if a field has been set.

### SetRightBehaviorHashNil

`func (o *SnapshotDiffEntry) SetRightBehaviorHashNil(b bool)`

 SetRightBehaviorHashNil sets the value for RightBehaviorHash to be an explicit nil

### UnsetRightBehaviorHash
`func (o *SnapshotDiffEntry) UnsetRightBehaviorHash()`

UnsetRightBehaviorHash ensures that no value is present for RightBehaviorHash, not even an explicit nil
### GetDetails

`func (o *SnapshotDiffEntry) GetDetails() string`

GetDetails returns the Details field if non-nil, zero value otherwise.

### GetDetailsOk

`func (o *SnapshotDiffEntry) GetDetailsOk() (*string, bool)`

GetDetailsOk returns a tuple with the Details field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDetails

`func (o *SnapshotDiffEntry) SetDetails(v string)`

SetDetails sets Details field to given value.

### HasDetails

`func (o *SnapshotDiffEntry) HasDetails() bool`

HasDetails returns a boolean if a field has been set.

### SetDetailsNil

`func (o *SnapshotDiffEntry) SetDetailsNil(b bool)`

 SetDetailsNil sets the value for Details to be an explicit nil

### UnsetDetails
`func (o *SnapshotDiffEntry) UnsetDetails()`

UnsetDetails ensures that no value is present for Details, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


