# BrowserVisualComparisonSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ComparisonId** | Pointer to **NullableString** |  | [optional]
**Status** | Pointer to [**BrowserVisualComparisonStatus**](BrowserVisualComparisonStatus.md) |  | [optional]
**DecisionStatus** | Pointer to [**BrowserVisualDecisionStatus**](BrowserVisualDecisionStatus.md) |  | [optional]
**ScopeType** | Pointer to [**BrowserVisualScopeType**](BrowserVisualScopeType.md) |  | [optional]
**CompareMode** | Pointer to [**BrowserVisualCompareMode**](BrowserVisualCompareMode.md) |  | [optional]
**StopPolicy** | Pointer to [**BrowserVisualStopPolicy**](BrowserVisualStopPolicy.md) |  | [optional]
**BaselineArtifactId** | Pointer to **NullableString** |  | [optional]
**ActualArtifactId** | Pointer to **NullableString** |  | [optional]
**DiffArtifactId** | Pointer to **NullableString** |  | [optional]
**DiffPixels** | Pointer to **NullableInt64** |  | [optional]
**DiffPixelRatio** | Pointer to **NullableFloat64** |  | [optional]
**Message** | Pointer to **NullableString** |  | [optional]
**ChangedDetails** | Pointer to **[]string** |  | [optional]
**ChangedRegions** | Pointer to [**[]BrowserVisualDiffRegion**](BrowserVisualDiffRegion.md) |  | [optional]
**AssertionRevision** | Pointer to **int64** |  | [optional]
**BaselineRevisionId** | Pointer to **NullableString** |  | [optional]
**GenerationNumber** | Pointer to **int32** |  | [optional]
**SourceComparisonId** | Pointer to **NullableString** |  | [optional]
**RootComparisonId** | Pointer to **NullableString** |  | [optional]
**ExcludedRegions** | Pointer to [**[]BrowserVisualExcludedRegion**](BrowserVisualExcludedRegion.md) |  | [optional]
**ChangedExcludedRegionIndexes** | Pointer to **[]int32** |  | [optional]

## Methods

### NewBrowserVisualComparisonSummary

`func NewBrowserVisualComparisonSummary() *BrowserVisualComparisonSummary`

NewBrowserVisualComparisonSummary instantiates a new BrowserVisualComparisonSummary object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserVisualComparisonSummaryWithDefaults

`func NewBrowserVisualComparisonSummaryWithDefaults() *BrowserVisualComparisonSummary`

NewBrowserVisualComparisonSummaryWithDefaults instantiates a new BrowserVisualComparisonSummary object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetComparisonId

`func (o *BrowserVisualComparisonSummary) GetComparisonId() string`

GetComparisonId returns the ComparisonId field if non-nil, zero value otherwise.

### GetComparisonIdOk

`func (o *BrowserVisualComparisonSummary) GetComparisonIdOk() (*string, bool)`

GetComparisonIdOk returns a tuple with the ComparisonId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComparisonId

`func (o *BrowserVisualComparisonSummary) SetComparisonId(v string)`

SetComparisonId sets ComparisonId field to given value.

### HasComparisonId

`func (o *BrowserVisualComparisonSummary) HasComparisonId() bool`

HasComparisonId returns a boolean if a field has been set.

### SetComparisonIdNil

`func (o *BrowserVisualComparisonSummary) SetComparisonIdNil(b bool)`

 SetComparisonIdNil sets the value for ComparisonId to be an explicit nil

### UnsetComparisonId
`func (o *BrowserVisualComparisonSummary) UnsetComparisonId()`

UnsetComparisonId ensures that no value is present for ComparisonId, not even an explicit nil
### GetStatus

