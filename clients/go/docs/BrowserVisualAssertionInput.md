# BrowserVisualAssertionInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | Pointer to **bool** |  | [optional]
**Name** | Pointer to **string** |  | [optional]
**ScopeType** | Pointer to [**BrowserVisualScopeType**](BrowserVisualScopeType.md) |  | [optional]
**CompareMode** | Pointer to [**BrowserVisualCompareMode**](BrowserVisualCompareMode.md) |  | [optional]
**StopPolicy** | Pointer to [**BrowserVisualStopPolicy**](BrowserVisualStopPolicy.md) |  | [optional]
**MaxDiffPixels** | Pointer to **int64** |  | [optional]
**MaxDiffPixelRatio** | Pointer to **float64** |  | [optional]
**ColorThreshold** | Pointer to **float64** |  | [optional]
**MoveTolerancePx** | Pointer to **float64** |  | [optional]
**Bounds** | Pointer to [**NullableBrowserVisualBounds**](BrowserVisualBounds.md) |  | [optional]
**ExcludedRegions** | Pointer to [**[]BrowserVisualExcludedRegion**](BrowserVisualExcludedRegion.md) |  | [optional]
**BaselineScreenshotBase64** | Pointer to **string** | Raw baseline capture supplied during authoring; omitted from saved definition reads. | [optional]
**BaselineSemanticJson** | Pointer to **string** |  | [optional]

## Methods

### NewBrowserVisualAssertionInput

`func NewBrowserVisualAssertionInput() *BrowserVisualAssertionInput`

NewBrowserVisualAssertionInput instantiates a new BrowserVisualAssertionInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserVisualAssertionInputWithDefaults

`func NewBrowserVisualAssertionInputWithDefaults() *BrowserVisualAssertionInput`

NewBrowserVisualAssertionInputWithDefaults instantiates a new BrowserVisualAssertionInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnabled

