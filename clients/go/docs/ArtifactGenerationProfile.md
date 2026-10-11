# ArtifactGenerationProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Revision** | **int64** |  |
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**ArtifactType** | **string** |  |
**Selection** | [**ArtifactSelection**](ArtifactSelection.md) |  |
**Atf** | [**AtfProjectConfig**](AtfProjectConfig.md) |  |
**Environments** | [**[]ArtifactGenerationProfileEnvironment**](ArtifactGenerationProfileEnvironment.md) |  |
**CreatedAt** | **time.Time** |  |
**UpdatedAt** | **time.Time** |  |

## Methods

### NewArtifactGenerationProfile

`func NewArtifactGenerationProfile(id string, revision int64, name string, artifactType string, selection ArtifactSelection, atf AtfProjectConfig, environments []ArtifactGenerationProfileEnvironment, createdAt time.Time, updatedAt time.Time, ) *ArtifactGenerationProfile`

NewArtifactGenerationProfile instantiates a new ArtifactGenerationProfile object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactGenerationProfileWithDefaults

`func NewArtifactGenerationProfileWithDefaults() *ArtifactGenerationProfile`

NewArtifactGenerationProfileWithDefaults instantiates a new ArtifactGenerationProfile object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ArtifactGenerationProfile) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ArtifactGenerationProfile) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ArtifactGenerationProfile) SetId(v string)`

SetId sets Id field to given value.


### GetRevision

`func (o *ArtifactGenerationProfile) GetRevision() int64`

GetRevision returns the Revision field if non-nil, zero value otherwise.

### GetRevisionOk

`func (o *ArtifactGenerationProfile) GetRevisionOk() (*int64, bool)`

GetRevisionOk returns a tuple with the Revision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevision

`func (o *ArtifactGenerationProfile) SetRevision(v int64)`

SetRevision sets Revision field to given value.


### GetName

`func (o *ArtifactGenerationProfile) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ArtifactGenerationProfile) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ArtifactGenerationProfile) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ArtifactGenerationProfile) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ArtifactGenerationProfile) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ArtifactGenerationProfile) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ArtifactGenerationProfile) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *ArtifactGenerationProfile) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *ArtifactGenerationProfile) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetArtifactType

`func (o *ArtifactGenerationProfile) GetArtifactType() string`

GetArtifactType returns the ArtifactType field if non-nil, zero value otherwise.

### GetArtifactTypeOk

`func (o *ArtifactGenerationProfile) GetArtifactTypeOk() (*string, bool)`

GetArtifactTypeOk returns a tuple with the ArtifactType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtifactType

`func (o *ArtifactGenerationProfile) SetArtifactType(v string)`

SetArtifactType sets ArtifactType field to given value.


### GetSelection

`func (o *ArtifactGenerationProfile) GetSelection() ArtifactSelection`

GetSelection returns the Selection field if non-nil, zero value otherwise.

### GetSelectionOk

`func (o *ArtifactGenerationProfile) GetSelectionOk() (*ArtifactSelection, bool)`

GetSelectionOk returns a tuple with the Selection field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelection

`func (o *ArtifactGenerationProfile) SetSelection(v ArtifactSelection)`

SetSelection sets Selection field to given value.


### GetAtf

`func (o *ArtifactGenerationProfile) GetAtf() AtfProjectConfig`

GetAtf returns the Atf field if non-nil, zero value otherwise.

### GetAtfOk

`func (o *ArtifactGenerationProfile) GetAtfOk() (*AtfProjectConfig, bool)`

GetAtfOk returns a tuple with the Atf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAtf

`func (o *ArtifactGenerationProfile) SetAtf(v AtfProjectConfig)`

SetAtf sets Atf field to given value.


### GetEnvironments

`func (o *ArtifactGenerationProfile) GetEnvironments() []ArtifactGenerationProfileEnvironment`

GetEnvironments returns the Environments field if non-nil, zero value otherwise.

### GetEnvironmentsOk

`func (o *ArtifactGenerationProfile) GetEnvironmentsOk() (*[]ArtifactGenerationProfileEnvironment, bool)`

GetEnvironmentsOk returns a tuple with the Environments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironments

`func (o *ArtifactGenerationProfile) SetEnvironments(v []ArtifactGenerationProfileEnvironment)`

SetEnvironments sets Environments field to given value.


### GetCreatedAt

`func (o *ArtifactGenerationProfile) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ArtifactGenerationProfile) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ArtifactGenerationProfile) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *ArtifactGenerationProfile) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *ArtifactGenerationProfile) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *ArtifactGenerationProfile) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
