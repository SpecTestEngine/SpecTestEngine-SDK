# ArtifactSpecRef

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SpecType** | **string** | Selects the owning engine used to resolve this specification. Streaming specifications are not currently representable by the HTTP ATF runtime and must fail through the compatibility policy. |

## Methods

### NewArtifactSpecRef

`func NewArtifactSpecRef(id string, specType string, ) *ArtifactSpecRef`

NewArtifactSpecRef instantiates a new ArtifactSpecRef object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactSpecRefWithDefaults

`func NewArtifactSpecRefWithDefaults() *ArtifactSpecRef`

NewArtifactSpecRefWithDefaults instantiates a new ArtifactSpecRef object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ArtifactSpecRef) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ArtifactSpecRef) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ArtifactSpecRef) SetId(v string)`

SetId sets Id field to given value.


### GetSpecType

`func (o *ArtifactSpecRef) GetSpecType() string`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *ArtifactSpecRef) GetSpecTypeOk() (*string, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *ArtifactSpecRef) SetSpecType(v string)`

SetSpecType sets SpecType field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
