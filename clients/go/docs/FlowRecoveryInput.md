# FlowRecoveryInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ManifestHash** | **string** |  |
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**Bindings** | **map[string]interface{}** | Exactly the binding keys requested by preview. Values must be scalar strings, numbers or booleans with their declared type, or variable placeholders; nested objects and null are rejected. Total encoded bindings at most 4 MiB. Values are not retained in the operation journal. |

## Methods

### NewFlowRecoveryInput

`func NewFlowRecoveryInput(manifestHash string, name string, bindings map[string]interface{}, ) *FlowRecoveryInput`

NewFlowRecoveryInput instantiates a new FlowRecoveryInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowRecoveryInputWithDefaults

`func NewFlowRecoveryInputWithDefaults() *FlowRecoveryInput`

NewFlowRecoveryInputWithDefaults instantiates a new FlowRecoveryInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetManifestHash

`func (o *FlowRecoveryInput) GetManifestHash() string`

GetManifestHash returns the ManifestHash field if non-nil, zero value otherwise.

### GetManifestHashOk

`func (o *FlowRecoveryInput) GetManifestHashOk() (*string, bool)`

GetManifestHashOk returns a tuple with the ManifestHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManifestHash

`func (o *FlowRecoveryInput) SetManifestHash(v string)`

SetManifestHash sets ManifestHash field to given value.


### GetName

`func (o *FlowRecoveryInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *FlowRecoveryInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *FlowRecoveryInput) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *FlowRecoveryInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *FlowRecoveryInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *FlowRecoveryInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *FlowRecoveryInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *FlowRecoveryInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *FlowRecoveryInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetBindings

`func (o *FlowRecoveryInput) GetBindings() map[string]interface{}`

GetBindings returns the Bindings field if non-nil, zero value otherwise.

### GetBindingsOk

`func (o *FlowRecoveryInput) GetBindingsOk() (*map[string]interface{}, bool)`

GetBindingsOk returns a tuple with the Bindings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBindings

`func (o *FlowRecoveryInput) SetBindings(v map[string]interface{})`

SetBindings sets Bindings field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
