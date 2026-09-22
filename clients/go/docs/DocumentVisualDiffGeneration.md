# DocumentVisualDiffGeneration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**GenerationId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**GenerationNumber** | **int32** |  |
**ExpectedSha256** | **string** |  |
**ColorThreshold** | **float64** |  |
**TotalPages** | **int32** |  |
**ChangedPages** | **int32** |  |
**DiffPixels** | **int64** |  |
**DiffPixelRatio** | **float64** |  |
**CreatedAt** | **time.Time** |  |
**ExpiresAt** | **time.Time** |  |
**ExcludedRegions** | [**[]DocumentVisualExcludedRegion**](DocumentVisualExcludedRegion.md) | Immutable normalized masks used by this generation. |
**ChangedExcludedRegionIndexes** | **[]int32** | Indexes into excludedRegions whose masked area contained a real change in this immutable generation. |
**Pages** | [**[]DocumentVisualDiffPage**](DocumentVisualDiffPage.md) |  |

## Methods

### NewDocumentVisualDiffGeneration

`func NewDocumentVisualDiffGeneration(generationId string, generationNumber int32, expectedSha256 string, colorThreshold float64, totalPages int32, changedPages int32, diffPixels int64, diffPixelRatio float64, createdAt time.Time, expiresAt time.Time, excludedRegions []DocumentVisualExcludedRegion, changedExcludedRegionIndexes []int32, pages []DocumentVisualDiffPage, ) *DocumentVisualDiffGeneration`

NewDocumentVisualDiffGeneration instantiates a new DocumentVisualDiffGeneration object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDocumentVisualDiffGenerationWithDefaults

`func NewDocumentVisualDiffGenerationWithDefaults() *DocumentVisualDiffGeneration`

NewDocumentVisualDiffGenerationWithDefaults instantiates a new DocumentVisualDiffGeneration object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetGenerationId

`func (o *DocumentVisualDiffGeneration) GetGenerationId() string`

GetGenerationId returns the GenerationId field if non-nil, zero value otherwise.

### GetGenerationIdOk

`func (o *DocumentVisualDiffGeneration) GetGenerationIdOk() (*string, bool)`

GetGenerationIdOk returns a tuple with the GenerationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGenerationId

`func (o *DocumentVisualDiffGeneration) SetGenerationId(v string)`

SetGenerationId sets GenerationId field to given value.


### GetGenerationNumber

`func (o *DocumentVisualDiffGeneration) GetGenerationNumber() int32`

GetGenerationNumber returns the GenerationNumber field if non-nil, zero value otherwise.

### GetGenerationNumberOk

`func (o *DocumentVisualDiffGeneration) GetGenerationNumberOk() (*int32, bool)`

GetGenerationNumberOk returns a tuple with the GenerationNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGenerationNumber

`func (o *DocumentVisualDiffGeneration) SetGenerationNumber(v int32)`

SetGenerationNumber sets GenerationNumber field to given value.


### GetExpectedSha256

`func (o *DocumentVisualDiffGeneration) GetExpectedSha256() string`

GetExpectedSha256 returns the ExpectedSha256 field if non-nil, zero value otherwise.

### GetExpectedSha256Ok

`func (o *DocumentVisualDiffGeneration) GetExpectedSha256Ok() (*string, bool)`

GetExpectedSha256Ok returns a tuple with the ExpectedSha256 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedSha256

`func (o *DocumentVisualDiffGeneration) SetExpectedSha256(v string)`

SetExpectedSha256 sets ExpectedSha256 field to given value.


### GetColorThreshold

`func (o *DocumentVisualDiffGeneration) GetColorThreshold() float64`

GetColorThreshold returns the ColorThreshold field if non-nil, zero value otherwise.

### GetColorThresholdOk

`func (o *DocumentVisualDiffGeneration) GetColorThresholdOk() (*float64, bool)`

GetColorThresholdOk returns a tuple with the ColorThreshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColorThreshold

`func (o *DocumentVisualDiffGeneration) SetColorThreshold(v float64)`

SetColorThreshold sets ColorThreshold field to given value.


### GetTotalPages

`func (o *DocumentVisualDiffGeneration) GetTotalPages() int32`

GetTotalPages returns the TotalPages field if non-nil, zero value otherwise.

### GetTotalPagesOk

