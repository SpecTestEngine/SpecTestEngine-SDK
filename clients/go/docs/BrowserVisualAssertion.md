# BrowserVisualAssertion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | **bool** |  |
**Name** | Pointer to **NullableString** |  | [optional]
**ScopeType** | Pointer to [**BrowserVisualScopeType**](BrowserVisualScopeType.md) |  | [optional]
**CompareMode** | Pointer to [**BrowserVisualCompareMode**](BrowserVisualCompareMode.md) |  | [optional]
**StopPolicy** | Pointer to [**BrowserVisualStopPolicy**](BrowserVisualStopPolicy.md) |  | [optional]
**BaselineArtifactId** | Pointer to **NullableString** |  | [optional]
**BaselineRevisionId** | Pointer to **NullableString** |  | [optional]
**AssertionRevision** | **int64** |  |
**MaxDiffPixels** | Pointer to **NullableInt64** |  | [optional]
**MaxDiffPixelRatio** | Pointer to **NullableFloat64** |  | [optional]
**ColorThreshold** | Pointer to **NullableFloat64** |  | [optional]
**MoveTolerancePx** | Pointer to **NullableFloat64** |  | [optional]
**Bounds** | Pointer to [**NullableBrowserVisualBounds**](BrowserVisualBounds.md) |  | [optional]
**ExcludedRegions** | [**[]BrowserVisualExcludedRegion**](BrowserVisualExcludedRegion.md) |  |

## Methods

### NewBrowserVisualAssertion

`func NewBrowserVisualAssertion(enabled bool, assertionRevision int64, excludedRegions []BrowserVisualExcludedRegion, ) *BrowserVisualAssertion`

NewBrowserVisualAssertion instantiates a new BrowserVisualAssertion object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserVisualAssertionWithDefaults

`func NewBrowserVisualAssertionWithDefaults() *BrowserVisualAssertion`

NewBrowserVisualAssertionWithDefaults instantiates a new BrowserVisualAssertion object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnabled

`func (o *BrowserVisualAssertion) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *BrowserVisualAssertion) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *BrowserVisualAssertion) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.


### GetName

`func (o *BrowserVisualAssertion) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *BrowserVisualAssertion) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *BrowserVisualAssertion) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *BrowserVisualAssertion) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *BrowserVisualAssertion) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *BrowserVisualAssertion) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetScopeType

`func (o *BrowserVisualAssertion) GetScopeType() BrowserVisualScopeType`

GetScopeType returns the ScopeType field if non-nil, zero value otherwise.

### GetScopeTypeOk

`func (o *BrowserVisualAssertion) GetScopeTypeOk() (*BrowserVisualScopeType, bool)`

GetScopeTypeOk returns a tuple with the ScopeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopeType

`func (o *BrowserVisualAssertion) SetScopeType(v BrowserVisualScopeType)`

SetScopeType sets ScopeType field to given value.

### HasScopeType

`func (o *BrowserVisualAssertion) HasScopeType() bool`

HasScopeType returns a boolean if a field has been set.

### GetCompareMode

`func (o *BrowserVisualAssertion) GetCompareMode() BrowserVisualCompareMode`

GetCompareMode returns the CompareMode field if non-nil, zero value otherwise.

### GetCompareModeOk

`func (o *BrowserVisualAssertion) GetCompareModeOk() (*BrowserVisualCompareMode, bool)`

GetCompareModeOk returns a tuple with the CompareMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompareMode

`func (o *BrowserVisualAssertion) SetCompareMode(v BrowserVisualCompareMode)`

SetCompareMode sets CompareMode field to given value.

### HasCompareMode

`func (o *BrowserVisualAssertion) HasCompareMode() bool`

HasCompareMode returns a boolean if a field has been set.

### GetStopPolicy

`func (o *BrowserVisualAssertion) GetStopPolicy() BrowserVisualStopPolicy`

GetStopPolicy returns the StopPolicy field if non-nil, zero value otherwise.

### GetStopPolicyOk

`func (o *BrowserVisualAssertion) GetStopPolicyOk() (*BrowserVisualStopPolicy, bool)`

GetStopPolicyOk returns a tuple with the StopPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStopPolicy

`func (o *BrowserVisualAssertion) SetStopPolicy(v BrowserVisualStopPolicy)`

SetStopPolicy sets StopPolicy field to given value.

### HasStopPolicy

`func (o *BrowserVisualAssertion) HasStopPolicy() bool`

HasStopPolicy returns a boolean if a field has been set.

### GetBaselineArtifactId

`func (o *BrowserVisualAssertion) GetBaselineArtifactId() string`

GetBaselineArtifactId returns the BaselineArtifactId field if non-nil, zero value otherwise.

### GetBaselineArtifactIdOk

