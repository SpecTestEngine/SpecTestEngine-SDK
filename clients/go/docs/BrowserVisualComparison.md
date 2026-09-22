# BrowserVisualComparison

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ComparisonId** | **string** |  |
**Status** | [**BrowserVisualComparisonStatus**](BrowserVisualComparisonStatus.md) |  |
**DecisionStatus** | [**BrowserVisualDecisionStatus**](BrowserVisualDecisionStatus.md) |  |
**ScopeType** | [**BrowserVisualScopeType**](BrowserVisualScopeType.md) |  |
**CompareMode** | [**BrowserVisualCompareMode**](BrowserVisualCompareMode.md) |  |
**StopPolicy** | [**BrowserVisualStopPolicy**](BrowserVisualStopPolicy.md) |  |
**BaselineArtifactId** | Pointer to **NullableString** |  | [optional]
**ActualArtifactId** | Pointer to **NullableString** |  | [optional]
**DiffArtifactId** | Pointer to **NullableString** |  | [optional]
**DiffPixels** | Pointer to **NullableInt64** |  | [optional]
**DiffPixelRatio** | Pointer to **NullableFloat64** |  | [optional]
**Message** | Pointer to **NullableString** |  | [optional]
**ChangedDetails** | Pointer to **[]string** |  | [optional]
**ChangedRegions** | Pointer to [**[]BrowserVisualDiffRegion**](BrowserVisualDiffRegion.md) |  | [optional]
**CreatedAt** | **time.Time** |  |
**ReviewedAt** | Pointer to **NullableTime** |  | [optional]
**AssertionRevision** | **int64** |  |
**BaselineRevisionId** | Pointer to **NullableString** |  | [optional]
**AppliedBaselineRevisionId** | Pointer to **NullableString** |  | [optional]
**GenerationNumber** | **int32** |  |
**SourceComparisonId** | Pointer to **NullableString** |  | [optional]
**RootComparisonId** | **string** |  |
**ExcludedRegions** | [**[]BrowserVisualExcludedRegion**](BrowserVisualExcludedRegion.md) |  |
**ChangedExcludedRegionIndexes** | **[]int32** |  |
**ReviewCapabilities** | [**BrowserVisualReviewCapabilities**](BrowserVisualReviewCapabilities.md) |  |

## Methods

### NewBrowserVisualComparison

`func NewBrowserVisualComparison(comparisonId string, status BrowserVisualComparisonStatus, decisionStatus BrowserVisualDecisionStatus, scopeType BrowserVisualScopeType, compareMode BrowserVisualCompareMode, stopPolicy BrowserVisualStopPolicy, createdAt time.Time, assertionRevision int64, generationNumber int32, rootComparisonId string, excludedRegions []BrowserVisualExcludedRegion, changedExcludedRegionIndexes []int32, reviewCapabilities BrowserVisualReviewCapabilities, ) *BrowserVisualComparison`

NewBrowserVisualComparison instantiates a new BrowserVisualComparison object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserVisualComparisonWithDefaults

`func NewBrowserVisualComparisonWithDefaults() *BrowserVisualComparison`

NewBrowserVisualComparisonWithDefaults instantiates a new BrowserVisualComparison object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetComparisonId

`func (o *BrowserVisualComparison) GetComparisonId() string`

GetComparisonId returns the ComparisonId field if non-nil, zero value otherwise.

### GetComparisonIdOk

`func (o *BrowserVisualComparison) GetComparisonIdOk() (*string, bool)`

GetComparisonIdOk returns a tuple with the ComparisonId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComparisonId

`func (o *BrowserVisualComparison) SetComparisonId(v string)`

SetComparisonId sets ComparisonId field to given value.


### GetStatus

`func (o *BrowserVisualComparison) GetStatus() BrowserVisualComparisonStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *BrowserVisualComparison) GetStatusOk() (*BrowserVisualComparisonStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *BrowserVisualComparison) SetStatus(v BrowserVisualComparisonStatus)`

SetStatus sets Status field to given value.


### GetDecisionStatus

`func (o *BrowserVisualComparison) GetDecisionStatus() BrowserVisualDecisionStatus`

GetDecisionStatus returns the DecisionStatus field if non-nil, zero value otherwise.

### GetDecisionStatusOk

`func (o *BrowserVisualComparison) GetDecisionStatusOk() (*BrowserVisualDecisionStatus, bool)`

GetDecisionStatusOk returns a tuple with the DecisionStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDecisionStatus

`func (o *BrowserVisualComparison) SetDecisionStatus(v BrowserVisualDecisionStatus)`

