# SentinelCheckInput

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

## Methods

### NewSentinelCheckInput

`func NewSentinelCheckInput(name string, environment string, type_ string, format ContentFormat, definition string, ) *SentinelCheckInput`

NewSentinelCheckInput instantiates a new SentinelCheckInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSentinelCheckInputWithDefaults

`func NewSentinelCheckInputWithDefaults() *SentinelCheckInput`

NewSentinelCheckInputWithDefaults instantiates a new SentinelCheckInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *SentinelCheckInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SentinelCheckInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SentinelCheckInput) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *SentinelCheckInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *SentinelCheckInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *SentinelCheckInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *SentinelCheckInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *SentinelCheckInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *SentinelCheckInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetSourceName

`func (o *SentinelCheckInput) GetSourceName() string`

GetSourceName returns the SourceName field if non-nil, zero value otherwise.

### GetSourceNameOk

`func (o *SentinelCheckInput) GetSourceNameOk() (*string, bool)`

GetSourceNameOk returns a tuple with the SourceName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceName

`func (o *SentinelCheckInput) SetSourceName(v string)`

SetSourceName sets SourceName field to given value.

### HasSourceName

`func (o *SentinelCheckInput) HasSourceName() bool`

HasSourceName returns a boolean if a field has been set.

### SetSourceNameNil

`func (o *SentinelCheckInput) SetSourceNameNil(b bool)`

 SetSourceNameNil sets the value for SourceName to be an explicit nil

### UnsetSourceName
`func (o *SentinelCheckInput) UnsetSourceName()`

UnsetSourceName ensures that no value is present for SourceName, not even an explicit nil
### GetEnvironment

`func (o *SentinelCheckInput) GetEnvironment() string`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *SentinelCheckInput) GetEnvironmentOk() (*string, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *SentinelCheckInput) SetEnvironment(v string)`

SetEnvironment sets Environment field to given value.


### GetType

`func (o *SentinelCheckInput) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *SentinelCheckInput) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *SentinelCheckInput) SetType(v string)`

SetType sets Type field to given value.


### GetSpecType

`func (o *SentinelCheckInput) GetSpecType() SpecType`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *SentinelCheckInput) GetSpecTypeOk() (*SpecType, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *SentinelCheckInput) SetSpecType(v SpecType)`

SetSpecType sets SpecType field to given value.

### HasSpecType

`func (o *SentinelCheckInput) HasSpecType() bool`

HasSpecType returns a boolean if a field has been set.

### SetSpecTypeNil

`func (o *SentinelCheckInput) SetSpecTypeNil(b bool)`

 SetSpecTypeNil sets the value for SpecType to be an explicit nil

### UnsetSpecType
`func (o *SentinelCheckInput) UnsetSpecType()`

UnsetSpecType ensures that no value is present for SpecType, not even an explicit nil
### GetFormat

`func (o *SentinelCheckInput) GetFormat() ContentFormat`

GetFormat returns the Format field if non-nil, zero value otherwise.

### GetFormatOk

`func (o *SentinelCheckInput) GetFormatOk() (*ContentFormat, bool)`

GetFormatOk returns a tuple with the Format field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFormat

`func (o *SentinelCheckInput) SetFormat(v ContentFormat)`

SetFormat sets Format field to given value.


### GetDefinition

`func (o *SentinelCheckInput) GetDefinition() string`

GetDefinition returns the Definition field if non-nil, zero value otherwise.

### GetDefinitionOk

`func (o *SentinelCheckInput) GetDefinitionOk() (*string, bool)`

GetDefinitionOk returns a tuple with the Definition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinition

`func (o *SentinelCheckInput) SetDefinition(v string)`

SetDefinition sets Definition field to given value.


### GetActive

