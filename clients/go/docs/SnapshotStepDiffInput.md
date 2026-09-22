# SnapshotStepDiffInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StepType** | [**SnapshotStepType**](SnapshotStepType.md) |  |
**LeftDefinitionPayload** | Pointer to **interface{}** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**RightDefinitionPayload** | Pointer to **interface{}** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**LeftBehaviorPayload** | Pointer to **interface{}** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**RightBehaviorPayload** | Pointer to **interface{}** | A JSON value whose shape depends on the captured test subject and step type. | [optional]

## Methods

### NewSnapshotStepDiffInput

`func NewSnapshotStepDiffInput(stepType SnapshotStepType, ) *SnapshotStepDiffInput`

NewSnapshotStepDiffInput instantiates a new SnapshotStepDiffInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSnapshotStepDiffInputWithDefaults

`func NewSnapshotStepDiffInputWithDefaults() *SnapshotStepDiffInput`

NewSnapshotStepDiffInputWithDefaults instantiates a new SnapshotStepDiffInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStepType

`func (o *SnapshotStepDiffInput) GetStepType() SnapshotStepType`

GetStepType returns the StepType field if non-nil, zero value otherwise.

### GetStepTypeOk

`func (o *SnapshotStepDiffInput) GetStepTypeOk() (*SnapshotStepType, bool)`

GetStepTypeOk returns a tuple with the StepType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepType

`func (o *SnapshotStepDiffInput) SetStepType(v SnapshotStepType)`

SetStepType sets StepType field to given value.


### GetLeftDefinitionPayload

`func (o *SnapshotStepDiffInput) GetLeftDefinitionPayload() interface{}`

GetLeftDefinitionPayload returns the LeftDefinitionPayload field if non-nil, zero value otherwise.

### GetLeftDefinitionPayloadOk

`func (o *SnapshotStepDiffInput) GetLeftDefinitionPayloadOk() (*interface{}, bool)`

GetLeftDefinitionPayloadOk returns a tuple with the LeftDefinitionPayload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeftDefinitionPayload

`func (o *SnapshotStepDiffInput) SetLeftDefinitionPayload(v interface{})`

SetLeftDefinitionPayload sets LeftDefinitionPayload field to given value.

### HasLeftDefinitionPayload

`func (o *SnapshotStepDiffInput) HasLeftDefinitionPayload() bool`

HasLeftDefinitionPayload returns a boolean if a field has been set.

### SetLeftDefinitionPayloadNil

`func (o *SnapshotStepDiffInput) SetLeftDefinitionPayloadNil(b bool)`

 SetLeftDefinitionPayloadNil sets the value for LeftDefinitionPayload to be an explicit nil

### UnsetLeftDefinitionPayload
`func (o *SnapshotStepDiffInput) UnsetLeftDefinitionPayload()`

UnsetLeftDefinitionPayload ensures that no value is present for LeftDefinitionPayload, not even an explicit nil
### GetRightDefinitionPayload

`func (o *SnapshotStepDiffInput) GetRightDefinitionPayload() interface{}`

GetRightDefinitionPayload returns the RightDefinitionPayload field if non-nil, zero value otherwise.

### GetRightDefinitionPayloadOk

`func (o *SnapshotStepDiffInput) GetRightDefinitionPayloadOk() (*interface{}, bool)`

GetRightDefinitionPayloadOk returns a tuple with the RightDefinitionPayload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRightDefinitionPayload

`func (o *SnapshotStepDiffInput) SetRightDefinitionPayload(v interface{})`

SetRightDefinitionPayload sets RightDefinitionPayload field to given value.

### HasRightDefinitionPayload

`func (o *SnapshotStepDiffInput) HasRightDefinitionPayload() bool`

HasRightDefinitionPayload returns a boolean if a field has been set.

### SetRightDefinitionPayloadNil

`func (o *SnapshotStepDiffInput) SetRightDefinitionPayloadNil(b bool)`

 SetRightDefinitionPayloadNil sets the value for RightDefinitionPayload to be an explicit nil

### UnsetRightDefinitionPayload
`func (o *SnapshotStepDiffInput) UnsetRightDefinitionPayload()`

UnsetRightDefinitionPayload ensures that no value is present for RightDefinitionPayload, not even an explicit nil
### GetLeftBehaviorPayload

`func (o *SnapshotStepDiffInput) GetLeftBehaviorPayload() interface{}`

GetLeftBehaviorPayload returns the LeftBehaviorPayload field if non-nil, zero value otherwise.

### GetLeftBehaviorPayloadOk

`func (o *SnapshotStepDiffInput) GetLeftBehaviorPayloadOk() (*interface{}, bool)`

GetLeftBehaviorPayloadOk returns a tuple with the LeftBehaviorPayload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeftBehaviorPayload

`func (o *SnapshotStepDiffInput) SetLeftBehaviorPayload(v interface{})`

SetLeftBehaviorPayload sets LeftBehaviorPayload field to given value.

### HasLeftBehaviorPayload

`func (o *SnapshotStepDiffInput) HasLeftBehaviorPayload() bool`

HasLeftBehaviorPayload returns a boolean if a field has been set.

### SetLeftBehaviorPayloadNil

`func (o *SnapshotStepDiffInput) SetLeftBehaviorPayloadNil(b bool)`

 SetLeftBehaviorPayloadNil sets the value for LeftBehaviorPayload to be an explicit nil

### UnsetLeftBehaviorPayload
`func (o *SnapshotStepDiffInput) UnsetLeftBehaviorPayload()`

UnsetLeftBehaviorPayload ensures that no value is present for LeftBehaviorPayload, not even an explicit nil
### GetRightBehaviorPayload

`func (o *SnapshotStepDiffInput) GetRightBehaviorPayload() interface{}`

GetRightBehaviorPayload returns the RightBehaviorPayload field if non-nil, zero value otherwise.

### GetRightBehaviorPayloadOk

`func (o *SnapshotStepDiffInput) GetRightBehaviorPayloadOk() (*interface{}, bool)`

GetRightBehaviorPayloadOk returns a tuple with the RightBehaviorPayload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRightBehaviorPayload

`func (o *SnapshotStepDiffInput) SetRightBehaviorPayload(v interface{})`

SetRightBehaviorPayload sets RightBehaviorPayload field to given value.

### HasRightBehaviorPayload

`func (o *SnapshotStepDiffInput) HasRightBehaviorPayload() bool`

HasRightBehaviorPayload returns a boolean if a field has been set.

### SetRightBehaviorPayloadNil

`func (o *SnapshotStepDiffInput) SetRightBehaviorPayloadNil(b bool)`

 SetRightBehaviorPayloadNil sets the value for RightBehaviorPayload to be an explicit nil

### UnsetRightBehaviorPayload
`func (o *SnapshotStepDiffInput) UnsetRightBehaviorPayload()`

UnsetRightBehaviorPayload ensures that no value is present for RightBehaviorPayload, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


