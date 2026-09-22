# BrowserMacroInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Description** | Pointer to **string** |  | [optional]
**StartUrl** | **string** |  |
**ViewportWidth** | Pointer to **int32** |  | [optional]
**ViewportHeight** | Pointer to **int32** |  | [optional]
**Steps** | [**[]BrowserMacroStepInput**](BrowserMacroStepInput.md) |  |

## Methods

### NewBrowserMacroInput

`func NewBrowserMacroInput(name string, startUrl string, steps []BrowserMacroStepInput, ) *BrowserMacroInput`

NewBrowserMacroInput instantiates a new BrowserMacroInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserMacroInputWithDefaults

`func NewBrowserMacroInputWithDefaults() *BrowserMacroInput`

NewBrowserMacroInputWithDefaults instantiates a new BrowserMacroInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *BrowserMacroInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *BrowserMacroInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *BrowserMacroInput) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *BrowserMacroInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *BrowserMacroInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *BrowserMacroInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *BrowserMacroInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetStartUrl

`func (o *BrowserMacroInput) GetStartUrl() string`

GetStartUrl returns the StartUrl field if non-nil, zero value otherwise.

### GetStartUrlOk

`func (o *BrowserMacroInput) GetStartUrlOk() (*string, bool)`

GetStartUrlOk returns a tuple with the StartUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartUrl

`func (o *BrowserMacroInput) SetStartUrl(v string)`

SetStartUrl sets StartUrl field to given value.


### GetViewportWidth

`func (o *BrowserMacroInput) GetViewportWidth() int32`

GetViewportWidth returns the ViewportWidth field if non-nil, zero value otherwise.

### GetViewportWidthOk

`func (o *BrowserMacroInput) GetViewportWidthOk() (*int32, bool)`

GetViewportWidthOk returns a tuple with the ViewportWidth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetViewportWidth

`func (o *BrowserMacroInput) SetViewportWidth(v int32)`

SetViewportWidth sets ViewportWidth field to given value.

### HasViewportWidth

`func (o *BrowserMacroInput) HasViewportWidth() bool`

HasViewportWidth returns a boolean if a field has been set.

### GetViewportHeight

`func (o *BrowserMacroInput) GetViewportHeight() int32`

GetViewportHeight returns the ViewportHeight field if non-nil, zero value otherwise.

### GetViewportHeightOk

`func (o *BrowserMacroInput) GetViewportHeightOk() (*int32, bool)`

GetViewportHeightOk returns a tuple with the ViewportHeight field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetViewportHeight

`func (o *BrowserMacroInput) SetViewportHeight(v int32)`

SetViewportHeight sets ViewportHeight field to given value.

### HasViewportHeight

`func (o *BrowserMacroInput) HasViewportHeight() bool`

HasViewportHeight returns a boolean if a field has been set.

### GetSteps

`func (o *BrowserMacroInput) GetSteps() []BrowserMacroStepInput`

GetSteps returns the Steps field if non-nil, zero value otherwise.

### GetStepsOk

`func (o *BrowserMacroInput) GetStepsOk() (*[]BrowserMacroStepInput, bool)`

GetStepsOk returns a tuple with the Steps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteps

`func (o *BrowserMacroInput) SetSteps(v []BrowserMacroStepInput)`

SetSteps sets Steps field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


