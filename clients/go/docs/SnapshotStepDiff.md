# SnapshotStepDiff

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StepType** | [**SnapshotStepType**](SnapshotStepType.md) |  |
**Overview** | **[]string** |  |
**Definition** | [**SnapshotStepDiffSection**](SnapshotStepDiffSection.md) |  |
**Behavior** | [**SnapshotStepDiffSection**](SnapshotStepDiffSection.md) |  |

## Methods

### NewSnapshotStepDiff

`func NewSnapshotStepDiff(stepType SnapshotStepType, overview []string, definition SnapshotStepDiffSection, behavior SnapshotStepDiffSection, ) *SnapshotStepDiff`

NewSnapshotStepDiff instantiates a new SnapshotStepDiff object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSnapshotStepDiffWithDefaults

`func NewSnapshotStepDiffWithDefaults() *SnapshotStepDiff`

NewSnapshotStepDiffWithDefaults instantiates a new SnapshotStepDiff object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStepType

`func (o *SnapshotStepDiff) GetStepType() SnapshotStepType`

GetStepType returns the StepType field if non-nil, zero value otherwise.

### GetStepTypeOk

`func (o *SnapshotStepDiff) GetStepTypeOk() (*SnapshotStepType, bool)`

GetStepTypeOk returns a tuple with the StepType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepType

`func (o *SnapshotStepDiff) SetStepType(v SnapshotStepType)`

SetStepType sets StepType field to given value.


### GetOverview

`func (o *SnapshotStepDiff) GetOverview() []string`

GetOverview returns the Overview field if non-nil, zero value otherwise.

### GetOverviewOk

`func (o *SnapshotStepDiff) GetOverviewOk() (*[]string, bool)`

GetOverviewOk returns a tuple with the Overview field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOverview

`func (o *SnapshotStepDiff) SetOverview(v []string)`

SetOverview sets Overview field to given value.


### GetDefinition

`func (o *SnapshotStepDiff) GetDefinition() SnapshotStepDiffSection`

GetDefinition returns the Definition field if non-nil, zero value otherwise.

### GetDefinitionOk

`func (o *SnapshotStepDiff) GetDefinitionOk() (*SnapshotStepDiffSection, bool)`

GetDefinitionOk returns a tuple with the Definition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinition

`func (o *SnapshotStepDiff) SetDefinition(v SnapshotStepDiffSection)`

SetDefinition sets Definition field to given value.


### GetBehavior

`func (o *SnapshotStepDiff) GetBehavior() SnapshotStepDiffSection`

GetBehavior returns the Behavior field if non-nil, zero value otherwise.

### GetBehaviorOk

`func (o *SnapshotStepDiff) GetBehaviorOk() (*SnapshotStepDiffSection, bool)`

GetBehaviorOk returns a tuple with the Behavior field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehavior

`func (o *SnapshotStepDiff) SetBehavior(v SnapshotStepDiffSection)`

SetBehavior sets Behavior field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


