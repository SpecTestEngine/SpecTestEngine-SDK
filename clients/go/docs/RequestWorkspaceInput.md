# RequestWorkspaceInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**Variables** | Pointer to **map[string]string** |  | [optional]
**GlobalVariableFallbacks** | Pointer to **map[string]string** |  | [optional]

## Methods

### NewRequestWorkspaceInput

`func NewRequestWorkspaceInput(name string, ) *RequestWorkspaceInput`

NewRequestWorkspaceInput instantiates a new RequestWorkspaceInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRequestWorkspaceInputWithDefaults

`func NewRequestWorkspaceInputWithDefaults() *RequestWorkspaceInput`

NewRequestWorkspaceInputWithDefaults instantiates a new RequestWorkspaceInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *RequestWorkspaceInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RequestWorkspaceInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *RequestWorkspaceInput) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *RequestWorkspaceInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *RequestWorkspaceInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *RequestWorkspaceInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *RequestWorkspaceInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *RequestWorkspaceInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *RequestWorkspaceInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetVariables

`func (o *RequestWorkspaceInput) GetVariables() map[string]string`

GetVariables returns the Variables field if non-nil, zero value otherwise.

### GetVariablesOk

`func (o *RequestWorkspaceInput) GetVariablesOk() (*map[string]string, bool)`

GetVariablesOk returns a tuple with the Variables field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariables

`func (o *RequestWorkspaceInput) SetVariables(v map[string]string)`

SetVariables sets Variables field to given value.

### HasVariables

`func (o *RequestWorkspaceInput) HasVariables() bool`

HasVariables returns a boolean if a field has been set.

### GetGlobalVariableFallbacks

`func (o *RequestWorkspaceInput) GetGlobalVariableFallbacks() map[string]string`

GetGlobalVariableFallbacks returns the GlobalVariableFallbacks field if non-nil, zero value otherwise.

### GetGlobalVariableFallbacksOk

`func (o *RequestWorkspaceInput) GetGlobalVariableFallbacksOk() (*map[string]string, bool)`

GetGlobalVariableFallbacksOk returns a tuple with the GlobalVariableFallbacks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGlobalVariableFallbacks

`func (o *RequestWorkspaceInput) SetGlobalVariableFallbacks(v map[string]string)`

SetGlobalVariableFallbacks sets GlobalVariableFallbacks field to given value.

### HasGlobalVariableFallbacks

`func (o *RequestWorkspaceInput) HasGlobalVariableFallbacks() bool`

HasGlobalVariableFallbacks returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
