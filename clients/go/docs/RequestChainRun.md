# RequestChainRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WorkspaceId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**RequestNodeId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**FlowName** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**OverallTestFlowStatus** | **string** |  |
**Steps** | **[]map[string]interface{}** |  |
**Context** | **map[string]interface{}** | Values explicitly captured during this run. Workflow/global input values and secret sources are not echoed here. |
**StartedAt** | **time.Time** |  |
**FinishedAt** | **time.Time** |  |

## Methods

### NewRequestChainRun

`func NewRequestChainRun(workspaceId string, requestNodeId string, flowName string, overallTestFlowStatus string, steps []map[string]interface{}, context map[string]interface{}, startedAt time.Time, finishedAt time.Time, ) *RequestChainRun`

NewRequestChainRun instantiates a new RequestChainRun object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRequestChainRunWithDefaults

`func NewRequestChainRunWithDefaults() *RequestChainRun`

NewRequestChainRunWithDefaults instantiates a new RequestChainRun object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWorkspaceId

`func (o *RequestChainRun) GetWorkspaceId() string`

GetWorkspaceId returns the WorkspaceId field if non-nil, zero value otherwise.

### GetWorkspaceIdOk

`func (o *RequestChainRun) GetWorkspaceIdOk() (*string, bool)`

GetWorkspaceIdOk returns a tuple with the WorkspaceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWorkspaceId

`func (o *RequestChainRun) SetWorkspaceId(v string)`

SetWorkspaceId sets WorkspaceId field to given value.


### GetRequestNodeId

`func (o *RequestChainRun) GetRequestNodeId() string`

GetRequestNodeId returns the RequestNodeId field if non-nil, zero value otherwise.

### GetRequestNodeIdOk

`func (o *RequestChainRun) GetRequestNodeIdOk() (*string, bool)`

GetRequestNodeIdOk returns a tuple with the RequestNodeId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestNodeId

`func (o *RequestChainRun) SetRequestNodeId(v string)`

SetRequestNodeId sets RequestNodeId field to given value.


### GetFlowName

`func (o *RequestChainRun) GetFlowName() string`

GetFlowName returns the FlowName field if non-nil, zero value otherwise.

### GetFlowNameOk

`func (o *RequestChainRun) GetFlowNameOk() (*string, bool)`

GetFlowNameOk returns a tuple with the FlowName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlowName

`func (o *RequestChainRun) SetFlowName(v string)`

SetFlowName sets FlowName field to given value.


### GetDescription

`func (o *RequestChainRun) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *RequestChainRun) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *RequestChainRun) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *RequestChainRun) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *RequestChainRun) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *RequestChainRun) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetOverallTestFlowStatus

`func (o *RequestChainRun) GetOverallTestFlowStatus() string`

GetOverallTestFlowStatus returns the OverallTestFlowStatus field if non-nil, zero value otherwise.

### GetOverallTestFlowStatusOk

`func (o *RequestChainRun) GetOverallTestFlowStatusOk() (*string, bool)`

GetOverallTestFlowStatusOk returns a tuple with the OverallTestFlowStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOverallTestFlowStatus

`func (o *RequestChainRun) SetOverallTestFlowStatus(v string)`

SetOverallTestFlowStatus sets OverallTestFlowStatus field to given value.


### GetSteps

`func (o *RequestChainRun) GetSteps() []map[string]interface{}`

GetSteps returns the Steps field if non-nil, zero value otherwise.

### GetStepsOk

`func (o *RequestChainRun) GetStepsOk() (*[]map[string]interface{}, bool)`

GetStepsOk returns a tuple with the Steps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteps

`func (o *RequestChainRun) SetSteps(v []map[string]interface{})`

SetSteps sets Steps field to given value.


### GetContext

`func (o *RequestChainRun) GetContext() map[string]interface{}`

GetContext returns the Context field if non-nil, zero value otherwise.

### GetContextOk

`func (o *RequestChainRun) GetContextOk() (*map[string]interface{}, bool)`

GetContextOk returns a tuple with the Context field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContext

`func (o *RequestChainRun) SetContext(v map[string]interface{})`

SetContext sets Context field to given value.


### GetStartedAt

`func (o *RequestChainRun) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *RequestChainRun) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *RequestChainRun) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.


### GetFinishedAt

`func (o *RequestChainRun) GetFinishedAt() time.Time`

GetFinishedAt returns the FinishedAt field if non-nil, zero value otherwise.

### GetFinishedAtOk

`func (o *RequestChainRun) GetFinishedAtOk() (*time.Time, bool)`

GetFinishedAtOk returns a tuple with the FinishedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinishedAt

`func (o *RequestChainRun) SetFinishedAt(v time.Time)`

SetFinishedAt sets FinishedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
