# SpecificationRunSummary

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

## Methods

### NewSpecificationRunSummary

`func NewSpecificationRunSummary(runId string, specId string, specName string, specType SpecType, overallTestStatus string, startedAt time.Time, finishedAt time.Time, ) *SpecificationRunSummary`

NewSpecificationRunSummary instantiates a new SpecificationRunSummary object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSpecificationRunSummaryWithDefaults

`func NewSpecificationRunSummaryWithDefaults() *SpecificationRunSummary`

NewSpecificationRunSummaryWithDefaults instantiates a new SpecificationRunSummary object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRunId

`func (o *SpecificationRunSummary) GetRunId() string`

GetRunId returns the RunId field if non-nil, zero value otherwise.

### GetRunIdOk

`func (o *SpecificationRunSummary) GetRunIdOk() (*string, bool)`

GetRunIdOk returns a tuple with the RunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRunId

`func (o *SpecificationRunSummary) SetRunId(v string)`

SetRunId sets RunId field to given value.


### GetSpecId

`func (o *SpecificationRunSummary) GetSpecId() string`

GetSpecId returns the SpecId field if non-nil, zero value otherwise.

### GetSpecIdOk

`func (o *SpecificationRunSummary) GetSpecIdOk() (*string, bool)`

GetSpecIdOk returns a tuple with the SpecId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecId

`func (o *SpecificationRunSummary) SetSpecId(v string)`

SetSpecId sets SpecId field to given value.


### GetSpecName

`func (o *SpecificationRunSummary) GetSpecName() string`

GetSpecName returns the SpecName field if non-nil, zero value otherwise.

### GetSpecNameOk

`func (o *SpecificationRunSummary) GetSpecNameOk() (*string, bool)`

GetSpecNameOk returns a tuple with the SpecName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecName

`func (o *SpecificationRunSummary) SetSpecName(v string)`

SetSpecName sets SpecName field to given value.


### GetSpecStableKey

`func (o *SpecificationRunSummary) GetSpecStableKey() string`

GetSpecStableKey returns the SpecStableKey field if non-nil, zero value otherwise.

### GetSpecStableKeyOk

`func (o *SpecificationRunSummary) GetSpecStableKeyOk() (*string, bool)`

GetSpecStableKeyOk returns a tuple with the SpecStableKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecStableKey

`func (o *SpecificationRunSummary) SetSpecStableKey(v string)`

SetSpecStableKey sets SpecStableKey field to given value.

### HasSpecStableKey

`func (o *SpecificationRunSummary) HasSpecStableKey() bool`

HasSpecStableKey returns a boolean if a field has been set.

### SetSpecStableKeyNil

`func (o *SpecificationRunSummary) SetSpecStableKeyNil(b bool)`

 SetSpecStableKeyNil sets the value for SpecStableKey to be an explicit nil

### UnsetSpecStableKey
`func (o *SpecificationRunSummary) UnsetSpecStableKey()`

UnsetSpecStableKey ensures that no value is present for SpecStableKey, not even an explicit nil
### GetSpecType

`func (o *SpecificationRunSummary) GetSpecType() SpecType`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *SpecificationRunSummary) GetSpecTypeOk() (*SpecType, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *SpecificationRunSummary) SetSpecType(v SpecType)`

SetSpecType sets SpecType field to given value.


### GetOverallTestStatus

`func (o *SpecificationRunSummary) GetOverallTestStatus() string`

GetOverallTestStatus returns the OverallTestStatus field if non-nil, zero value otherwise.

### GetOverallTestStatusOk

`func (o *SpecificationRunSummary) GetOverallTestStatusOk() (*string, bool)`

GetOverallTestStatusOk returns a tuple with the OverallTestStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOverallTestStatus

`func (o *SpecificationRunSummary) SetOverallTestStatus(v string)`

SetOverallTestStatus sets OverallTestStatus field to given value.


### GetStartedAt

`func (o *SpecificationRunSummary) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *SpecificationRunSummary) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *SpecificationRunSummary) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.


### GetFinishedAt

`func (o *SpecificationRunSummary) GetFinishedAt() time.Time`

GetFinishedAt returns the FinishedAt field if non-nil, zero value otherwise.

### GetFinishedAtOk

`func (o *SpecificationRunSummary) GetFinishedAtOk() (*time.Time, bool)`

GetFinishedAtOk returns a tuple with the FinishedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinishedAt

`func (o *SpecificationRunSummary) SetFinishedAt(v time.Time)`

SetFinishedAt sets FinishedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
