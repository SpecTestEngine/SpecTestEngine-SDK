# SnapshotStepDiffItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Path** | **string** |  |
**Label** | **string** |  |
**LeftValue** | Pointer to **interface{}** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**RightValue** | Pointer to **interface{}** | A JSON value whose shape depends on the captured test subject and step type. | [optional]

## Methods

### NewSnapshotStepDiffItem

`func NewSnapshotStepDiffItem(path string, label string, ) *SnapshotStepDiffItem`

NewSnapshotStepDiffItem instantiates a new SnapshotStepDiffItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSnapshotStepDiffItemWithDefaults

`func NewSnapshotStepDiffItemWithDefaults() *SnapshotStepDiffItem`

NewSnapshotStepDiffItemWithDefaults instantiates a new SnapshotStepDiffItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPath

`func (o *SnapshotStepDiffItem) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *SnapshotStepDiffItem) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *SnapshotStepDiffItem) SetPath(v string)`

SetPath sets Path field to given value.


### GetLabel

`func (o *SnapshotStepDiffItem) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *SnapshotStepDiffItem) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *SnapshotStepDiffItem) SetLabel(v string)`

SetLabel sets Label field to given value.


### GetLeftValue

`func (o *SnapshotStepDiffItem) GetLeftValue() interface{}`

GetLeftValue returns the LeftValue field if non-nil, zero value otherwise.

### GetLeftValueOk

`func (o *SnapshotStepDiffItem) GetLeftValueOk() (*interface{}, bool)`

GetLeftValueOk returns a tuple with the LeftValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeftValue

`func (o *SnapshotStepDiffItem) SetLeftValue(v interface{})`

SetLeftValue sets LeftValue field to given value.

### HasLeftValue

`func (o *SnapshotStepDiffItem) HasLeftValue() bool`

HasLeftValue returns a boolean if a field has been set.

### SetLeftValueNil

`func (o *SnapshotStepDiffItem) SetLeftValueNil(b bool)`

 SetLeftValueNil sets the value for LeftValue to be an explicit nil

### UnsetLeftValue
`func (o *SnapshotStepDiffItem) UnsetLeftValue()`

UnsetLeftValue ensures that no value is present for LeftValue, not even an explicit nil
### GetRightValue

`func (o *SnapshotStepDiffItem) GetRightValue() interface{}`

GetRightValue returns the RightValue field if non-nil, zero value otherwise.

### GetRightValueOk

`func (o *SnapshotStepDiffItem) GetRightValueOk() (*interface{}, bool)`

GetRightValueOk returns a tuple with the RightValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRightValue

`func (o *SnapshotStepDiffItem) SetRightValue(v interface{})`

SetRightValue sets RightValue field to given value.

### HasRightValue

`func (o *SnapshotStepDiffItem) HasRightValue() bool`

HasRightValue returns a boolean if a field has been set.

### SetRightValueNil

`func (o *SnapshotStepDiffItem) SetRightValueNil(b bool)`

 SetRightValueNil sets the value for RightValue to be an explicit nil

### UnsetRightValue
`func (o *SnapshotStepDiffItem) UnsetRightValue()`

UnsetRightValue ensures that no value is present for RightValue, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