SetDecisionStatus sets DecisionStatus field to given value.


### GetScopeType

`func (o *BrowserVisualComparison) GetScopeType() BrowserVisualScopeType`

GetScopeType returns the ScopeType field if non-nil, zero value otherwise.

### GetScopeTypeOk

`func (o *BrowserVisualComparison) GetScopeTypeOk() (*BrowserVisualScopeType, bool)`

GetScopeTypeOk returns a tuple with the ScopeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopeType

`func (o *BrowserVisualComparison) SetScopeType(v BrowserVisualScopeType)`

SetScopeType sets ScopeType field to given value.


### GetCompareMode

`func (o *BrowserVisualComparison) GetCompareMode() BrowserVisualCompareMode`

GetCompareMode returns the CompareMode field if non-nil, zero value otherwise.

### GetCompareModeOk

`func (o *BrowserVisualComparison) GetCompareModeOk() (*BrowserVisualCompareMode, bool)`

GetCompareModeOk returns a tuple with the CompareMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompareMode

`func (o *BrowserVisualComparison) SetCompareMode(v BrowserVisualCompareMode)`

SetCompareMode sets CompareMode field to given value.


### GetStopPolicy

`func (o *BrowserVisualComparison) GetStopPolicy() BrowserVisualStopPolicy`

GetStopPolicy returns the StopPolicy field if non-nil, zero value otherwise.

### GetStopPolicyOk

`func (o *BrowserVisualComparison) GetStopPolicyOk() (*BrowserVisualStopPolicy, bool)`

GetStopPolicyOk returns a tuple with the StopPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStopPolicy

`func (o *BrowserVisualComparison) SetStopPolicy(v BrowserVisualStopPolicy)`

SetStopPolicy sets StopPolicy field to given value.


### GetBaselineArtifactId

`func (o *BrowserVisualComparison) GetBaselineArtifactId() string`

GetBaselineArtifactId returns the BaselineArtifactId field if non-nil, zero value otherwise.

### GetBaselineArtifactIdOk

`func (o *BrowserVisualComparison) GetBaselineArtifactIdOk() (*string, bool)`

GetBaselineArtifactIdOk returns a tuple with the BaselineArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaselineArtifactId

`func (o *BrowserVisualComparison) SetBaselineArtifactId(v string)`

SetBaselineArtifactId sets BaselineArtifactId field to given value.

### HasBaselineArtifactId

`func (o *BrowserVisualComparison) HasBaselineArtifactId() bool`

HasBaselineArtifactId returns a boolean if a field has been set.

### SetBaselineArtifactIdNil

`func (o *BrowserVisualComparison) SetBaselineArtifactIdNil(b bool)`

 SetBaselineArtifactIdNil sets the value for BaselineArtifactId to be an explicit nil

### UnsetBaselineArtifactId
`func (o *BrowserVisualComparison) UnsetBaselineArtifactId()`

UnsetBaselineArtifactId ensures that no value is present for BaselineArtifactId, not even an explicit nil
### GetActualArtifactId

`func (o *BrowserVisualComparison) GetActualArtifactId() string`

GetActualArtifactId returns the ActualArtifactId field if non-nil, zero value otherwise.

### GetActualArtifactIdOk

`func (o *BrowserVisualComparison) GetActualArtifactIdOk() (*string, bool)`

GetActualArtifactIdOk returns a tuple with the ActualArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActualArtifactId

`func (o *BrowserVisualComparison) SetActualArtifactId(v string)`

SetActualArtifactId sets ActualArtifactId field to given value.

### HasActualArtifactId

`func (o *BrowserVisualComparison) HasActualArtifactId() bool`

HasActualArtifactId returns a boolean if a field has been set.

### SetActualArtifactIdNil

`func (o *BrowserVisualComparison) SetActualArtifactIdNil(b bool)`

 SetActualArtifactIdNil sets the value for ActualArtifactId to be an explicit nil

### UnsetActualArtifactId
`func (o *BrowserVisualComparison) UnsetActualArtifactId()`

UnsetActualArtifactId ensures that no value is present for ActualArtifactId, not even an explicit nil
### GetDiffArtifactId

`func (o *BrowserVisualComparison) GetDiffArtifactId() string`

GetDiffArtifactId returns the DiffArtifactId field if non-nil, zero value otherwise.

### GetDiffArtifactIdOk

`func (o *BrowserVisualComparison) GetDiffArtifactIdOk() (*string, bool)`

GetDiffArtifactIdOk returns a tuple with the DiffArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiffArtifactId

`func (o *BrowserVisualComparison) SetDiffArtifactId(v string)`

