# FragmentInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**SpecType** | [**SpecType**](SpecType.md) |  |
**StreamingTransport** | Pointer to [**NullableStreamingTransport**](StreamingTransport.md) |  | [optional]
**Type** | [**FragmentType**](FragmentType.md) |  |
**Content** | **map[string]interface{}** |  |

## Methods

### NewFragmentInput

`func NewFragmentInput(name string, specType SpecType, type_ FragmentType, content map[string]interface{}, ) *FragmentInput`

NewFragmentInput instantiates a new FragmentInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFragmentInputWithDefaults

`func NewFragmentInputWithDefaults() *FragmentInput`

NewFragmentInputWithDefaults instantiates a new FragmentInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *FragmentInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *FragmentInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *FragmentInput) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *FragmentInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *FragmentInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *FragmentInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *FragmentInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *FragmentInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *FragmentInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetSpecType

`func (o *FragmentInput) GetSpecType() SpecType`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *FragmentInput) GetSpecTypeOk() (*SpecType, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *FragmentInput) SetSpecType(v SpecType)`

SetSpecType sets SpecType field to given value.


### GetStreamingTransport

`func (o *FragmentInput) GetStreamingTransport() StreamingTransport`

GetStreamingTransport returns the StreamingTransport field if non-nil, zero value otherwise.

### GetStreamingTransportOk

`func (o *FragmentInput) GetStreamingTransportOk() (*StreamingTransport, bool)`

GetStreamingTransportOk returns a tuple with the StreamingTransport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreamingTransport

`func (o *FragmentInput) SetStreamingTransport(v StreamingTransport)`

SetStreamingTransport sets StreamingTransport field to given value.

### HasStreamingTransport

`func (o *FragmentInput) HasStreamingTransport() bool`

HasStreamingTransport returns a boolean if a field has been set.

### SetStreamingTransportNil

`func (o *FragmentInput) SetStreamingTransportNil(b bool)`

 SetStreamingTransportNil sets the value for StreamingTransport to be an explicit nil

### UnsetStreamingTransport
`func (o *FragmentInput) UnsetStreamingTransport()`

UnsetStreamingTransport ensures that no value is present for StreamingTransport, not even an explicit nil
### GetType

`func (o *FragmentInput) GetType() FragmentType`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *FragmentInput) GetTypeOk() (*FragmentType, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *FragmentInput) SetType(v FragmentType)`

SetType sets Type field to given value.


### GetContent

`func (o *FragmentInput) GetContent() map[string]interface{}`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *FragmentInput) GetContentOk() (*map[string]interface{}, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *FragmentInput) SetContent(v map[string]interface{})`

SetContent sets Content field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