`func (o *BrowserVisualComparisonSummary) GetStatus() BrowserVisualComparisonStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *BrowserVisualComparisonSummary) GetStatusOk() (*BrowserVisualComparisonStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *BrowserVisualComparisonSummary) SetStatus(v BrowserVisualComparisonStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *BrowserVisualComparisonSummary) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetDecisionStatus

`func (o *BrowserVisualComparisonSummary) GetDecisionStatus() BrowserVisualDecisionStatus`

GetDecisionStatus returns the DecisionStatus field if non-nil, zero value otherwise.

### GetDecisionStatusOk

`func (o *BrowserVisualComparisonSummary) GetDecisionStatusOk() (*BrowserVisualDecisionStatus, bool)`

GetDecisionStatusOk returns a tuple with the DecisionStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDecisionStatus

`func (o *BrowserVisualComparisonSummary) SetDecisionStatus(v BrowserVisualDecisionStatus)`

SetDecisionStatus sets DecisionStatus field to given value.

### HasDecisionStatus

`func (o *BrowserVisualComparisonSummary) HasDecisionStatus() bool`

HasDecisionStatus returns a boolean if a field has been set.

### GetScopeType

`func (o *BrowserVisualComparisonSummary) GetScopeType() BrowserVisualScopeType`

GetScopeType returns the ScopeType field if non-nil, zero value otherwise.

### GetScopeTypeOk

`func (o *BrowserVisualComparisonSummary) GetScopeTypeOk() (*BrowserVisualScopeType, bool)`

GetScopeTypeOk returns a tuple with the ScopeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopeType

`func (o *BrowserVisualComparisonSummary) SetScopeType(v BrowserVisualScopeType)`

SetScopeType sets ScopeType field to given value.

### HasScopeType

`func (o *BrowserVisualComparisonSummary) HasScopeType() bool`

HasScopeType returns a boolean if a field has been set.

### GetCompareMode

`func (o *BrowserVisualComparisonSummary) GetCompareMode() BrowserVisualCompareMode`

GetCompareMode returns the CompareMode field if non-nil, zero value otherwise.

### GetCompareModeOk

`func (o *BrowserVisualComparisonSummary) GetCompareModeOk() (*BrowserVisualCompareMode, bool)`

GetCompareModeOk returns a tuple with the CompareMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompareMode

`func (o *BrowserVisualComparisonSummary) SetCompareMode(v BrowserVisualCompareMode)`

SetCompareMode sets CompareMode field to given value.

### HasCompareMode

`func (o *BrowserVisualComparisonSummary) HasCompareMode() bool`

HasCompareMode returns a boolean if a field has been set.

### GetStopPolicy

`func (o *BrowserVisualComparisonSummary) GetStopPolicy() BrowserVisualStopPolicy`

GetStopPolicy returns the StopPolicy field if non-nil, zero value otherwise.

### GetStopPolicyOk

`func (o *BrowserVisualComparisonSummary) GetStopPolicyOk() (*BrowserVisualStopPolicy, bool)`

GetStopPolicyOk returns a tuple with the StopPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStopPolicy

`func (o *BrowserVisualComparisonSummary) SetStopPolicy(v BrowserVisualStopPolicy)`

SetStopPolicy sets StopPolicy field to given value.

### HasStopPolicy

`func (o *BrowserVisualComparisonSummary) HasStopPolicy() bool`

HasStopPolicy returns a boolean if a field has been set.

### GetBaselineArtifactId

`func (o *BrowserVisualComparisonSummary) GetBaselineArtifactId() string`

GetBaselineArtifactId returns the BaselineArtifactId field if non-nil, zero value otherwise.

### GetBaselineArtifactIdOk

`func (o *BrowserVisualComparisonSummary) GetBaselineArtifactIdOk() (*string, bool)`

GetBaselineArtifactIdOk returns a tuple with the BaselineArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaselineArtifactId

`func (o *BrowserVisualComparisonSummary) SetBaselineArtifactId(v string)`

SetBaselineArtifactId sets BaselineArtifactId field to given value.

### HasBaselineArtifactId

`func (o *BrowserVisualComparisonSummary) HasBaselineArtifactId() bool`

HasBaselineArtifactId returns a boolean if a field has been set.

### SetBaselineArtifactIdNil

`func (o *BrowserVisualComparisonSummary) SetBaselineArtifactIdNil(b bool)`

 SetBaselineArtifactIdNil sets the value for BaselineArtifactId to be an explicit nil

### UnsetBaselineArtifactId
`func (o *BrowserVisualComparisonSummary) UnsetBaselineArtifactId()`

UnsetBaselineArtifactId ensures that no value is present for BaselineArtifactId, not even an explicit nil
### GetActualArtifactId

`func (o *BrowserVisualComparisonSummary) GetActualArtifactId() string`

GetActualArtifactId returns the ActualArtifactId field if non-nil, zero value otherwise.

### GetActualArtifactIdOk

`func (o *BrowserVisualComparisonSummary) GetActualArtifactIdOk() (*string, bool)`

GetActualArtifactIdOk returns a tuple with the ActualArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActualArtifactId

`func (o *BrowserVisualComparisonSummary) SetActualArtifactId(v string)`

SetActualArtifactId sets ActualArtifactId field to given value.

### HasActualArtifactId

`func (o *BrowserVisualComparisonSummary) HasActualArtifactId() bool`

HasActualArtifactId returns a boolean if a field has been set.

### SetActualArtifactIdNil

`func (o *BrowserVisualComparisonSummary) SetActualArtifactIdNil(b bool)`

 SetActualArtifactIdNil sets the value for ActualArtifactId to be an explicit nil

### UnsetActualArtifactId
`func (o *BrowserVisualComparisonSummary) UnsetActualArtifactId()`

UnsetActualArtifactId ensures that no value is present for ActualArtifactId, not even an explicit nil
### GetDiffArtifactId

`func (o *BrowserVisualComparisonSummary) GetDiffArtifactId() string`

GetDiffArtifactId returns the DiffArtifactId field if non-nil, zero value otherwise.

### GetDiffArtifactIdOk

`func (o *BrowserVisualComparisonSummary) GetDiffArtifactIdOk() (*string, bool)`

GetDiffArtifactIdOk returns a tuple with the DiffArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiffArtifactId

`func (o *BrowserVisualComparisonSummary) SetDiffArtifactId(v string)`

SetDiffArtifactId sets DiffArtifactId field to given value.

### HasDiffArtifactId

`func (o *BrowserVisualComparisonSummary) HasDiffArtifactId() bool`

HasDiffArtifactId returns a boolean if a field has been set.

### SetDiffArtifactIdNil

`func (o *BrowserVisualComparisonSummary) SetDiffArtifactIdNil(b bool)`

 SetDiffArtifactIdNil sets the value for DiffArtifactId to be an explicit nil

### UnsetDiffArtifactId
`func (o *BrowserVisualComparisonSummary) UnsetDiffArtifactId()`

UnsetDiffArtifactId ensures that no value is present for DiffArtifactId, not even an explicit nil
### GetDiffPixels

`func (o *BrowserVisualComparisonSummary) GetDiffPixels() int64`

GetDiffPixels returns the DiffPixels field if non-nil, zero value otherwise.

### GetDiffPixelsOk

`func (o *BrowserVisualComparisonSummary) GetDiffPixelsOk() (*int64, bool)`

GetDiffPixelsOk returns a tuple with the DiffPixels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiffPixels

`func (o *BrowserVisualComparisonSummary) SetDiffPixels(v int64)`

SetDiffPixels sets DiffPixels field to given value.

### HasDiffPixels

`func (o *BrowserVisualComparisonSummary) HasDiffPixels() bool`

HasDiffPixels returns a boolean if a field has been set.

### SetDiffPixelsNil

`func (o *BrowserVisualComparisonSummary) SetDiffPixelsNil(b bool)`

 SetDiffPixelsNil sets the value for DiffPixels to be an explicit nil

### UnsetDiffPixels
`func (o *BrowserVisualComparisonSummary) UnsetDiffPixels()`

UnsetDiffPixels ensures that no value is present for DiffPixels, not even an explicit nil
### GetDiffPixelRatio

`func (o *BrowserVisualComparisonSummary) GetDiffPixelRatio() float64`

GetDiffPixelRatio returns the DiffPixelRatio field if non-nil, zero value otherwise.

### GetDiffPixelRatioOk

`func (o *BrowserVisualComparisonSummary) GetDiffPixelRatioOk() (*float64, bool)`

GetDiffPixelRatioOk returns a tuple with the DiffPixelRatio field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiffPixelRatio

`func (o *BrowserVisualComparisonSummary) SetDiffPixelRatio(v float64)`

SetDiffPixelRatio sets DiffPixelRatio field to given value.

### HasDiffPixelRatio

`func (o *BrowserVisualComparisonSummary) HasDiffPixelRatio() bool`

HasDiffPixelRatio returns a boolean if a field has been set.

### SetDiffPixelRatioNil

`func (o *BrowserVisualComparisonSummary) SetDiffPixelRatioNil(b bool)`

 SetDiffPixelRatioNil sets the value for DiffPixelRatio to be an explicit nil

### UnsetDiffPixelRatio
`func (o *BrowserVisualComparisonSummary) UnsetDiffPixelRatio()`

UnsetDiffPixelRatio ensures that no value is present for DiffPixelRatio, not even an explicit nil
### GetMessage

`func (o *BrowserVisualComparisonSummary) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *BrowserVisualComparisonSummary) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *BrowserVisualComparisonSummary) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *BrowserVisualComparisonSummary) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### SetMessageNil

