# OpenApiGenerationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OpenApiUrl** | Pointer to **NullableString** |  | [optional]
**GeneratedSpecsCount** | **int32** |  |
**GeneratedSpecs** | **[]map[string]interface{}** |  |
**IncludeNegativeTests** | **bool** |  |
**GenerateFlowScenarios** | **bool** |  |
**GeneratedFlowScenariosCount** | Pointer to **NullableInt32** |  | [optional]
**GeneratedFlowScenarios** | Pointer to [**[]FlowInput**](FlowInput.md) |  | [optional]
**Coverage** | Pointer to **map[string]interface{}** |  | [optional]

## Methods

### NewOpenApiGenerationResult

`func NewOpenApiGenerationResult(generatedSpecsCount int32, generatedSpecs []map[string]interface{}, includeNegativeTests bool, generateFlowScenarios bool, ) *OpenApiGenerationResult`

NewOpenApiGenerationResult instantiates a new OpenApiGenerationResult object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenApiGenerationResultWithDefaults

`func NewOpenApiGenerationResultWithDefaults() *OpenApiGenerationResult`

NewOpenApiGenerationResultWithDefaults instantiates a new OpenApiGenerationResult object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOpenApiUrl

`func (o *OpenApiGenerationResult) GetOpenApiUrl() string`

GetOpenApiUrl returns the OpenApiUrl field if non-nil, zero value otherwise.

### GetOpenApiUrlOk

`func (o *OpenApiGenerationResult) GetOpenApiUrlOk() (*string, bool)`

GetOpenApiUrlOk returns a tuple with the OpenApiUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenApiUrl

`func (o *OpenApiGenerationResult) SetOpenApiUrl(v string)`

SetOpenApiUrl sets OpenApiUrl field to given value.

### HasOpenApiUrl

`func (o *OpenApiGenerationResult) HasOpenApiUrl() bool`

HasOpenApiUrl returns a boolean if a field has been set.

### SetOpenApiUrlNil

`func (o *OpenApiGenerationResult) SetOpenApiUrlNil(b bool)`

 SetOpenApiUrlNil sets the value for OpenApiUrl to be an explicit nil

### UnsetOpenApiUrl
`func (o *OpenApiGenerationResult) UnsetOpenApiUrl()`

UnsetOpenApiUrl ensures that no value is present for OpenApiUrl, not even an explicit nil
### GetGeneratedSpecsCount

`func (o *OpenApiGenerationResult) GetGeneratedSpecsCount() int32`

GetGeneratedSpecsCount returns the GeneratedSpecsCount field if non-nil, zero value otherwise.

### GetGeneratedSpecsCountOk

`func (o *OpenApiGenerationResult) GetGeneratedSpecsCountOk() (*int32, bool)`

GetGeneratedSpecsCountOk returns a tuple with the GeneratedSpecsCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGeneratedSpecsCount

`func (o *OpenApiGenerationResult) SetGeneratedSpecsCount(v int32)`

SetGeneratedSpecsCount sets GeneratedSpecsCount field to given value.


### GetGeneratedSpecs

`func (o *OpenApiGenerationResult) GetGeneratedSpecs() []map[string]interface{}`

GetGeneratedSpecs returns the GeneratedSpecs field if non-nil, zero value otherwise.

### GetGeneratedSpecsOk

`func (o *OpenApiGenerationResult) GetGeneratedSpecsOk() (*[]map[string]interface{}, bool)`

GetGeneratedSpecsOk returns a tuple with the GeneratedSpecs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGeneratedSpecs

`func (o *OpenApiGenerationResult) SetGeneratedSpecs(v []map[string]interface{})`

SetGeneratedSpecs sets GeneratedSpecs field to given value.


### GetIncludeNegativeTests

`func (o *OpenApiGenerationResult) GetIncludeNegativeTests() bool`

GetIncludeNegativeTests returns the IncludeNegativeTests field if non-nil, zero value otherwise.

### GetIncludeNegativeTestsOk

`func (o *OpenApiGenerationResult) GetIncludeNegativeTestsOk() (*bool, bool)`

GetIncludeNegativeTestsOk returns a tuple with the IncludeNegativeTests field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeNegativeTests

`func (o *OpenApiGenerationResult) SetIncludeNegativeTests(v bool)`

SetIncludeNegativeTests sets IncludeNegativeTests field to given value.


### GetGenerateFlowScenarios

`func (o *OpenApiGenerationResult) GetGenerateFlowScenarios() bool`

