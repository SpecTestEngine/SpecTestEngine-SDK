# SentinelIncident

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Environment** | **string** |  |
**CheckId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**CheckName** | **string** |  |
**Fingerprint** | **string** |  |
**Status** | **string** |  |
**ConsecutiveFailures** | **int32** |  |
**LastRunId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**Summary** | Pointer to **NullableString** |  | [optional]
**StartedAt** | Pointer to **NullableTime** |  | [optional]
**ResolvedAt** | Pointer to **NullableTime** |  | [optional]

## Methods

### NewSentinelIncident

`func NewSentinelIncident(id string, environment string, checkId string, checkName string, fingerprint string, status string, consecutiveFailures int32, ) *SentinelIncident`

NewSentinelIncident instantiates a new SentinelIncident object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSentinelIncidentWithDefaults

`func NewSentinelIncidentWithDefaults() *SentinelIncident`

NewSentinelIncidentWithDefaults instantiates a new SentinelIncident object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SentinelIncident) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SentinelIncident) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SentinelIncident) SetId(v string)`

SetId sets Id field to given value.


### GetEnvironment

`func (o *SentinelIncident) GetEnvironment() string`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *SentinelIncident) GetEnvironmentOk() (*string, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *SentinelIncident) SetEnvironment(v string)`

SetEnvironment sets Environment field to given value.


### GetCheckId

`func (o *SentinelIncident) GetCheckId() string`

GetCheckId returns the CheckId field if non-nil, zero value otherwise.

### GetCheckIdOk

`func (o *SentinelIncident) GetCheckIdOk() (*string, bool)`

GetCheckIdOk returns a tuple with the CheckId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckId

`func (o *SentinelIncident) SetCheckId(v string)`

SetCheckId sets CheckId field to given value.


### GetCheckName

`func (o *SentinelIncident) GetCheckName() string`

GetCheckName returns the CheckName field if non-nil, zero value otherwise.

### GetCheckNameOk

`func (o *SentinelIncident) GetCheckNameOk() (*string, bool)`

GetCheckNameOk returns a tuple with the CheckName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckName

`func (o *SentinelIncident) SetCheckName(v string)`

SetCheckName sets CheckName field to given value.


### GetFingerprint

`func (o *SentinelIncident) GetFingerprint() string`

GetFingerprint returns the Fingerprint field if non-nil, zero value otherwise.

### GetFingerprintOk

`func (o *SentinelIncident) GetFingerprintOk() (*string, bool)`

GetFingerprintOk returns a tuple with the Fingerprint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFingerprint

`func (o *SentinelIncident) SetFingerprint(v string)`

SetFingerprint sets Fingerprint field to given value.


### GetStatus

`func (o *SentinelIncident) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SentinelIncident) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SentinelIncident) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetConsecutiveFailures

`func (o *SentinelIncident) GetConsecutiveFailures() int32`

GetConsecutiveFailures returns the ConsecutiveFailures field if non-nil, zero value otherwise.

### GetConsecutiveFailuresOk

`func (o *SentinelIncident) GetConsecutiveFailuresOk() (*int32, bool)`

GetConsecutiveFailuresOk returns a tuple with the ConsecutiveFailures field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConsecutiveFailures

`func (o *SentinelIncident) SetConsecutiveFailures(v int32)`

SetConsecutiveFailures sets ConsecutiveFailures field to given value.


### GetLastRunId

`func (o *SentinelIncident) GetLastRunId() string`

GetLastRunId returns the LastRunId field if non-nil, zero value otherwise.

### GetLastRunIdOk

`func (o *SentinelIncident) GetLastRunIdOk() (*string, bool)`

GetLastRunIdOk returns a tuple with the LastRunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRunId

`func (o *SentinelIncident) SetLastRunId(v string)`

SetLastRunId sets LastRunId field to given value.

### HasLastRunId

`func (o *SentinelIncident) HasLastRunId() bool`

HasLastRunId returns a boolean if a field has been set.

### SetLastRunIdNil

`func (o *SentinelIncident) SetLastRunIdNil(b bool)`

 SetLastRunIdNil sets the value for LastRunId to be an explicit nil

### UnsetLastRunId
`func (o *SentinelIncident) UnsetLastRunId()`

UnsetLastRunId ensures that no value is present for LastRunId, not even an explicit nil
### GetSummary

`func (o *SentinelIncident) GetSummary() string`

GetSummary returns the Summary field if non-nil, zero value otherwise.

### GetSummaryOk

`func (o *SentinelIncident) GetSummaryOk() (*string, bool)`

GetSummaryOk returns a tuple with the Summary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSummary

`func (o *SentinelIncident) SetSummary(v string)`

SetSummary sets Summary field to given value.

### HasSummary

`func (o *SentinelIncident) HasSummary() bool`

HasSummary returns a boolean if a field has been set.

### SetSummaryNil

`func (o *SentinelIncident) SetSummaryNil(b bool)`

 SetSummaryNil sets the value for Summary to be an explicit nil

### UnsetSummary
`func (o *SentinelIncident) UnsetSummary()`

UnsetSummary ensures that no value is present for Summary, not even an explicit nil
### GetStartedAt

`func (o *SentinelIncident) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *SentinelIncident) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *SentinelIncident) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.

### HasStartedAt

`func (o *SentinelIncident) HasStartedAt() bool`

HasStartedAt returns a boolean if a field has been set.

### SetStartedAtNil

`func (o *SentinelIncident) SetStartedAtNil(b bool)`

 SetStartedAtNil sets the value for StartedAt to be an explicit nil

### UnsetStartedAt
`func (o *SentinelIncident) UnsetStartedAt()`

UnsetStartedAt ensures that no value is present for StartedAt, not even an explicit nil
### GetResolvedAt

`func (o *SentinelIncident) GetResolvedAt() time.Time`

GetResolvedAt returns the ResolvedAt field if non-nil, zero value otherwise.

### GetResolvedAtOk

`func (o *SentinelIncident) GetResolvedAtOk() (*time.Time, bool)`

GetResolvedAtOk returns a tuple with the ResolvedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResolvedAt

`func (o *SentinelIncident) SetResolvedAt(v time.Time)`

SetResolvedAt sets ResolvedAt field to given value.

### HasResolvedAt

`func (o *SentinelIncident) HasResolvedAt() bool`

HasResolvedAt returns a boolean if a field has been set.

### SetResolvedAtNil

`func (o *SentinelIncident) SetResolvedAtNil(b bool)`

 SetResolvedAtNil sets the value for ResolvedAt to be an explicit nil

### UnsetResolvedAt
`func (o *SentinelIncident) UnsetResolvedAt()`

UnsetResolvedAt ensures that no value is present for ResolvedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
