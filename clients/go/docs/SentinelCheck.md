# SentinelCheck

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**SourceName** | Pointer to **NullableString** |  | [optional]
**Environment** | **string** | Immutable environment scope for the check and its runs. |
**Type** | **string** |  |
**SpecType** | Pointer to [**NullableSpecType**](SpecType.md) | Required when type is SPEC and prohibited when type is FLOW or URL. | [optional]
**Format** | [**ContentFormat**](ContentFormat.md) |  | [default to CONTENTFORMAT_JSON]
**Definition** | **string** |  |
**Active** | Pointer to **bool** |  | [optional] [default to true]
**TimeoutMs** | Pointer to **int64** |  | [optional] [default to 10000]
**FailureStrategy** | Pointer to **string** |  | [optional] [default to "FAIL_FAST"]
**MaxRetries** | Pointer to **int32** |  | [optional] [default to 3]
**RetryDelayMinMs** | Pointer to **int64** |  | [optional] [default to 5000]
**RetryDelayMaxMs** | Pointer to **int64** |  | [optional] [default to 10000]
**CircuitBreakerFailureThreshold** | Pointer to **int32** |  | [optional] [default to 5]
**CooldownMs** | Pointer to **int64** |  | [optional] [default to 300000]
**Id** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**DefinitionHash** | **string** |  |
**ConsecutiveFailures** | **int32** |  |
**PausedUntil** | Pointer to **NullableTime** |  | [optional]
**LastRunAt** | Pointer to **NullableTime** |  | [optional]
**LastRunStatus** | Pointer to [**NullableRunStatus**](RunStatus.md) |  | [optional]
**CreatedAt** | **time.Time** |  |
**UpdatedAt** | **time.Time** |  |

## Methods

### NewSentinelCheck

`func NewSentinelCheck(name string, environment string, type_ string, format ContentFormat, definition string, id string, definitionHash string, consecutiveFailures int32, createdAt time.Time, updatedAt time.Time, ) *SentinelCheck`

NewSentinelCheck instantiates a new SentinelCheck object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSentinelCheckWithDefaults

`func NewSentinelCheckWithDefaults() *SentinelCheck`

NewSentinelCheckWithDefaults instantiates a new SentinelCheck object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *SentinelCheck) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SentinelCheck) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SentinelCheck) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *SentinelCheck) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *SentinelCheck) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *SentinelCheck) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *SentinelCheck) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *SentinelCheck) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *SentinelCheck) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetSourceName

`func (o *SentinelCheck) GetSourceName() string`

GetSourceName returns the SourceName field if non-nil, zero value otherwise.

### GetSourceNameOk

`func (o *SentinelCheck) GetSourceNameOk() (*string, bool)`

GetSourceNameOk returns a tuple with the SourceName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceName

`func (o *SentinelCheck) SetSourceName(v string)`

SetSourceName sets SourceName field to given value.

### HasSourceName

`func (o *SentinelCheck) HasSourceName() bool`

HasSourceName returns a boolean if a field has been set.

### SetSourceNameNil

`func (o *SentinelCheck) SetSourceNameNil(b bool)`

 SetSourceNameNil sets the value for SourceName to be an explicit nil

### UnsetSourceName
`func (o *SentinelCheck) UnsetSourceName()`

UnsetSourceName ensures that no value is present for SourceName, not even an explicit nil
### GetEnvironment

`func (o *SentinelCheck) GetEnvironment() string`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *SentinelCheck) GetEnvironmentOk() (*string, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *SentinelCheck) SetEnvironment(v string)`

SetEnvironment sets Environment field to given value.


### GetType

`func (o *SentinelCheck) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *SentinelCheck) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *SentinelCheck) SetType(v string)`

SetType sets Type field to given value.


### GetSpecType

`func (o *SentinelCheck) GetSpecType() SpecType`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *SentinelCheck) GetSpecTypeOk() (*SpecType, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *SentinelCheck) SetSpecType(v SpecType)`

SetSpecType sets SpecType field to given value.

### HasSpecType

`func (o *SentinelCheck) HasSpecType() bool`

HasSpecType returns a boolean if a field has been set.

### SetSpecTypeNil

`func (o *SentinelCheck) SetSpecTypeNil(b bool)`

 SetSpecTypeNil sets the value for SpecType to be an explicit nil

### UnsetSpecType
`func (o *SentinelCheck) UnsetSpecType()`

UnsetSpecType ensures that no value is present for SpecType, not even an explicit nil
### GetFormat

`func (o *SentinelCheck) GetFormat() ContentFormat`

GetFormat returns the Format field if non-nil, zero value otherwise.

### GetFormatOk

`func (o *SentinelCheck) GetFormatOk() (*ContentFormat, bool)`

GetFormatOk returns a tuple with the Format field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFormat

`func (o *SentinelCheck) SetFormat(v ContentFormat)`

SetFormat sets Format field to given value.


### GetDefinition

`func (o *SentinelCheck) GetDefinition() string`

GetDefinition returns the Definition field if non-nil, zero value otherwise.

### GetDefinitionOk

`func (o *SentinelCheck) GetDefinitionOk() (*string, bool)`

