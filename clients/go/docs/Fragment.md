# Fragment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**SpecType** | [**SpecType**](SpecType.md) |  |
**StreamingTransport** | Pointer to [**NullableStreamingTransport**](StreamingTransport.md) |  | [optional]
**Type** | [**FragmentType**](FragmentType.md) |  |
**Content** | **map[string]interface{}** |  |
**FragmentId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**CreatedAt** | **time.Time** |  |

## Methods

### NewFragment

`func NewFragment(name string, specType SpecType, type_ FragmentType, content map[string]interface{}, fragmentId string, createdAt time.Time, ) *Fragment`

NewFragment instantiates a new Fragment object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFragmentWithDefaults

`func NewFragmentWithDefaults() *Fragment`

NewFragmentWithDefaults instantiates a new Fragment object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *Fragment) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Fragment) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Fragment) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *Fragment) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Fragment) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Fragment) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Fragment) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *Fragment) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *Fragment) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetSpecType

`func (o *Fragment) GetSpecType() SpecType`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *Fragment) GetSpecTypeOk() (*SpecType, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *Fragment) SetSpecType(v SpecType)`

SetSpecType sets SpecType field to given value.


### GetStreamingTransport

`func (o *Fragment) GetStreamingTransport() StreamingTransport`

GetStreamingTransport returns the StreamingTransport field if non-nil, zero value otherwise.

### GetStreamingTransportOk

`func (o *Fragment) GetStreamingTransportOk() (*StreamingTransport, bool)`

GetStreamingTransportOk returns a tuple with the StreamingTransport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreamingTransport

`func (o *Fragment) SetStreamingTransport(v StreamingTransport)`

SetStreamingTransport sets StreamingTransport field to given value.

### HasStreamingTransport

`func (o *Fragment) HasStreamingTransport() bool`

HasStreamingTransport returns a boolean if a field has been set.

### SetStreamingTransportNil

`func (o *Fragment) SetStreamingTransportNil(b bool)`

 SetStreamingTransportNil sets the value for StreamingTransport to be an explicit nil

### UnsetStreamingTransport
`func (o *Fragment) UnsetStreamingTransport()`

UnsetStreamingTransport ensures that no value is present for StreamingTransport, not even an explicit nil
### GetType

`func (o *Fragment) GetType() FragmentType`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Fragment) GetTypeOk() (*FragmentType, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Fragment) SetType(v FragmentType)`

SetType sets Type field to given value.


### GetContent

`func (o *Fragment) GetContent() map[string]interface{}`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *Fragment) GetContentOk() (*map[string]interface{}, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *Fragment) SetContent(v map[string]interface{})`

SetContent sets Content field to given value.


### GetFragmentId

`func (o *Fragment) GetFragmentId() string`

GetFragmentId returns the FragmentId field if non-nil, zero value otherwise.

### GetFragmentIdOk

`func (o *Fragment) GetFragmentIdOk() (*string, bool)`

GetFragmentIdOk returns a tuple with the FragmentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFragmentId

`func (o *Fragment) SetFragmentId(v string)`

SetFragmentId sets FragmentId field to given value.


### GetCreatedAt

`func (o *Fragment) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Fragment) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Fragment) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


