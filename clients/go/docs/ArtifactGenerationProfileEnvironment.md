# ArtifactGenerationProfileEnvironment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EnvironmentKey** | **string** |  |
**ResolutionMode** | **string** |  |
**BaseUrlMode** | Pointer to [**AtfBaseUrlMode**](AtfBaseUrlMode.md) |  | [optional]
**BaseUrlVariableName** | Pointer to **string** |  | [optional]
**SnapshotBundleHash** | Pointer to **NullableString** |  | [optional]
**SnapshotAt** | Pointer to **NullableTime** |  | [optional]
**CachedBundleHash** | Pointer to **NullableString** |  | [optional]
**CachedAt** | Pointer to **NullableTime** |  | [optional]

## Methods

### NewArtifactGenerationProfileEnvironment

`func NewArtifactGenerationProfileEnvironment(environmentKey string, resolutionMode string, ) *ArtifactGenerationProfileEnvironment`

NewArtifactGenerationProfileEnvironment instantiates a new ArtifactGenerationProfileEnvironment object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactGenerationProfileEnvironmentWithDefaults

`func NewArtifactGenerationProfileEnvironmentWithDefaults() *ArtifactGenerationProfileEnvironment`

NewArtifactGenerationProfileEnvironmentWithDefaults instantiates a new ArtifactGenerationProfileEnvironment object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnvironmentKey

`func (o *ArtifactGenerationProfileEnvironment) GetEnvironmentKey() string`

GetEnvironmentKey returns the EnvironmentKey field if non-nil, zero value otherwise.

### GetEnvironmentKeyOk

`func (o *ArtifactGenerationProfileEnvironment) GetEnvironmentKeyOk() (*string, bool)`

GetEnvironmentKeyOk returns a tuple with the EnvironmentKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironmentKey

`func (o *ArtifactGenerationProfileEnvironment) SetEnvironmentKey(v string)`

SetEnvironmentKey sets EnvironmentKey field to given value.


### GetResolutionMode

`func (o *ArtifactGenerationProfileEnvironment) GetResolutionMode() string`

GetResolutionMode returns the ResolutionMode field if non-nil, zero value otherwise.

### GetResolutionModeOk

`func (o *ArtifactGenerationProfileEnvironment) GetResolutionModeOk() (*string, bool)`

GetResolutionModeOk returns a tuple with the ResolutionMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResolutionMode

`func (o *ArtifactGenerationProfileEnvironment) SetResolutionMode(v string)`

SetResolutionMode sets ResolutionMode field to given value.


### GetBaseUrlMode

`func (o *ArtifactGenerationProfileEnvironment) GetBaseUrlMode() AtfBaseUrlMode`

GetBaseUrlMode returns the BaseUrlMode field if non-nil, zero value otherwise.

### GetBaseUrlModeOk

`func (o *ArtifactGenerationProfileEnvironment) GetBaseUrlModeOk() (*AtfBaseUrlMode, bool)`

GetBaseUrlModeOk returns a tuple with the BaseUrlMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseUrlMode

`func (o *ArtifactGenerationProfileEnvironment) SetBaseUrlMode(v AtfBaseUrlMode)`

SetBaseUrlMode sets BaseUrlMode field to given value.

### HasBaseUrlMode

`func (o *ArtifactGenerationProfileEnvironment) HasBaseUrlMode() bool`

HasBaseUrlMode returns a boolean if a field has been set.

### GetBaseUrlVariableName

`func (o *ArtifactGenerationProfileEnvironment) GetBaseUrlVariableName() string`

GetBaseUrlVariableName returns the BaseUrlVariableName field if non-nil, zero value otherwise.

### GetBaseUrlVariableNameOk

`func (o *ArtifactGenerationProfileEnvironment) GetBaseUrlVariableNameOk() (*string, bool)`

GetBaseUrlVariableNameOk returns a tuple with the BaseUrlVariableName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseUrlVariableName

`func (o *ArtifactGenerationProfileEnvironment) SetBaseUrlVariableName(v string)`

SetBaseUrlVariableName sets BaseUrlVariableName field to given value.

### HasBaseUrlVariableName

`func (o *ArtifactGenerationProfileEnvironment) HasBaseUrlVariableName() bool`

HasBaseUrlVariableName returns a boolean if a field has been set.

### GetSnapshotBundleHash

`func (o *ArtifactGenerationProfileEnvironment) GetSnapshotBundleHash() string`

GetSnapshotBundleHash returns the SnapshotBundleHash field if non-nil, zero value otherwise.

### GetSnapshotBundleHashOk

`func (o *ArtifactGenerationProfileEnvironment) GetSnapshotBundleHashOk() (*string, bool)`

