# ArtifactGenerationProfileInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Revision** | Pointer to **NullableInt64** | Omit when creating. Send the last returned revision when updating. | [optional]
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**ArtifactType** | **string** |  |
**Selection** | [**ArtifactSelection**](ArtifactSelection.md) |  |
**Atf** | [**AtfProjectConfig**](AtfProjectConfig.md) |  |
**Environments** | [**[]ArtifactGenerationProfileEnvironmentInput**](ArtifactGenerationProfileEnvironmentInput.md) |  |

## Methods

### NewArtifactGenerationProfileInput

`func NewArtifactGenerationProfileInput(name string, artifactType string, selection ArtifactSelection, atf AtfProjectConfig, environments []ArtifactGenerationProfileEnvironmentInput, ) *ArtifactGenerationProfileInput`

NewArtifactGenerationProfileInput instantiates a new ArtifactGenerationProfileInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactGenerationProfileInputWithDefaults

`func NewArtifactGenerationProfileInputWithDefaults() *ArtifactGenerationProfileInput`

NewArtifactGenerationProfileInputWithDefaults instantiates a new ArtifactGenerationProfileInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRevision

`func (o *ArtifactGenerationProfileInput) GetRevision() int64`

GetRevision returns the Revision field if non-nil, zero value otherwise.

### GetRevisionOk

`func (o *ArtifactGenerationProfileInput) GetRevisionOk() (*int64, bool)`

GetRevisionOk returns a tuple with the Revision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevision

`func (o *ArtifactGenerationProfileInput) SetRevision(v int64)`

SetRevision sets Revision field to given value.

### HasRevision

`func (o *ArtifactGenerationProfileInput) HasRevision() bool`

HasRevision returns a boolean if a field has been set.

### SetRevisionNil

`func (o *ArtifactGenerationProfileInput) SetRevisionNil(b bool)`

 SetRevisionNil sets the value for Revision to be an explicit nil

### UnsetRevision
`func (o *ArtifactGenerationProfileInput) UnsetRevision()`

UnsetRevision ensures that no value is present for Revision, not even an explicit nil
### GetName

`func (o *ArtifactGenerationProfileInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ArtifactGenerationProfileInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ArtifactGenerationProfileInput) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ArtifactGenerationProfileInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ArtifactGenerationProfileInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ArtifactGenerationProfileInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ArtifactGenerationProfileInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *ArtifactGenerationProfileInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *ArtifactGenerationProfileInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetArtifactType

`func (o *ArtifactGenerationProfileInput) GetArtifactType() string`

GetArtifactType returns the ArtifactType field if non-nil, zero value otherwise.

### GetArtifactTypeOk

`func (o *ArtifactGenerationProfileInput) GetArtifactTypeOk() (*string, bool)`

GetArtifactTypeOk returns a tuple with the ArtifactType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtifactType

`func (o *ArtifactGenerationProfileInput) SetArtifactType(v string)`

SetArtifactType sets ArtifactType field to given value.


### GetSelection

`func (o *ArtifactGenerationProfileInput) GetSelection() ArtifactSelection`

GetSelection returns the Selection field if non-nil, zero value otherwise.

### GetSelectionOk

`func (o *ArtifactGenerationProfileInput) GetSelectionOk() (*ArtifactSelection, bool)`

GetSelectionOk returns a tuple with the Selection field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelection

`func (o *ArtifactGenerationProfileInput) SetSelection(v ArtifactSelection)`

SetSelection sets Selection field to given value.


### GetAtf

`func (o *ArtifactGenerationProfileInput) GetAtf() AtfProjectConfig`

GetAtf returns the Atf field if non-nil, zero value otherwise.

### GetAtfOk

`func (o *ArtifactGenerationProfileInput) GetAtfOk() (*AtfProjectConfig, bool)`

GetAtfOk returns a tuple with the Atf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAtf

`func (o *ArtifactGenerationProfileInput) SetAtf(v AtfProjectConfig)`

SetAtf sets Atf field to given value.


### GetEnvironments

`func (o *ArtifactGenerationProfileInput) GetEnvironments() []ArtifactGenerationProfileEnvironmentInput`

GetEnvironments returns the Environments field if non-nil, zero value otherwise.

### GetEnvironmentsOk

`func (o *ArtifactGenerationProfileInput) GetEnvironmentsOk() (*[]ArtifactGenerationProfileEnvironmentInput, bool)`

GetEnvironmentsOk returns a tuple with the Environments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironments

`func (o *ArtifactGenerationProfileInput) SetEnvironments(v []ArtifactGenerationProfileEnvironmentInput)`

SetEnvironments sets Environments field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