SetDiffArtifactId sets DiffArtifactId field to given value.

### HasDiffArtifactId

`func (o *BrowserVisualComparison) HasDiffArtifactId() bool`

HasDiffArtifactId returns a boolean if a field has been set.

### SetDiffArtifactIdNil

`func (o *BrowserVisualComparison) SetDiffArtifactIdNil(b bool)`

 SetDiffArtifactIdNil sets the value for DiffArtifactId to be an explicit nil

### UnsetDiffArtifactId
`func (o *BrowserVisualComparison) UnsetDiffArtifactId()`

UnsetDiffArtifactId ensures that no value is present for DiffArtifactId, not even an explicit nil
### GetDiffPixels

`func (o *BrowserVisualComparison) GetDiffPixels() int64`

GetDiffPixels returns the DiffPixels field if non-nil, zero value otherwise.

### GetDiffPixelsOk

`func (o *BrowserVisualComparison) GetDiffPixelsOk() (*int64, bool)`

GetDiffPixelsOk returns a tuple with the DiffPixels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiffPixels

`func (o *BrowserVisualComparison) SetDiffPixels(v int64)`

SetDiffPixels sets DiffPixels field to given value.

### HasDiffPixels

`func (o *BrowserVisualComparison) HasDiffPixels() bool`

HasDiffPixels returns a boolean if a field has been set.

### SetDiffPixelsNil

`func (o *BrowserVisualComparison) SetDiffPixelsNil(b bool)`

 SetDiffPixelsNil sets the value for DiffPixels to be an explicit nil

### UnsetDiffPixels
`func (o *BrowserVisualComparison) UnsetDiffPixels()`

UnsetDiffPixels ensures that no value is present for DiffPixels, not even an explicit nil
### GetDiffPixelRatio

`func (o *BrowserVisualComparison) GetDiffPixelRatio() float64`

GetDiffPixelRatio returns the DiffPixelRatio field if non-nil, zero value otherwise.

### GetDiffPixelRatioOk

`func (o *BrowserVisualComparison) GetDiffPixelRatioOk() (*float64, bool)`

GetDiffPixelRatioOk returns a tuple with the DiffPixelRatio field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiffPixelRatio

`func (o *BrowserVisualComparison) SetDiffPixelRatio(v float64)`

SetDiffPixelRatio sets DiffPixelRatio field to given value.

### HasDiffPixelRatio

`func (o *BrowserVisualComparison) HasDiffPixelRatio() bool`

HasDiffPixelRatio returns a boolean if a field has been set.

### SetDiffPixelRatioNil

`func (o *BrowserVisualComparison) SetDiffPixelRatioNil(b bool)`

 SetDiffPixelRatioNil sets the value for DiffPixelRatio to be an explicit nil

### UnsetDiffPixelRatio
`func (o *BrowserVisualComparison) UnsetDiffPixelRatio()`

UnsetDiffPixelRatio ensures that no value is present for DiffPixelRatio, not even an explicit nil
### GetMessage

`func (o *BrowserVisualComparison) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *BrowserVisualComparison) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *BrowserVisualComparison) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *BrowserVisualComparison) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### SetMessageNil

`func (o *BrowserVisualComparison) SetMessageNil(b bool)`

 SetMessageNil sets the value for Message to be an explicit nil

### UnsetMessage
`func (o *BrowserVisualComparison) UnsetMessage()`

UnsetMessage ensures that no value is present for Message, not even an explicit nil
### GetChangedDetails

`func (o *BrowserVisualComparison) GetChangedDetails() []string`

GetChangedDetails returns the ChangedDetails field if non-nil, zero value otherwise.

### GetChangedDetailsOk

`func (o *BrowserVisualComparison) GetChangedDetailsOk() (*[]string, bool)`

GetChangedDetailsOk returns a tuple with the ChangedDetails field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangedDetails

`func (o *BrowserVisualComparison) SetChangedDetails(v []string)`

SetChangedDetails sets ChangedDetails field to given value.

### HasChangedDetails

`func (o *BrowserVisualComparison) HasChangedDetails() bool`

HasChangedDetails returns a boolean if a field has been set.

### GetChangedRegions

`func (o *BrowserVisualComparison) GetChangedRegions() []BrowserVisualDiffRegion`

GetChangedRegions returns the ChangedRegions field if non-nil, zero value otherwise.

### GetChangedRegionsOk

`func (o *BrowserVisualComparison) GetChangedRegionsOk() (*[]BrowserVisualDiffRegion, bool)`

GetChangedRegionsOk returns a tuple with the ChangedRegions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangedRegions

`func (o *BrowserVisualComparison) SetChangedRegions(v []BrowserVisualDiffRegion)`

SetChangedRegions sets ChangedRegions field to given value.

### HasChangedRegions

`func (o *BrowserVisualComparison) HasChangedRegions() bool`

HasChangedRegions returns a boolean if a field has been set.

### GetCreatedAt

`func (o *BrowserVisualComparison) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *BrowserVisualComparison) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *BrowserVisualComparison) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetReviewedAt

