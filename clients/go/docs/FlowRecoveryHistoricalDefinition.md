# FlowRecoveryHistoricalDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FlowId** | **string** |  |
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**GlobalVariableFallbacks** | Pointer to **map[string]string** |  | [optional]
**BrowserStartUrl** | Pointer to **NullableString** |  | [optional]
**BrowserViewportWidth** | Pointer to **NullableInt32** |  | [optional]
**BrowserViewportHeight** | Pointer to **NullableInt32** |  | [optional]
**BrowserViewportPreset** | Pointer to **NullableString** |  | [optional]
**Steps** | [**[]FlowStep**](FlowStep.md) |  |

## Methods

### NewFlowRecoveryHistoricalDefinition

`func NewFlowRecoveryHistoricalDefinition(flowId string, name string, steps []FlowStep, ) *FlowRecoveryHistoricalDefinition`

NewFlowRecoveryHistoricalDefinition instantiates a new FlowRecoveryHistoricalDefinition object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowRecoveryHistoricalDefinitionWithDefaults

`func NewFlowRecoveryHistoricalDefinitionWithDefaults() *FlowRecoveryHistoricalDefinition`

NewFlowRecoveryHistoricalDefinitionWithDefaults instantiates a new FlowRecoveryHistoricalDefinition object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFlowId

`func (o *FlowRecoveryHistoricalDefinition) GetFlowId() string`

GetFlowId returns the FlowId field if non-nil, zero value otherwise.

### GetFlowIdOk

`func (o *FlowRecoveryHistoricalDefinition) GetFlowIdOk() (*string, bool)`

GetFlowIdOk returns a tuple with the FlowId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlowId

`func (o *FlowRecoveryHistoricalDefinition) SetFlowId(v string)`

SetFlowId sets FlowId field to given value.


### GetName