`func (o *BrowserVisualComparisonSummary) SetMessageNil(b bool)`

 SetMessageNil sets the value for Message to be an explicit nil

### UnsetMessage
`func (o *BrowserVisualComparisonSummary) UnsetMessage()`

UnsetMessage ensures that no value is present for Message, not even an explicit nil
### GetChangedDetails

`func (o *BrowserVisualComparisonSummary) GetChangedDetails() []string`

GetChangedDetails returns the ChangedDetails field if non-nil, zero value otherwise.

### GetChangedDetailsOk

`func (o *BrowserVisualComparisonSummary) GetChangedDetailsOk() (*[]string, bool)`

GetChangedDetailsOk returns a tuple with the ChangedDetails field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangedDetails

`func (o *BrowserVisualComparisonSummary) SetChangedDetails(v []string)`

SetChangedDetails sets ChangedDetails field to given value.

### HasChangedDetails

`func (o *BrowserVisualComparisonSummary) HasChangedDetails() bool`

HasChangedDetails returns a boolean if a field has been set.

### GetChangedRegions

`func (o *BrowserVisualComparisonSummary) GetChangedRegions() []BrowserVisualDiffRegion`

GetChangedRegions returns the ChangedRegions field if non-nil, zero value otherwise.

### GetChangedRegionsOk

