# FlowRecoveryProjection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DefinitionJson** | Pointer to **NullableString** | Safe authoring JSON only; no runtime values or worker grants. | [optional]
**Bindings** | [**[]FlowRecoveryBinding**](FlowRecoveryBinding.md) |  |
**UnavailableReason** | Pointer to **NullableString** |  | [optional]

## Methods

### NewFlowRecoveryProjection

`func NewFlowRecoveryProjection(bindings []FlowRecoveryBinding, ) *FlowRecoveryProjection`

NewFlowRecoveryProjection instantiates a new FlowRecoveryProjection object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowRecoveryProjectionWithDefaults

`func NewFlowRecoveryProjectionWithDefaults() *FlowRecoveryProjection`

NewFlowRecoveryProjectionWithDefaults instantiates a new FlowRecoveryProjection object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDefinitionJson

`func (o *FlowRecoveryProjection) GetDefinitionJson() string`

GetDefinitionJson returns the DefinitionJson field if non-nil, zero value otherwise.

### GetDefinitionJsonOk

`func (o *FlowRecoveryProjection) GetDefinitionJsonOk() (*string, bool)`

GetDefinitionJsonOk returns a tuple with the DefinitionJson field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinitionJson

`func (o *FlowRecoveryProjection) SetDefinitionJson(v string)`

SetDefinitionJson sets DefinitionJson field to given value.

### HasDefinitionJson

`func (o *FlowRecoveryProjection) HasDefinitionJson() bool`

HasDefinitionJson returns a boolean if a field has been set.

### SetDefinitionJsonNil

`func (o *FlowRecoveryProjection) SetDefinitionJsonNil(b bool)`

 SetDefinitionJsonNil sets the value for DefinitionJson to be an explicit nil

### UnsetDefinitionJson
`func (o *FlowRecoveryProjection) UnsetDefinitionJson()`

UnsetDefinitionJson ensures that no value is present for DefinitionJson, not even an explicit nil
### GetBindings

`func (o *FlowRecoveryProjection) GetBindings() []FlowRecoveryBinding`

GetBindings returns the Bindings field if non-nil, zero value otherwise.

### GetBindingsOk

`func (o *FlowRecoveryProjection) GetBindingsOk() (*[]FlowRecoveryBinding, bool)`

GetBindingsOk returns a tuple with the Bindings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBindings

`func (o *FlowRecoveryProjection) SetBindings(v []FlowRecoveryBinding)`

SetBindings sets Bindings field to given value.


### GetUnavailableReason

`func (o *FlowRecoveryProjection) GetUnavailableReason() string`

GetUnavailableReason returns the UnavailableReason field if non-nil, zero value otherwise.

### GetUnavailableReasonOk

`func (o *FlowRecoveryProjection) GetUnavailableReasonOk() (*string, bool)`

GetUnavailableReasonOk returns a tuple with the UnavailableReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnavailableReason

`func (o *FlowRecoveryProjection) SetUnavailableReason(v string)`

SetUnavailableReason sets UnavailableReason field to given value.

### HasUnavailableReason

`func (o *FlowRecoveryProjection) HasUnavailableReason() bool`

HasUnavailableReason returns a boolean if a field has been set.

### SetUnavailableReasonNil

`func (o *FlowRecoveryProjection) SetUnavailableReasonNil(b bool)`

 SetUnavailableReasonNil sets the value for UnavailableReason to be an explicit nil

### UnsetUnavailableReason
`func (o *FlowRecoveryProjection) UnsetUnavailableReason()`

UnsetUnavailableReason ensures that no value is present for UnavailableReason, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