`func (o *FlowRecoveryHistoricalDefinition) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *FlowRecoveryHistoricalDefinition) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *FlowRecoveryHistoricalDefinition) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *FlowRecoveryHistoricalDefinition) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *FlowRecoveryHistoricalDefinition) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *FlowRecoveryHistoricalDefinition) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *FlowRecoveryHistoricalDefinition) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *FlowRecoveryHistoricalDefinition) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *FlowRecoveryHistoricalDefinition) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetGlobalVariableFallbacks

`func (o *FlowRecoveryHistoricalDefinition) GetGlobalVariableFallbacks() map[string]string`

GetGlobalVariableFallbacks returns the GlobalVariableFallbacks field if non-nil, zero value otherwise.

### GetGlobalVariableFallbacksOk

`func (o *FlowRecoveryHistoricalDefinition) GetGlobalVariableFallbacksOk() (*map[string]string, bool)`

GetGlobalVariableFallbacksOk returns a tuple with the GlobalVariableFallbacks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGlobalVariableFallbacks

`func (o *FlowRecoveryHistoricalDefinition) SetGlobalVariableFallbacks(v map[string]string)`

SetGlobalVariableFallbacks sets GlobalVariableFallbacks field to given value.

### HasGlobalVariableFallbacks

`func (o *FlowRecoveryHistoricalDefinition) HasGlobalVariableFallbacks() bool`

HasGlobalVariableFallbacks returns a boolean if a field has been set.

### GetBrowserStartUrl

`func (o *FlowRecoveryHistoricalDefinition) GetBrowserStartUrl() string`

GetBrowserStartUrl returns the BrowserStartUrl field if non-nil, zero value otherwise.

### GetBrowserStartUrlOk

`func (o *FlowRecoveryHistoricalDefinition) GetBrowserStartUrlOk() (*string, bool)`

GetBrowserStartUrlOk returns a tuple with the BrowserStartUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrowserStartUrl

`func (o *FlowRecoveryHistoricalDefinition) SetBrowserStartUrl(v string)`

SetBrowserStartUrl sets BrowserStartUrl field to given value.

### HasBrowserStartUrl

`func (o *FlowRecoveryHistoricalDefinition) HasBrowserStartUrl() bool`

HasBrowserStartUrl returns a boolean if a field has been set.

### SetBrowserStartUrlNil

`func (o *FlowRecoveryHistoricalDefinition) SetBrowserStartUrlNil(b bool)`

 SetBrowserStartUrlNil sets the value for BrowserStartUrl to be an explicit nil

### UnsetBrowserStartUrl
`func (o *FlowRecoveryHistoricalDefinition) UnsetBrowserStartUrl()`

UnsetBrowserStartUrl ensures that no value is present for BrowserStartUrl, not even an explicit nil
### GetBrowserViewportWidth

`func (o *FlowRecoveryHistoricalDefinition) GetBrowserViewportWidth() int32`

GetBrowserViewportWidth returns the BrowserViewportWidth field if non-nil, zero value otherwise.

### GetBrowserViewportWidthOk

`func (o *FlowRecoveryHistoricalDefinition) GetBrowserViewportWidthOk() (*int32, bool)`

GetBrowserViewportWidthOk returns a tuple with the BrowserViewportWidth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrowserViewportWidth

`func (o *FlowRecoveryHistoricalDefinition) SetBrowserViewportWidth(v int32)`

SetBrowserViewportWidth sets BrowserViewportWidth field to given value.

### HasBrowserViewportWidth

`func (o *FlowRecoveryHistoricalDefinition) HasBrowserViewportWidth() bool`

HasBrowserViewportWidth returns a boolean if a field has been set.

### SetBrowserViewportWidthNil

`func (o *FlowRecoveryHistoricalDefinition) SetBrowserViewportWidthNil(b bool)`

 SetBrowserViewportWidthNil sets the value for BrowserViewportWidth to be an explicit nil

### UnsetBrowserViewportWidth
`func (o *FlowRecoveryHistoricalDefinition) UnsetBrowserViewportWidth()`

UnsetBrowserViewportWidth ensures that no value is present for BrowserViewportWidth, not even an explicit nil
### GetBrowserViewportHeight

`func (o *FlowRecoveryHistoricalDefinition) GetBrowserViewportHeight() int32`

GetBrowserViewportHeight returns the BrowserViewportHeight field if non-nil, zero value otherwise.

### GetBrowserViewportHeightOk

`func (o *FlowRecoveryHistoricalDefinition) GetBrowserViewportHeightOk() (*int32, bool)`

GetBrowserViewportHeightOk returns a tuple with the BrowserViewportHeight field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrowserViewportHeight

`func (o *FlowRecoveryHistoricalDefinition) SetBrowserViewportHeight(v int32)`

SetBrowserViewportHeight sets BrowserViewportHeight field to given value.

### HasBrowserViewportHeight

`func (o *FlowRecoveryHistoricalDefinition) HasBrowserViewportHeight() bool`

HasBrowserViewportHeight returns a boolean if a field has been set.

### SetBrowserViewportHeightNil

`func (o *FlowRecoveryHistoricalDefinition) SetBrowserViewportHeightNil(b bool)`

 SetBrowserViewportHeightNil sets the value for BrowserViewportHeight to be an explicit nil

### UnsetBrowserViewportHeight
`func (o *FlowRecoveryHistoricalDefinition) UnsetBrowserViewportHeight()`

UnsetBrowserViewportHeight ensures that no value is present for BrowserViewportHeight, not even an explicit nil
### GetBrowserViewportPreset

`func (o *FlowRecoveryHistoricalDefinition) GetBrowserViewportPreset() string`

GetBrowserViewportPreset returns the BrowserViewportPreset field if non-nil, zero value otherwise.

### GetBrowserViewportPresetOk

`func (o *FlowRecoveryHistoricalDefinition) GetBrowserViewportPresetOk() (*string, bool)`

GetBrowserViewportPresetOk returns a tuple with the BrowserViewportPreset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrowserViewportPreset

`func (o *FlowRecoveryHistoricalDefinition) SetBrowserViewportPreset(v string)`

SetBrowserViewportPreset sets BrowserViewportPreset field to given value.

### HasBrowserViewportPreset

`func (o *FlowRecoveryHistoricalDefinition) HasBrowserViewportPreset() bool`

HasBrowserViewportPreset returns a boolean if a field has been set.

### SetBrowserViewportPresetNil

`func (o *FlowRecoveryHistoricalDefinition) SetBrowserViewportPresetNil(b bool)`

 SetBrowserViewportPresetNil sets the value for BrowserViewportPreset to be an explicit nil

### UnsetBrowserViewportPreset
`func (o *FlowRecoveryHistoricalDefinition) UnsetBrowserViewportPreset()`

UnsetBrowserViewportPreset ensures that no value is present for BrowserViewportPreset, not even an explicit nil
### GetSteps

`func (o *FlowRecoveryHistoricalDefinition) GetSteps() []FlowStep`

GetSteps returns the Steps field if non-nil, zero value otherwise.

### GetStepsOk

`func (o *FlowRecoveryHistoricalDefinition) GetStepsOk() (*[]FlowStep, bool)`

GetStepsOk returns a tuple with the Steps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteps

`func (o *FlowRecoveryHistoricalDefinition) SetSteps(v []FlowStep)`

SetSteps sets Steps field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
