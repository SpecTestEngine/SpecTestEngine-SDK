# SentinelRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**ExecutionId** | **string** |  |
**Environment** | **string** | Environment captured when the run was queued. |
**CheckId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**CheckName** | **string** |  |
**CheckType** | **string** |  |
**DefinitionHash** | **string** |  |
**BehaviorHash** | Pointer to **NullableString** | Assertion-relevant behavior fingerprint of the completed run; null while unavailable. | [optional]
**Region** | **string** |  |
**TriggerType** | **string** |  |
**Status** | [**RunStatus**](RunStatus.md) |  |
**ErrorType** | Pointer to **NullableString** |  | [optional]
**FinalStatusCode** | Pointer to **NullableInt32** |  | [optional]
**LatencyMs** | Pointer to **NullableInt64** |  | [optional]
**ResponseSizeBytes** | Pointer to **NullableInt64** |  | [optional]
**ErrorMessage** | Pointer to **NullableString** |  | [optional]
**ResultLog** | Pointer to **NullableString** |  | [optional]
**QueuedAt** | **time.Time** |  |
**StartedAt** | Pointer to **NullableTime** |  | [optional]
**FinishedAt** | Pointer to **NullableTime** |  | [optional]
**Attempts** | Pointer to **[]map[string]interface{}** |  | [optional]
**Baseline** | Pointer to [**NullableSentinelRunBaseline**](SentinelRunBaseline.md) |  | [optional]

## Methods

### NewSentinelRun

`func NewSentinelRun(id string, executionId string, environment string, checkId string, checkName string, checkType string, definitionHash string, region string, triggerType string, status RunStatus, queuedAt time.Time, ) *SentinelRun`

NewSentinelRun instantiates a new SentinelRun object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSentinelRunWithDefaults

`func NewSentinelRunWithDefaults() *SentinelRun`

NewSentinelRunWithDefaults instantiates a new SentinelRun object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SentinelRun) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SentinelRun) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SentinelRun) SetId(v string)`

SetId sets Id field to given value.


### GetExecutionId

`func (o *SentinelRun) GetExecutionId() string`

GetExecutionId returns the ExecutionId field if non-nil, zero value otherwise.

### GetExecutionIdOk

`func (o *SentinelRun) GetExecutionIdOk() (*string, bool)`

GetExecutionIdOk returns a tuple with the ExecutionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExecutionId

`func (o *SentinelRun) SetExecutionId(v string)`

SetExecutionId sets ExecutionId field to given value.


### GetEnvironment

`func (o *SentinelRun) GetEnvironment() string`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *SentinelRun) GetEnvironmentOk() (*string, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *SentinelRun) SetEnvironment(v string)`

SetEnvironment sets Environment field to given value.


### GetCheckId

`func (o *SentinelRun) GetCheckId() string`

GetCheckId returns the CheckId field if non-nil, zero value otherwise.

### GetCheckIdOk

`func (o *SentinelRun) GetCheckIdOk() (*string, bool)`

GetCheckIdOk returns a tuple with the CheckId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckId

`func (o *SentinelRun) SetCheckId(v string)`

SetCheckId sets CheckId field to given value.


### GetCheckName

`func (o *SentinelRun) GetCheckName() string`

GetCheckName returns the CheckName field if non-nil, zero value otherwise.

### GetCheckNameOk

`func (o *SentinelRun) GetCheckNameOk() (*string, bool)`

GetCheckNameOk returns a tuple with the CheckName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckName

`func (o *SentinelRun) SetCheckName(v string)`

SetCheckName sets CheckName field to given value.


### GetCheckType

`func (o *SentinelRun) GetCheckType() string`

GetCheckType returns the CheckType field if non-nil, zero value otherwise.

### GetCheckTypeOk

`func (o *SentinelRun) GetCheckTypeOk() (*string, bool)`

GetCheckTypeOk returns a tuple with the CheckType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckType

`func (o *SentinelRun) SetCheckType(v string)`

SetCheckType sets CheckType field to given value.


### GetDefinitionHash