`func (o *BrowserVisualAssertionInput) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *BrowserVisualAssertionInput) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *BrowserVisualAssertionInput) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *BrowserVisualAssertionInput) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetName

`func (o *BrowserVisualAssertionInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *BrowserVisualAssertionInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *BrowserVisualAssertionInput) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *BrowserVisualAssertionInput) HasName() bool`

HasName returns a boolean if a field has been set.

### GetScopeType

`func (o *BrowserVisualAssertionInput) GetScopeType() BrowserVisualScopeType`

GetScopeType returns the ScopeType field if non-nil, zero value otherwise.

### GetScopeTypeOk

`func (o *BrowserVisualAssertionInput) GetScopeTypeOk() (*BrowserVisualScopeType, bool)`

GetScopeTypeOk returns a tuple with the ScopeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopeType

`func (o *BrowserVisualAssertionInput) SetScopeType(v BrowserVisualScopeType)`

SetScopeType sets ScopeType field to given value.

### HasScopeType

`func (o *BrowserVisualAssertionInput) HasScopeType() bool`

HasScopeType returns a boolean if a field has been set.

### GetCompareMode

`func (o *BrowserVisualAssertionInput) GetCompareMode() BrowserVisualCompareMode`

GetCompareMode returns the CompareMode field if non-nil, zero value otherwise.

### GetCompareModeOk

`func (o *BrowserVisualAssertionInput) GetCompareModeOk() (*BrowserVisualCompareMode, bool)`

GetCompareModeOk returns a tuple with the CompareMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompareMode

`func (o *BrowserVisualAssertionInput) SetCompareMode(v BrowserVisualCompareMode)`

SetCompareMode sets CompareMode field to given value.

### HasCompareMode

`func (o *BrowserVisualAssertionInput) HasCompareMode() bool`

HasCompareMode returns a boolean if a field has been set.

### GetStopPolicy

`func (o *BrowserVisualAssertionInput) GetStopPolicy() BrowserVisualStopPolicy`

GetStopPolicy returns the StopPolicy field if non-nil, zero value otherwise.

### GetStopPolicyOk

`func (o *BrowserVisualAssertionInput) GetStopPolicyOk() (*BrowserVisualStopPolicy, bool)`

GetStopPolicyOk returns a tuple with the StopPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStopPolicy

`func (o *BrowserVisualAssertionInput) SetStopPolicy(v BrowserVisualStopPolicy)`

SetStopPolicy sets StopPolicy field to given value.

### HasStopPolicy

`func (o *BrowserVisualAssertionInput) HasStopPolicy() bool`

HasStopPolicy returns a boolean if a field has been set.

### GetMaxDiffPixels

`func (o *BrowserVisualAssertionInput) GetMaxDiffPixels() int64`

GetMaxDiffPixels returns the MaxDiffPixels field if non-nil, zero value otherwise.

### GetMaxDiffPixelsOk

`func (o *BrowserVisualAssertionInput) GetMaxDiffPixelsOk() (*int64, bool)`

GetMaxDiffPixelsOk returns a tuple with the MaxDiffPixels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxDiffPixels

`func (o *BrowserVisualAssertionInput) SetMaxDiffPixels(v int64)`

SetMaxDiffPixels sets MaxDiffPixels field to given value.

### HasMaxDiffPixels

`func (o *BrowserVisualAssertionInput) HasMaxDiffPixels() bool`

HasMaxDiffPixels returns a boolean if a field has been set.

### GetMaxDiffPixelRatio

`func (o *BrowserVisualAssertionInput) GetMaxDiffPixelRatio() float64`

GetMaxDiffPixelRatio returns the MaxDiffPixelRatio field if non-nil, zero value otherwise.

### GetMaxDiffPixelRatioOk

`func (o *BrowserVisualAssertionInput) GetMaxDiffPixelRatioOk() (*float64, bool)`

GetMaxDiffPixelRatioOk returns a tuple with the MaxDiffPixelRatio field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxDiffPixelRatio

`func (o *BrowserVisualAssertionInput) SetMaxDiffPixelRatio(v float64)`

SetMaxDiffPixelRatio sets MaxDiffPixelRatio field to given value.

### HasMaxDiffPixelRatio

`func (o *BrowserVisualAssertionInput) HasMaxDiffPixelRatio() bool`

HasMaxDiffPixelRatio returns a boolean if a field has been set.

### GetColorThreshold

`func (o *BrowserVisualAssertionInput) GetColorThreshold() float64`

GetColorThreshold returns the ColorThreshold field if non-nil, zero value otherwise.

### GetColorThresholdOk

`func (o *BrowserVisualAssertionInput) GetColorThresholdOk() (*float64, bool)`

GetColorThresholdOk returns a tuple with the ColorThreshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColorThreshold

`func (o *BrowserVisualAssertionInput) SetColorThreshold(v float64)`

SetColorThreshold sets ColorThreshold field to given value.

### HasColorThreshold

`func (o *BrowserVisualAssertionInput) HasColorThreshold() bool`

HasColorThreshold returns a boolean if a field has been set.

### GetMoveTolerancePx

`func (o *BrowserVisualAssertionInput) GetMoveTolerancePx() float64`

GetMoveTolerancePx returns the MoveTolerancePx field if non-nil, zero value otherwise.

### GetMoveTolerancePxOk

`func (o *BrowserVisualAssertionInput) GetMoveTolerancePxOk() (*float64, bool)`

GetMoveTolerancePxOk returns a tuple with the MoveTolerancePx field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMoveTolerancePx

`func (o *BrowserVisualAssertionInput) SetMoveTolerancePx(v float64)`

SetMoveTolerancePx sets MoveTolerancePx field to given value.

### HasMoveTolerancePx

`func (o *BrowserVisualAssertionInput) HasMoveTolerancePx() bool`

HasMoveTolerancePx returns a boolean if a field has been set.

### GetBounds

`func (o *BrowserVisualAssertionInput) GetBounds() BrowserVisualBounds`

GetBounds returns the Bounds field if non-nil, zero value otherwise.

### GetBoundsOk

`func (o *BrowserVisualAssertionInput) GetBoundsOk() (*BrowserVisualBounds, bool)`

GetBoundsOk returns a tuple with the Bounds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBounds

`func (o *BrowserVisualAssertionInput) SetBounds(v BrowserVisualBounds)`

SetBounds sets Bounds field to given value.

### HasBounds

`func (o *BrowserVisualAssertionInput) HasBounds() bool`

HasBounds returns a boolean if a field has been set.

### SetBoundsNil

`func (o *BrowserVisualAssertionInput) SetBoundsNil(b bool)`

 SetBoundsNil sets the value for Bounds to be an explicit nil

### UnsetBounds
`func (o *BrowserVisualAssertionInput) UnsetBounds()`

UnsetBounds ensures that no value is present for Bounds, not even an explicit nil
### GetExcludedRegions

`func (o *BrowserVisualAssertionInput) GetExcludedRegions() []BrowserVisualExcludedRegion`

GetExcludedRegions returns the ExcludedRegions field if non-nil, zero value otherwise.

### GetExcludedRegionsOk

`func (o *BrowserVisualAssertionInput) GetExcludedRegionsOk() (*[]BrowserVisualExcludedRegion, bool)`

GetExcludedRegionsOk returns a tuple with the ExcludedRegions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludedRegions

`func (o *BrowserVisualAssertionInput) SetExcludedRegions(v []BrowserVisualExcludedRegion)`

SetExcludedRegions sets ExcludedRegions field to given value.

### HasExcludedRegions

`func (o *BrowserVisualAssertionInput) HasExcludedRegions() bool`

HasExcludedRegions returns a boolean if a field has been set.

### GetBaselineScreenshotBase64

`func (o *BrowserVisualAssertionInput) GetBaselineScreenshotBase64() string`

GetBaselineScreenshotBase64 returns the BaselineScreenshotBase64 field if non-nil, zero value otherwise.

### GetBaselineScreenshotBase64Ok

`func (o *BrowserVisualAssertionInput) GetBaselineScreenshotBase64Ok() (*string, bool)`

GetBaselineScreenshotBase64Ok returns a tuple with the BaselineScreenshotBase64 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaselineScreenshotBase64

`func (o *BrowserVisualAssertionInput) SetBaselineScreenshotBase64(v string)`

SetBaselineScreenshotBase64 sets BaselineScreenshotBase64 field to given value.

### HasBaselineScreenshotBase64

`func (o *BrowserVisualAssertionInput) HasBaselineScreenshotBase64() bool`

HasBaselineScreenshotBase64 returns a boolean if a field has been set.

### GetBaselineSemanticJson

`func (o *BrowserVisualAssertionInput) GetBaselineSemanticJson() string`

GetBaselineSemanticJson returns the BaselineSemanticJson field if non-nil, zero value otherwise.

### GetBaselineSemanticJsonOk

`func (o *BrowserVisualAssertionInput) GetBaselineSemanticJsonOk() (*string, bool)`

GetBaselineSemanticJsonOk returns a tuple with the BaselineSemanticJson field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaselineSemanticJson

`func (o *BrowserVisualAssertionInput) SetBaselineSemanticJson(v string)`

SetBaselineSemanticJson sets BaselineSemanticJson field to given value.

### HasBaselineSemanticJson

`func (o *BrowserVisualAssertionInput) HasBaselineSemanticJson() bool`

HasBaselineSemanticJson returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


