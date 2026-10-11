# FlowStepInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StepType** | **string** |  |
**OrderIndex** | **int32** |  |
**SpecId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**SpecType** | Pointer to [**NullableSpecType**](SpecType.md) |  | [optional]
**SpecName** | Pointer to **NullableString** |  | [optional]
**UiMacroId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**UiMacro** | Pointer to [**NullableBrowserMacroInput**](BrowserMacroInput.md) |  | [optional]
**BrowserAction** | Pointer to [**NullableBrowserActionInput**](BrowserActionInput.md) |  | [optional]
**StoreValues** | Pointer to **map[string]string** |  | [optional]
**OverrideValues** | Pointer to **map[string]interface{}** |  | [optional]

## Methods

### NewFlowStepInput

`func NewFlowStepInput(stepType string, orderIndex int32, ) *FlowStepInput`

NewFlowStepInput instantiates a new FlowStepInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowStepInputWithDefaults

`func NewFlowStepInputWithDefaults() *FlowStepInput`

NewFlowStepInputWithDefaults instantiates a new FlowStepInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStepType

`func (o *FlowStepInput) GetStepType() string`

GetStepType returns the StepType field if non-nil, zero value otherwise.

### GetStepTypeOk

`func (o *FlowStepInput) GetStepTypeOk() (*string, bool)`

GetStepTypeOk returns a tuple with the StepType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepType

`func (o *FlowStepInput) SetStepType(v string)`

SetStepType sets StepType field to given value.


### GetOrderIndex

`func (o *FlowStepInput) GetOrderIndex() int32`

GetOrderIndex returns the OrderIndex field if non-nil, zero value otherwise.

### GetOrderIndexOk

`func (o *FlowStepInput) GetOrderIndexOk() (*int32, bool)`

GetOrderIndexOk returns a tuple with the OrderIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrderIndex

`func (o *FlowStepInput) SetOrderIndex(v int32)`

SetOrderIndex sets OrderIndex field to given value.


### GetSpecId

`func (o *FlowStepInput) GetSpecId() string`

GetSpecId returns the SpecId field if non-nil, zero value otherwise.

### GetSpecIdOk

`func (o *FlowStepInput) GetSpecIdOk() (*string, bool)`

GetSpecIdOk returns a tuple with the SpecId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecId

`func (o *FlowStepInput) SetSpecId(v string)`

SetSpecId sets SpecId field to given value.

### HasSpecId

`func (o *FlowStepInput) HasSpecId() bool`

HasSpecId returns a boolean if a field has been set.

### SetSpecIdNil

`func (o *FlowStepInput) SetSpecIdNil(b bool)`

 SetSpecIdNil sets the value for SpecId to be an explicit nil

### UnsetSpecId
`func (o *FlowStepInput) UnsetSpecId()`

UnsetSpecId ensures that no value is present for SpecId, not even an explicit nil
### GetSpecType

