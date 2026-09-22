# CraftsmanRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RunId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**WorkspaceId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**NodeId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**State** | [**CraftsmanRunState**](CraftsmanRunState.md) |  |
**Result** | Pointer to [**NullableRequestChainRun**](RequestChainRun.md) |  | [optional]
**Transcript** | Pointer to **interface{}** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**ErrorMessage** | Pointer to **NullableString** |  | [optional]
**CreatedAt** | **time.Time** |  |
**StartedAt** | Pointer to **NullableTime** |  | [optional]
**FinishedAt** | Pointer to **NullableTime** |  | [optional]

## Methods

### NewCraftsmanRun

`func NewCraftsmanRun(runId string, state CraftsmanRunState, createdAt time.Time, ) *CraftsmanRun`

NewCraftsmanRun instantiates a new CraftsmanRun object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCraftsmanRunWithDefaults

`func NewCraftsmanRunWithDefaults() *CraftsmanRun`

NewCraftsmanRunWithDefaults instantiates a new CraftsmanRun object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRunId

`func (o *CraftsmanRun) GetRunId() string`

GetRunId returns the RunId field if non-nil, zero value otherwise.

### GetRunIdOk

`func (o *CraftsmanRun) GetRunIdOk() (*string, bool)`

GetRunIdOk returns a tuple with the RunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRunId

`func (o *CraftsmanRun) SetRunId(v string)`

SetRunId sets RunId field to given value.


### GetWorkspaceId

`func (o *CraftsmanRun) GetWorkspaceId() string`

GetWorkspaceId returns the WorkspaceId field if non-nil, zero value otherwise.

### GetWorkspaceIdOk

`func (o *CraftsmanRun) GetWorkspaceIdOk() (*string, bool)`

GetWorkspaceIdOk returns a tuple with the WorkspaceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWorkspaceId

`func (o *CraftsmanRun) SetWorkspaceId(v string)`

SetWorkspaceId sets WorkspaceId field to given value.

### HasWorkspaceId

`func (o *CraftsmanRun) HasWorkspaceId() bool`

HasWorkspaceId returns a boolean if a field has been set.

### SetWorkspaceIdNil

`func (o *CraftsmanRun) SetWorkspaceIdNil(b bool)`

 SetWorkspaceIdNil sets the value for WorkspaceId to be an explicit nil

### UnsetWorkspaceId
`func (o *CraftsmanRun) UnsetWorkspaceId()`

UnsetWorkspaceId ensures that no value is present for WorkspaceId, not even an explicit nil
### GetNodeId

`func (o *CraftsmanRun) GetNodeId() string`

GetNodeId returns the NodeId field if non-nil, zero value otherwise.

### GetNodeIdOk

`func (o *CraftsmanRun) GetNodeIdOk() (*string, bool)`

GetNodeIdOk returns a tuple with the NodeId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNodeId

`func (o *CraftsmanRun) SetNodeId(v string)`

SetNodeId sets NodeId field to given value.

### HasNodeId

`func (o *CraftsmanRun) HasNodeId() bool`

HasNodeId returns a boolean if a field has been set.

### SetNodeIdNil

`func (o *CraftsmanRun) SetNodeIdNil(b bool)`

 SetNodeIdNil sets the value for NodeId to be an explicit nil

### UnsetNodeId
`func (o *CraftsmanRun) UnsetNodeId()`

UnsetNodeId ensures that no value is present for NodeId, not even an explicit nil
### GetState

