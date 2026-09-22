# FlowRunSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RunId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**FlowId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**FlowName** | **string** |  |
**OverallTestFlowStatus** | **string** |  |
**StartedAt** | **time.Time** |  |
**FinishedAt** | **time.Time** |  |

## Methods

### NewFlowRunSummary

`func NewFlowRunSummary(runId string, flowId string, flowName string, overallTestFlowStatus string, startedAt time.Time, finishedAt time.Time, ) *FlowRunSummary`

NewFlowRunSummary instantiates a new FlowRunSummary object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowRunSummaryWithDefaults

`func NewFlowRunSummaryWithDefaults() *FlowRunSummary`

NewFlowRunSummaryWithDefaults instantiates a new FlowRunSummary object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRunId

`func (o *FlowRunSummary) GetRunId() string`

GetRunId returns the RunId field if non-nil, zero value otherwise.

### GetRunIdOk

`func (o *FlowRunSummary) GetRunIdOk() (*string, bool)`

GetRunIdOk returns a tuple with the RunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRunId

`func (o *FlowRunSummary) SetRunId(v string)`

SetRunId sets RunId field to given value.


### GetFlowId

`func (o *FlowRunSummary) GetFlowId() string`

GetFlowId returns the FlowId field if non-nil, zero value otherwise.

### GetFlowIdOk

`func (o *FlowRunSummary) GetFlowIdOk() (*string, bool)`

GetFlowIdOk returns a tuple with the FlowId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlowId

`func (o *FlowRunSummary) SetFlowId(v string)`

SetFlowId sets FlowId field to given value.


### GetFlowName

`func (o *FlowRunSummary) GetFlowName() string`

GetFlowName returns the FlowName field if non-nil, zero value otherwise.

### GetFlowNameOk

`func (o *FlowRunSummary) GetFlowNameOk() (*string, bool)`

GetFlowNameOk returns a tuple with the FlowName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlowName

`func (o *FlowRunSummary) SetFlowName(v string)`

SetFlowName sets FlowName field to given value.


### GetOverallTestFlowStatus

`func (o *FlowRunSummary) GetOverallTestFlowStatus() string`

GetOverallTestFlowStatus returns the OverallTestFlowStatus field if non-nil, zero value otherwise.

### GetOverallTestFlowStatusOk

`func (o *FlowRunSummary) GetOverallTestFlowStatusOk() (*string, bool)`

GetOverallTestFlowStatusOk returns a tuple with the OverallTestFlowStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOverallTestFlowStatus

`func (o *FlowRunSummary) SetOverallTestFlowStatus(v string)`

SetOverallTestFlowStatus sets OverallTestFlowStatus field to given value.


### GetStartedAt

`func (o *FlowRunSummary) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *FlowRunSummary) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *FlowRunSummary) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.


### GetFinishedAt

`func (o *FlowRunSummary) GetFinishedAt() time.Time`

GetFinishedAt returns the FinishedAt field if non-nil, zero value otherwise.

### GetFinishedAtOk

`func (o *FlowRunSummary) GetFinishedAtOk() (*time.Time, bool)`

GetFinishedAtOk returns a tuple with the FinishedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinishedAt

`func (o *FlowRunSummary) SetFinishedAt(v time.Time)`

SetFinishedAt sets FinishedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


