# BrowserVisualPromoteBaselineRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ActionId** | **string** | Client-generated idempotency key for this review command. |
**ExpectedAssertionRevision** | **int64** | Current assertion revision. A stale value is rejected with HTTP 409. |

## Methods

### NewBrowserVisualPromoteBaselineRequest

`func NewBrowserVisualPromoteBaselineRequest(actionId string, expectedAssertionRevision int64, ) *BrowserVisualPromoteBaselineRequest`

NewBrowserVisualPromoteBaselineRequest instantiates a new BrowserVisualPromoteBaselineRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserVisualPromoteBaselineRequestWithDefaults

`func NewBrowserVisualPromoteBaselineRequestWithDefaults() *BrowserVisualPromoteBaselineRequest`

NewBrowserVisualPromoteBaselineRequestWithDefaults instantiates a new BrowserVisualPromoteBaselineRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetActionId

`func (o *BrowserVisualPromoteBaselineRequest) GetActionId() string`

GetActionId returns the ActionId field if non-nil, zero value otherwise.

### GetActionIdOk

`func (o *BrowserVisualPromoteBaselineRequest) GetActionIdOk() (*string, bool)`

GetActionIdOk returns a tuple with the ActionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActionId

`func (o *BrowserVisualPromoteBaselineRequest) SetActionId(v string)`

SetActionId sets ActionId field to given value.


### GetExpectedAssertionRevision

`func (o *BrowserVisualPromoteBaselineRequest) GetExpectedAssertionRevision() int64`

GetExpectedAssertionRevision returns the ExpectedAssertionRevision field if non-nil, zero value otherwise.

### GetExpectedAssertionRevisionOk

`func (o *BrowserVisualPromoteBaselineRequest) GetExpectedAssertionRevisionOk() (*int64, bool)`

GetExpectedAssertionRevisionOk returns a tuple with the ExpectedAssertionRevision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedAssertionRevision

`func (o *BrowserVisualPromoteBaselineRequest) SetExpectedAssertionRevision(v int64)`

SetExpectedAssertionRevision sets ExpectedAssertionRevision field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