`func (o *BrowserVisualComparisonSummary) GetChangedRegionsOk() (*[]BrowserVisualDiffRegion, bool)`

GetChangedRegionsOk returns a tuple with the ChangedRegions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangedRegions

`func (o *BrowserVisualComparisonSummary) SetChangedRegions(v []BrowserVisualDiffRegion)`

SetChangedRegions sets ChangedRegions field to given value.

### HasChangedRegions

`func (o *BrowserVisualComparisonSummary) HasChangedRegions() bool`

HasChangedRegions returns a boolean if a field has been set.

### GetAssertionRevision

`func (o *BrowserVisualComparisonSummary) GetAssertionRevision() int64`

GetAssertionRevision returns the AssertionRevision field if non-nil, zero value otherwise.

### GetAssertionRevisionOk

`func (o *BrowserVisualComparisonSummary) GetAssertionRevisionOk() (*int64, bool)`

GetAssertionRevisionOk returns a tuple with the AssertionRevision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssertionRevision

`func (o *BrowserVisualComparisonSummary) SetAssertionRevision(v int64)`

SetAssertionRevision sets AssertionRevision field to given value.

### HasAssertionRevision

`func (o *BrowserVisualComparisonSummary) HasAssertionRevision() bool`

HasAssertionRevision returns a boolean if a field has been set.

### GetBaselineRevisionId

`func (o *BrowserVisualComparisonSummary) GetBaselineRevisionId() string`

GetBaselineRevisionId returns the BaselineRevisionId field if non-nil, zero value otherwise.

### GetBaselineRevisionIdOk

`func (o *BrowserVisualComparisonSummary) GetBaselineRevisionIdOk() (*string, bool)`

GetBaselineRevisionIdOk returns a tuple with the BaselineRevisionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaselineRevisionId

`func (o *BrowserVisualComparisonSummary) SetBaselineRevisionId(v string)`

SetBaselineRevisionId sets BaselineRevisionId field to given value.

### HasBaselineRevisionId

`func (o *BrowserVisualComparisonSummary) HasBaselineRevisionId() bool`

HasBaselineRevisionId returns a boolean if a field has been set.

### SetBaselineRevisionIdNil

`func (o *BrowserVisualComparisonSummary) SetBaselineRevisionIdNil(b bool)`

 SetBaselineRevisionIdNil sets the value for BaselineRevisionId to be an explicit nil

### UnsetBaselineRevisionId
`func (o *BrowserVisualComparisonSummary) UnsetBaselineRevisionId()`

UnsetBaselineRevisionId ensures that no value is present for BaselineRevisionId, not even an explicit nil
### GetGenerationNumber

`func (o *BrowserVisualComparisonSummary) GetGenerationNumber() int32`

GetGenerationNumber returns the GenerationNumber field if non-nil, zero value otherwise.

### GetGenerationNumberOk

`func (o *BrowserVisualComparisonSummary) GetGenerationNumberOk() (*int32, bool)`

GetGenerationNumberOk returns a tuple with the GenerationNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGenerationNumber

`func (o *BrowserVisualComparisonSummary) SetGenerationNumber(v int32)`

SetGenerationNumber sets GenerationNumber field to given value.

