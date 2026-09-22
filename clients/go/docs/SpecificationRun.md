# SpecificationRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RunId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SpecId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SpecName** | **string** |  |
**SpecStableKey** | Pointer to **NullableString** |  | [optional]
**SpecType** | [**SpecType**](SpecType.md) |  |
**OverallTestStatus** | **string** |  |
**StartedAt** | **time.Time** |  |
**FinishedAt** | **time.Time** |  |
**SpecDefinitionHash** | Pointer to **NullableString** |  | [optional]
**Format** | Pointer to [**ContentFormat**](ContentFormat.md) |  | [optional] [default to CONTENTFORMAT_JSON]
**TestResultLog** | **map[string]interface{}** |  |
**RawSpec** | **string** |  |

## Methods

### NewSpecificationRun

`func NewSpecificationRun(runId string, specId string, specName string, specType SpecType, overallTestStatus string, startedAt time.Time, finishedAt time.Time, testResultLog map[string]interface{}, rawSpec string, ) *SpecificationRun`

NewSpecificationRun instantiates a new SpecificationRun object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSpecificationRunWithDefaults

`func NewSpecificationRunWithDefaults() *SpecificationRun`

NewSpecificationRunWithDefaults instantiates a new SpecificationRun object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRunId

`func (o *SpecificationRun) GetRunId() string`

GetRunId returns the RunId field if non-nil, zero value otherwise.

### GetRunIdOk

`func (o *SpecificationRun) GetRunIdOk() (*string, bool)`

GetRunIdOk returns a tuple with the RunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRunId

`func (o *SpecificationRun) SetRunId(v string)`

SetRunId sets RunId field to given value.


### GetSpecId

`func (o *SpecificationRun) GetSpecId() string`

GetSpecId returns the SpecId field if non-nil, zero value otherwise.

### GetSpecIdOk

`func (o *SpecificationRun) GetSpecIdOk() (*string, bool)`

GetSpecIdOk returns a tuple with the SpecId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecId

`func (o *SpecificationRun) SetSpecId(v string)`

SetSpecId sets SpecId field to given value.


### GetSpecName

`func (o *SpecificationRun) GetSpecName() string`

GetSpecName returns the SpecName field if non-nil, zero value otherwise.

### GetSpecNameOk

`func (o *SpecificationRun) GetSpecNameOk() (*string, bool)`

GetSpecNameOk returns a tuple with the SpecName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecName

`func (o *SpecificationRun) SetSpecName(v string)`

SetSpecName sets SpecName field to given value.


### GetSpecStableKey

`func (o *SpecificationRun) GetSpecStableKey() string`

GetSpecStableKey returns the SpecStableKey field if non-nil, zero value otherwise.

### GetSpecStableKeyOk

`func (o *SpecificationRun) GetSpecStableKeyOk() (*string, bool)`

GetSpecStableKeyOk returns a tuple with the SpecStableKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecStableKey

`func (o *SpecificationRun) SetSpecStableKey(v string)`

SetSpecStableKey sets SpecStableKey field to given value.

### HasSpecStableKey

`func (o *SpecificationRun) HasSpecStableKey() bool`

HasSpecStableKey returns a boolean if a field has been set.

### SetSpecStableKeyNil

`func (o *SpecificationRun) SetSpecStableKeyNil(b bool)`

 SetSpecStableKeyNil sets the value for SpecStableKey to be an explicit nil

### UnsetSpecStableKey
`func (o *SpecificationRun) UnsetSpecStableKey()`

UnsetSpecStableKey ensures that no value is present for SpecStableKey, not even an explicit nil
### GetSpecType

