# CompiledSpecification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Format** | [**ContentFormat**](ContentFormat.md) |  | [default to CONTENTFORMAT_JSON]
**RawSpec** | **string** |  |
**CompiledSpec** | **map[string]interface{}** |  |

## Methods

### NewCompiledSpecification

`func NewCompiledSpecification(format ContentFormat, rawSpec string, compiledSpec map[string]interface{}, ) *CompiledSpecification`

NewCompiledSpecification instantiates a new CompiledSpecification object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCompiledSpecificationWithDefaults

`func NewCompiledSpecificationWithDefaults() *CompiledSpecification`

NewCompiledSpecificationWithDefaults instantiates a new CompiledSpecification object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFormat

`func (o *CompiledSpecification) GetFormat() ContentFormat`

GetFormat returns the Format field if non-nil, zero value otherwise.

### GetFormatOk

`func (o *CompiledSpecification) GetFormatOk() (*ContentFormat, bool)`

GetFormatOk returns a tuple with the Format field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFormat

`func (o *CompiledSpecification) SetFormat(v ContentFormat)`

SetFormat sets Format field to given value.


### GetRawSpec

`func (o *CompiledSpecification) GetRawSpec() string`

GetRawSpec returns the RawSpec field if non-nil, zero value otherwise.

### GetRawSpecOk

`func (o *CompiledSpecification) GetRawSpecOk() (*string, bool)`

GetRawSpecOk returns a tuple with the RawSpec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRawSpec

`func (o *CompiledSpecification) SetRawSpec(v string)`

SetRawSpec sets RawSpec field to given value.


### GetCompiledSpec

`func (o *CompiledSpecification) GetCompiledSpec() map[string]interface{}`

GetCompiledSpec returns the CompiledSpec field if non-nil, zero value otherwise.

### GetCompiledSpecOk

`func (o *CompiledSpecification) GetCompiledSpecOk() (*map[string]interface{}, bool)`

GetCompiledSpecOk returns a tuple with the CompiledSpec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompiledSpec

`func (o *CompiledSpecification) SetCompiledSpec(v map[string]interface{})`

SetCompiledSpec sets CompiledSpec field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


