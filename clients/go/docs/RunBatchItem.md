# RunBatchItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ItemId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SubjectType** | [**SnapshotSubjectType**](SnapshotSubjectType.md) |  |
**SubjectId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SubjectKey** | **string** |  |
**SubjectName** | **string** |  |
**SourceRunType** | [**SnapshotSourceRunType**](SnapshotSourceRunType.md) |  |
**SourceRunId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Status** | **string** |  |
**DefinitionHash** | Pointer to **NullableString** |  | [optional]
**BehaviorHash** | Pointer to **NullableString** |  | [optional]
**DefinitionPayload** | Pointer to **interface{}** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**BehaviorPayload** | Pointer to **interface{}** | A JSON value whose shape depends on the captured test subject and step type. | [optional]
**RecordedAt** | **time.Time** |  |

## Methods

### NewRunBatchItem

`func NewRunBatchItem(itemId string, subjectType SnapshotSubjectType, subjectId string, subjectKey string, subjectName string, sourceRunType SnapshotSourceRunType, sourceRunId string, status string, recordedAt time.Time, ) *RunBatchItem`

NewRunBatchItem instantiates a new RunBatchItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRunBatchItemWithDefaults

`func NewRunBatchItemWithDefaults() *RunBatchItem`

NewRunBatchItemWithDefaults instantiates a new RunBatchItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItemId

`func (o *RunBatchItem) GetItemId() string`

GetItemId returns the ItemId field if non-nil, zero value otherwise.

### GetItemIdOk

`func (o *RunBatchItem) GetItemIdOk() (*string, bool)`

GetItemIdOk returns a tuple with the ItemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemId

`func (o *RunBatchItem) SetItemId(v string)`

SetItemId sets ItemId field to given value.


### GetSubjectType

`func (o *RunBatchItem) GetSubjectType() SnapshotSubjectType`

GetSubjectType returns the SubjectType field if non-nil, zero value otherwise.

### GetSubjectTypeOk

`func (o *RunBatchItem) GetSubjectTypeOk() (*SnapshotSubjectType, bool)`

GetSubjectTypeOk returns a tuple with the SubjectType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubjectType

`func (o *RunBatchItem) SetSubjectType(v SnapshotSubjectType)`

SetSubjectType sets SubjectType field to given value.


### GetSubjectId

`func (o *RunBatchItem) GetSubjectId() string`

GetSubjectId returns the SubjectId field if non-nil, zero value otherwise.

### GetSubjectIdOk

`func (o *RunBatchItem) GetSubjectIdOk() (*string, bool)`

GetSubjectIdOk returns a tuple with the SubjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubjectId

`func (o *RunBatchItem) SetSubjectId(v string)`

SetSubjectId sets SubjectId field to given value.


### GetSubjectKey

`func (o *RunBatchItem) GetSubjectKey() string`

GetSubjectKey returns the SubjectKey field if non-nil, zero value otherwise.

### GetSubjectKeyOk

`func (o *RunBatchItem) GetSubjectKeyOk() (*string, bool)`

GetSubjectKeyOk returns a tuple with the SubjectKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubjectKey

`func (o *RunBatchItem) SetSubjectKey(v string)`

SetSubjectKey sets SubjectKey field to given value.


### GetSubjectName

`func (o *RunBatchItem) GetSubjectName() string`

GetSubjectName returns the SubjectName field if non-nil, zero value otherwise.

### GetSubjectNameOk

`func (o *RunBatchItem) GetSubjectNameOk() (*string, bool)`

GetSubjectNameOk returns a tuple with the SubjectName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubjectName

`func (o *RunBatchItem) SetSubjectName(v string)`

SetSubjectName sets SubjectName field to given value.


### GetSourceRunType

`func (o *RunBatchItem) GetSourceRunType() SnapshotSourceRunType`

GetSourceRunType returns the SourceRunType field if non-nil, zero value otherwise.

### GetSourceRunTypeOk

`func (o *RunBatchItem) GetSourceRunTypeOk() (*SnapshotSourceRunType, bool)`

GetSourceRunTypeOk returns a tuple with the SourceRunType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceRunType

`func (o *RunBatchItem) SetSourceRunType(v SnapshotSourceRunType)`

SetSourceRunType sets SourceRunType field to given value.


### GetSourceRunId

`func (o *RunBatchItem) GetSourceRunId() string`

GetSourceRunId returns the SourceRunId field if non-nil, zero value otherwise.

### GetSourceRunIdOk

`func (o *RunBatchItem) GetSourceRunIdOk() (*string, bool)`

GetSourceRunIdOk returns a tuple with the SourceRunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceRunId

`func (o *RunBatchItem) SetSourceRunId(v string)`

SetSourceRunId sets SourceRunId field to given value.


### GetStatus