`func (o *SentinelRun) GetDefinitionHash() string`

GetDefinitionHash returns the DefinitionHash field if non-nil, zero value otherwise.

### GetDefinitionHashOk

`func (o *SentinelRun) GetDefinitionHashOk() (*string, bool)`

GetDefinitionHashOk returns a tuple with the DefinitionHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinitionHash

`func (o *SentinelRun) SetDefinitionHash(v string)`

SetDefinitionHash sets DefinitionHash field to given value.


### GetBehaviorHash

`func (o *SentinelRun) GetBehaviorHash() string`

GetBehaviorHash returns the BehaviorHash field if non-nil, zero value otherwise.

### GetBehaviorHashOk

`func (o *SentinelRun) GetBehaviorHashOk() (*string, bool)`

GetBehaviorHashOk returns a tuple with the BehaviorHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviorHash

`func (o *SentinelRun) SetBehaviorHash(v string)`

SetBehaviorHash sets BehaviorHash field to given value.

### HasBehaviorHash

`func (o *SentinelRun) HasBehaviorHash() bool`

HasBehaviorHash returns a boolean if a field has been set.

### SetBehaviorHashNil

`func (o *SentinelRun) SetBehaviorHashNil(b bool)`

 SetBehaviorHashNil sets the value for BehaviorHash to be an explicit nil

### UnsetBehaviorHash
`func (o *SentinelRun) UnsetBehaviorHash()`

UnsetBehaviorHash ensures that no value is present for BehaviorHash, not even an explicit nil
### GetRegion