`func (o *SentinelCheckInput) GetActive() bool`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *SentinelCheckInput) GetActiveOk() (*bool, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *SentinelCheckInput) SetActive(v bool)`

SetActive sets Active field to given value.

### HasActive

`func (o *SentinelCheckInput) HasActive() bool`

HasActive returns a boolean if a field has been set.

### GetTimeoutMs

`func (o *SentinelCheckInput) GetTimeoutMs() int64`

GetTimeoutMs returns the TimeoutMs field if non-nil, zero value otherwise.

### GetTimeoutMsOk

`func (o *SentinelCheckInput) GetTimeoutMsOk() (*int64, bool)`

GetTimeoutMsOk returns a tuple with the TimeoutMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimeoutMs

`func (o *SentinelCheckInput) SetTimeoutMs(v int64)`

SetTimeoutMs sets TimeoutMs field to given value.

### HasTimeoutMs

`func (o *SentinelCheckInput) HasTimeoutMs() bool`

HasTimeoutMs returns a boolean if a field has been set.

### GetFailureStrategy

`func (o *SentinelCheckInput) GetFailureStrategy() string`

GetFailureStrategy returns the FailureStrategy field if non-nil, zero value otherwise.

### GetFailureStrategyOk

`func (o *SentinelCheckInput) GetFailureStrategyOk() (*string, bool)`

GetFailureStrategyOk returns a tuple with the FailureStrategy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFailureStrategy

`func (o *SentinelCheckInput) SetFailureStrategy(v string)`

SetFailureStrategy sets FailureStrategy field to given value.

### HasFailureStrategy

`func (o *SentinelCheckInput) HasFailureStrategy() bool`

HasFailureStrategy returns a boolean if a field has been set.

### GetMaxRetries

`func (o *SentinelCheckInput) GetMaxRetries() int32`

GetMaxRetries returns the MaxRetries field if non-nil, zero value otherwise.

### GetMaxRetriesOk

`func (o *SentinelCheckInput) GetMaxRetriesOk() (*int32, bool)`

GetMaxRetriesOk returns a tuple with the MaxRetries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxRetries

`func (o *SentinelCheckInput) SetMaxRetries(v int32)`

SetMaxRetries sets MaxRetries field to given value.

### HasMaxRetries

`func (o *SentinelCheckInput) HasMaxRetries() bool`

HasMaxRetries returns a boolean if a field has been set.

### GetRetryDelayMinMs

`func (o *SentinelCheckInput) GetRetryDelayMinMs() int64`

GetRetryDelayMinMs returns the RetryDelayMinMs field if non-nil, zero value otherwise.

### GetRetryDelayMinMsOk

`func (o *SentinelCheckInput) GetRetryDelayMinMsOk() (*int64, bool)`

GetRetryDelayMinMsOk returns a tuple with the RetryDelayMinMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRetryDelayMinMs

`func (o *SentinelCheckInput) SetRetryDelayMinMs(v int64)`

SetRetryDelayMinMs sets RetryDelayMinMs field to given value.

### HasRetryDelayMinMs

`func (o *SentinelCheckInput) HasRetryDelayMinMs() bool`

HasRetryDelayMinMs returns a boolean if a field has been set.

### GetRetryDelayMaxMs

`func (o *SentinelCheckInput) GetRetryDelayMaxMs() int64`

GetRetryDelayMaxMs returns the RetryDelayMaxMs field if non-nil, zero value otherwise.

### GetRetryDelayMaxMsOk

`func (o *SentinelCheckInput) GetRetryDelayMaxMsOk() (*int64, bool)`

GetRetryDelayMaxMsOk returns a tuple with the RetryDelayMaxMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRetryDelayMaxMs

`func (o *SentinelCheckInput) SetRetryDelayMaxMs(v int64)`

SetRetryDelayMaxMs sets RetryDelayMaxMs field to given value.

### HasRetryDelayMaxMs

`func (o *SentinelCheckInput) HasRetryDelayMaxMs() bool`

HasRetryDelayMaxMs returns a boolean if a field has been set.

### GetCircuitBreakerFailureThreshold

`func (o *SentinelCheckInput) GetCircuitBreakerFailureThreshold() int32`

GetCircuitBreakerFailureThreshold returns the CircuitBreakerFailureThreshold field if non-nil, zero value otherwise.

### GetCircuitBreakerFailureThresholdOk

`func (o *SentinelCheckInput) GetCircuitBreakerFailureThresholdOk() (*int32, bool)`

GetCircuitBreakerFailureThresholdOk returns a tuple with the CircuitBreakerFailureThreshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCircuitBreakerFailureThreshold

`func (o *SentinelCheckInput) SetCircuitBreakerFailureThreshold(v int32)`

SetCircuitBreakerFailureThreshold sets CircuitBreakerFailureThreshold field to given value.

### HasCircuitBreakerFailureThreshold

`func (o *SentinelCheckInput) HasCircuitBreakerFailureThreshold() bool`

HasCircuitBreakerFailureThreshold returns a boolean if a field has been set.

### GetCooldownMs

`func (o *SentinelCheckInput) GetCooldownMs() int64`

GetCooldownMs returns the CooldownMs field if non-nil, zero value otherwise.

### GetCooldownMsOk

`func (o *SentinelCheckInput) GetCooldownMsOk() (*int64, bool)`

GetCooldownMsOk returns a tuple with the CooldownMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCooldownMs

`func (o *SentinelCheckInput) SetCooldownMs(v int64)`

SetCooldownMs sets CooldownMs field to given value.

### HasCooldownMs

`func (o *SentinelCheckInput) HasCooldownMs() bool`

HasCooldownMs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