`func (o *RunBatchItem) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *RunBatchItem) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *RunBatchItem) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetDefinitionHash

`func (o *RunBatchItem) GetDefinitionHash() string`

GetDefinitionHash returns the DefinitionHash field if non-nil, zero value otherwise.

### GetDefinitionHashOk

`func (o *RunBatchItem) GetDefinitionHashOk() (*string, bool)`

GetDefinitionHashOk returns a tuple with the DefinitionHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinitionHash

`func (o *RunBatchItem) SetDefinitionHash(v string)`

SetDefinitionHash sets DefinitionHash field to given value.

### HasDefinitionHash

`func (o *RunBatchItem) HasDefinitionHash() bool`

HasDefinitionHash returns a boolean if a field has been set.

### SetDefinitionHashNil

`func (o *RunBatchItem) SetDefinitionHashNil(b bool)`

 SetDefinitionHashNil sets the value for DefinitionHash to be an explicit nil

### UnsetDefinitionHash
`func (o *RunBatchItem) UnsetDefinitionHash()`

UnsetDefinitionHash ensures that no value is present for DefinitionHash, not even an explicit nil
### GetBehaviorHash

`func (o *RunBatchItem) GetBehaviorHash() string`

GetBehaviorHash returns the BehaviorHash field if non-nil, zero value otherwise.

### GetBehaviorHashOk

`func (o *RunBatchItem) GetBehaviorHashOk() (*string, bool)`

GetBehaviorHashOk returns a tuple with the BehaviorHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviorHash

`func (o *RunBatchItem) SetBehaviorHash(v string)`

SetBehaviorHash sets BehaviorHash field to given value.

### HasBehaviorHash

`func (o *RunBatchItem) HasBehaviorHash() bool`

HasBehaviorHash returns a boolean if a field has been set.

### SetBehaviorHashNil

`func (o *RunBatchItem) SetBehaviorHashNil(b bool)`

 SetBehaviorHashNil sets the value for BehaviorHash to be an explicit nil

### UnsetBehaviorHash
`func (o *RunBatchItem) UnsetBehaviorHash()`

UnsetBehaviorHash ensures that no value is present for BehaviorHash, not even an explicit nil
### GetDefinitionPayload

`func (o *RunBatchItem) GetDefinitionPayload() interface{}`

GetDefinitionPayload returns the DefinitionPayload field if non-nil, zero value otherwise.

### GetDefinitionPayloadOk

`func (o *RunBatchItem) GetDefinitionPayloadOk() (*interface{}, bool)`

GetDefinitionPayloadOk returns a tuple with the DefinitionPayload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinitionPayload

`func (o *RunBatchItem) SetDefinitionPayload(v interface{})`

SetDefinitionPayload sets DefinitionPayload field to given value.

### HasDefinitionPayload

`func (o *RunBatchItem) HasDefinitionPayload() bool`

HasDefinitionPayload returns a boolean if a field has been set.

### SetDefinitionPayloadNil

`func (o *RunBatchItem) SetDefinitionPayloadNil(b bool)`

 SetDefinitionPayloadNil sets the value for DefinitionPayload to be an explicit nil

### UnsetDefinitionPayload
`func (o *RunBatchItem) UnsetDefinitionPayload()`

UnsetDefinitionPayload ensures that no value is present for DefinitionPayload, not even an explicit nil
### GetBehaviorPayload

`func (o *RunBatchItem) GetBehaviorPayload() interface{}`

GetBehaviorPayload returns the BehaviorPayload field if non-nil, zero value otherwise.

### GetBehaviorPayloadOk

`func (o *RunBatchItem) GetBehaviorPayloadOk() (*interface{}, bool)`

GetBehaviorPayloadOk returns a tuple with the BehaviorPayload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviorPayload

`func (o *RunBatchItem) SetBehaviorPayload(v interface{})`

SetBehaviorPayload sets BehaviorPayload field to given value.

### HasBehaviorPayload

`func (o *RunBatchItem) HasBehaviorPayload() bool`

HasBehaviorPayload returns a boolean if a field has been set.

### SetBehaviorPayloadNil

`func (o *RunBatchItem) SetBehaviorPayloadNil(b bool)`

 SetBehaviorPayloadNil sets the value for BehaviorPayload to be an explicit nil

### UnsetBehaviorPayload
`func (o *RunBatchItem) UnsetBehaviorPayload()`

UnsetBehaviorPayload ensures that no value is present for BehaviorPayload, not even an explicit nil
### GetRecordedAt

`func (o *RunBatchItem) GetRecordedAt() time.Time`

GetRecordedAt returns the RecordedAt field if non-nil, zero value otherwise.

### GetRecordedAtOk

`func (o *RunBatchItem) GetRecordedAtOk() (*time.Time, bool)`

GetRecordedAtOk returns a tuple with the RecordedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecordedAt

`func (o *RunBatchItem) SetRecordedAt(v time.Time)`

SetRecordedAt sets RecordedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
