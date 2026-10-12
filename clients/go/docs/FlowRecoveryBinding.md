# FlowRecoveryBinding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Key** | **string** |  |
**Label** | Pointer to **NullableString** |  | [optional]
**Path** | **string** | JSON Pointer in the safe authoring definition. |
**ValueType** | **string** |  |
**DependencyKey** | Pointer to **NullableString** | Selected dependency identity; null for a Flow-level binding. | [optional]

## Methods

### NewFlowRecoveryBinding

`func NewFlowRecoveryBinding(key string, path string, valueType string, ) *FlowRecoveryBinding`

NewFlowRecoveryBinding instantiates a new FlowRecoveryBinding object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowRecoveryBindingWithDefaults

`func NewFlowRecoveryBindingWithDefaults() *FlowRecoveryBinding`

NewFlowRecoveryBindingWithDefaults instantiates a new FlowRecoveryBinding object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetKey

`func (o *FlowRecoveryBinding) GetKey() string`

GetKey returns the Key field if non-nil, zero value otherwise.

### GetKeyOk

`func (o *FlowRecoveryBinding) GetKeyOk() (*string, bool)`

GetKeyOk returns a tuple with the Key field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKey

`func (o *FlowRecoveryBinding) SetKey(v string)`

SetKey sets Key field to given value.


### GetLabel

`func (o *FlowRecoveryBinding) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *FlowRecoveryBinding) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *FlowRecoveryBinding) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *FlowRecoveryBinding) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### SetLabelNil

`func (o *FlowRecoveryBinding) SetLabelNil(b bool)`

 SetLabelNil sets the value for Label to be an explicit nil

### UnsetLabel
`func (o *FlowRecoveryBinding) UnsetLabel()`

UnsetLabel ensures that no value is present for Label, not even an explicit nil
### GetPath

`func (o *FlowRecoveryBinding) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *FlowRecoveryBinding) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *FlowRecoveryBinding) SetPath(v string)`

SetPath sets Path field to given value.


### GetValueType

`func (o *FlowRecoveryBinding) GetValueType() string`

GetValueType returns the ValueType field if non-nil, zero value otherwise.

### GetValueTypeOk

`func (o *FlowRecoveryBinding) GetValueTypeOk() (*string, bool)`

GetValueTypeOk returns a tuple with the ValueType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValueType

`func (o *FlowRecoveryBinding) SetValueType(v string)`

SetValueType sets ValueType field to given value.


### GetDependencyKey

`func (o *FlowRecoveryBinding) GetDependencyKey() string`

GetDependencyKey returns the DependencyKey field if non-nil, zero value otherwise.

### GetDependencyKeyOk

`func (o *FlowRecoveryBinding) GetDependencyKeyOk() (*string, bool)`

GetDependencyKeyOk returns a tuple with the DependencyKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependencyKey

`func (o *FlowRecoveryBinding) SetDependencyKey(v string)`

SetDependencyKey sets DependencyKey field to given value.

### HasDependencyKey

`func (o *FlowRecoveryBinding) HasDependencyKey() bool`

HasDependencyKey returns a boolean if a field has been set.

### SetDependencyKeyNil

`func (o *FlowRecoveryBinding) SetDependencyKeyNil(b bool)`

 SetDependencyKeyNil sets the value for DependencyKey to be an explicit nil

### UnsetDependencyKey
`func (o *FlowRecoveryBinding) UnsetDependencyKey()`

UnsetDependencyKey ensures that no value is present for DependencyKey, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