`func (o *SpecificationRun) GetSpecType() SpecType`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *SpecificationRun) GetSpecTypeOk() (*SpecType, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *SpecificationRun) SetSpecType(v SpecType)`

SetSpecType sets SpecType field to given value.


### GetOverallTestStatus

`func (o *SpecificationRun) GetOverallTestStatus() string`

GetOverallTestStatus returns the OverallTestStatus field if non-nil, zero value otherwise.

### GetOverallTestStatusOk

`func (o *SpecificationRun) GetOverallTestStatusOk() (*string, bool)`

GetOverallTestStatusOk returns a tuple with the OverallTestStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOverallTestStatus

`func (o *SpecificationRun) SetOverallTestStatus(v string)`

SetOverallTestStatus sets OverallTestStatus field to given value.


### GetStartedAt

`func (o *SpecificationRun) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *SpecificationRun) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *SpecificationRun) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.


### GetFinishedAt

`func (o *SpecificationRun) GetFinishedAt() time.Time`

GetFinishedAt returns the FinishedAt field if non-nil, zero value otherwise.

### GetFinishedAtOk

`func (o *SpecificationRun) GetFinishedAtOk() (*time.Time, bool)`

GetFinishedAtOk returns a tuple with the FinishedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinishedAt

`func (o *SpecificationRun) SetFinishedAt(v time.Time)`

SetFinishedAt sets FinishedAt field to given value.


### GetSpecDefinitionHash

`func (o *SpecificationRun) GetSpecDefinitionHash() string`

GetSpecDefinitionHash returns the SpecDefinitionHash field if non-nil, zero value otherwise.

### GetSpecDefinitionHashOk

`func (o *SpecificationRun) GetSpecDefinitionHashOk() (*string, bool)`

GetSpecDefinitionHashOk returns a tuple with the SpecDefinitionHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecDefinitionHash

`func (o *SpecificationRun) SetSpecDefinitionHash(v string)`

SetSpecDefinitionHash sets SpecDefinitionHash field to given value.

### HasSpecDefinitionHash

`func (o *SpecificationRun) HasSpecDefinitionHash() bool`

HasSpecDefinitionHash returns a boolean if a field has been set.

### SetSpecDefinitionHashNil

`func (o *SpecificationRun) SetSpecDefinitionHashNil(b bool)`

 SetSpecDefinitionHashNil sets the value for SpecDefinitionHash to be an explicit nil

### UnsetSpecDefinitionHash
`func (o *SpecificationRun) UnsetSpecDefinitionHash()`

UnsetSpecDefinitionHash ensures that no value is present for SpecDefinitionHash, not even an explicit nil
### GetFormat

`func (o *SpecificationRun) GetFormat() ContentFormat`

GetFormat returns the Format field if non-nil, zero value otherwise.

### GetFormatOk

`func (o *SpecificationRun) GetFormatOk() (*ContentFormat, bool)`

GetFormatOk returns a tuple with the Format field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFormat

`func (o *SpecificationRun) SetFormat(v ContentFormat)`

SetFormat sets Format field to given value.

### HasFormat

`func (o *SpecificationRun) HasFormat() bool`

HasFormat returns a boolean if a field has been set.

### GetTestResultLog

`func (o *SpecificationRun) GetTestResultLog() map[string]interface{}`

GetTestResultLog returns the TestResultLog field if non-nil, zero value otherwise.

### GetTestResultLogOk

`func (o *SpecificationRun) GetTestResultLogOk() (*map[string]interface{}, bool)`

GetTestResultLogOk returns a tuple with the TestResultLog field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTestResultLog

`func (o *SpecificationRun) SetTestResultLog(v map[string]interface{})`

SetTestResultLog sets TestResultLog field to given value.


### GetRawSpec

`func (o *SpecificationRun) GetRawSpec() string`

GetRawSpec returns the RawSpec field if non-nil, zero value otherwise.

### GetRawSpecOk

`func (o *SpecificationRun) GetRawSpecOk() (*string, bool)`

GetRawSpecOk returns a tuple with the RawSpec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRawSpec

`func (o *SpecificationRun) SetRawSpec(v string)`

SetRawSpec sets RawSpec field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


