# StreamingRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SpecId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**SpecName** | **string** |  |
**SpecStableKey** | Pointer to **NullableString** |  | [optional]
**SpecType** | **string** |  |
**Format** | **string** |  |
**Transport** | [**StreamingTransport**](StreamingTransport.md) |  |
**DefinitionHash** | **string** |  |
**State** | [**StreamingRunState**](StreamingRunState.md) |  |
**Outcome** | Pointer to [**NullableStreamingRunOutcome**](StreamingRunOutcome.md) |  | [optional]
**TerminationReason** | Pointer to **NullableString** |  | [optional]
**EventCount** | **int64** |  |
**ByteCount** | **int64** |  |
**AssertionPassCount** | **int32** |  |
**AssertionFailCount** | **int32** |  |
**EvidenceSummary** | Pointer to **map[string]interface{}** |  | [optional]
**ErrorMessage** | Pointer to **NullableString** |  | [optional]
**CreatedAt** | **time.Time** |  |
**StartedAt** | Pointer to **NullableTime** |  | [optional]
**FinishedAt** | Pointer to **NullableTime** |  | [optional]

## Methods

### NewStreamingRun

`func NewStreamingRun(id string, specName string, specType string, format string, transport StreamingTransport, definitionHash string, state StreamingRunState, eventCount int64, byteCount int64, assertionPassCount int32, assertionFailCount int32, createdAt time.Time, ) *StreamingRun`

NewStreamingRun instantiates a new StreamingRun object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStreamingRunWithDefaults

`func NewStreamingRunWithDefaults() *StreamingRun`

NewStreamingRunWithDefaults instantiates a new StreamingRun object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *StreamingRun) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *StreamingRun) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *StreamingRun) SetId(v string)`

SetId sets Id field to given value.


### GetSpecId

`func (o *StreamingRun) GetSpecId() string`

GetSpecId returns the SpecId field if non-nil, zero value otherwise.

### GetSpecIdOk

`func (o *StreamingRun) GetSpecIdOk() (*string, bool)`

GetSpecIdOk returns a tuple with the SpecId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecId

`func (o *StreamingRun) SetSpecId(v string)`

SetSpecId sets SpecId field to given value.

### HasSpecId

`func (o *StreamingRun) HasSpecId() bool`

HasSpecId returns a boolean if a field has been set.

### SetSpecIdNil

`func (o *StreamingRun) SetSpecIdNil(b bool)`

 SetSpecIdNil sets the value for SpecId to be an explicit nil

### UnsetSpecId
`func (o *StreamingRun) UnsetSpecId()`

UnsetSpecId ensures that no value is present for SpecId, not even an explicit nil
### GetSpecName

`func (o *StreamingRun) GetSpecName() string`

GetSpecName returns the SpecName field if non-nil, zero value otherwise.

### GetSpecNameOk

`func (o *StreamingRun) GetSpecNameOk() (*string, bool)`

GetSpecNameOk returns a tuple with the SpecName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecName

`func (o *StreamingRun) SetSpecName(v string)`

SetSpecName sets SpecName field to given value.


### GetSpecStableKey

`func (o *StreamingRun) GetSpecStableKey() string`

GetSpecStableKey returns the SpecStableKey field if non-nil, zero value otherwise.

### GetSpecStableKeyOk

`func (o *StreamingRun) GetSpecStableKeyOk() (*string, bool)`

GetSpecStableKeyOk returns a tuple with the SpecStableKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecStableKey

`func (o *StreamingRun) SetSpecStableKey(v string)`

SetSpecStableKey sets SpecStableKey field to given value.

### HasSpecStableKey

`func (o *StreamingRun) HasSpecStableKey() bool`

HasSpecStableKey returns a boolean if a field has been set.

### SetSpecStableKeyNil

`func (o *StreamingRun) SetSpecStableKeyNil(b bool)`

 SetSpecStableKeyNil sets the value for SpecStableKey to be an explicit nil

### UnsetSpecStableKey
`func (o *StreamingRun) UnsetSpecStableKey()`

UnsetSpecStableKey ensures that no value is present for SpecStableKey, not even an explicit nil
### GetSpecType

`func (o *StreamingRun) GetSpecType() string`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *StreamingRun) GetSpecTypeOk() (*string, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *StreamingRun) SetSpecType(v string)`

SetSpecType sets SpecType field to given value.


### GetFormat

`func (o *StreamingRun) GetFormat() string`

GetFormat returns the Format field if non-nil, zero value otherwise.

### GetFormatOk

