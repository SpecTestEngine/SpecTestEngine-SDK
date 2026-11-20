# PreparationOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Path** | **string** | JSON Pointer into the native response surface (REST body, GraphQL envelope, namespace-local SOAP projection, or Streaming events) |
**Type** | Pointer to **NullableString** |  | [optional]
**Required** | **bool** |  | [default to true]

## Methods

### NewPreparationOutput

`func NewPreparationOutput(path string, required bool, ) *PreparationOutput`

NewPreparationOutput instantiates a new PreparationOutput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPreparationOutputWithDefaults

`func NewPreparationOutputWithDefaults() *PreparationOutput`

NewPreparationOutputWithDefaults instantiates a new PreparationOutput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPath

`func (o *PreparationOutput) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *PreparationOutput) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *PreparationOutput) SetPath(v string)`

SetPath sets Path field to given value.


### GetType

`func (o *PreparationOutput) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *PreparationOutput) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *PreparationOutput) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *PreparationOutput) HasType() bool`

HasType returns a boolean if a field has been set.

### SetTypeNil

`func (o *PreparationOutput) SetTypeNil(b bool)`

 SetTypeNil sets the value for Type to be an explicit nil

### UnsetType
`func (o *PreparationOutput) UnsetType()`

UnsetType ensures that no value is present for Type, not even an explicit nil
### GetRequired

`func (o *PreparationOutput) GetRequired() bool`

GetRequired returns the Required field if non-nil, zero value otherwise.

### GetRequiredOk

`func (o *PreparationOutput) GetRequiredOk() (*bool, bool)`

GetRequiredOk returns a tuple with the Required field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequired

`func (o *PreparationOutput) SetRequired(v bool)`

SetRequired sets Required field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
