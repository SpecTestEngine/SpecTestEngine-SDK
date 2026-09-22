# DocumentVisualDiffRegenerateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ColorThreshold** | Pointer to **float64** |  | [optional] [default to 24]
**ExcludedRegions** | Pointer to [**[]DocumentVisualExcludedRegion**](DocumentVisualExcludedRegion.md) |  | [optional]

## Methods

### NewDocumentVisualDiffRegenerateRequest

`func NewDocumentVisualDiffRegenerateRequest() *DocumentVisualDiffRegenerateRequest`

NewDocumentVisualDiffRegenerateRequest instantiates a new DocumentVisualDiffRegenerateRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDocumentVisualDiffRegenerateRequestWithDefaults

`func NewDocumentVisualDiffRegenerateRequestWithDefaults() *DocumentVisualDiffRegenerateRequest`

NewDocumentVisualDiffRegenerateRequestWithDefaults instantiates a new DocumentVisualDiffRegenerateRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetColorThreshold

`func (o *DocumentVisualDiffRegenerateRequest) GetColorThreshold() float64`

GetColorThreshold returns the ColorThreshold field if non-nil, zero value otherwise.

### GetColorThresholdOk

`func (o *DocumentVisualDiffRegenerateRequest) GetColorThresholdOk() (*float64, bool)`

GetColorThresholdOk returns a tuple with the ColorThreshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColorThreshold

`func (o *DocumentVisualDiffRegenerateRequest) SetColorThreshold(v float64)`

SetColorThreshold sets ColorThreshold field to given value.

### HasColorThreshold

`func (o *DocumentVisualDiffRegenerateRequest) HasColorThreshold() bool`

HasColorThreshold returns a boolean if a field has been set.

### GetExcludedRegions

`func (o *DocumentVisualDiffRegenerateRequest) GetExcludedRegions() []DocumentVisualExcludedRegion`

GetExcludedRegions returns the ExcludedRegions field if non-nil, zero value otherwise.

### GetExcludedRegionsOk

`func (o *DocumentVisualDiffRegenerateRequest) GetExcludedRegionsOk() (*[]DocumentVisualExcludedRegion, bool)`

GetExcludedRegionsOk returns a tuple with the ExcludedRegions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludedRegions

`func (o *DocumentVisualDiffRegenerateRequest) SetExcludedRegions(v []DocumentVisualExcludedRegion)`

SetExcludedRegions sets ExcludedRegions field to given value.

### HasExcludedRegions

`func (o *DocumentVisualDiffRegenerateRequest) HasExcludedRegions() bool`

HasExcludedRegions returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


