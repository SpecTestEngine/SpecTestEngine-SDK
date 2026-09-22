# FragmentCatalog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SpecType** | [**SpecType**](SpecType.md) |  |
**StreamingTransport** | Pointer to [**NullableStreamingTransport**](StreamingTransport.md) |  | [optional]
**Types** | [**[]FragmentCatalogType**](FragmentCatalogType.md) |  |

## Methods

### NewFragmentCatalog

`func NewFragmentCatalog(specType SpecType, types []FragmentCatalogType, ) *FragmentCatalog`

NewFragmentCatalog instantiates a new FragmentCatalog object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFragmentCatalogWithDefaults

`func NewFragmentCatalogWithDefaults() *FragmentCatalog`

NewFragmentCatalogWithDefaults instantiates a new FragmentCatalog object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSpecType

`func (o *FragmentCatalog) GetSpecType() SpecType`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *FragmentCatalog) GetSpecTypeOk() (*SpecType, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *FragmentCatalog) SetSpecType(v SpecType)`

SetSpecType sets SpecType field to given value.


### GetStreamingTransport

`func (o *FragmentCatalog) GetStreamingTransport() StreamingTransport`

GetStreamingTransport returns the StreamingTransport field if non-nil, zero value otherwise.

### GetStreamingTransportOk

`func (o *FragmentCatalog) GetStreamingTransportOk() (*StreamingTransport, bool)`

GetStreamingTransportOk returns a tuple with the StreamingTransport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreamingTransport

`func (o *FragmentCatalog) SetStreamingTransport(v StreamingTransport)`

SetStreamingTransport sets StreamingTransport field to given value.

### HasStreamingTransport

`func (o *FragmentCatalog) HasStreamingTransport() bool`

HasStreamingTransport returns a boolean if a field has been set.

### SetStreamingTransportNil

`func (o *FragmentCatalog) SetStreamingTransportNil(b bool)`

 SetStreamingTransportNil sets the value for StreamingTransport to be an explicit nil

### UnsetStreamingTransport
`func (o *FragmentCatalog) UnsetStreamingTransport()`

UnsetStreamingTransport ensures that no value is present for StreamingTransport, not even an explicit nil
### GetTypes

`func (o *FragmentCatalog) GetTypes() []FragmentCatalogType`

GetTypes returns the Types field if non-nil, zero value otherwise.

### GetTypesOk

`func (o *FragmentCatalog) GetTypesOk() (*[]FragmentCatalogType, bool)`

GetTypesOk returns a tuple with the Types field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTypes

`func (o *FragmentCatalog) SetTypes(v []FragmentCatalogType)`

SetTypes sets Types field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