`func (o *SentinelRun) GetRegion() string`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *SentinelRun) GetRegionOk() (*string, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *SentinelRun) SetRegion(v string)`

SetRegion sets Region field to given value.


### GetTriggerType

`func (o *SentinelRun) GetTriggerType() string`

GetTriggerType returns the TriggerType field if non-nil, zero value otherwise.

### GetTriggerTypeOk

`func (o *SentinelRun) GetTriggerTypeOk() (*string, bool)`

GetTriggerTypeOk returns a tuple with the TriggerType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTriggerType

`func (o *SentinelRun) SetTriggerType(v string)`

SetTriggerType sets TriggerType field to given value.


### GetStatus

`func (o *SentinelRun) GetStatus() RunStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SentinelRun) GetStatusOk() (*RunStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SentinelRun) SetStatus(v RunStatus)`

SetStatus sets Status field to given value.


### GetErrorType

`func (o *SentinelRun) GetErrorType() string`

GetErrorType returns the ErrorType field if non-nil, zero value otherwise.

### GetErrorTypeOk

`func (o *SentinelRun) GetErrorTypeOk() (*string, bool)`

GetErrorTypeOk returns a tuple with the ErrorType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorType

`func (o *SentinelRun) SetErrorType(v string)`

SetErrorType sets ErrorType field to given value.

### HasErrorType

`func (o *SentinelRun) HasErrorType() bool`

HasErrorType returns a boolean if a field has been set.

### SetErrorTypeNil

`func (o *SentinelRun) SetErrorTypeNil(b bool)`

 SetErrorTypeNil sets the value for ErrorType to be an explicit nil

### UnsetErrorType
`func (o *SentinelRun) UnsetErrorType()`

UnsetErrorType ensures that no value is present for ErrorType, not even an explicit nil
### GetFinalStatusCode

`func (o *SentinelRun) GetFinalStatusCode() int32`

GetFinalStatusCode returns the FinalStatusCode field if non-nil, zero value otherwise.

### GetFinalStatusCodeOk

`func (o *SentinelRun) GetFinalStatusCodeOk() (*int32, bool)`

GetFinalStatusCodeOk returns a tuple with the FinalStatusCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinalStatusCode

`func (o *SentinelRun) SetFinalStatusCode(v int32)`

SetFinalStatusCode sets FinalStatusCode field to given value.

### HasFinalStatusCode

`func (o *SentinelRun) HasFinalStatusCode() bool`

HasFinalStatusCode returns a boolean if a field has been set.

### SetFinalStatusCodeNil

`func (o *SentinelRun) SetFinalStatusCodeNil(b bool)`

 SetFinalStatusCodeNil sets the value for FinalStatusCode to be an explicit nil

### UnsetFinalStatusCode
`func (o *SentinelRun) UnsetFinalStatusCode()`

UnsetFinalStatusCode ensures that no value is present for FinalStatusCode, not even an explicit nil
### GetLatencyMs

`func (o *SentinelRun) GetLatencyMs() int64`

GetLatencyMs returns the LatencyMs field if non-nil, zero value otherwise.

### GetLatencyMsOk

`func (o *SentinelRun) GetLatencyMsOk() (*int64, bool)`

GetLatencyMsOk returns a tuple with the LatencyMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLatencyMs

`func (o *SentinelRun) SetLatencyMs(v int64)`

SetLatencyMs sets LatencyMs field to given value.

### HasLatencyMs

`func (o *SentinelRun) HasLatencyMs() bool`

HasLatencyMs returns a boolean if a field has been set.

### SetLatencyMsNil

`func (o *SentinelRun) SetLatencyMsNil(b bool)`

 SetLatencyMsNil sets the value for LatencyMs to be an explicit nil

### UnsetLatencyMs
`func (o *SentinelRun) UnsetLatencyMs()`

UnsetLatencyMs ensures that no value is present for LatencyMs, not even an explicit nil
### GetResponseSizeBytes

`func (o *SentinelRun) GetResponseSizeBytes() int64`

GetResponseSizeBytes returns the ResponseSizeBytes field if non-nil, zero value otherwise.

### GetResponseSizeBytesOk

`func (o *SentinelRun) GetResponseSizeBytesOk() (*int64, bool)`

GetResponseSizeBytesOk returns a tuple with the ResponseSizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseSizeBytes

`func (o *SentinelRun) SetResponseSizeBytes(v int64)`

SetResponseSizeBytes sets ResponseSizeBytes field to given value.

### HasResponseSizeBytes

`func (o *SentinelRun) HasResponseSizeBytes() bool`

HasResponseSizeBytes returns a boolean if a field has been set.

### SetResponseSizeBytesNil

`func (o *SentinelRun) SetResponseSizeBytesNil(b bool)`

 SetResponseSizeBytesNil sets the value for ResponseSizeBytes to be an explicit nil

### UnsetResponseSizeBytes
`func (o *SentinelRun) UnsetResponseSizeBytes()`

UnsetResponseSizeBytes ensures that no value is present for ResponseSizeBytes, not even an explicit nil
### GetErrorMessage

`func (o *SentinelRun) GetErrorMessage() string`

GetErrorMessage returns the ErrorMessage field if non-nil, zero value otherwise.

### GetErrorMessageOk

`func (o *SentinelRun) GetErrorMessageOk() (*string, bool)`

GetErrorMessageOk returns a tuple with the ErrorMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorMessage

`func (o *SentinelRun) SetErrorMessage(v string)`

SetErrorMessage sets ErrorMessage field to given value.

### HasErrorMessage

`func (o *SentinelRun) HasErrorMessage() bool`

HasErrorMessage returns a boolean if a field has been set.

### SetErrorMessageNil

`func (o *SentinelRun) SetErrorMessageNil(b bool)`

 SetErrorMessageNil sets the value for ErrorMessage to be an explicit nil

### UnsetErrorMessage
`func (o *SentinelRun) UnsetErrorMessage()`

UnsetErrorMessage ensures that no value is present for ErrorMessage, not even an explicit nil
### GetResultLog

`func (o *SentinelRun) GetResultLog() string`

GetResultLog returns the ResultLog field if non-nil, zero value otherwise.

### GetResultLogOk

`func (o *SentinelRun) GetResultLogOk() (*string, bool)`

GetResultLogOk returns a tuple with the ResultLog field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResultLog

`func (o *SentinelRun) SetResultLog(v string)`

SetResultLog sets ResultLog field to given value.

### HasResultLog

`func (o *SentinelRun) HasResultLog() bool`

HasResultLog returns a boolean if a field has been set.

### SetResultLogNil

`func (o *SentinelRun) SetResultLogNil(b bool)`

 SetResultLogNil sets the value for ResultLog to be an explicit nil

### UnsetResultLog
`func (o *SentinelRun) UnsetResultLog()`

UnsetResultLog ensures that no value is present for ResultLog, not even an explicit nil
### GetQueuedAt

`func (o *SentinelRun) GetQueuedAt() time.Time`

GetQueuedAt returns the QueuedAt field if non-nil, zero value otherwise.

### GetQueuedAtOk

`func (o *SentinelRun) GetQueuedAtOk() (*time.Time, bool)`

GetQueuedAtOk returns a tuple with the QueuedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueuedAt

`func (o *SentinelRun) SetQueuedAt(v time.Time)`

SetQueuedAt sets QueuedAt field to given value.


### GetStartedAt

`func (o *SentinelRun) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *SentinelRun) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *SentinelRun) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.