`func (o *BrowserVisualComparison) GetReviewedAt() time.Time`

GetReviewedAt returns the ReviewedAt field if non-nil, zero value otherwise.

### GetReviewedAtOk

`func (o *BrowserVisualComparison) GetReviewedAtOk() (*time.Time, bool)`

GetReviewedAtOk returns a tuple with the ReviewedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewedAt

`func (o *BrowserVisualComparison) SetReviewedAt(v time.Time)`

SetReviewedAt sets ReviewedAt field to given value.

### HasReviewedAt

`func (o *BrowserVisualComparison) HasReviewedAt() bool`

HasReviewedAt returns a boolean if a field has been set.

### SetReviewedAtNil

`func (o *BrowserVisualComparison) SetReviewedAtNil(b bool)`

 SetReviewedAtNil sets the value for ReviewedAt to be an explicit nil

### UnsetReviewedAt
`func (o *BrowserVisualComparison) UnsetReviewedAt()`

UnsetReviewedAt ensures that no value is present for ReviewedAt, not even an explicit nil
### GetAssertionRevision

`func (o *BrowserVisualComparison) GetAssertionRevision() int64`

GetAssertionRevision returns the AssertionRevision field if non-nil, zero value otherwise.

### GetAssertionRevisionOk

`func (o *BrowserVisualComparison) GetAssertionRevisionOk() (*int64, bool)`

GetAssertionRevisionOk returns a tuple with the AssertionRevision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssertionRevision

`func (o *BrowserVisualComparison) SetAssertionRevision(v int64)`

SetAssertionRevision sets AssertionRevision field to given value.


### GetBaselineRevisionId

`func (o *BrowserVisualComparison) GetBaselineRevisionId() string`

GetBaselineRevisionId returns the BaselineRevisionId field if non-nil, zero value otherwise.

### GetBaselineRevisionIdOk

`func (o *BrowserVisualComparison) GetBaselineRevisionIdOk() (*string, bool)`

GetBaselineRevisionIdOk returns a tuple with the BaselineRevisionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaselineRevisionId

`func (o *BrowserVisualComparison) SetBaselineRevisionId(v string)`

SetBaselineRevisionId sets BaselineRevisionId field to given value.

### HasBaselineRevisionId

`func (o *BrowserVisualComparison) HasBaselineRevisionId() bool`

HasBaselineRevisionId returns a boolean if a field has been set.

### SetBaselineRevisionIdNil

`func (o *BrowserVisualComparison) SetBaselineRevisionIdNil(b bool)`

 SetBaselineRevisionIdNil sets the value for BaselineRevisionId to be an explicit nil

### UnsetBaselineRevisionId
`func (o *BrowserVisualComparison) UnsetBaselineRevisionId()`

UnsetBaselineRevisionId ensures that no value is present for BaselineRevisionId, not even an explicit nil
### GetAppliedBaselineRevisionId

`func (o *BrowserVisualComparison) GetAppliedBaselineRevisionId() string`

GetAppliedBaselineRevisionId returns the AppliedBaselineRevisionId field if non-nil, zero value otherwise.

### GetAppliedBaselineRevisionIdOk

`func (o *BrowserVisualComparison) GetAppliedBaselineRevisionIdOk() (*string, bool)`

GetAppliedBaselineRevisionIdOk returns a tuple with the AppliedBaselineRevisionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAppliedBaselineRevisionId

`func (o *BrowserVisualComparison) SetAppliedBaselineRevisionId(v string)`

SetAppliedBaselineRevisionId sets AppliedBaselineRevisionId field to given value.

### HasAppliedBaselineRevisionId

`func (o *BrowserVisualComparison) HasAppliedBaselineRevisionId() bool`

HasAppliedBaselineRevisionId returns a boolean if a field has been set.

### SetAppliedBaselineRevisionIdNil

`func (o *BrowserVisualComparison) SetAppliedBaselineRevisionIdNil(b bool)`

 SetAppliedBaselineRevisionIdNil sets the value for AppliedBaselineRevisionId to be an explicit nil

