# FlowInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**Steps** | [**[]FlowStepInput**](FlowStepInput.md) |  |
**GlobalVariableFallbacks** | Pointer to **map[string]string** |  | [optional]
**BrowserSession** | Pointer to [**BrowserSessionInput**](BrowserSessionInput.md) |  | [optional]

## Methods

### NewFlowInput

`func NewFlowInput(name string, steps []FlowStepInput, ) *FlowInput`

NewFlowInput instantiates a new FlowInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowInputWithDefaults

`func NewFlowInputWithDefaults() *FlowInput`

NewFlowInputWithDefaults instantiates a new FlowInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *FlowInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *FlowInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *FlowInput) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *FlowInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *FlowInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *FlowInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *FlowInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *FlowInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *FlowInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetSteps

`func (o *FlowInput) GetSteps() []FlowStepInput`

GetSteps returns the Steps field if non-nil, zero value otherwise.

### GetStepsOk

`func (o *FlowInput) GetStepsOk() (*[]FlowStepInput, bool)`

GetStepsOk returns a tuple with the Steps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteps

`func (o *FlowInput) SetSteps(v []FlowStepInput)`

SetSteps sets Steps field to given value.


### GetGlobalVariableFallbacks

`func (o *FlowInput) GetGlobalVariableFallbacks() map[string]string`

GetGlobalVariableFallbacks returns the GlobalVariableFallbacks field if non-nil, zero value otherwise.

### GetGlobalVariableFallbacksOk

`func (o *FlowInput) GetGlobalVariableFallbacksOk() (*map[string]string, bool)`

GetGlobalVariableFallbacksOk returns a tuple with the GlobalVariableFallbacks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGlobalVariableFallbacks

`func (o *FlowInput) SetGlobalVariableFallbacks(v map[string]string)`

SetGlobalVariableFallbacks sets GlobalVariableFallbacks field to given value.

### HasGlobalVariableFallbacks

`func (o *FlowInput) HasGlobalVariableFallbacks() bool`

HasGlobalVariableFallbacks returns a boolean if a field has been set.

### GetBrowserSession

`func (o *FlowInput) GetBrowserSession() BrowserSessionInput`

GetBrowserSession returns the BrowserSession field if non-nil, zero value otherwise.

### GetBrowserSessionOk

`func (o *FlowInput) GetBrowserSessionOk() (*BrowserSessionInput, bool)`

GetBrowserSessionOk returns a tuple with the BrowserSession field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrowserSession

`func (o *FlowInput) SetBrowserSession(v BrowserSessionInput)`

SetBrowserSession sets BrowserSession field to given value.

### HasBrowserSession

`func (o *FlowInput) HasBrowserSession() bool`

HasBrowserSession returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