### HasStartedAt

`func (o *SentinelRun) HasStartedAt() bool`

HasStartedAt returns a boolean if a field has been set.

### SetStartedAtNil

`func (o *SentinelRun) SetStartedAtNil(b bool)`

 SetStartedAtNil sets the value for StartedAt to be an explicit nil

### UnsetStartedAt
`func (o *SentinelRun) UnsetStartedAt()`

UnsetStartedAt ensures that no value is present for StartedAt, not even an explicit nil
### GetFinishedAt

`func (o *SentinelRun) GetFinishedAt() time.Time`

GetFinishedAt returns the FinishedAt field if non-nil, zero value otherwise.

### GetFinishedAtOk

`func (o *SentinelRun) GetFinishedAtOk() (*time.Time, bool)`

GetFinishedAtOk returns a tuple with the FinishedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinishedAt

`func (o *SentinelRun) SetFinishedAt(v time.Time)`

SetFinishedAt sets FinishedAt field to given value.

### HasFinishedAt

`func (o *SentinelRun) HasFinishedAt() bool`

HasFinishedAt returns a boolean if a field has been set.

### SetFinishedAtNil

`func (o *SentinelRun) SetFinishedAtNil(b bool)`

 SetFinishedAtNil sets the value for FinishedAt to be an explicit nil

### UnsetFinishedAt
`func (o *SentinelRun) UnsetFinishedAt()`

UnsetFinishedAt ensures that no value is present for FinishedAt, not even an explicit nil
### GetAttempts

`func (o *SentinelRun) GetAttempts() []map[string]interface{}`

GetAttempts returns the Attempts field if non-nil, zero value otherwise.

### GetAttemptsOk

`func (o *SentinelRun) GetAttemptsOk() (*[]map[string]interface{}, bool)`

GetAttemptsOk returns a tuple with the Attempts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttempts

`func (o *SentinelRun) SetAttempts(v []map[string]interface{})`

SetAttempts sets Attempts field to given value.

### HasAttempts

`func (o *SentinelRun) HasAttempts() bool`

HasAttempts returns a boolean if a field has been set.

### GetBaseline

`func (o *SentinelRun) GetBaseline() SentinelRunBaseline`

GetBaseline returns the Baseline field if non-nil, zero value otherwise.

### GetBaselineOk

`func (o *SentinelRun) GetBaselineOk() (*SentinelRunBaseline, bool)`

GetBaselineOk returns a tuple with the Baseline field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseline

`func (o *SentinelRun) SetBaseline(v SentinelRunBaseline)`

SetBaseline sets Baseline field to given value.

### HasBaseline

`func (o *SentinelRun) HasBaseline() bool`

HasBaseline returns a boolean if a field has been set.

### SetBaselineNil

`func (o *SentinelRun) SetBaselineNil(b bool)`

 SetBaselineNil sets the value for Baseline to be an explicit nil

### UnsetBaseline
`func (o *SentinelRun) UnsetBaseline()`

UnsetBaseline ensures that no value is present for Baseline, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
