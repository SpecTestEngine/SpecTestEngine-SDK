# FragmentDraftAssembly

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SpecType** | [**SpecType**](SpecType.md) |  |
**StreamingTransport** | Pointer to [**NullableStreamingTransport**](StreamingTransport.md) |  | [optional]
**Fragments** | [**[]FragmentDraftInput**](FragmentDraftInput.md) |  |

## Methods

### NewFragmentDraftAssembly

`func NewFragmentDraftAssembly(specType SpecType, fragments []FragmentDraftInput, ) *FragmentDraftAssembly`

NewFragmentDraftAssembly instantiates a new FragmentDraftAssembly object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFragmentDraftAssemblyWithDefaults

`func NewFragmentDraftAssemblyWithDefaults() *FragmentDraftAssembly`

NewFragmentDraftAssemblyWithDefaults instantiates a new FragmentDraftAssembly object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSpecType

`func (o *FragmentDraftAssembly) GetSpecType() SpecType`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *FragmentDraftAssembly) GetSpecTypeOk() (*SpecType, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *FragmentDraftAssembly) SetSpecType(v SpecType)`

SetSpecType sets SpecType field to given value.


### GetStreamingTransport

`func (o *FragmentDraftAssembly) GetStreamingTransport() StreamingTransport`

GetStreamingTransport returns the StreamingTransport field if non-nil, zero value otherwise.

### GetStreamingTransportOk

`func (o *FragmentDraftAssembly) GetStreamingTransportOk() (*StreamingTransport, bool)`

GetStreamingTransportOk returns a tuple with the StreamingTransport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreamingTransport

`func (o *FragmentDraftAssembly) SetStreamingTransport(v StreamingTransport)`

SetStreamingTransport sets StreamingTransport field to given value.

### HasStreamingTransport

`func (o *FragmentDraftAssembly) HasStreamingTransport() bool`

HasStreamingTransport returns a boolean if a field has been set.

### SetStreamingTransportNil

`func (o *FragmentDraftAssembly) SetStreamingTransportNil(b bool)`

 SetStreamingTransportNil sets the value for StreamingTransport to be an explicit nil

### UnsetStreamingTransport
`func (o *FragmentDraftAssembly) UnsetStreamingTransport()`

UnsetStreamingTransport ensures that no value is present for StreamingTransport, not even an explicit nil
### GetFragments

`func (o *FragmentDraftAssembly) GetFragments() []FragmentDraftInput`

GetFragments returns the Fragments field if non-nil, zero value otherwise.

### GetFragmentsOk

`func (o *FragmentDraftAssembly) GetFragmentsOk() (*[]FragmentDraftInput, bool)`

GetFragmentsOk returns a tuple with the Fragments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFragments

`func (o *FragmentDraftAssembly) SetFragments(v []FragmentDraftInput)`

SetFragments sets Fragments field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