### HasGenerationNumber

`func (o *BrowserVisualComparisonSummary) HasGenerationNumber() bool`

HasGenerationNumber returns a boolean if a field has been set.

### GetSourceComparisonId

`func (o *BrowserVisualComparisonSummary) GetSourceComparisonId() string`

GetSourceComparisonId returns the SourceComparisonId field if non-nil, zero value otherwise.

### GetSourceComparisonIdOk

`func (o *BrowserVisualComparisonSummary) GetSourceComparisonIdOk() (*string, bool)`

GetSourceComparisonIdOk returns a tuple with the SourceComparisonId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceComparisonId

`func (o *BrowserVisualComparisonSummary) SetSourceComparisonId(v string)`

SetSourceComparisonId sets SourceComparisonId field to given value.

### HasSourceComparisonId

`func (o *BrowserVisualComparisonSummary) HasSourceComparisonId() bool`

HasSourceComparisonId returns a boolean if a field has been set.

### SetSourceComparisonIdNil

`func (o *BrowserVisualComparisonSummary) SetSourceComparisonIdNil(b bool)`

 SetSourceComparisonIdNil sets the value for SourceComparisonId to be an explicit nil

### UnsetSourceComparisonId
`func (o *BrowserVisualComparisonSummary) UnsetSourceComparisonId()`

UnsetSourceComparisonId ensures that no value is present for SourceComparisonId, not even an explicit nil
### GetRootComparisonId

`func (o *BrowserVisualComparisonSummary) GetRootComparisonId() string`

GetRootComparisonId returns the RootComparisonId field if non-nil, zero value otherwise.

### GetRootComparisonIdOk

`func (o *BrowserVisualComparisonSummary) GetRootComparisonIdOk() (*string, bool)`

GetRootComparisonIdOk returns a tuple with the RootComparisonId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRootComparisonId

`func (o *BrowserVisualComparisonSummary) SetRootComparisonId(v string)`

SetRootComparisonId sets RootComparisonId field to given value.

### HasRootComparisonId

`func (o *BrowserVisualComparisonSummary) HasRootComparisonId() bool`

HasRootComparisonId returns a boolean if a field has been set.

### SetRootComparisonIdNil

`func (o *BrowserVisualComparisonSummary) SetRootComparisonIdNil(b bool)`

 SetRootComparisonIdNil sets the value for RootComparisonId to be an explicit nil

### UnsetRootComparisonId
`func (o *BrowserVisualComparisonSummary) UnsetRootComparisonId()`

UnsetRootComparisonId ensures that no value is present for RootComparisonId, not even an explicit nil
### GetExcludedRegions

`func (o *BrowserVisualComparisonSummary) GetExcludedRegions() []BrowserVisualExcludedRegion`

GetExcludedRegions returns the ExcludedRegions field if non-nil, zero value otherwise.

### GetExcludedRegionsOk

`func (o *BrowserVisualComparisonSummary) GetExcludedRegionsOk() (*[]BrowserVisualExcludedRegion, bool)`

GetExcludedRegionsOk returns a tuple with the ExcludedRegions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludedRegions

`func (o *BrowserVisualComparisonSummary) SetExcludedRegions(v []BrowserVisualExcludedRegion)`

SetExcludedRegions sets ExcludedRegions field to given value.

### HasExcludedRegions

`func (o *BrowserVisualComparisonSummary) HasExcludedRegions() bool`

HasExcludedRegions returns a boolean if a field has been set.

### GetChangedExcludedRegionIndexes

`func (o *BrowserVisualComparisonSummary) GetChangedExcludedRegionIndexes() []int32`

GetChangedExcludedRegionIndexes returns the ChangedExcludedRegionIndexes field if non-nil, zero value otherwise.

### GetChangedExcludedRegionIndexesOk

`func (o *BrowserVisualComparisonSummary) GetChangedExcludedRegionIndexesOk() (*[]int32, bool)`

GetChangedExcludedRegionIndexesOk returns a tuple with the ChangedExcludedRegionIndexes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangedExcludedRegionIndexes

`func (o *BrowserVisualComparisonSummary) SetChangedExcludedRegionIndexes(v []int32)`

SetChangedExcludedRegionIndexes sets ChangedExcludedRegionIndexes field to given value.

### HasChangedExcludedRegionIndexes

`func (o *BrowserVisualComparisonSummary) HasChangedExcludedRegionIndexes() bool`

HasChangedExcludedRegionIndexes returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