GetDefinitionOk returns a tuple with the Definition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinition

`func (o *SentinelCheck) SetDefinition(v string)`

SetDefinition sets Definition field to given value.


### GetActive

`func (o *SentinelCheck) GetActive() bool`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *SentinelCheck) GetActiveOk() (*bool, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *SentinelCheck) SetActive(v bool)`

SetActive sets Active field to given value.

### HasActive

`func (o *SentinelCheck) HasActive() bool`

HasActive returns a boolean if a field has been set.

### GetTimeoutMs

`func (o *SentinelCheck) GetTimeoutMs() int64`

GetTimeoutMs returns the TimeoutMs field if non-nil, zero value otherwise.

### GetTimeoutMsOk

`func (o *SentinelCheck) GetTimeoutMsOk() (*int64, bool)`

GetTimeoutMsOk returns a tuple with the TimeoutMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimeoutMs

`func (o *SentinelCheck) SetTimeoutMs(v int64)`

SetTimeoutMs sets TimeoutMs field to given value.

### HasTimeoutMs

`func (o *SentinelCheck) HasTimeoutMs() bool`

HasTimeoutMs returns a boolean if a field has been set.

### GetFailureStrategy

`func (o *SentinelCheck) GetFailureStrategy() string`

GetFailureStrategy returns the FailureStrategy field if non-nil, zero value otherwise.

### GetFailureStrategyOk

`func (o *SentinelCheck) GetFailureStrategyOk() (*string, bool)`

GetFailureStrategyOk returns a tuple with the FailureStrategy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFailureStrategy

`func (o *SentinelCheck) SetFailureStrategy(v string)`

SetFailureStrategy sets FailureStrategy field to given value.

### HasFailureStrategy

`func (o *SentinelCheck) HasFailureStrategy() bool`

HasFailureStrategy returns a boolean if a field has been set.

### GetMaxRetries

`func (o *SentinelCheck) GetMaxRetries() int32`

GetMaxRetries returns the MaxRetries field if non-nil, zero value otherwise.

### GetMaxRetriesOk

`func (o *SentinelCheck) GetMaxRetriesOk() (*int32, bool)`

GetMaxRetriesOk returns a tuple with the MaxRetries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxRetries

`func (o *SentinelCheck) SetMaxRetries(v int32)`

SetMaxRetries sets MaxRetries field to given value.

### HasMaxRetries

`func (o *SentinelCheck) HasMaxRetries() bool`

HasMaxRetries returns a boolean if a field has been set.

### GetRetryDelayMinMs

`func (o *SentinelCheck) GetRetryDelayMinMs() int64`

GetRetryDelayMinMs returns the RetryDelayMinMs field if non-nil, zero value otherwise.

### GetRetryDelayMinMsOk

`func (o *SentinelCheck) GetRetryDelayMinMsOk() (*int64, bool)`

GetRetryDelayMinMsOk returns a tuple with the RetryDelayMinMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRetryDelayMinMs

`func (o *SentinelCheck) SetRetryDelayMinMs(v int64)`

SetRetryDelayMinMs sets RetryDelayMinMs field to given value.

### HasRetryDelayMinMs

`func (o *SentinelCheck) HasRetryDelayMinMs() bool`

HasRetryDelayMinMs returns a boolean if a field has been set.

### GetRetryDelayMaxMs

`func (o *SentinelCheck) GetRetryDelayMaxMs() int64`

GetRetryDelayMaxMs returns the RetryDelayMaxMs field if non-nil, zero value otherwise.

### GetRetryDelayMaxMsOk

`func (o *SentinelCheck) GetRetryDelayMaxMsOk() (*int64, bool)`

GetRetryDelayMaxMsOk returns a tuple with the RetryDelayMaxMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRetryDelayMaxMs

`func (o *SentinelCheck) SetRetryDelayMaxMs(v int64)`

SetRetryDelayMaxMs sets RetryDelayMaxMs field to given value.

### HasRetryDelayMaxMs

`func (o *SentinelCheck) HasRetryDelayMaxMs() bool`

HasRetryDelayMaxMs returns a boolean if a field has been set.

### GetCircuitBreakerFailureThreshold

`func (o *SentinelCheck) GetCircuitBreakerFailureThreshold() int32`

GetCircuitBreakerFailureThreshold returns the CircuitBreakerFailureThreshold field if non-nil, zero value otherwise.

### GetCircuitBreakerFailureThresholdOk

`func (o *SentinelCheck) GetCircuitBreakerFailureThresholdOk() (*int32, bool)`

GetCircuitBreakerFailureThresholdOk returns a tuple with the CircuitBreakerFailureThreshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCircuitBreakerFailureThreshold

`func (o *SentinelCheck) SetCircuitBreakerFailureThreshold(v int32)`

SetCircuitBreakerFailureThreshold sets CircuitBreakerFailureThreshold field to given value.

### HasCircuitBreakerFailureThreshold

`func (o *SentinelCheck) HasCircuitBreakerFailureThreshold() bool`

HasCircuitBreakerFailureThreshold returns a boolean if a field has been set.

### GetCooldownMs

`func (o *SentinelCheck) GetCooldownMs() int64`

GetCooldownMs returns the CooldownMs field if non-nil, zero value otherwise.

### GetCooldownMsOk

`func (o *SentinelCheck) GetCooldownMsOk() (*int64, bool)`

GetCooldownMsOk returns a tuple with the CooldownMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCooldownMs

`func (o *SentinelCheck) SetCooldownMs(v int64)`

SetCooldownMs sets CooldownMs field to given value.

### HasCooldownMs

`func (o *SentinelCheck) HasCooldownMs() bool`

HasCooldownMs returns a boolean if a field has been set.

### GetId

`func (o *SentinelCheck) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SentinelCheck) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SentinelCheck) SetId(v string)`

SetId sets Id field to given value.


### GetDefinitionHash

`func (o *SentinelCheck) GetDefinitionHash() string`

GetDefinitionHash returns the DefinitionHash field if non-nil, zero value otherwise.

### GetDefinitionHashOk

`func (o *SentinelCheck) GetDefinitionHashOk() (*string, bool)`

GetDefinitionHashOk returns a tuple with the DefinitionHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinitionHash

`func (o *SentinelCheck) SetDefinitionHash(v string)`

SetDefinitionHash sets DefinitionHash field to given value.


### GetConsecutiveFailures

`func (o *SentinelCheck) GetConsecutiveFailures() int32`

GetConsecutiveFailures returns the ConsecutiveFailures field if non-nil, zero value otherwise.

### GetConsecutiveFailuresOk

`func (o *SentinelCheck) GetConsecutiveFailuresOk() (*int32, bool)`

GetConsecutiveFailuresOk returns a tuple with the ConsecutiveFailures field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConsecutiveFailures

`func (o *SentinelCheck) SetConsecutiveFailures(v int32)`

SetConsecutiveFailures sets ConsecutiveFailures field to given value.


### GetPausedUntil

`func (o *SentinelCheck) GetPausedUntil() time.Time`

GetPausedUntil returns the PausedUntil field if non-nil, zero value otherwise.

### GetPausedUntilOk

`func (o *SentinelCheck) GetPausedUntilOk() (*time.Time, bool)`

GetPausedUntilOk returns a tuple with the PausedUntil field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPausedUntil

`func (o *SentinelCheck) SetPausedUntil(v time.Time)`

SetPausedUntil sets PausedUntil field to given value.

### HasPausedUntil

`func (o *SentinelCheck) HasPausedUntil() bool`

HasPausedUntil returns a boolean if a field has been set.

### SetPausedUntilNil

`func (o *SentinelCheck) SetPausedUntilNil(b bool)`

 SetPausedUntilNil sets the value for PausedUntil to be an explicit nil

### UnsetPausedUntil
`func (o *SentinelCheck) UnsetPausedUntil()`

UnsetPausedUntil ensures that no value is present for PausedUntil, not even an explicit nil
### GetLastRunAt

`func (o *SentinelCheck) GetLastRunAt() time.Time`

GetLastRunAt returns the LastRunAt field if non-nil, zero value otherwise.

### GetLastRunAtOk

`func (o *SentinelCheck) GetLastRunAtOk() (*time.Time, bool)`

GetLastRunAtOk returns a tuple with the LastRunAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRunAt

`func (o *SentinelCheck) SetLastRunAt(v time.Time)`

SetLastRunAt sets LastRunAt field to given value.

### HasLastRunAt

`func (o *SentinelCheck) HasLastRunAt() bool`

HasLastRunAt returns a boolean if a field has been set.

### SetLastRunAtNil

`func (o *SentinelCheck) SetLastRunAtNil(b bool)`

 SetLastRunAtNil sets the value for LastRunAt to be an explicit nil

### UnsetLastRunAt
`func (o *SentinelCheck) UnsetLastRunAt()`

UnsetLastRunAt ensures that no value is present for LastRunAt, not even an explicit nil
### GetLastRunStatus

`func (o *SentinelCheck) GetLastRunStatus() RunStatus`

GetLastRunStatus returns the LastRunStatus field if non-nil, zero value otherwise.

### GetLastRunStatusOk

`func (o *SentinelCheck) GetLastRunStatusOk() (*RunStatus, bool)`

GetLastRunStatusOk returns a tuple with the LastRunStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRunStatus

`func (o *SentinelCheck) SetLastRunStatus(v RunStatus)`

SetLastRunStatus sets LastRunStatus field to given value.

### HasLastRunStatus

`func (o *SentinelCheck) HasLastRunStatus() bool`

HasLastRunStatus returns a boolean if a field has been set.

### SetLastRunStatusNil

`func (o *SentinelCheck) SetLastRunStatusNil(b bool)`

 SetLastRunStatusNil sets the value for LastRunStatus to be an explicit nil

### UnsetLastRunStatus
`func (o *SentinelCheck) UnsetLastRunStatus()`

UnsetLastRunStatus ensures that no value is present for LastRunStatus, not even an explicit nil
### GetCreatedAt

`func (o *SentinelCheck) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SentinelCheck) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SentinelCheck) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *SentinelCheck) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *SentinelCheck) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *SentinelCheck) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


