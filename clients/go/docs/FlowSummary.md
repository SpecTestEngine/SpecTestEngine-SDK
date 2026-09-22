# FlowSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FlowId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**Steps** | **[]map[string]interface{}** |  |
**CreatedAt** | **time.Time** |  |
**UpdatedAt** | **time.Time** |  |
**LastRunId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**PreviousRunId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**LastRunAt** | Pointer to **NullableTime** |  | [optional]
**LastRunStatus** | Pointer to **NullableString** |  | [optional]

## Methods

### NewFlowSummary

`func NewFlowSummary(flowId string, name string, steps []map[string]interface{}, createdAt time.Time, updatedAt time.Time, ) *FlowSummary`

NewFlowSummary instantiates a new FlowSummary object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowSummaryWithDefaults

`func NewFlowSummaryWithDefaults() *FlowSummary`

NewFlowSummaryWithDefaults instantiates a new FlowSummary object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFlowId

`func (o *FlowSummary) GetFlowId() string`

GetFlowId returns the FlowId field if non-nil, zero value otherwise.

### GetFlowIdOk

`func (o *FlowSummary) GetFlowIdOk() (*string, bool)`

GetFlowIdOk returns a tuple with the FlowId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlowId

`func (o *FlowSummary) SetFlowId(v string)`

SetFlowId sets FlowId field to given value.


### GetName

`func (o *FlowSummary) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *FlowSummary) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *FlowSummary) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *FlowSummary) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *FlowSummary) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *FlowSummary) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *FlowSummary) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *FlowSummary) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *FlowSummary) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetSteps

`func (o *FlowSummary) GetSteps() []map[string]interface{}`

GetSteps returns the Steps field if non-nil, zero value otherwise.

### GetStepsOk

`func (o *FlowSummary) GetStepsOk() (*[]map[string]interface{}, bool)`

GetStepsOk returns a tuple with the Steps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteps

`func (o *FlowSummary) SetSteps(v []map[string]interface{})`

SetSteps sets Steps field to given value.


### GetCreatedAt

`func (o *FlowSummary) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *FlowSummary) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *FlowSummary) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *FlowSummary) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *FlowSummary) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *FlowSummary) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetLastRunId

`func (o *FlowSummary) GetLastRunId() string`

GetLastRunId returns the LastRunId field if non-nil, zero value otherwise.

### GetLastRunIdOk

`func (o *FlowSummary) GetLastRunIdOk() (*string, bool)`

GetLastRunIdOk returns a tuple with the LastRunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRunId

`func (o *FlowSummary) SetLastRunId(v string)`

SetLastRunId sets LastRunId field to given value.

### HasLastRunId

`func (o *FlowSummary) HasLastRunId() bool`

HasLastRunId returns a boolean if a field has been set.

### SetLastRunIdNil

`func (o *FlowSummary) SetLastRunIdNil(b bool)`

 SetLastRunIdNil sets the value for LastRunId to be an explicit nil

### UnsetLastRunId
`func (o *FlowSummary) UnsetLastRunId()`

UnsetLastRunId ensures that no value is present for LastRunId, not even an explicit nil
### GetPreviousRunId

`func (o *FlowSummary) GetPreviousRunId() string`

GetPreviousRunId returns the PreviousRunId field if non-nil, zero value otherwise.

### GetPreviousRunIdOk

`func (o *FlowSummary) GetPreviousRunIdOk() (*string, bool)`

GetPreviousRunIdOk returns a tuple with the PreviousRunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPreviousRunId

`func (o *FlowSummary) SetPreviousRunId(v string)`

SetPreviousRunId sets PreviousRunId field to given value.

### HasPreviousRunId

`func (o *FlowSummary) HasPreviousRunId() bool`

HasPreviousRunId returns a boolean if a field has been set.

### SetPreviousRunIdNil

`func (o *FlowSummary) SetPreviousRunIdNil(b bool)`

 SetPreviousRunIdNil sets the value for PreviousRunId to be an explicit nil

### UnsetPreviousRunId
`func (o *FlowSummary) UnsetPreviousRunId()`

UnsetPreviousRunId ensures that no value is present for PreviousRunId, not even an explicit nil
### GetLastRunAt

`func (o *FlowSummary) GetLastRunAt() time.Time`

GetLastRunAt returns the LastRunAt field if non-nil, zero value otherwise.

### GetLastRunAtOk

`func (o *FlowSummary) GetLastRunAtOk() (*time.Time, bool)`

GetLastRunAtOk returns a tuple with the LastRunAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRunAt

`func (o *FlowSummary) SetLastRunAt(v time.Time)`

SetLastRunAt sets LastRunAt field to given value.

### HasLastRunAt

`func (o *FlowSummary) HasLastRunAt() bool`

HasLastRunAt returns a boolean if a field has been set.

### SetLastRunAtNil

`func (o *FlowSummary) SetLastRunAtNil(b bool)`

 SetLastRunAtNil sets the value for LastRunAt to be an explicit nil

### UnsetLastRunAt
`func (o *FlowSummary) UnsetLastRunAt()`

UnsetLastRunAt ensures that no value is present for LastRunAt, not even an explicit nil
### GetLastRunStatus

`func (o *FlowSummary) GetLastRunStatus() string`

GetLastRunStatus returns the LastRunStatus field if non-nil, zero value otherwise.

### GetLastRunStatusOk

`func (o *FlowSummary) GetLastRunStatusOk() (*string, bool)`

GetLastRunStatusOk returns a tuple with the LastRunStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRunStatus

`func (o *FlowSummary) SetLastRunStatus(v string)`

SetLastRunStatus sets LastRunStatus field to given value.

### HasLastRunStatus

`func (o *FlowSummary) HasLastRunStatus() bool`

HasLastRunStatus returns a boolean if a field has been set.

### SetLastRunStatusNil

`func (o *FlowSummary) SetLastRunStatusNil(b bool)`

 SetLastRunStatusNil sets the value for LastRunStatus to be an explicit nil

### UnsetLastRunStatus
`func (o *FlowSummary) UnsetLastRunStatus()`

UnsetLastRunStatus ensures that no value is present for LastRunStatus, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