GetGenerateFlowScenarios returns the GenerateFlowScenarios field if non-nil, zero value otherwise.

### GetGenerateFlowScenariosOk

`func (o *OpenApiGenerationResult) GetGenerateFlowScenariosOk() (*bool, bool)`

GetGenerateFlowScenariosOk returns a tuple with the GenerateFlowScenarios field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGenerateFlowScenarios

`func (o *OpenApiGenerationResult) SetGenerateFlowScenarios(v bool)`

SetGenerateFlowScenarios sets GenerateFlowScenarios field to given value.


### GetGeneratedFlowScenariosCount

`func (o *OpenApiGenerationResult) GetGeneratedFlowScenariosCount() int32`

GetGeneratedFlowScenariosCount returns the GeneratedFlowScenariosCount field if non-nil, zero value otherwise.

### GetGeneratedFlowScenariosCountOk

`func (o *OpenApiGenerationResult) GetGeneratedFlowScenariosCountOk() (*int32, bool)`

GetGeneratedFlowScenariosCountOk returns a tuple with the GeneratedFlowScenariosCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGeneratedFlowScenariosCount

`func (o *OpenApiGenerationResult) SetGeneratedFlowScenariosCount(v int32)`

SetGeneratedFlowScenariosCount sets GeneratedFlowScenariosCount field to given value.

### HasGeneratedFlowScenariosCount

`func (o *OpenApiGenerationResult) HasGeneratedFlowScenariosCount() bool`

HasGeneratedFlowScenariosCount returns a boolean if a field has been set.

### SetGeneratedFlowScenariosCountNil

`func (o *OpenApiGenerationResult) SetGeneratedFlowScenariosCountNil(b bool)`

 SetGeneratedFlowScenariosCountNil sets the value for GeneratedFlowScenariosCount to be an explicit nil

### UnsetGeneratedFlowScenariosCount
`func (o *OpenApiGenerationResult) UnsetGeneratedFlowScenariosCount()`

UnsetGeneratedFlowScenariosCount ensures that no value is present for GeneratedFlowScenariosCount, not even an explicit nil
### GetGeneratedFlowScenarios

`func (o *OpenApiGenerationResult) GetGeneratedFlowScenarios() []FlowInput`

GetGeneratedFlowScenarios returns the GeneratedFlowScenarios field if non-nil, zero value otherwise.

### GetGeneratedFlowScenariosOk

`func (o *OpenApiGenerationResult) GetGeneratedFlowScenariosOk() (*[]FlowInput, bool)`

GetGeneratedFlowScenariosOk returns a tuple with the GeneratedFlowScenarios field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGeneratedFlowScenarios

`func (o *OpenApiGenerationResult) SetGeneratedFlowScenarios(v []FlowInput)`

SetGeneratedFlowScenarios sets GeneratedFlowScenarios field to given value.

### HasGeneratedFlowScenarios

`func (o *OpenApiGenerationResult) HasGeneratedFlowScenarios() bool`

HasGeneratedFlowScenarios returns a boolean if a field has been set.

### SetGeneratedFlowScenariosNil

`func (o *OpenApiGenerationResult) SetGeneratedFlowScenariosNil(b bool)`

 SetGeneratedFlowScenariosNil sets the value for GeneratedFlowScenarios to be an explicit nil

### UnsetGeneratedFlowScenarios
`func (o *OpenApiGenerationResult) UnsetGeneratedFlowScenarios()`

UnsetGeneratedFlowScenarios ensures that no value is present for GeneratedFlowScenarios, not even an explicit nil
### GetCoverage

`func (o *OpenApiGenerationResult) GetCoverage() map[string]interface{}`

GetCoverage returns the Coverage field if non-nil, zero value otherwise.

### GetCoverageOk

`func (o *OpenApiGenerationResult) GetCoverageOk() (*map[string]interface{}, bool)`

GetCoverageOk returns a tuple with the Coverage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCoverage

`func (o *OpenApiGenerationResult) SetCoverage(v map[string]interface{})`

SetCoverage sets Coverage field to given value.

### HasCoverage

`func (o *OpenApiGenerationResult) HasCoverage() bool`

HasCoverage returns a boolean if a field has been set.

### SetCoverageNil

`func (o *OpenApiGenerationResult) SetCoverageNil(b bool)`

 SetCoverageNil sets the value for Coverage to be an explicit nil

### UnsetCoverage
`func (o *OpenApiGenerationResult) UnsetCoverage()`

UnsetCoverage ensures that no value is present for Coverage, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
