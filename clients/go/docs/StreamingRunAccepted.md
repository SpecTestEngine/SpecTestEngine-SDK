# StreamingRunAccepted

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RunId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**State** | [**StreamingRunState**](StreamingRunState.md) |  |
**StatusUrl** | **string** |  |
**TranscriptUrl** | **string** |  |
**CancelUrl** | **string** |  |
**CreatedAt** | **time.Time** |  |

## Methods

### NewStreamingRunAccepted

`func NewStreamingRunAccepted(runId string, state StreamingRunState, statusUrl string, transcriptUrl string, cancelUrl string, createdAt time.Time, ) *StreamingRunAccepted`

NewStreamingRunAccepted instantiates a new StreamingRunAccepted object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStreamingRunAcceptedWithDefaults

`func NewStreamingRunAcceptedWithDefaults() *StreamingRunAccepted`

NewStreamingRunAcceptedWithDefaults instantiates a new StreamingRunAccepted object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRunId

`func (o *StreamingRunAccepted) GetRunId() string`

GetRunId returns the RunId field if non-nil, zero value otherwise.

### GetRunIdOk

`func (o *StreamingRunAccepted) GetRunIdOk() (*string, bool)`

GetRunIdOk returns a tuple with the RunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRunId

`func (o *StreamingRunAccepted) SetRunId(v string)`

SetRunId sets RunId field to given value.


### GetState

`func (o *StreamingRunAccepted) GetState() StreamingRunState`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *StreamingRunAccepted) GetStateOk() (*StreamingRunState, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *StreamingRunAccepted) SetState(v StreamingRunState)`

SetState sets State field to given value.


### GetStatusUrl

`func (o *StreamingRunAccepted) GetStatusUrl() string`

GetStatusUrl returns the StatusUrl field if non-nil, zero value otherwise.

### GetStatusUrlOk

`func (o *StreamingRunAccepted) GetStatusUrlOk() (*string, bool)`

GetStatusUrlOk returns a tuple with the StatusUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusUrl

`func (o *StreamingRunAccepted) SetStatusUrl(v string)`

SetStatusUrl sets StatusUrl field to given value.


### GetTranscriptUrl

`func (o *StreamingRunAccepted) GetTranscriptUrl() string`

GetTranscriptUrl returns the TranscriptUrl field if non-nil, zero value otherwise.

### GetTranscriptUrlOk

`func (o *StreamingRunAccepted) GetTranscriptUrlOk() (*string, bool)`

GetTranscriptUrlOk returns a tuple with the TranscriptUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTranscriptUrl

`func (o *StreamingRunAccepted) SetTranscriptUrl(v string)`

SetTranscriptUrl sets TranscriptUrl field to given value.


### GetCancelUrl

`func (o *StreamingRunAccepted) GetCancelUrl() string`

GetCancelUrl returns the CancelUrl field if non-nil, zero value otherwise.

### GetCancelUrlOk

`func (o *StreamingRunAccepted) GetCancelUrlOk() (*string, bool)`

GetCancelUrlOk returns a tuple with the CancelUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCancelUrl

`func (o *StreamingRunAccepted) SetCancelUrl(v string)`

SetCancelUrl sets CancelUrl field to given value.


### GetCreatedAt

`func (o *StreamingRunAccepted) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *StreamingRunAccepted) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *StreamingRunAccepted) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
