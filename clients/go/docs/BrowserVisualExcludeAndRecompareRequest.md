# BrowserVisualExcludeAndRecompareRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ActionId** | **string** | Client-generated idempotency key for this review command. |
**ExpectedAssertionRevision** | **int64** | Current assertion revision. A stale value is rejected with HTTP 409. |
**ExcludedRegions** | [**[]BrowserVisualExcludedRegion**](BrowserVisualExcludedRegion.md) | Complete normalized exclusion set for the next assertion revision. Overlaps are valid; rectangles crossing right or bottom edges are clamped to the comparison canvas. |

## Methods

### NewBrowserVisualExcludeAndRecompareRequest

`func NewBrowserVisualExcludeAndRecompareRequest(actionId string, expectedAssertionRevision int64, excludedRegions []BrowserVisualExcludedRegion, ) *BrowserVisualExcludeAndRecompareRequest`

NewBrowserVisualExcludeAndRecompareRequest instantiates a new BrowserVisualExcludeAndRecompareRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserVisualExcludeAndRecompareRequestWithDefaults

`func NewBrowserVisualExcludeAndRecompareRequestWithDefaults() *BrowserVisualExcludeAndRecompareRequest`

NewBrowserVisualExcludeAndRecompareRequestWithDefaults instantiates a new BrowserVisualExcludeAndRecompareRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetActionId

`func (o *BrowserVisualExcludeAndRecompareRequest) GetActionId() string`

GetActionId returns the ActionId field if non-nil, zero value otherwise.

### GetActionIdOk

`func (o *BrowserVisualExcludeAndRecompareRequest) GetActionIdOk() (*string, bool)`

GetActionIdOk returns a tuple with the ActionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActionId

`func (o *BrowserVisualExcludeAndRecompareRequest) SetActionId(v string)`

SetActionId sets ActionId field to given value.


### GetExpectedAssertionRevision

`func (o *BrowserVisualExcludeAndRecompareRequest) GetExpectedAssertionRevision() int64`

GetExpectedAssertionRevision returns the ExpectedAssertionRevision field if non-nil, zero value otherwise.

### GetExpectedAssertionRevisionOk

`func (o *BrowserVisualExcludeAndRecompareRequest) GetExpectedAssertionRevisionOk() (*int64, bool)`

GetExpectedAssertionRevisionOk returns a tuple with the ExpectedAssertionRevision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedAssertionRevision

`func (o *BrowserVisualExcludeAndRecompareRequest) SetExpectedAssertionRevision(v int64)`

SetExpectedAssertionRevision sets ExpectedAssertionRevision field to given value.


### GetExcludedRegions

`func (o *BrowserVisualExcludeAndRecompareRequest) GetExcludedRegions() []BrowserVisualExcludedRegion`

GetExcludedRegions returns the ExcludedRegions field if non-nil, zero value otherwise.

### GetExcludedRegionsOk

`func (o *BrowserVisualExcludeAndRecompareRequest) GetExcludedRegionsOk() (*[]BrowserVisualExcludedRegion, bool)`

GetExcludedRegionsOk returns a tuple with the ExcludedRegions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludedRegions

`func (o *BrowserVisualExcludeAndRecompareRequest) SetExcludedRegions(v []BrowserVisualExcludedRegion)`

SetExcludedRegions sets ExcludedRegions field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


