# FragmentAssembly

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SpecType** | [**SpecType**](SpecType.md) |  |
**StreamingTransport** | Pointer to [**NullableStreamingTransport**](StreamingTransport.md) |  | [optional]
**FragmentIds** | **[]string** |  |

## Methods

### NewFragmentAssembly

`func NewFragmentAssembly(specType SpecType, fragmentIds []string, ) *FragmentAssembly`

NewFragmentAssembly instantiates a new FragmentAssembly object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFragmentAssemblyWithDefaults

`func NewFragmentAssemblyWithDefaults() *FragmentAssembly`

NewFragmentAssemblyWithDefaults instantiates a new FragmentAssembly object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSpecType

`func (o *FragmentAssembly) GetSpecType() SpecType`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *FragmentAssembly) GetSpecTypeOk() (*SpecType, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *FragmentAssembly) SetSpecType(v SpecType)`

SetSpecType sets SpecType field to given value.


### GetStreamingTransport

`func (o *FragmentAssembly) GetStreamingTransport() StreamingTransport`

GetStreamingTransport returns the StreamingTransport field if non-nil, zero value otherwise.

### GetStreamingTransportOk

`func (o *FragmentAssembly) GetStreamingTransportOk() (*StreamingTransport, bool)`

GetStreamingTransportOk returns a tuple with the StreamingTransport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreamingTransport

`func (o *FragmentAssembly) SetStreamingTransport(v StreamingTransport)`

SetStreamingTransport sets StreamingTransport field to given value.

### HasStreamingTransport

`func (o *FragmentAssembly) HasStreamingTransport() bool`

HasStreamingTransport returns a boolean if a field has been set.

### SetStreamingTransportNil

`func (o *FragmentAssembly) SetStreamingTransportNil(b bool)`

 SetStreamingTransportNil sets the value for StreamingTransport to be an explicit nil

### UnsetStreamingTransport
`func (o *FragmentAssembly) UnsetStreamingTransport()`

UnsetStreamingTransport ensures that no value is present for StreamingTransport, not even an explicit nil
### GetFragmentIds

`func (o *FragmentAssembly) GetFragmentIds() []string`

GetFragmentIds returns the FragmentIds field if non-nil, zero value otherwise.

### GetFragmentIdsOk

`func (o *FragmentAssembly) GetFragmentIdsOk() (*[]string, bool)`

GetFragmentIdsOk returns a tuple with the FragmentIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFragmentIds

`func (o *FragmentAssembly) SetFragmentIds(v []string)`

SetFragmentIds sets FragmentIds field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