`func (o *BrowserVisualAssertion) GetBaselineArtifactIdOk() (*string, bool)`

GetBaselineArtifactIdOk returns a tuple with the BaselineArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaselineArtifactId

`func (o *BrowserVisualAssertion) SetBaselineArtifactId(v string)`

SetBaselineArtifactId sets BaselineArtifactId field to given value.

### HasBaselineArtifactId

`func (o *BrowserVisualAssertion) HasBaselineArtifactId() bool`

HasBaselineArtifactId returns a boolean if a field has been set.

### SetBaselineArtifactIdNil

`func (o *BrowserVisualAssertion) SetBaselineArtifactIdNil(b bool)`

 SetBaselineArtifactIdNil sets the value for BaselineArtifactId to be an explicit nil

### UnsetBaselineArtifactId
`func (o *BrowserVisualAssertion) UnsetBaselineArtifactId()`

UnsetBaselineArtifactId ensures that no value is present for BaselineArtifactId, not even an explicit nil
### GetBaselineRevisionId

`func (o *BrowserVisualAssertion) GetBaselineRevisionId() string`

GetBaselineRevisionId returns the BaselineRevisionId field if non-nil, zero value otherwise.

### GetBaselineRevisionIdOk

`func (o *BrowserVisualAssertion) GetBaselineRevisionIdOk() (*string, bool)`

GetBaselineRevisionIdOk returns a tuple with the BaselineRevisionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaselineRevisionId

`func (o *BrowserVisualAssertion) SetBaselineRevisionId(v string)`

SetBaselineRevisionId sets BaselineRevisionId field to given value.

### HasBaselineRevisionId

`func (o *BrowserVisualAssertion) HasBaselineRevisionId() bool`

HasBaselineRevisionId returns a boolean if a field has been set.

### SetBaselineRevisionIdNil

`func (o *BrowserVisualAssertion) SetBaselineRevisionIdNil(b bool)`

 SetBaselineRevisionIdNil sets the value for BaselineRevisionId to be an explicit nil

### UnsetBaselineRevisionId
`func (o *BrowserVisualAssertion) UnsetBaselineRevisionId()`

UnsetBaselineRevisionId ensures that no value is present for BaselineRevisionId, not even an explicit nil
### GetAssertionRevision

`func (o *BrowserVisualAssertion) GetAssertionRevision() int64`

GetAssertionRevision returns the AssertionRevision field if non-nil, zero value otherwise.

### GetAssertionRevisionOk

`func (o *BrowserVisualAssertion) GetAssertionRevisionOk() (*int64, bool)`

GetAssertionRevisionOk returns a tuple with the AssertionRevision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssertionRevision

`func (o *BrowserVisualAssertion) SetAssertionRevision(v int64)`

SetAssertionRevision sets AssertionRevision field to given value.


### GetMaxDiffPixels

`func (o *BrowserVisualAssertion) GetMaxDiffPixels() int64`

GetMaxDiffPixels returns the MaxDiffPixels field if non-nil, zero value otherwise.

### GetMaxDiffPixelsOk

`func (o *BrowserVisualAssertion) GetMaxDiffPixelsOk() (*int64, bool)`

GetMaxDiffPixelsOk returns a tuple with the MaxDiffPixels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxDiffPixels

`func (o *BrowserVisualAssertion) SetMaxDiffPixels(v int64)`

SetMaxDiffPixels sets MaxDiffPixels field to given value.

### HasMaxDiffPixels

`func (o *BrowserVisualAssertion) HasMaxDiffPixels() bool`

HasMaxDiffPixels returns a boolean if a field has been set.

### SetMaxDiffPixelsNil

`func (o *BrowserVisualAssertion) SetMaxDiffPixelsNil(b bool)`

 SetMaxDiffPixelsNil sets the value for MaxDiffPixels to be an explicit nil

### UnsetMaxDiffPixels
`func (o *BrowserVisualAssertion) UnsetMaxDiffPixels()`

UnsetMaxDiffPixels ensures that no value is present for MaxDiffPixels, not even an explicit nil
### GetMaxDiffPixelRatio

`func (o *BrowserVisualAssertion) GetMaxDiffPixelRatio() float64`

GetMaxDiffPixelRatio returns the MaxDiffPixelRatio field if non-nil, zero value otherwise.

### GetMaxDiffPixelRatioOk

`func (o *BrowserVisualAssertion) GetMaxDiffPixelRatioOk() (*float64, bool)`

GetMaxDiffPixelRatioOk returns a tuple with the MaxDiffPixelRatio field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxDiffPixelRatio

`func (o *BrowserVisualAssertion) SetMaxDiffPixelRatio(v float64)`

SetMaxDiffPixelRatio sets MaxDiffPixelRatio field to given value.

