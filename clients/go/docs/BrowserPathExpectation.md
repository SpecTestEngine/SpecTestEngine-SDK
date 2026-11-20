# BrowserPathExpectation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Path** | **string** |  |
**Value** | Pointer to **interface{}** | Exact JSON value, including null. Absence selects pattern matching instead. | [optional]
**Pattern** | Pointer to **string** |  | [optional]

## Methods

### NewBrowserPathExpectation

`func NewBrowserPathExpectation(path string, ) *BrowserPathExpectation`

NewBrowserPathExpectation instantiates a new BrowserPathExpectation object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserPathExpectationWithDefaults

`func NewBrowserPathExpectationWithDefaults() *BrowserPathExpectation`

NewBrowserPathExpectationWithDefaults instantiates a new BrowserPathExpectation object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPath

`func (o *BrowserPathExpectation) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *BrowserPathExpectation) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *BrowserPathExpectation) SetPath(v string)`

SetPath sets Path field to given value.


### GetValue

`func (o *BrowserPathExpectation) GetValue() interface{}`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *BrowserPathExpectation) GetValueOk() (*interface{}, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *BrowserPathExpectation) SetValue(v interface{})`

SetValue sets Value field to given value.

### HasValue

`func (o *BrowserPathExpectation) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValueNil

`func (o *BrowserPathExpectation) SetValueNil(b bool)`

 SetValueNil sets the value for Value to be an explicit nil

### UnsetValue
`func (o *BrowserPathExpectation) UnsetValue()`

UnsetValue ensures that no value is present for Value, not even an explicit nil
### GetPattern

`func (o *BrowserPathExpectation) GetPattern() string`

GetPattern returns the Pattern field if non-nil, zero value otherwise.

### GetPatternOk

`func (o *BrowserPathExpectation) GetPatternOk() (*string, bool)`

GetPatternOk returns a tuple with the Pattern field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPattern

`func (o *BrowserPathExpectation) SetPattern(v string)`

SetPattern sets Pattern field to given value.

### HasPattern

`func (o *BrowserPathExpectation) HasPattern() bool`

HasPattern returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
