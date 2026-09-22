# SnapshotItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SnapshotFlowId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SourceBatchItemId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
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
**CreatedAt** | **time.Time** |  |

## Methods

### NewSnapshotItem

`func NewSnapshotItem(snapshotFlowId string, sourceBatchItemId string, subjectType SnapshotSubjectType, subjectId string, subjectKey string, subjectName string, sourceRunType SnapshotSourceRunType, sourceRunId string, status string, createdAt time.Time, ) *SnapshotItem`

NewSnapshotItem instantiates a new SnapshotItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSnapshotItemWithDefaults

`func NewSnapshotItemWithDefaults() *SnapshotItem`

NewSnapshotItemWithDefaults instantiates a new SnapshotItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSnapshotFlowId

`func (o *SnapshotItem) GetSnapshotFlowId() string`

GetSnapshotFlowId returns the SnapshotFlowId field if non-nil, zero value otherwise.

### GetSnapshotFlowIdOk

`func (o *SnapshotItem) GetSnapshotFlowIdOk() (*string, bool)`

GetSnapshotFlowIdOk returns a tuple with the SnapshotFlowId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSnapshotFlowId

`func (o *SnapshotItem) SetSnapshotFlowId(v string)`

SetSnapshotFlowId sets SnapshotFlowId field to given value.


### GetSourceBatchItemId

`func (o *SnapshotItem) GetSourceBatchItemId() string`

GetSourceBatchItemId returns the SourceBatchItemId field if non-nil, zero value otherwise.

### GetSourceBatchItemIdOk

`func (o *SnapshotItem) GetSourceBatchItemIdOk() (*string, bool)`

GetSourceBatchItemIdOk returns a tuple with the SourceBatchItemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceBatchItemId

`func (o *SnapshotItem) SetSourceBatchItemId(v string)`

SetSourceBatchItemId sets SourceBatchItemId field to given value.


### GetSubjectType

`func (o *SnapshotItem) GetSubjectType() SnapshotSubjectType`

GetSubjectType returns the SubjectType field if non-nil, zero value otherwise.

### GetSubjectTypeOk

`func (o *SnapshotItem) GetSubjectTypeOk() (*SnapshotSubjectType, bool)`

GetSubjectTypeOk returns a tuple with the SubjectType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubjectType

`func (o *SnapshotItem) SetSubjectType(v SnapshotSubjectType)`

SetSubjectType sets SubjectType field to given value.


### GetSubjectId

`func (o *SnapshotItem) GetSubjectId() string`

GetSubjectId returns the SubjectId field if non-nil, zero value otherwise.

### GetSubjectIdOk

`func (o *SnapshotItem) GetSubjectIdOk() (*string, bool)`

GetSubjectIdOk returns a tuple with the SubjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubjectId

`func (o *SnapshotItem) SetSubjectId(v string)`

SetSubjectId sets SubjectId field to given value.


### GetSubjectKey

`func (o *SnapshotItem) GetSubjectKey() string`

GetSubjectKey returns the SubjectKey field if non-nil, zero value otherwise.

### GetSubjectKeyOk

`func (o *SnapshotItem) GetSubjectKeyOk() (*string, bool)`

GetSubjectKeyOk returns a tuple with the SubjectKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubjectKey

`func (o *SnapshotItem) SetSubjectKey(v string)`

SetSubjectKey sets SubjectKey field to given value.


### GetSubjectName

`func (o *SnapshotItem) GetSubjectName() string`

GetSubjectName returns the SubjectName field if non-nil, zero value otherwise.

### GetSubjectNameOk

`func (o *SnapshotItem) GetSubjectNameOk() (*string, bool)`

GetSubjectNameOk returns a tuple with the SubjectName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubjectName

`func (o *SnapshotItem) SetSubjectName(v string)`

SetSubjectName sets SubjectName field to given value.


### GetSourceRunType

`func (o *SnapshotItem) GetSourceRunType() SnapshotSourceRunType`

GetSourceRunType returns the SourceRunType field if non-nil, zero value otherwise.

### GetSourceRunTypeOk

`func (o *SnapshotItem) GetSourceRunTypeOk() (*SnapshotSourceRunType, bool)`

GetSourceRunTypeOk returns a tuple with the SourceRunType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceRunType

`func (o *SnapshotItem) SetSourceRunType(v SnapshotSourceRunType)`

SetSourceRunType sets SourceRunType field to given value.


### GetSourceRunId

`func (o *SnapshotItem) GetSourceRunId() string`

GetSourceRunId returns the SourceRunId field if non-nil, zero value otherwise.

### GetSourceRunIdOk

`func (o *SnapshotItem) GetSourceRunIdOk() (*string, bool)`

GetSourceRunIdOk returns a tuple with the SourceRunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceRunId

