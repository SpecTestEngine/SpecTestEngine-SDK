# SnapshotStepDiffSection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Added** | [**[]SnapshotStepDiffGroup**](SnapshotStepDiffGroup.md) |  |
**Removed** | [**[]SnapshotStepDiffGroup**](SnapshotStepDiffGroup.md) |  |
**Changed** | [**[]SnapshotStepDiffGroup**](SnapshotStepDiffGroup.md) |  |

## Methods

### NewSnapshotStepDiffSection

`func NewSnapshotStepDiffSection(added []SnapshotStepDiffGroup, removed []SnapshotStepDiffGroup, changed []SnapshotStepDiffGroup, ) *SnapshotStepDiffSection`

NewSnapshotStepDiffSection instantiates a new SnapshotStepDiffSection object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSnapshotStepDiffSectionWithDefaults

`func NewSnapshotStepDiffSectionWithDefaults() *SnapshotStepDiffSection`

NewSnapshotStepDiffSectionWithDefaults instantiates a new SnapshotStepDiffSection object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAdded

`func (o *SnapshotStepDiffSection) GetAdded() []SnapshotStepDiffGroup`

GetAdded returns the Added field if non-nil, zero value otherwise.

### GetAddedOk

`func (o *SnapshotStepDiffSection) GetAddedOk() (*[]SnapshotStepDiffGroup, bool)`

GetAddedOk returns a tuple with the Added field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdded

`func (o *SnapshotStepDiffSection) SetAdded(v []SnapshotStepDiffGroup)`

SetAdded sets Added field to given value.


### GetRemoved

`func (o *SnapshotStepDiffSection) GetRemoved() []SnapshotStepDiffGroup`

GetRemoved returns the Removed field if non-nil, zero value otherwise.

### GetRemovedOk

`func (o *SnapshotStepDiffSection) GetRemovedOk() (*[]SnapshotStepDiffGroup, bool)`

GetRemovedOk returns a tuple with the Removed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoved

`func (o *SnapshotStepDiffSection) SetRemoved(v []SnapshotStepDiffGroup)`

SetRemoved sets Removed field to given value.


### GetChanged

`func (o *SnapshotStepDiffSection) GetChanged() []SnapshotStepDiffGroup`

GetChanged returns the Changed field if non-nil, zero value otherwise.

### GetChangedOk

`func (o *SnapshotStepDiffSection) GetChangedOk() (*[]SnapshotStepDiffGroup, bool)`

GetChangedOk returns a tuple with the Changed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChanged

`func (o *SnapshotStepDiffSection) SetChanged(v []SnapshotStepDiffGroup)`

SetChanged sets Changed field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


