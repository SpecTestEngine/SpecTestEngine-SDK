# ArtifactGenerationProfileEnvironmentInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EnvironmentKey** | **string** |  |
**ResolutionMode** | **string** |  |
**BaseUrlMode** | Pointer to [**AtfBaseUrlMode**](AtfBaseUrlMode.md) |  | [optional]
**BaseUrlVariableName** | Pointer to **string** |  | [optional]

## Methods

### NewArtifactGenerationProfileEnvironmentInput

`func NewArtifactGenerationProfileEnvironmentInput(environmentKey string, resolutionMode string, ) *ArtifactGenerationProfileEnvironmentInput`

NewArtifactGenerationProfileEnvironmentInput instantiates a new ArtifactGenerationProfileEnvironmentInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactGenerationProfileEnvironmentInputWithDefaults

`func NewArtifactGenerationProfileEnvironmentInputWithDefaults() *ArtifactGenerationProfileEnvironmentInput`

NewArtifactGenerationProfileEnvironmentInputWithDefaults instantiates a new ArtifactGenerationProfileEnvironmentInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnvironmentKey

`func (o *ArtifactGenerationProfileEnvironmentInput) GetEnvironmentKey() string`

GetEnvironmentKey returns the EnvironmentKey field if non-nil, zero value otherwise.

### GetEnvironmentKeyOk

`func (o *ArtifactGenerationProfileEnvironmentInput) GetEnvironmentKeyOk() (*string, bool)`

GetEnvironmentKeyOk returns a tuple with the EnvironmentKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironmentKey

`func (o *ArtifactGenerationProfileEnvironmentInput) SetEnvironmentKey(v string)`

SetEnvironmentKey sets EnvironmentKey field to given value.


### GetResolutionMode

`func (o *ArtifactGenerationProfileEnvironmentInput) GetResolutionMode() string`

GetResolutionMode returns the ResolutionMode field if non-nil, zero value otherwise.

### GetResolutionModeOk

`func (o *ArtifactGenerationProfileEnvironmentInput) GetResolutionModeOk() (*string, bool)`

GetResolutionModeOk returns a tuple with the ResolutionMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResolutionMode

`func (o *ArtifactGenerationProfileEnvironmentInput) SetResolutionMode(v string)`

SetResolutionMode sets ResolutionMode field to given value.


### GetBaseUrlMode

`func (o *ArtifactGenerationProfileEnvironmentInput) GetBaseUrlMode() AtfBaseUrlMode`

GetBaseUrlMode returns the BaseUrlMode field if non-nil, zero value otherwise.

### GetBaseUrlModeOk

`func (o *ArtifactGenerationProfileEnvironmentInput) GetBaseUrlModeOk() (*AtfBaseUrlMode, bool)`

GetBaseUrlModeOk returns a tuple with the BaseUrlMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseUrlMode

`func (o *ArtifactGenerationProfileEnvironmentInput) SetBaseUrlMode(v AtfBaseUrlMode)`

SetBaseUrlMode sets BaseUrlMode field to given value.

### HasBaseUrlMode

`func (o *ArtifactGenerationProfileEnvironmentInput) HasBaseUrlMode() bool`

HasBaseUrlMode returns a boolean if a field has been set.

### GetBaseUrlVariableName

`func (o *ArtifactGenerationProfileEnvironmentInput) GetBaseUrlVariableName() string`

GetBaseUrlVariableName returns the BaseUrlVariableName field if non-nil, zero value otherwise.

### GetBaseUrlVariableNameOk

`func (o *ArtifactGenerationProfileEnvironmentInput) GetBaseUrlVariableNameOk() (*string, bool)`

GetBaseUrlVariableNameOk returns a tuple with the BaseUrlVariableName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseUrlVariableName

`func (o *ArtifactGenerationProfileEnvironmentInput) SetBaseUrlVariableName(v string)`

SetBaseUrlVariableName sets BaseUrlVariableName field to given value.

### HasBaseUrlVariableName

`func (o *ArtifactGenerationProfileEnvironmentInput) HasBaseUrlVariableName() bool`

HasBaseUrlVariableName returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


