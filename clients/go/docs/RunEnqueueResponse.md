# RunEnqueueResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RunId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**ExecutionId** | **string** |  |
**Queued** | **bool** |  |
**Message** | **string** |  |

## Methods

### NewRunEnqueueResponse

`func NewRunEnqueueResponse(runId string, executionId string, queued bool, message string, ) *RunEnqueueResponse`

NewRunEnqueueResponse instantiates a new RunEnqueueResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRunEnqueueResponseWithDefaults

`func NewRunEnqueueResponseWithDefaults() *RunEnqueueResponse`

NewRunEnqueueResponseWithDefaults instantiates a new RunEnqueueResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRunId

`func (o *RunEnqueueResponse) GetRunId() string`

GetRunId returns the RunId field if non-nil, zero value otherwise.

### GetRunIdOk

`func (o *RunEnqueueResponse) GetRunIdOk() (*string, bool)`

GetRunIdOk returns a tuple with the RunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRunId

`func (o *RunEnqueueResponse) SetRunId(v string)`

SetRunId sets RunId field to given value.


### GetExecutionId

`func (o *RunEnqueueResponse) GetExecutionId() string`

GetExecutionId returns the ExecutionId field if non-nil, zero value otherwise.

### GetExecutionIdOk

`func (o *RunEnqueueResponse) GetExecutionIdOk() (*string, bool)`

GetExecutionIdOk returns a tuple with the ExecutionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExecutionId

`func (o *RunEnqueueResponse) SetExecutionId(v string)`

SetExecutionId sets ExecutionId field to given value.


### GetQueued

`func (o *RunEnqueueResponse) GetQueued() bool`

GetQueued returns the Queued field if non-nil, zero value otherwise.

### GetQueuedOk

`func (o *RunEnqueueResponse) GetQueuedOk() (*bool, bool)`

GetQueuedOk returns a tuple with the Queued field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueued

`func (o *RunEnqueueResponse) SetQueued(v bool)`

SetQueued sets Queued field to given value.


### GetMessage

`func (o *RunEnqueueResponse) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *RunEnqueueResponse) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *RunEnqueueResponse) SetMessage(v string)`

SetMessage sets Message field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