`func (o *StreamingRun) GetFormatOk() (*string, bool)`

GetFormatOk returns a tuple with the Format field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFormat

`func (o *StreamingRun) SetFormat(v string)`

SetFormat sets Format field to given value.


### GetTransport

`func (o *StreamingRun) GetTransport() StreamingTransport`

GetTransport returns the Transport field if non-nil, zero value otherwise.

### GetTransportOk

`func (o *StreamingRun) GetTransportOk() (*StreamingTransport, bool)`

GetTransportOk returns a tuple with the Transport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransport

`func (o *StreamingRun) SetTransport(v StreamingTransport)`

SetTransport sets Transport field to given value.


### GetDefinitionHash

`func (o *StreamingRun) GetDefinitionHash() string`

GetDefinitionHash returns the DefinitionHash field if non-nil, zero value otherwise.

### GetDefinitionHashOk

`func (o *StreamingRun) GetDefinitionHashOk() (*string, bool)`

GetDefinitionHashOk returns a tuple with the DefinitionHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinitionHash

`func (o *StreamingRun) SetDefinitionHash(v string)`

SetDefinitionHash sets DefinitionHash field to given value.


### GetState

`func (o *StreamingRun) GetState() StreamingRunState`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *StreamingRun) GetStateOk() (*StreamingRunState, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *StreamingRun) SetState(v StreamingRunState)`

SetState sets State field to given value.


### GetOutcome

`func (o *StreamingRun) GetOutcome() StreamingRunOutcome`

GetOutcome returns the Outcome field if non-nil, zero value otherwise.

### GetOutcomeOk

`func (o *StreamingRun) GetOutcomeOk() (*StreamingRunOutcome, bool)`

GetOutcomeOk returns a tuple with the Outcome field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutcome

`func (o *StreamingRun) SetOutcome(v StreamingRunOutcome)`

SetOutcome sets Outcome field to given value.

### HasOutcome

`func (o *StreamingRun) HasOutcome() bool`

HasOutcome returns a boolean if a field has been set.

### SetOutcomeNil

`func (o *StreamingRun) SetOutcomeNil(b bool)`

 SetOutcomeNil sets the value for Outcome to be an explicit nil

### UnsetOutcome
`func (o *StreamingRun) UnsetOutcome()`

UnsetOutcome ensures that no value is present for Outcome, not even an explicit nil
### GetTerminationReason

`func (o *StreamingRun) GetTerminationReason() string`

GetTerminationReason returns the TerminationReason field if non-nil, zero value otherwise.

### GetTerminationReasonOk

`func (o *StreamingRun) GetTerminationReasonOk() (*string, bool)`

GetTerminationReasonOk returns a tuple with the TerminationReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTerminationReason

`func (o *StreamingRun) SetTerminationReason(v string)`

SetTerminationReason sets TerminationReason field to given value.

### HasTerminationReason

`func (o *StreamingRun) HasTerminationReason() bool`

HasTerminationReason returns a boolean if a field has been set.

### SetTerminationReasonNil

`func (o *StreamingRun) SetTerminationReasonNil(b bool)`

 SetTerminationReasonNil sets the value for TerminationReason to be an explicit nil

### UnsetTerminationReason
`func (o *StreamingRun) UnsetTerminationReason()`

UnsetTerminationReason ensures that no value is present for TerminationReason, not even an explicit nil
### GetEventCount

`func (o *StreamingRun) GetEventCount() int64`

GetEventCount returns the EventCount field if non-nil, zero value otherwise.

### GetEventCountOk

`func (o *StreamingRun) GetEventCountOk() (*int64, bool)`

GetEventCountOk returns a tuple with the EventCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEventCount

`func (o *StreamingRun) SetEventCount(v int64)`

SetEventCount sets EventCount field to given value.


### GetByteCount

`func (o *StreamingRun) GetByteCount() int64`

GetByteCount returns the ByteCount field if non-nil, zero value otherwise.

### GetByteCountOk

`func (o *StreamingRun) GetByteCountOk() (*int64, bool)`

GetByteCountOk returns a tuple with the ByteCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetByteCount

`func (o *StreamingRun) SetByteCount(v int64)`

SetByteCount sets ByteCount field to given value.


### GetAssertionPassCount

`func (o *StreamingRun) GetAssertionPassCount() int32`

GetAssertionPassCount returns the AssertionPassCount field if non-nil, zero value otherwise.

### GetAssertionPassCountOk

`func (o *StreamingRun) GetAssertionPassCountOk() (*int32, bool)`

GetAssertionPassCountOk returns a tuple with the AssertionPassCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssertionPassCount

`func (o *StreamingRun) SetAssertionPassCount(v int32)`

SetAssertionPassCount sets AssertionPassCount field to given value.


### GetAssertionFailCount

`func (o *StreamingRun) GetAssertionFailCount() int32`

GetAssertionFailCount returns the AssertionFailCount field if non-nil, zero value otherwise.

### GetAssertionFailCountOk

`func (o *StreamingRun) GetAssertionFailCountOk() (*int32, bool)`

GetAssertionFailCountOk returns a tuple with the AssertionFailCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssertionFailCount

`func (o *StreamingRun) SetAssertionFailCount(v int32)`

SetAssertionFailCount sets AssertionFailCount field to given value.


### GetEvidenceSummary

`func (o *StreamingRun) GetEvidenceSummary() map[string]interface{}`

GetEvidenceSummary returns the EvidenceSummary field if non-nil, zero value otherwise.

### GetEvidenceSummaryOk

`func (o *StreamingRun) GetEvidenceSummaryOk() (*map[string]interface{}, bool)`

GetEvidenceSummaryOk returns a tuple with the EvidenceSummary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvidenceSummary

`func (o *StreamingRun) SetEvidenceSummary(v map[string]interface{})`

SetEvidenceSummary sets EvidenceSummary field to given value.

### HasEvidenceSummary

`func (o *StreamingRun) HasEvidenceSummary() bool`

HasEvidenceSummary returns a boolean if a field has been set.

### SetEvidenceSummaryNil

`func (o *StreamingRun) SetEvidenceSummaryNil(b bool)`

 SetEvidenceSummaryNil sets the value for EvidenceSummary to be an explicit nil

### UnsetEvidenceSummary
`func (o *StreamingRun) UnsetEvidenceSummary()`

UnsetEvidenceSummary ensures that no value is present for EvidenceSummary, not even an explicit nil
### GetErrorMessage

`func (o *StreamingRun) GetErrorMessage() string`

GetErrorMessage returns the ErrorMessage field if non-nil, zero value otherwise.

### GetErrorMessageOk

`func (o *StreamingRun) GetErrorMessageOk() (*string, bool)`

GetErrorMessageOk returns a tuple with the ErrorMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorMessage

`func (o *StreamingRun) SetErrorMessage(v string)`

SetErrorMessage sets ErrorMessage field to given value.

### HasErrorMessage

`func (o *StreamingRun) HasErrorMessage() bool`

HasErrorMessage returns a boolean if a field has been set.

### SetErrorMessageNil

`func (o *StreamingRun) SetErrorMessageNil(b bool)`

 SetErrorMessageNil sets the value for ErrorMessage to be an explicit nil

### UnsetErrorMessage
`func (o *StreamingRun) UnsetErrorMessage()`

UnsetErrorMessage ensures that no value is present for ErrorMessage, not even an explicit nil
### GetCreatedAt

`func (o *StreamingRun) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *StreamingRun) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *StreamingRun) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetStartedAt

