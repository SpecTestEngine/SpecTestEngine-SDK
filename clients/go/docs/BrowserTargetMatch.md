# BrowserTargetMatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Role** | **string** |  |
**Name** | **string** |  |
**Destination** | Pointer to [**BrowserTargetIdentity**](BrowserTargetIdentity.md) |  | [optional]

## Methods

### NewBrowserTargetMatch

`func NewBrowserTargetMatch(role string, name string, ) *BrowserTargetMatch`

NewBrowserTargetMatch instantiates a new BrowserTargetMatch object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserTargetMatchWithDefaults

`func NewBrowserTargetMatchWithDefaults() *BrowserTargetMatch`

NewBrowserTargetMatchWithDefaults instantiates a new BrowserTargetMatch object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRole

`func (o *BrowserTargetMatch) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *BrowserTargetMatch) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *BrowserTargetMatch) SetRole(v string)`

SetRole sets Role field to given value.


### GetName

`func (o *BrowserTargetMatch) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *BrowserTargetMatch) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *BrowserTargetMatch) SetName(v string)`

SetName sets Name field to given value.


### GetDestination

`func (o *BrowserTargetMatch) GetDestination() BrowserTargetIdentity`

GetDestination returns the Destination field if non-nil, zero value otherwise.

### GetDestinationOk

`func (o *BrowserTargetMatch) GetDestinationOk() (*BrowserTargetIdentity, bool)`

GetDestinationOk returns a tuple with the Destination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestination

`func (o *BrowserTargetMatch) SetDestination(v BrowserTargetIdentity)`

SetDestination sets Destination field to given value.

### HasDestination

`func (o *BrowserTargetMatch) HasDestination() bool`

HasDestination returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