GetSnapshotBundleHashOk returns a tuple with the SnapshotBundleHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSnapshotBundleHash

`func (o *ArtifactGenerationProfileEnvironment) SetSnapshotBundleHash(v string)`

SetSnapshotBundleHash sets SnapshotBundleHash field to given value.

### HasSnapshotBundleHash

`func (o *ArtifactGenerationProfileEnvironment) HasSnapshotBundleHash() bool`

HasSnapshotBundleHash returns a boolean if a field has been set.

### SetSnapshotBundleHashNil

`func (o *ArtifactGenerationProfileEnvironment) SetSnapshotBundleHashNil(b bool)`

 SetSnapshotBundleHashNil sets the value for SnapshotBundleHash to be an explicit nil

### UnsetSnapshotBundleHash
`func (o *ArtifactGenerationProfileEnvironment) UnsetSnapshotBundleHash()`

UnsetSnapshotBundleHash ensures that no value is present for SnapshotBundleHash, not even an explicit nil
### GetSnapshotAt

`func (o *ArtifactGenerationProfileEnvironment) GetSnapshotAt() time.Time`

GetSnapshotAt returns the SnapshotAt field if non-nil, zero value otherwise.

### GetSnapshotAtOk

`func (o *ArtifactGenerationProfileEnvironment) GetSnapshotAtOk() (*time.Time, bool)`

GetSnapshotAtOk returns a tuple with the SnapshotAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSnapshotAt

`func (o *ArtifactGenerationProfileEnvironment) SetSnapshotAt(v time.Time)`

SetSnapshotAt sets SnapshotAt field to given value.

### HasSnapshotAt

`func (o *ArtifactGenerationProfileEnvironment) HasSnapshotAt() bool`

HasSnapshotAt returns a boolean if a field has been set.

### SetSnapshotAtNil

`func (o *ArtifactGenerationProfileEnvironment) SetSnapshotAtNil(b bool)`

 SetSnapshotAtNil sets the value for SnapshotAt to be an explicit nil

### UnsetSnapshotAt
`func (o *ArtifactGenerationProfileEnvironment) UnsetSnapshotAt()`

UnsetSnapshotAt ensures that no value is present for SnapshotAt, not even an explicit nil
### GetCachedBundleHash

`func (o *ArtifactGenerationProfileEnvironment) GetCachedBundleHash() string`

GetCachedBundleHash returns the CachedBundleHash field if non-nil, zero value otherwise.

### GetCachedBundleHashOk

`func (o *ArtifactGenerationProfileEnvironment) GetCachedBundleHashOk() (*string, bool)`

GetCachedBundleHashOk returns a tuple with the CachedBundleHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCachedBundleHash

`func (o *ArtifactGenerationProfileEnvironment) SetCachedBundleHash(v string)`

SetCachedBundleHash sets CachedBundleHash field to given value.

### HasCachedBundleHash

`func (o *ArtifactGenerationProfileEnvironment) HasCachedBundleHash() bool`

HasCachedBundleHash returns a boolean if a field has been set.

### SetCachedBundleHashNil

`func (o *ArtifactGenerationProfileEnvironment) SetCachedBundleHashNil(b bool)`

 SetCachedBundleHashNil sets the value for CachedBundleHash to be an explicit nil

### UnsetCachedBundleHash
`func (o *ArtifactGenerationProfileEnvironment) UnsetCachedBundleHash()`

UnsetCachedBundleHash ensures that no value is present for CachedBundleHash, not even an explicit nil
### GetCachedAt

`func (o *ArtifactGenerationProfileEnvironment) GetCachedAt() time.Time`

GetCachedAt returns the CachedAt field if non-nil, zero value otherwise.

### GetCachedAtOk

`func (o *ArtifactGenerationProfileEnvironment) GetCachedAtOk() (*time.Time, bool)`

GetCachedAtOk returns a tuple with the CachedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCachedAt

`func (o *ArtifactGenerationProfileEnvironment) SetCachedAt(v time.Time)`

SetCachedAt sets CachedAt field to given value.

### HasCachedAt

`func (o *ArtifactGenerationProfileEnvironment) HasCachedAt() bool`

HasCachedAt returns a boolean if a field has been set.

### SetCachedAtNil

`func (o *ArtifactGenerationProfileEnvironment) SetCachedAtNil(b bool)`

 SetCachedAtNil sets the value for CachedAt to be an explicit nil

### UnsetCachedAt
`func (o *ArtifactGenerationProfileEnvironment) UnsetCachedAt()`

UnsetCachedAt ensures that no value is present for CachedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