`func (o *StreamingRun) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *StreamingRun) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *StreamingRun) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.

### HasStartedAt

`func (o *StreamingRun) HasStartedAt() bool`

HasStartedAt returns a boolean if a field has been set.

### SetStartedAtNil

`func (o *StreamingRun) SetStartedAtNil(b bool)`

 SetStartedAtNil sets the value for StartedAt to be an explicit nil

### UnsetStartedAt
`func (o *StreamingRun) UnsetStartedAt()`

UnsetStartedAt ensures that no value is present for StartedAt, not even an explicit nil
### GetFinishedAt

`func (o *StreamingRun) GetFinishedAt() time.Time`

GetFinishedAt returns the FinishedAt field if non-nil, zero value otherwise.

### GetFinishedAtOk

`func (o *StreamingRun) GetFinishedAtOk() (*time.Time, bool)`

GetFinishedAtOk returns a tuple with the FinishedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinishedAt

`func (o *StreamingRun) SetFinishedAt(v time.Time)`

SetFinishedAt sets FinishedAt field to given value.

### HasFinishedAt

`func (o *StreamingRun) HasFinishedAt() bool`

HasFinishedAt returns a boolean if a field has been set.

### SetFinishedAtNil

`func (o *StreamingRun) SetFinishedAtNil(b bool)`

 SetFinishedAtNil sets the value for FinishedAt to be an explicit nil

### UnsetFinishedAt
`func (o *StreamingRun) UnsetFinishedAt()`

UnsetFinishedAt ensures that no value is present for FinishedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