`func (o *SnapshotItem) SetSourceRunId(v string)`

SetSourceRunId sets SourceRunId field to given value.


### GetStatus

`func (o *SnapshotItem) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SnapshotItem) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SnapshotItem) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetDefinitionHash

`func (o *SnapshotItem) GetDefinitionHash() string`

GetDefinitionHash returns the DefinitionHash field if non-nil, zero value otherwise.

### GetDefinitionHashOk

`func (o *SnapshotItem) GetDefinitionHashOk() (*string, bool)`

GetDefinitionHashOk returns a tuple with the DefinitionHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinitionHash

`func (o *SnapshotItem) SetDefinitionHash(v string)`

SetDefinitionHash sets DefinitionHash field to given value.

### HasDefinitionHash

`func (o *SnapshotItem) HasDefinitionHash() bool`

HasDefinitionHash returns a boolean if a field has been set.

### SetDefinitionHashNil

`func (o *SnapshotItem) SetDefinitionHashNil(b bool)`

 SetDefinitionHashNil sets the value for DefinitionHash to be an explicit nil

### UnsetDefinitionHash
`func (o *SnapshotItem) UnsetDefinitionHash()`

UnsetDefinitionHash ensures that no value is present for DefinitionHash, not even an explicit nil
### GetBehaviorHash

`func (o *SnapshotItem) GetBehaviorHash() string`

GetBehaviorHash returns the BehaviorHash field if non-nil, zero value otherwise.

### GetBehaviorHashOk

`func (o *SnapshotItem) GetBehaviorHashOk() (*string, bool)`

GetBehaviorHashOk returns a tuple with the BehaviorHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviorHash

`func (o *SnapshotItem) SetBehaviorHash(v string)`

SetBehaviorHash sets BehaviorHash field to given value.

### HasBehaviorHash

`func (o *SnapshotItem) HasBehaviorHash() bool`

HasBehaviorHash returns a boolean if a field has been set.

### SetBehaviorHashNil

`func (o *SnapshotItem) SetBehaviorHashNil(b bool)`

 SetBehaviorHashNil sets the value for BehaviorHash to be an explicit nil

### UnsetBehaviorHash
`func (o *SnapshotItem) UnsetBehaviorHash()`

UnsetBehaviorHash ensures that no value is present for BehaviorHash, not even an explicit nil
### GetDefinitionPayload

`func (o *SnapshotItem) GetDefinitionPayload() interface{}`

GetDefinitionPayload returns the DefinitionPayload field if non-nil, zero value otherwise.

### GetDefinitionPayloadOk

`func (o *SnapshotItem) GetDefinitionPayloadOk() (*interface{}, bool)`

GetDefinitionPayloadOk returns a tuple with the DefinitionPayload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinitionPayload

`func (o *SnapshotItem) SetDefinitionPayload(v interface{})`

SetDefinitionPayload sets DefinitionPayload field to given value.

### HasDefinitionPayload

`func (o *SnapshotItem) HasDefinitionPayload() bool`

HasDefinitionPayload returns a boolean if a field has been set.

### SetDefinitionPayloadNil

`func (o *SnapshotItem) SetDefinitionPayloadNil(b bool)`

 SetDefinitionPayloadNil sets the value for DefinitionPayload to be an explicit nil

### UnsetDefinitionPayload
`func (o *SnapshotItem) UnsetDefinitionPayload()`

UnsetDefinitionPayload ensures that no value is present for DefinitionPayload, not even an explicit nil
### GetBehaviorPayload

`func (o *SnapshotItem) GetBehaviorPayload() interface{}`

GetBehaviorPayload returns the BehaviorPayload field if non-nil, zero value otherwise.

### GetBehaviorPayloadOk

`func (o *SnapshotItem) GetBehaviorPayloadOk() (*interface{}, bool)`

GetBehaviorPayloadOk returns a tuple with the BehaviorPayload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviorPayload

`func (o *SnapshotItem) SetBehaviorPayload(v interface{})`

SetBehaviorPayload sets BehaviorPayload field to given value.

### HasBehaviorPayload

`func (o *SnapshotItem) HasBehaviorPayload() bool`

HasBehaviorPayload returns a boolean if a field has been set.

### SetBehaviorPayloadNil

`func (o *SnapshotItem) SetBehaviorPayloadNil(b bool)`

 SetBehaviorPayloadNil sets the value for BehaviorPayload to be an explicit nil

### UnsetBehaviorPayload
`func (o *SnapshotItem) UnsetBehaviorPayload()`

UnsetBehaviorPayload ensures that no value is present for BehaviorPayload, not even an explicit nil
### GetCreatedAt

`func (o *SnapshotItem) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SnapshotItem) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SnapshotItem) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