`func (o *DocumentVisualDiffGeneration) GetTotalPagesOk() (*int32, bool)`

GetTotalPagesOk returns a tuple with the TotalPages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalPages

`func (o *DocumentVisualDiffGeneration) SetTotalPages(v int32)`

SetTotalPages sets TotalPages field to given value.


### GetChangedPages

`func (o *DocumentVisualDiffGeneration) GetChangedPages() int32`

GetChangedPages returns the ChangedPages field if non-nil, zero value otherwise.

### GetChangedPagesOk

`func (o *DocumentVisualDiffGeneration) GetChangedPagesOk() (*int32, bool)`

GetChangedPagesOk returns a tuple with the ChangedPages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangedPages

`func (o *DocumentVisualDiffGeneration) SetChangedPages(v int32)`

SetChangedPages sets ChangedPages field to given value.


### GetDiffPixels

`func (o *DocumentVisualDiffGeneration) GetDiffPixels() int64`

GetDiffPixels returns the DiffPixels field if non-nil, zero value otherwise.

### GetDiffPixelsOk

`func (o *DocumentVisualDiffGeneration) GetDiffPixelsOk() (*int64, bool)`

GetDiffPixelsOk returns a tuple with the DiffPixels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiffPixels

`func (o *DocumentVisualDiffGeneration) SetDiffPixels(v int64)`

SetDiffPixels sets DiffPixels field to given value.


### GetDiffPixelRatio

`func (o *DocumentVisualDiffGeneration) GetDiffPixelRatio() float64`

GetDiffPixelRatio returns the DiffPixelRatio field if non-nil, zero value otherwise.

### GetDiffPixelRatioOk

`func (o *DocumentVisualDiffGeneration) GetDiffPixelRatioOk() (*float64, bool)`

GetDiffPixelRatioOk returns a tuple with the DiffPixelRatio field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiffPixelRatio

`func (o *DocumentVisualDiffGeneration) SetDiffPixelRatio(v float64)`

SetDiffPixelRatio sets DiffPixelRatio field to given value.


### GetCreatedAt

`func (o *DocumentVisualDiffGeneration) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *DocumentVisualDiffGeneration) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *DocumentVisualDiffGeneration) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetExpiresAt

`func (o *DocumentVisualDiffGeneration) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *DocumentVisualDiffGeneration) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *DocumentVisualDiffGeneration) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.


### GetExcludedRegions

`func (o *DocumentVisualDiffGeneration) GetExcludedRegions() []DocumentVisualExcludedRegion`

GetExcludedRegions returns the ExcludedRegions field if non-nil, zero value otherwise.

### GetExcludedRegionsOk

`func (o *DocumentVisualDiffGeneration) GetExcludedRegionsOk() (*[]DocumentVisualExcludedRegion, bool)`

GetExcludedRegionsOk returns a tuple with the ExcludedRegions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludedRegions

`func (o *DocumentVisualDiffGeneration) SetExcludedRegions(v []DocumentVisualExcludedRegion)`

SetExcludedRegions sets ExcludedRegions field to given value.


### GetChangedExcludedRegionIndexes

`func (o *DocumentVisualDiffGeneration) GetChangedExcludedRegionIndexes() []int32`

GetChangedExcludedRegionIndexes returns the ChangedExcludedRegionIndexes field if non-nil, zero value otherwise.

### GetChangedExcludedRegionIndexesOk

`func (o *DocumentVisualDiffGeneration) GetChangedExcludedRegionIndexesOk() (*[]int32, bool)`

GetChangedExcludedRegionIndexesOk returns a tuple with the ChangedExcludedRegionIndexes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangedExcludedRegionIndexes

`func (o *DocumentVisualDiffGeneration) SetChangedExcludedRegionIndexes(v []int32)`

SetChangedExcludedRegionIndexes sets ChangedExcludedRegionIndexes field to given value.


### GetPages

`func (o *DocumentVisualDiffGeneration) GetPages() []DocumentVisualDiffPage`

GetPages returns the Pages field if non-nil, zero value otherwise.

### GetPagesOk

`func (o *DocumentVisualDiffGeneration) GetPagesOk() (*[]DocumentVisualDiffPage, bool)`

GetPagesOk returns a tuple with the Pages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPages

`func (o *DocumentVisualDiffGeneration) SetPages(v []DocumentVisualDiffPage)`

SetPages sets Pages field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