### UnsetAppliedBaselineRevisionId
`func (o *BrowserVisualComparison) UnsetAppliedBaselineRevisionId()`

UnsetAppliedBaselineRevisionId ensures that no value is present for AppliedBaselineRevisionId, not even an explicit nil
### GetGenerationNumber

`func (o *BrowserVisualComparison) GetGenerationNumber() int32`

GetGenerationNumber returns the GenerationNumber field if non-nil, zero value otherwise.

### GetGenerationNumberOk

`func (o *BrowserVisualComparison) GetGenerationNumberOk() (*int32, bool)`

GetGenerationNumberOk returns a tuple with the GenerationNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGenerationNumber

`func (o *BrowserVisualComparison) SetGenerationNumber(v int32)`

SetGenerationNumber sets GenerationNumber field to given value.


### GetSourceComparisonId

`func (o *BrowserVisualComparison) GetSourceComparisonId() string`

GetSourceComparisonId returns the SourceComparisonId field if non-nil, zero value otherwise.

### GetSourceComparisonIdOk

`func (o *BrowserVisualComparison) GetSourceComparisonIdOk() (*string, bool)`

GetSourceComparisonIdOk returns a tuple with the SourceComparisonId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceComparisonId

`func (o *BrowserVisualComparison) SetSourceComparisonId(v string)`

SetSourceComparisonId sets SourceComparisonId field to given value.

### HasSourceComparisonId

`func (o *BrowserVisualComparison) HasSourceComparisonId() bool`

HasSourceComparisonId returns a boolean if a field has been set.

### SetSourceComparisonIdNil

`func (o *BrowserVisualComparison) SetSourceComparisonIdNil(b bool)`

 SetSourceComparisonIdNil sets the value for SourceComparisonId to be an explicit nil

### UnsetSourceComparisonId
`func (o *BrowserVisualComparison) UnsetSourceComparisonId()`

UnsetSourceComparisonId ensures that no value is present for SourceComparisonId, not even an explicit nil
### GetRootComparisonId

`func (o *BrowserVisualComparison) GetRootComparisonId() string`

GetRootComparisonId returns the RootComparisonId field if non-nil, zero value otherwise.

### GetRootComparisonIdOk

`func (o *BrowserVisualComparison) GetRootComparisonIdOk() (*string, bool)`

GetRootComparisonIdOk returns a tuple with the RootComparisonId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRootComparisonId

`func (o *BrowserVisualComparison) SetRootComparisonId(v string)`

SetRootComparisonId sets RootComparisonId field to given value.


### GetExcludedRegions

`func (o *BrowserVisualComparison) GetExcludedRegions() []BrowserVisualExcludedRegion`

GetExcludedRegions returns the ExcludedRegions field if non-nil, zero value otherwise.

### GetExcludedRegionsOk

`func (o *BrowserVisualComparison) GetExcludedRegionsOk() (*[]BrowserVisualExcludedRegion, bool)`

GetExcludedRegionsOk returns a tuple with the ExcludedRegions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludedRegions

`func (o *BrowserVisualComparison) SetExcludedRegions(v []BrowserVisualExcludedRegion)`

SetExcludedRegions sets ExcludedRegions field to given value.


### GetChangedExcludedRegionIndexes

`func (o *BrowserVisualComparison) GetChangedExcludedRegionIndexes() []int32`

GetChangedExcludedRegionIndexes returns the ChangedExcludedRegionIndexes field if non-nil, zero value otherwise.

### GetChangedExcludedRegionIndexesOk

`func (o *BrowserVisualComparison) GetChangedExcludedRegionIndexesOk() (*[]int32, bool)`

GetChangedExcludedRegionIndexesOk returns a tuple with the ChangedExcludedRegionIndexes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangedExcludedRegionIndexes

`func (o *BrowserVisualComparison) SetChangedExcludedRegionIndexes(v []int32)`

SetChangedExcludedRegionIndexes sets ChangedExcludedRegionIndexes field to given value.


### GetReviewCapabilities

`func (o *BrowserVisualComparison) GetReviewCapabilities() BrowserVisualReviewCapabilities`

GetReviewCapabilities returns the ReviewCapabilities field if non-nil, zero value otherwise.

### GetReviewCapabilitiesOk

`func (o *BrowserVisualComparison) GetReviewCapabilitiesOk() (*BrowserVisualReviewCapabilities, bool)`

GetReviewCapabilitiesOk returns a tuple with the ReviewCapabilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewCapabilities

`func (o *BrowserVisualComparison) SetReviewCapabilities(v BrowserVisualReviewCapabilities)`

SetReviewCapabilities sets ReviewCapabilities field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


