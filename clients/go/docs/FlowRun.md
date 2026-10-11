# FlowRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RunId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**FlowId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**FlowName** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**OverallTestFlowStatus** | **string** |  |
**Steps** | [**[]FlowRunStep**](FlowRunStep.md) |  |
**StartedAt** | **time.Time** |  |
**FinishedAt** | **time.Time** |  |

## Methods

### NewFlowRun

`func NewFlowRun(runId string, flowId string, flowName string, overallTestFlowStatus string, steps []FlowRunStep, startedAt time.Time, finishedAt time.Time, ) *FlowRun`

NewFlowRun instantiates a new FlowRun object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowRunWithDefaults

`func NewFlowRunWithDefaults() *FlowRun`

NewFlowRunWithDefaults instantiates a new FlowRun object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRunId

`func (o *FlowRun) GetRunId() string`

GetRunId returns the RunId field if non-nil, zero value otherwise.

### GetRunIdOk

`func (o *FlowRun) GetRunIdOk() (*string, bool)`

GetRunIdOk returns a tuple with the RunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRunId

`func (o *FlowRun) SetRunId(v string)`

SetRunId sets RunId field to given value.


### GetFlowId

`func (o *FlowRun) GetFlowId() string`

GetFlowId returns the FlowId field if non-nil, zero value otherwise.

### GetFlowIdOk

`func (o *FlowRun) GetFlowIdOk() (*string, bool)`

GetFlowIdOk returns a tuple with the FlowId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlowId

`func (o *FlowRun) SetFlowId(v string)`

SetFlowId sets FlowId field to given value.


### GetFlowName

`func (o *FlowRun) GetFlowName() string`

GetFlowName returns the FlowName field if non-nil, zero value otherwise.

### GetFlowNameOk

`func (o *FlowRun) GetFlowNameOk() (*string, bool)`

GetFlowNameOk returns a tuple with the FlowName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlowName

`func (o *FlowRun) SetFlowName(v string)`

SetFlowName sets FlowName field to given value.


### GetDescription

`func (o *FlowRun) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *FlowRun) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *FlowRun) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *FlowRun) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *FlowRun) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *FlowRun) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetOverallTestFlowStatus

`func (o *FlowRun) GetOverallTestFlowStatus() string`

GetOverallTestFlowStatus returns the OverallTestFlowStatus field if non-nil, zero value otherwise.

### GetOverallTestFlowStatusOk

`func (o *FlowRun) GetOverallTestFlowStatusOk() (*string, bool)`

GetOverallTestFlowStatusOk returns a tuple with the OverallTestFlowStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOverallTestFlowStatus

`func (o *FlowRun) SetOverallTestFlowStatus(v string)`

SetOverallTestFlowStatus sets OverallTestFlowStatus field to given value.


### GetSteps

`func (o *FlowRun) GetSteps() []FlowRunStep`

GetSteps returns the Steps field if non-nil, zero value otherwise.

### GetStepsOk

`func (o *FlowRun) GetStepsOk() (*[]FlowRunStep, bool)`

GetStepsOk returns a tuple with the Steps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteps

`func (o *FlowRun) SetSteps(v []FlowRunStep)`

SetSteps sets Steps field to given value.


### GetStartedAt

`func (o *FlowRun) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *FlowRun) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *FlowRun) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.


### GetFinishedAt

`func (o *FlowRun) GetFinishedAt() time.Time`

GetFinishedAt returns the FinishedAt field if non-nil, zero value otherwise.

### GetFinishedAtOk

`func (o *FlowRun) GetFinishedAtOk() (*time.Time, bool)`

GetFinishedAtOk returns a tuple with the FinishedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinishedAt

`func (o *FlowRun) SetFinishedAt(v time.Time)`

SetFinishedAt sets FinishedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