`func (o *FlowStepInput) GetSpecType() SpecType`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *FlowStepInput) GetSpecTypeOk() (*SpecType, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *FlowStepInput) SetSpecType(v SpecType)`

SetSpecType sets SpecType field to given value.

### HasSpecType

`func (o *FlowStepInput) HasSpecType() bool`

HasSpecType returns a boolean if a field has been set.

### SetSpecTypeNil

`func (o *FlowStepInput) SetSpecTypeNil(b bool)`

 SetSpecTypeNil sets the value for SpecType to be an explicit nil

### UnsetSpecType
`func (o *FlowStepInput) UnsetSpecType()`

UnsetSpecType ensures that no value is present for SpecType, not even an explicit nil
### GetSpecName

`func (o *FlowStepInput) GetSpecName() string`

GetSpecName returns the SpecName field if non-nil, zero value otherwise.

### GetSpecNameOk

`func (o *FlowStepInput) GetSpecNameOk() (*string, bool)`

GetSpecNameOk returns a tuple with the SpecName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecName

`func (o *FlowStepInput) SetSpecName(v string)`

SetSpecName sets SpecName field to given value.

### HasSpecName

`func (o *FlowStepInput) HasSpecName() bool`

HasSpecName returns a boolean if a field has been set.

### SetSpecNameNil

`func (o *FlowStepInput) SetSpecNameNil(b bool)`

 SetSpecNameNil sets the value for SpecName to be an explicit nil

### UnsetSpecName
`func (o *FlowStepInput) UnsetSpecName()`

UnsetSpecName ensures that no value is present for SpecName, not even an explicit nil
### GetUiMacroId

`func (o *FlowStepInput) GetUiMacroId() string`

GetUiMacroId returns the UiMacroId field if non-nil, zero value otherwise.

### GetUiMacroIdOk

`func (o *FlowStepInput) GetUiMacroIdOk() (*string, bool)`

GetUiMacroIdOk returns a tuple with the UiMacroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiMacroId

`func (o *FlowStepInput) SetUiMacroId(v string)`

SetUiMacroId sets UiMacroId field to given value.

### HasUiMacroId

`func (o *FlowStepInput) HasUiMacroId() bool`

HasUiMacroId returns a boolean if a field has been set.

### SetUiMacroIdNil

`func (o *FlowStepInput) SetUiMacroIdNil(b bool)`

 SetUiMacroIdNil sets the value for UiMacroId to be an explicit nil

### UnsetUiMacroId
`func (o *FlowStepInput) UnsetUiMacroId()`

UnsetUiMacroId ensures that no value is present for UiMacroId, not even an explicit nil
### GetUiMacro

`func (o *FlowStepInput) GetUiMacro() BrowserMacroInput`

GetUiMacro returns the UiMacro field if non-nil, zero value otherwise.

### GetUiMacroOk

`func (o *FlowStepInput) GetUiMacroOk() (*BrowserMacroInput, bool)`

GetUiMacroOk returns a tuple with the UiMacro field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiMacro

`func (o *FlowStepInput) SetUiMacro(v BrowserMacroInput)`

SetUiMacro sets UiMacro field to given value.

### HasUiMacro

`func (o *FlowStepInput) HasUiMacro() bool`

HasUiMacro returns a boolean if a field has been set.

### SetUiMacroNil

`func (o *FlowStepInput) SetUiMacroNil(b bool)`

 SetUiMacroNil sets the value for UiMacro to be an explicit nil

### UnsetUiMacro
`func (o *FlowStepInput) UnsetUiMacro()`

UnsetUiMacro ensures that no value is present for UiMacro, not even an explicit nil
### GetBrowserAction

`func (o *FlowStepInput) GetBrowserAction() BrowserActionInput`

GetBrowserAction returns the BrowserAction field if non-nil, zero value otherwise.

### GetBrowserActionOk

`func (o *FlowStepInput) GetBrowserActionOk() (*BrowserActionInput, bool)`

GetBrowserActionOk returns a tuple with the BrowserAction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrowserAction

`func (o *FlowStepInput) SetBrowserAction(v BrowserActionInput)`

SetBrowserAction sets BrowserAction field to given value.

### HasBrowserAction

`func (o *FlowStepInput) HasBrowserAction() bool`

HasBrowserAction returns a boolean if a field has been set.

### SetBrowserActionNil

`func (o *FlowStepInput) SetBrowserActionNil(b bool)`

 SetBrowserActionNil sets the value for BrowserAction to be an explicit nil

### UnsetBrowserAction
`func (o *FlowStepInput) UnsetBrowserAction()`

UnsetBrowserAction ensures that no value is present for BrowserAction, not even an explicit nil
### GetStoreValues

`func (o *FlowStepInput) GetStoreValues() map[string]string`

GetStoreValues returns the StoreValues field if non-nil, zero value otherwise.

### GetStoreValuesOk

`func (o *FlowStepInput) GetStoreValuesOk() (*map[string]string, bool)`

GetStoreValuesOk returns a tuple with the StoreValues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStoreValues

`func (o *FlowStepInput) SetStoreValues(v map[string]string)`

SetStoreValues sets StoreValues field to given value.

### HasStoreValues

`func (o *FlowStepInput) HasStoreValues() bool`

HasStoreValues returns a boolean if a field has been set.

### GetOverrideValues

`func (o *FlowStepInput) GetOverrideValues() map[string]interface{}`

GetOverrideValues returns the OverrideValues field if non-nil, zero value otherwise.

### GetOverrideValuesOk

`func (o *FlowStepInput) GetOverrideValuesOk() (*map[string]interface{}, bool)`

GetOverrideValuesOk returns a tuple with the OverrideValues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOverrideValues

`func (o *FlowStepInput) SetOverrideValues(v map[string]interface{})`

SetOverrideValues sets OverrideValues field to given value.

### HasOverrideValues

`func (o *FlowStepInput) HasOverrideValues() bool`

HasOverrideValues returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