`func (o *CraftsmanRun) GetState() CraftsmanRunState`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *CraftsmanRun) GetStateOk() (*CraftsmanRunState, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *CraftsmanRun) SetState(v CraftsmanRunState)`

SetState sets State field to given value.


### GetResult

`func (o *CraftsmanRun) GetResult() RequestChainRun`

GetResult returns the Result field if non-nil, zero value otherwise.

### GetResultOk

`func (o *CraftsmanRun) GetResultOk() (*RequestChainRun, bool)`

GetResultOk returns a tuple with the Result field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResult

`func (o *CraftsmanRun) SetResult(v RequestChainRun)`

SetResult sets Result field to given value.

### HasResult

`func (o *CraftsmanRun) HasResult() bool`

HasResult returns a boolean if a field has been set.

### SetResultNil

`func (o *CraftsmanRun) SetResultNil(b bool)`

 SetResultNil sets the value for Result to be an explicit nil

### UnsetResult
`func (o *CraftsmanRun) UnsetResult()`

UnsetResult ensures that no value is present for Result, not even an explicit nil
### GetTranscript

`func (o *CraftsmanRun) GetTranscript() interface{}`

GetTranscript returns the Transcript field if non-nil, zero value otherwise.

### GetTranscriptOk

`func (o *CraftsmanRun) GetTranscriptOk() (*interface{}, bool)`

GetTranscriptOk returns a tuple with the Transcript field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTranscript

`func (o *CraftsmanRun) SetTranscript(v interface{})`

SetTranscript sets Transcript field to given value.

### HasTranscript

`func (o *CraftsmanRun) HasTranscript() bool`

HasTranscript returns a boolean if a field has been set.

### SetTranscriptNil

`func (o *CraftsmanRun) SetTranscriptNil(b bool)`

 SetTranscriptNil sets the value for Transcript to be an explicit nil

### UnsetTranscript
`func (o *CraftsmanRun) UnsetTranscript()`

UnsetTranscript ensures that no value is present for Transcript, not even an explicit nil
### GetErrorMessage

`func (o *CraftsmanRun) GetErrorMessage() string`

GetErrorMessage returns the ErrorMessage field if non-nil, zero value otherwise.

### GetErrorMessageOk

`func (o *CraftsmanRun) GetErrorMessageOk() (*string, bool)`

GetErrorMessageOk returns a tuple with the ErrorMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorMessage

`func (o *CraftsmanRun) SetErrorMessage(v string)`

SetErrorMessage sets ErrorMessage field to given value.

### HasErrorMessage

`func (o *CraftsmanRun) HasErrorMessage() bool`

HasErrorMessage returns a boolean if a field has been set.

### SetErrorMessageNil

`func (o *CraftsmanRun) SetErrorMessageNil(b bool)`

 SetErrorMessageNil sets the value for ErrorMessage to be an explicit nil

### UnsetErrorMessage
`func (o *CraftsmanRun) UnsetErrorMessage()`

UnsetErrorMessage ensures that no value is present for ErrorMessage, not even an explicit nil
### GetCreatedAt

`func (o *CraftsmanRun) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *CraftsmanRun) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *CraftsmanRun) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetStartedAt

`func (o *CraftsmanRun) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *CraftsmanRun) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *CraftsmanRun) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.

### HasStartedAt

`func (o *CraftsmanRun) HasStartedAt() bool`

HasStartedAt returns a boolean if a field has been set.

### SetStartedAtNil

`func (o *CraftsmanRun) SetStartedAtNil(b bool)`

 SetStartedAtNil sets the value for StartedAt to be an explicit nil

### UnsetStartedAt
`func (o *CraftsmanRun) UnsetStartedAt()`

UnsetStartedAt ensures that no value is present for StartedAt, not even an explicit nil
### GetFinishedAt

`func (o *CraftsmanRun) GetFinishedAt() time.Time`

GetFinishedAt returns the FinishedAt field if non-nil, zero value otherwise.

### GetFinishedAtOk

`func (o *CraftsmanRun) GetFinishedAtOk() (*time.Time, bool)`

GetFinishedAtOk returns a tuple with the FinishedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinishedAt

`func (o *CraftsmanRun) SetFinishedAt(v time.Time)`

SetFinishedAt sets FinishedAt field to given value.

### HasFinishedAt

`func (o *CraftsmanRun) HasFinishedAt() bool`

HasFinishedAt returns a boolean if a field has been set.

### SetFinishedAtNil

`func (o *CraftsmanRun) SetFinishedAtNil(b bool)`

 SetFinishedAtNil sets the value for FinishedAt to be an explicit nil

### UnsetFinishedAt
`func (o *CraftsmanRun) UnsetFinishedAt()`

UnsetFinishedAt ensures that no value is present for FinishedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


