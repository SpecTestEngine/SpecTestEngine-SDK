# CraftsmanStreamingRunInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** |  | [optional]
**StreamingSpec** | [**StreamingDefinition**](StreamingDefinition.md) |  |

## Methods

### NewCraftsmanStreamingRunInput

`func NewCraftsmanStreamingRunInput(streamingSpec StreamingDefinition, ) *CraftsmanStreamingRunInput`

NewCraftsmanStreamingRunInput instantiates a new CraftsmanStreamingRunInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCraftsmanStreamingRunInputWithDefaults

`func NewCraftsmanStreamingRunInputWithDefaults() *CraftsmanStreamingRunInput`

NewCraftsmanStreamingRunInputWithDefaults instantiates a new CraftsmanStreamingRunInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CraftsmanStreamingRunInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CraftsmanStreamingRunInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CraftsmanStreamingRunInput) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *CraftsmanStreamingRunInput) HasName() bool`

HasName returns a boolean if a field has been set.

### GetStreamingSpec

`func (o *CraftsmanStreamingRunInput) GetStreamingSpec() StreamingDefinition`

GetStreamingSpec returns the StreamingSpec field if non-nil, zero value otherwise.

### GetStreamingSpecOk

`func (o *CraftsmanStreamingRunInput) GetStreamingSpecOk() (*StreamingDefinition, bool)`

GetStreamingSpecOk returns a tuple with the StreamingSpec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreamingSpec

`func (o *CraftsmanStreamingRunInput) SetStreamingSpec(v StreamingDefinition)`

SetStreamingSpec sets StreamingSpec field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


