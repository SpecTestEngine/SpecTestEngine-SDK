# FlowRecoveryReview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Historical** | [**FlowRecoveryPreview**](FlowRecoveryPreview.md) |  |
**TargetRevision** | **int64** |  |
**TargetName** | Pointer to **NullableString** |  | [optional]
**TargetDescription** | Pointer to **NullableString** |  | [optional]
**DependencyRevisions** | **map[string]int64** |  |
**Occurrences** | [**[]FlowRecoveryOccurrence**](FlowRecoveryOccurrence.md) |  |
**RestoreAvailable** | **bool** |  |
**RestoreReason** | Pointer to **NullableString** |  | [optional]

## Methods

### NewFlowRecoveryReview

`func NewFlowRecoveryReview(historical FlowRecoveryPreview, targetRevision int64, dependencyRevisions map[string]int64, occurrences []FlowRecoveryOccurrence, restoreAvailable bool, ) *FlowRecoveryReview`

NewFlowRecoveryReview instantiates a new FlowRecoveryReview object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowRecoveryReviewWithDefaults

`func NewFlowRecoveryReviewWithDefaults() *FlowRecoveryReview`

NewFlowRecoveryReviewWithDefaults instantiates a new FlowRecoveryReview object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetHistorical

`func (o *FlowRecoveryReview) GetHistorical() FlowRecoveryPreview`

GetHistorical returns the Historical field if non-nil, zero value otherwise.

### GetHistoricalOk

`func (o *FlowRecoveryReview) GetHistoricalOk() (*FlowRecoveryPreview, bool)`

GetHistoricalOk returns a tuple with the Historical field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHistorical

`func (o *FlowRecoveryReview) SetHistorical(v FlowRecoveryPreview)`

SetHistorical sets Historical field to given value.


### GetTargetRevision

`func (o *FlowRecoveryReview) GetTargetRevision() int64`

GetTargetRevision returns the TargetRevision field if non-nil, zero value otherwise.

### GetTargetRevisionOk

`func (o *FlowRecoveryReview) GetTargetRevisionOk() (*int64, bool)`

GetTargetRevisionOk returns a tuple with the TargetRevision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetRevision

`func (o *FlowRecoveryReview) SetTargetRevision(v int64)`

SetTargetRevision sets TargetRevision field to given value.


### GetTargetName

`func (o *FlowRecoveryReview) GetTargetName() string`

GetTargetName returns the TargetName field if non-nil, zero value otherwise.

### GetTargetNameOk

`func (o *FlowRecoveryReview) GetTargetNameOk() (*string, bool)`

GetTargetNameOk returns a tuple with the TargetName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetName

`func (o *FlowRecoveryReview) SetTargetName(v string)`

SetTargetName sets TargetName field to given value.

### HasTargetName

`func (o *FlowRecoveryReview) HasTargetName() bool`

HasTargetName returns a boolean if a field has been set.

### SetTargetNameNil

`func (o *FlowRecoveryReview) SetTargetNameNil(b bool)`

 SetTargetNameNil sets the value for TargetName to be an explicit nil

### UnsetTargetName
`func (o *FlowRecoveryReview) UnsetTargetName()`

UnsetTargetName ensures that no value is present for TargetName, not even an explicit nil
### GetTargetDescription

`func (o *FlowRecoveryReview) GetTargetDescription() string`

GetTargetDescription returns the TargetDescription field if non-nil, zero value otherwise.

### GetTargetDescriptionOk

`func (o *FlowRecoveryReview) GetTargetDescriptionOk() (*string, bool)`

GetTargetDescriptionOk returns a tuple with the TargetDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetDescription

`func (o *FlowRecoveryReview) SetTargetDescription(v string)`

SetTargetDescription sets TargetDescription field to given value.

### HasTargetDescription

`func (o *FlowRecoveryReview) HasTargetDescription() bool`

HasTargetDescription returns a boolean if a field has been set.

### SetTargetDescriptionNil

`func (o *FlowRecoveryReview) SetTargetDescriptionNil(b bool)`

 SetTargetDescriptionNil sets the value for TargetDescription to be an explicit nil

### UnsetTargetDescription
`func (o *FlowRecoveryReview) UnsetTargetDescription()`

UnsetTargetDescription ensures that no value is present for TargetDescription, not even an explicit nil
### GetDependencyRevisions

`func (o *FlowRecoveryReview) GetDependencyRevisions() map[string]int64`

GetDependencyRevisions returns the DependencyRevisions field if non-nil, zero value otherwise.

### GetDependencyRevisionsOk

`func (o *FlowRecoveryReview) GetDependencyRevisionsOk() (*map[string]int64, bool)`

GetDependencyRevisionsOk returns a tuple with the DependencyRevisions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependencyRevisions

`func (o *FlowRecoveryReview) SetDependencyRevisions(v map[string]int64)`

SetDependencyRevisions sets DependencyRevisions field to given value.


### GetOccurrences

`func (o *FlowRecoveryReview) GetOccurrences() []FlowRecoveryOccurrence`

GetOccurrences returns the Occurrences field if non-nil, zero value otherwise.

### GetOccurrencesOk

`func (o *FlowRecoveryReview) GetOccurrencesOk() (*[]FlowRecoveryOccurrence, bool)`

GetOccurrencesOk returns a tuple with the Occurrences field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOccurrences

`func (o *FlowRecoveryReview) SetOccurrences(v []FlowRecoveryOccurrence)`

SetOccurrences sets Occurrences field to given value.


### GetRestoreAvailable

`func (o *FlowRecoveryReview) GetRestoreAvailable() bool`

GetRestoreAvailable returns the RestoreAvailable field if non-nil, zero value otherwise.

### GetRestoreAvailableOk

`func (o *FlowRecoveryReview) GetRestoreAvailableOk() (*bool, bool)`

GetRestoreAvailableOk returns a tuple with the RestoreAvailable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRestoreAvailable

`func (o *FlowRecoveryReview) SetRestoreAvailable(v bool)`

SetRestoreAvailable sets RestoreAvailable field to given value.


### GetRestoreReason

`func (o *FlowRecoveryReview) GetRestoreReason() string`

GetRestoreReason returns the RestoreReason field if non-nil, zero value otherwise.

### GetRestoreReasonOk

`func (o *FlowRecoveryReview) GetRestoreReasonOk() (*string, bool)`

GetRestoreReasonOk returns a tuple with the RestoreReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRestoreReason

`func (o *FlowRecoveryReview) SetRestoreReason(v string)`

SetRestoreReason sets RestoreReason field to given value.

### HasRestoreReason

`func (o *FlowRecoveryReview) HasRestoreReason() bool`

HasRestoreReason returns a boolean if a field has been set.

### SetRestoreReasonNil

`func (o *FlowRecoveryReview) SetRestoreReasonNil(b bool)`

 SetRestoreReasonNil sets the value for RestoreReason to be an explicit nil

### UnsetRestoreReason
`func (o *FlowRecoveryReview) UnsetRestoreReason()`

UnsetRestoreReason ensures that no value is present for RestoreReason, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
