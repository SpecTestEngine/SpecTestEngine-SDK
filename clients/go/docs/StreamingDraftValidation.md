# StreamingDraftValidation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Valid** | **bool** |  |
**SpecType** | **string** |  |
**Transport** | [**StreamingTransport**](StreamingTransport.md) |  |

## Methods

### NewStreamingDraftValidation

`func NewStreamingDraftValidation(valid bool, specType string, transport StreamingTransport, ) *StreamingDraftValidation`

NewStreamingDraftValidation instantiates a new StreamingDraftValidation object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStreamingDraftValidationWithDefaults

`func NewStreamingDraftValidationWithDefaults() *StreamingDraftValidation`

NewStreamingDraftValidationWithDefaults instantiates a new StreamingDraftValidation object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetValid

`func (o *StreamingDraftValidation) GetValid() bool`

GetValid returns the Valid field if non-nil, zero value otherwise.

### GetValidOk

`func (o *StreamingDraftValidation) GetValidOk() (*bool, bool)`

GetValidOk returns a tuple with the Valid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValid

`func (o *StreamingDraftValidation) SetValid(v bool)`

SetValid sets Valid field to given value.


### GetSpecType

`func (o *StreamingDraftValidation) GetSpecType() string`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *StreamingDraftValidation) GetSpecTypeOk() (*string, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *StreamingDraftValidation) SetSpecType(v string)`

SetSpecType sets SpecType field to given value.


### GetTransport

`func (o *StreamingDraftValidation) GetTransport() StreamingTransport`

GetTransport returns the Transport field if non-nil, zero value otherwise.

### GetTransportOk

`func (o *StreamingDraftValidation) GetTransportOk() (*StreamingTransport, bool)`

GetTransportOk returns a tuple with the Transport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransport

`func (o *StreamingDraftValidation) SetTransport(v StreamingTransport)`

SetTransport sets Transport field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


