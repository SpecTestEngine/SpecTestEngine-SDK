# SnapshotDiff

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LeftSnapshotId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**RightSnapshotId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**BatchId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**Entries** | [**[]SnapshotDiffEntry**](SnapshotDiffEntry.md) |  |
**GeneratedAt** | **time.Time** |  |

## Methods

### NewSnapshotDiff

`func NewSnapshotDiff(entries []SnapshotDiffEntry, generatedAt time.Time, ) *SnapshotDiff`

NewSnapshotDiff instantiates a new SnapshotDiff object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSnapshotDiffWithDefaults

`func NewSnapshotDiffWithDefaults() *SnapshotDiff`

NewSnapshotDiffWithDefaults instantiates a new SnapshotDiff object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLeftSnapshotId

`func (o *SnapshotDiff) GetLeftSnapshotId() string`

GetLeftSnapshotId returns the LeftSnapshotId field if non-nil, zero value otherwise.

### GetLeftSnapshotIdOk

`func (o *SnapshotDiff) GetLeftSnapshotIdOk() (*string, bool)`

GetLeftSnapshotIdOk returns a tuple with the LeftSnapshotId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeftSnapshotId

`func (o *SnapshotDiff) SetLeftSnapshotId(v string)`

SetLeftSnapshotId sets LeftSnapshotId field to given value.

### HasLeftSnapshotId

`func (o *SnapshotDiff) HasLeftSnapshotId() bool`

HasLeftSnapshotId returns a boolean if a field has been set.

### SetLeftSnapshotIdNil

`func (o *SnapshotDiff) SetLeftSnapshotIdNil(b bool)`

 SetLeftSnapshotIdNil sets the value for LeftSnapshotId to be an explicit nil

### UnsetLeftSnapshotId
`func (o *SnapshotDiff) UnsetLeftSnapshotId()`

UnsetLeftSnapshotId ensures that no value is present for LeftSnapshotId, not even an explicit nil
### GetRightSnapshotId

`func (o *SnapshotDiff) GetRightSnapshotId() string`

GetRightSnapshotId returns the RightSnapshotId field if non-nil, zero value otherwise.

### GetRightSnapshotIdOk

`func (o *SnapshotDiff) GetRightSnapshotIdOk() (*string, bool)`

GetRightSnapshotIdOk returns a tuple with the RightSnapshotId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRightSnapshotId

`func (o *SnapshotDiff) SetRightSnapshotId(v string)`

SetRightSnapshotId sets RightSnapshotId field to given value.

### HasRightSnapshotId

`func (o *SnapshotDiff) HasRightSnapshotId() bool`

HasRightSnapshotId returns a boolean if a field has been set.

### SetRightSnapshotIdNil

`func (o *SnapshotDiff) SetRightSnapshotIdNil(b bool)`

 SetRightSnapshotIdNil sets the value for RightSnapshotId to be an explicit nil

### UnsetRightSnapshotId
`func (o *SnapshotDiff) UnsetRightSnapshotId()`

UnsetRightSnapshotId ensures that no value is present for RightSnapshotId, not even an explicit nil
### GetBatchId

`func (o *SnapshotDiff) GetBatchId() string`

GetBatchId returns the BatchId field if non-nil, zero value otherwise.

### GetBatchIdOk

`func (o *SnapshotDiff) GetBatchIdOk() (*string, bool)`

GetBatchIdOk returns a tuple with the BatchId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBatchId

`func (o *SnapshotDiff) SetBatchId(v string)`

SetBatchId sets BatchId field to given value.

### HasBatchId

`func (o *SnapshotDiff) HasBatchId() bool`

HasBatchId returns a boolean if a field has been set.

### SetBatchIdNil

`func (o *SnapshotDiff) SetBatchIdNil(b bool)`

 SetBatchIdNil sets the value for BatchId to be an explicit nil

### UnsetBatchId
`func (o *SnapshotDiff) UnsetBatchId()`

UnsetBatchId ensures that no value is present for BatchId, not even an explicit nil
### GetEntries

`func (o *SnapshotDiff) GetEntries() []SnapshotDiffEntry`

GetEntries returns the Entries field if non-nil, zero value otherwise.

### GetEntriesOk

`func (o *SnapshotDiff) GetEntriesOk() (*[]SnapshotDiffEntry, bool)`

GetEntriesOk returns a tuple with the Entries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntries

`func (o *SnapshotDiff) SetEntries(v []SnapshotDiffEntry)`

SetEntries sets Entries field to given value.


### GetGeneratedAt

`func (o *SnapshotDiff) GetGeneratedAt() time.Time`

GetGeneratedAt returns the GeneratedAt field if non-nil, zero value otherwise.

### GetGeneratedAtOk

`func (o *SnapshotDiff) GetGeneratedAtOk() (*time.Time, bool)`

GetGeneratedAtOk returns a tuple with the GeneratedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGeneratedAt

`func (o *SnapshotDiff) SetGeneratedAt(v time.Time)`

SetGeneratedAt sets GeneratedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


