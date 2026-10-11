# SpecGenerationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SpecGenerationType** | **string** |  |
**GeneratedSpec** | **map[string]interface{}** | Complete executable REST, SOAP, GraphQL, or Streaming specification DSL. |

## Methods

### NewSpecGenerationResult

`func NewSpecGenerationResult(specGenerationType string, generatedSpec map[string]interface{}, ) *SpecGenerationResult`

NewSpecGenerationResult instantiates a new SpecGenerationResult object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSpecGenerationResultWithDefaults

`func NewSpecGenerationResultWithDefaults() *SpecGenerationResult`

NewSpecGenerationResultWithDefaults instantiates a new SpecGenerationResult object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSpecGenerationType

`func (o *SpecGenerationResult) GetSpecGenerationType() string`

GetSpecGenerationType returns the SpecGenerationType field if non-nil, zero value otherwise.

### GetSpecGenerationTypeOk

`func (o *SpecGenerationResult) GetSpecGenerationTypeOk() (*string, bool)`

GetSpecGenerationTypeOk returns a tuple with the SpecGenerationType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecGenerationType

`func (o *SpecGenerationResult) SetSpecGenerationType(v string)`

SetSpecGenerationType sets SpecGenerationType field to given value.


### GetGeneratedSpec

`func (o *SpecGenerationResult) GetGeneratedSpec() map[string]interface{}`

GetGeneratedSpec returns the GeneratedSpec field if non-nil, zero value otherwise.

### GetGeneratedSpecOk

`func (o *SpecGenerationResult) GetGeneratedSpecOk() (*map[string]interface{}, bool)`

GetGeneratedSpecOk returns a tuple with the GeneratedSpec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGeneratedSpec

`func (o *SpecGenerationResult) SetGeneratedSpec(v map[string]interface{})`

SetGeneratedSpec sets GeneratedSpec field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
