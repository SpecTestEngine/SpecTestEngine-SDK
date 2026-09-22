# DocumentVisualAssertion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Version** | **int32** |  |
**Algorithm** | **string** |  |
**RenderProfile** | **string** |  |
**Pages** | [**[]DocumentVisualAssertionPage**](DocumentVisualAssertionPage.md) |  |
**ExcludedRegions** | [**[]DocumentVisualExcludedRegion**](DocumentVisualExcludedRegion.md) |  |

## Methods

### NewDocumentVisualAssertion

`func NewDocumentVisualAssertion(version int32, algorithm string, renderProfile string, pages []DocumentVisualAssertionPage, excludedRegions []DocumentVisualExcludedRegion, ) *DocumentVisualAssertion`

NewDocumentVisualAssertion instantiates a new DocumentVisualAssertion object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDocumentVisualAssertionWithDefaults

`func NewDocumentVisualAssertionWithDefaults() *DocumentVisualAssertion`

NewDocumentVisualAssertionWithDefaults instantiates a new DocumentVisualAssertion object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetVersion

`func (o *DocumentVisualAssertion) GetVersion() int32`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *DocumentVisualAssertion) GetVersionOk() (*int32, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *DocumentVisualAssertion) SetVersion(v int32)`

SetVersion sets Version field to given value.


### GetAlgorithm

`func (o *DocumentVisualAssertion) GetAlgorithm() string`

GetAlgorithm returns the Algorithm field if non-nil, zero value otherwise.

### GetAlgorithmOk

`func (o *DocumentVisualAssertion) GetAlgorithmOk() (*string, bool)`

GetAlgorithmOk returns a tuple with the Algorithm field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlgorithm

`func (o *DocumentVisualAssertion) SetAlgorithm(v string)`

SetAlgorithm sets Algorithm field to given value.


### GetRenderProfile

`func (o *DocumentVisualAssertion) GetRenderProfile() string`

GetRenderProfile returns the RenderProfile field if non-nil, zero value otherwise.

### GetRenderProfileOk

`func (o *DocumentVisualAssertion) GetRenderProfileOk() (*string, bool)`

GetRenderProfileOk returns a tuple with the RenderProfile field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRenderProfile

`func (o *DocumentVisualAssertion) SetRenderProfile(v string)`

SetRenderProfile sets RenderProfile field to given value.


### GetPages

`func (o *DocumentVisualAssertion) GetPages() []DocumentVisualAssertionPage`

GetPages returns the Pages field if non-nil, zero value otherwise.

### GetPagesOk

`func (o *DocumentVisualAssertion) GetPagesOk() (*[]DocumentVisualAssertionPage, bool)`

GetPagesOk returns a tuple with the Pages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPages

`func (o *DocumentVisualAssertion) SetPages(v []DocumentVisualAssertionPage)`

SetPages sets Pages field to given value.


### GetExcludedRegions

`func (o *DocumentVisualAssertion) GetExcludedRegions() []DocumentVisualExcludedRegion`

GetExcludedRegions returns the ExcludedRegions field if non-nil, zero value otherwise.

### GetExcludedRegionsOk

`func (o *DocumentVisualAssertion) GetExcludedRegionsOk() (*[]DocumentVisualExcludedRegion, bool)`

GetExcludedRegionsOk returns a tuple with the ExcludedRegions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludedRegions

`func (o *DocumentVisualAssertion) SetExcludedRegions(v []DocumentVisualExcludedRegion)`

SetExcludedRegions sets ExcludedRegions field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