### HasMaxDiffPixelRatio

`func (o *BrowserVisualAssertion) HasMaxDiffPixelRatio() bool`

HasMaxDiffPixelRatio returns a boolean if a field has been set.

### SetMaxDiffPixelRatioNil

`func (o *BrowserVisualAssertion) SetMaxDiffPixelRatioNil(b bool)`

 SetMaxDiffPixelRatioNil sets the value for MaxDiffPixelRatio to be an explicit nil

### UnsetMaxDiffPixelRatio
`func (o *BrowserVisualAssertion) UnsetMaxDiffPixelRatio()`

UnsetMaxDiffPixelRatio ensures that no value is present for MaxDiffPixelRatio, not even an explicit nil
### GetColorThreshold

`func (o *BrowserVisualAssertion) GetColorThreshold() float64`

GetColorThreshold returns the ColorThreshold field if non-nil, zero value otherwise.

### GetColorThresholdOk

`func (o *BrowserVisualAssertion) GetColorThresholdOk() (*float64, bool)`

GetColorThresholdOk returns a tuple with the ColorThreshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColorThreshold

`func (o *BrowserVisualAssertion) SetColorThreshold(v float64)`

SetColorThreshold sets ColorThreshold field to given value.

### HasColorThreshold

`func (o *BrowserVisualAssertion) HasColorThreshold() bool`

HasColorThreshold returns a boolean if a field has been set.

### SetColorThresholdNil

`func (o *BrowserVisualAssertion) SetColorThresholdNil(b bool)`

 SetColorThresholdNil sets the value for ColorThreshold to be an explicit nil

### UnsetColorThreshold
`func (o *BrowserVisualAssertion) UnsetColorThreshold()`

UnsetColorThreshold ensures that no value is present for ColorThreshold, not even an explicit nil
### GetMoveTolerancePx

`func (o *BrowserVisualAssertion) GetMoveTolerancePx() float64`

GetMoveTolerancePx returns the MoveTolerancePx field if non-nil, zero value otherwise.

### GetMoveTolerancePxOk

`func (o *BrowserVisualAssertion) GetMoveTolerancePxOk() (*float64, bool)`

GetMoveTolerancePxOk returns a tuple with the MoveTolerancePx field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMoveTolerancePx

`func (o *BrowserVisualAssertion) SetMoveTolerancePx(v float64)`

SetMoveTolerancePx sets MoveTolerancePx field to given value.

### HasMoveTolerancePx

`func (o *BrowserVisualAssertion) HasMoveTolerancePx() bool`

HasMoveTolerancePx returns a boolean if a field has been set.

### SetMoveTolerancePxNil

`func (o *BrowserVisualAssertion) SetMoveTolerancePxNil(b bool)`

 SetMoveTolerancePxNil sets the value for MoveTolerancePx to be an explicit nil

### UnsetMoveTolerancePx
`func (o *BrowserVisualAssertion) UnsetMoveTolerancePx()`

UnsetMoveTolerancePx ensures that no value is present for MoveTolerancePx, not even an explicit nil
### GetBounds

`func (o *BrowserVisualAssertion) GetBounds() BrowserVisualBounds`

GetBounds returns the Bounds field if non-nil, zero value otherwise.

### GetBoundsOk

`func (o *BrowserVisualAssertion) GetBoundsOk() (*BrowserVisualBounds, bool)`

GetBoundsOk returns a tuple with the Bounds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBounds

`func (o *BrowserVisualAssertion) SetBounds(v BrowserVisualBounds)`

SetBounds sets Bounds field to given value.

### HasBounds

`func (o *BrowserVisualAssertion) HasBounds() bool`

HasBounds returns a boolean if a field has been set.

### SetBoundsNil

`func (o *BrowserVisualAssertion) SetBoundsNil(b bool)`

 SetBoundsNil sets the value for Bounds to be an explicit nil

### UnsetBounds
`func (o *BrowserVisualAssertion) UnsetBounds()`

UnsetBounds ensures that no value is present for Bounds, not even an explicit nil
### GetExcludedRegions

`func (o *BrowserVisualAssertion) GetExcludedRegions() []BrowserVisualExcludedRegion`

GetExcludedRegions returns the ExcludedRegions field if non-nil, zero value otherwise.

### GetExcludedRegionsOk

`func (o *BrowserVisualAssertion) GetExcludedRegionsOk() (*[]BrowserVisualExcludedRegion, bool)`

GetExcludedRegionsOk returns a tuple with the ExcludedRegions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludedRegions

`func (o *BrowserVisualAssertion) SetExcludedRegions(v []BrowserVisualExcludedRegion)`

SetExcludedRegions sets ExcludedRegions field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
