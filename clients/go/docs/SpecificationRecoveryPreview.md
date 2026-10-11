# SpecificationRecoveryPreview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SpecId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SpecName** | **string** |  |
**SpecType** | [**SpecType**](SpecType.md) |  |
**CurrentSpec** | **map[string]interface{}** |  |
**RecoveredSpec** | **map[string]interface{}** |  |
**CurrentRawSpec** | **string** |  |
**RecoveredRawSpec** | **string** |  |
**SourceRunId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SourceRunStatus** | **string** | Completed passing or assertion-failing status as retained by the owning engine. |
**Changes** | [**[]SpecificationRecoveryChange**](SpecificationRecoveryChange.md) |  |

## Methods

### NewSpecificationRecoveryPreview

`func NewSpecificationRecoveryPreview(specId string, specName string, specType SpecType, currentSpec map[string]interface{}, recoveredSpec map[string]interface{}, currentRawSpec string, recoveredRawSpec string, sourceRunId string, sourceRunStatus string, changes []SpecificationRecoveryChange, ) *SpecificationRecoveryPreview`

NewSpecificationRecoveryPreview instantiates a new SpecificationRecoveryPreview object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSpecificationRecoveryPreviewWithDefaults

`func NewSpecificationRecoveryPreviewWithDefaults() *SpecificationRecoveryPreview`

NewSpecificationRecoveryPreviewWithDefaults instantiates a new SpecificationRecoveryPreview object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSpecId

`func (o *SpecificationRecoveryPreview) GetSpecId() string`

GetSpecId returns the SpecId field if non-nil, zero value otherwise.

### GetSpecIdOk

`func (o *SpecificationRecoveryPreview) GetSpecIdOk() (*string, bool)`

GetSpecIdOk returns a tuple with the SpecId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecId

`func (o *SpecificationRecoveryPreview) SetSpecId(v string)`

SetSpecId sets SpecId field to given value.


### GetSpecName

`func (o *SpecificationRecoveryPreview) GetSpecName() string`

GetSpecName returns the SpecName field if non-nil, zero value otherwise.

### GetSpecNameOk

`func (o *SpecificationRecoveryPreview) GetSpecNameOk() (*string, bool)`

GetSpecNameOk returns a tuple with the SpecName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecName

`func (o *SpecificationRecoveryPreview) SetSpecName(v string)`

SetSpecName sets SpecName field to given value.


### GetSpecType

`func (o *SpecificationRecoveryPreview) GetSpecType() SpecType`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *SpecificationRecoveryPreview) GetSpecTypeOk() (*SpecType, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *SpecificationRecoveryPreview) SetSpecType(v SpecType)`

SetSpecType sets SpecType field to given value.


### GetCurrentSpec

`func (o *SpecificationRecoveryPreview) GetCurrentSpec() map[string]interface{}`

GetCurrentSpec returns the CurrentSpec field if non-nil, zero value otherwise.

### GetCurrentSpecOk

`func (o *SpecificationRecoveryPreview) GetCurrentSpecOk() (*map[string]interface{}, bool)`

GetCurrentSpecOk returns a tuple with the CurrentSpec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentSpec

`func (o *SpecificationRecoveryPreview) SetCurrentSpec(v map[string]interface{})`

SetCurrentSpec sets CurrentSpec field to given value.


### GetRecoveredSpec

`func (o *SpecificationRecoveryPreview) GetRecoveredSpec() map[string]interface{}`

GetRecoveredSpec returns the RecoveredSpec field if non-nil, zero value otherwise.

### GetRecoveredSpecOk

`func (o *SpecificationRecoveryPreview) GetRecoveredSpecOk() (*map[string]interface{}, bool)`

GetRecoveredSpecOk returns a tuple with the RecoveredSpec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecoveredSpec

`func (o *SpecificationRecoveryPreview) SetRecoveredSpec(v map[string]interface{})`

SetRecoveredSpec sets RecoveredSpec field to given value.


### GetCurrentRawSpec

`func (o *SpecificationRecoveryPreview) GetCurrentRawSpec() string`

GetCurrentRawSpec returns the CurrentRawSpec field if non-nil, zero value otherwise.

### GetCurrentRawSpecOk

`func (o *SpecificationRecoveryPreview) GetCurrentRawSpecOk() (*string, bool)`

GetCurrentRawSpecOk returns a tuple with the CurrentRawSpec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentRawSpec

`func (o *SpecificationRecoveryPreview) SetCurrentRawSpec(v string)`

SetCurrentRawSpec sets CurrentRawSpec field to given value.


### GetRecoveredRawSpec

`func (o *SpecificationRecoveryPreview) GetRecoveredRawSpec() string`

GetRecoveredRawSpec returns the RecoveredRawSpec field if non-nil, zero value otherwise.

### GetRecoveredRawSpecOk

`func (o *SpecificationRecoveryPreview) GetRecoveredRawSpecOk() (*string, bool)`

GetRecoveredRawSpecOk returns a tuple with the RecoveredRawSpec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecoveredRawSpec

`func (o *SpecificationRecoveryPreview) SetRecoveredRawSpec(v string)`

SetRecoveredRawSpec sets RecoveredRawSpec field to given value.


### GetSourceRunId

`func (o *SpecificationRecoveryPreview) GetSourceRunId() string`

GetSourceRunId returns the SourceRunId field if non-nil, zero value otherwise.

### GetSourceRunIdOk

`func (o *SpecificationRecoveryPreview) GetSourceRunIdOk() (*string, bool)`

GetSourceRunIdOk returns a tuple with the SourceRunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceRunId

`func (o *SpecificationRecoveryPreview) SetSourceRunId(v string)`

SetSourceRunId sets SourceRunId field to given value.


### GetSourceRunStatus

`func (o *SpecificationRecoveryPreview) GetSourceRunStatus() string`

GetSourceRunStatus returns the SourceRunStatus field if non-nil, zero value otherwise.

### GetSourceRunStatusOk

`func (o *SpecificationRecoveryPreview) GetSourceRunStatusOk() (*string, bool)`

GetSourceRunStatusOk returns a tuple with the SourceRunStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceRunStatus

`func (o *SpecificationRecoveryPreview) SetSourceRunStatus(v string)`

SetSourceRunStatus sets SourceRunStatus field to given value.


### GetChanges

`func (o *SpecificationRecoveryPreview) GetChanges() []SpecificationRecoveryChange`

GetChanges returns the Changes field if non-nil, zero value otherwise.

### GetChangesOk

`func (o *SpecificationRecoveryPreview) GetChangesOk() (*[]SpecificationRecoveryChange, bool)`

GetChangesOk returns a tuple with the Changes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChanges

`func (o *SpecificationRecoveryPreview) SetChanges(v []SpecificationRecoveryChange)`

SetChanges sets Changes field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
