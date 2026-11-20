# BrowserStreamMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Transport** | **string** |  |
**Direction** | **string** |  |
**EventName** | Pointer to **string** |  | [optional]
**Binary** | Pointer to **bool** |  | [optional] [default to false]
**Failed** | Pointer to **bool** |  | [optional] [default to false]

## Methods

### NewBrowserStreamMessage

`func NewBrowserStreamMessage(transport string, direction string, ) *BrowserStreamMessage`

NewBrowserStreamMessage instantiates a new BrowserStreamMessage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserStreamMessageWithDefaults

`func NewBrowserStreamMessageWithDefaults() *BrowserStreamMessage`

NewBrowserStreamMessageWithDefaults instantiates a new BrowserStreamMessage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTransport

`func (o *BrowserStreamMessage) GetTransport() string`

GetTransport returns the Transport field if non-nil, zero value otherwise.

### GetTransportOk

`func (o *BrowserStreamMessage) GetTransportOk() (*string, bool)`

GetTransportOk returns a tuple with the Transport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransport

`func (o *BrowserStreamMessage) SetTransport(v string)`

SetTransport sets Transport field to given value.


### GetDirection

`func (o *BrowserStreamMessage) GetDirection() string`

GetDirection returns the Direction field if non-nil, zero value otherwise.

### GetDirectionOk

`func (o *BrowserStreamMessage) GetDirectionOk() (*string, bool)`

GetDirectionOk returns a tuple with the Direction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDirection

`func (o *BrowserStreamMessage) SetDirection(v string)`

SetDirection sets Direction field to given value.


### GetEventName

`func (o *BrowserStreamMessage) GetEventName() string`

GetEventName returns the EventName field if non-nil, zero value otherwise.

### GetEventNameOk

`func (o *BrowserStreamMessage) GetEventNameOk() (*string, bool)`

GetEventNameOk returns a tuple with the EventName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEventName

`func (o *BrowserStreamMessage) SetEventName(v string)`

SetEventName sets EventName field to given value.

### HasEventName

`func (o *BrowserStreamMessage) HasEventName() bool`

HasEventName returns a boolean if a field has been set.

### GetBinary

`func (o *BrowserStreamMessage) GetBinary() bool`

GetBinary returns the Binary field if non-nil, zero value otherwise.

### GetBinaryOk

`func (o *BrowserStreamMessage) GetBinaryOk() (*bool, bool)`

GetBinaryOk returns a tuple with the Binary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBinary

`func (o *BrowserStreamMessage) SetBinary(v bool)`

SetBinary sets Binary field to given value.

### HasBinary

`func (o *BrowserStreamMessage) HasBinary() bool`

HasBinary returns a boolean if a field has been set.

### GetFailed

`func (o *BrowserStreamMessage) GetFailed() bool`

GetFailed returns the Failed field if non-nil, zero value otherwise.

### GetFailedOk

`func (o *BrowserStreamMessage) GetFailedOk() (*bool, bool)`

GetFailedOk returns a tuple with the Failed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFailed

`func (o *BrowserStreamMessage) SetFailed(v bool)`

SetFailed sets Failed field to given value.

### HasFailed

`func (o *BrowserStreamMessage) HasFailed() bool`

HasFailed returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
