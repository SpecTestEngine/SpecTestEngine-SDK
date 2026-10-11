# StreamingDefinitionStream

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Transport** | [**StreamingTransport**](StreamingTransport.md) |  |
**Endpoint** | **string** |  |
**Connection** | Pointer to **map[string]interface{}** |  | [optional]
**Steps** | Pointer to **[]map[string]interface{}** |  | [optional]

## Methods

### NewStreamingDefinitionStream

`func NewStreamingDefinitionStream(transport StreamingTransport, endpoint string, ) *StreamingDefinitionStream`

NewStreamingDefinitionStream instantiates a new StreamingDefinitionStream object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStreamingDefinitionStreamWithDefaults

`func NewStreamingDefinitionStreamWithDefaults() *StreamingDefinitionStream`

NewStreamingDefinitionStreamWithDefaults instantiates a new StreamingDefinitionStream object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTransport

`func (o *StreamingDefinitionStream) GetTransport() StreamingTransport`

GetTransport returns the Transport field if non-nil, zero value otherwise.

### GetTransportOk

`func (o *StreamingDefinitionStream) GetTransportOk() (*StreamingTransport, bool)`

GetTransportOk returns a tuple with the Transport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransport

`func (o *StreamingDefinitionStream) SetTransport(v StreamingTransport)`

SetTransport sets Transport field to given value.


### GetEndpoint

`func (o *StreamingDefinitionStream) GetEndpoint() string`

GetEndpoint returns the Endpoint field if non-nil, zero value otherwise.

### GetEndpointOk

`func (o *StreamingDefinitionStream) GetEndpointOk() (*string, bool)`

GetEndpointOk returns a tuple with the Endpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndpoint

`func (o *StreamingDefinitionStream) SetEndpoint(v string)`

SetEndpoint sets Endpoint field to given value.


### GetConnection

`func (o *StreamingDefinitionStream) GetConnection() map[string]interface{}`

GetConnection returns the Connection field if non-nil, zero value otherwise.

### GetConnectionOk

`func (o *StreamingDefinitionStream) GetConnectionOk() (*map[string]interface{}, bool)`

GetConnectionOk returns a tuple with the Connection field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConnection

`func (o *StreamingDefinitionStream) SetConnection(v map[string]interface{})`

SetConnection sets Connection field to given value.

### HasConnection

`func (o *StreamingDefinitionStream) HasConnection() bool`

HasConnection returns a boolean if a field has been set.

### GetSteps

`func (o *StreamingDefinitionStream) GetSteps() []map[string]interface{}`

GetSteps returns the Steps field if non-nil, zero value otherwise.

### GetStepsOk

`func (o *StreamingDefinitionStream) GetStepsOk() (*[]map[string]interface{}, bool)`

GetStepsOk returns a tuple with the Steps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteps

`func (o *StreamingDefinitionStream) SetSteps(v []map[string]interface{})`

SetSteps sets Steps field to given value.

### HasSteps

`func (o *StreamingDefinitionStream) HasSteps() bool`

HasSteps returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
