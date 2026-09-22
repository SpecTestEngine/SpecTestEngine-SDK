# StreamingDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Stream** | [**StreamingDefinitionStream**](StreamingDefinitionStream.md) |  |
**ExpectedConnection** | Pointer to **map[string]interface{}** |  | [optional]
**ExpectedStream** | Pointer to **map[string]interface{}** |  | [optional]
**ExpectedTermination** | Pointer to **map[string]interface{}** |  | [optional]
**Exclusions** | Pointer to **[]string** |  | [optional]
**Redactions** | Pointer to **[]string** |  | [optional]
**ObservationOnly** | Pointer to **bool** |  | [optional] [default to false]

## Methods

### NewStreamingDefinition

`func NewStreamingDefinition(stream StreamingDefinitionStream, ) *StreamingDefinition`

NewStreamingDefinition instantiates a new StreamingDefinition object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStreamingDefinitionWithDefaults

`func NewStreamingDefinitionWithDefaults() *StreamingDefinition`

NewStreamingDefinitionWithDefaults instantiates a new StreamingDefinition object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStream

`func (o *StreamingDefinition) GetStream() StreamingDefinitionStream`

GetStream returns the Stream field if non-nil, zero value otherwise.

### GetStreamOk

`func (o *StreamingDefinition) GetStreamOk() (*StreamingDefinitionStream, bool)`

GetStreamOk returns a tuple with the Stream field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStream

`func (o *StreamingDefinition) SetStream(v StreamingDefinitionStream)`

SetStream sets Stream field to given value.


### GetExpectedConnection

`func (o *StreamingDefinition) GetExpectedConnection() map[string]interface{}`

GetExpectedConnection returns the ExpectedConnection field if non-nil, zero value otherwise.

### GetExpectedConnectionOk

`func (o *StreamingDefinition) GetExpectedConnectionOk() (*map[string]interface{}, bool)`

GetExpectedConnectionOk returns a tuple with the ExpectedConnection field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedConnection

`func (o *StreamingDefinition) SetExpectedConnection(v map[string]interface{})`

SetExpectedConnection sets ExpectedConnection field to given value.

### HasExpectedConnection

`func (o *StreamingDefinition) HasExpectedConnection() bool`

HasExpectedConnection returns a boolean if a field has been set.

### GetExpectedStream

`func (o *StreamingDefinition) GetExpectedStream() map[string]interface{}`

GetExpectedStream returns the ExpectedStream field if non-nil, zero value otherwise.

### GetExpectedStreamOk

`func (o *StreamingDefinition) GetExpectedStreamOk() (*map[string]interface{}, bool)`

GetExpectedStreamOk returns a tuple with the ExpectedStream field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedStream

`func (o *StreamingDefinition) SetExpectedStream(v map[string]interface{})`

SetExpectedStream sets ExpectedStream field to given value.

### HasExpectedStream

`func (o *StreamingDefinition) HasExpectedStream() bool`

HasExpectedStream returns a boolean if a field has been set.

### GetExpectedTermination

`func (o *StreamingDefinition) GetExpectedTermination() map[string]interface{}`

GetExpectedTermination returns the ExpectedTermination field if non-nil, zero value otherwise.

### GetExpectedTerminationOk

`func (o *StreamingDefinition) GetExpectedTerminationOk() (*map[string]interface{}, bool)`

GetExpectedTerminationOk returns a tuple with the ExpectedTermination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedTermination

`func (o *StreamingDefinition) SetExpectedTermination(v map[string]interface{})`

SetExpectedTermination sets ExpectedTermination field to given value.

### HasExpectedTermination

`func (o *StreamingDefinition) HasExpectedTermination() bool`

HasExpectedTermination returns a boolean if a field has been set.

### GetExclusions

`func (o *StreamingDefinition) GetExclusions() []string`

GetExclusions returns the Exclusions field if non-nil, zero value otherwise.

### GetExclusionsOk

`func (o *StreamingDefinition) GetExclusionsOk() (*[]string, bool)`

GetExclusionsOk returns a tuple with the Exclusions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExclusions

`func (o *StreamingDefinition) SetExclusions(v []string)`

SetExclusions sets Exclusions field to given value.

### HasExclusions

`func (o *StreamingDefinition) HasExclusions() bool`

HasExclusions returns a boolean if a field has been set.

### GetRedactions

`func (o *StreamingDefinition) GetRedactions() []string`

GetRedactions returns the Redactions field if non-nil, zero value otherwise.

### GetRedactionsOk

`func (o *StreamingDefinition) GetRedactionsOk() (*[]string, bool)`

GetRedactionsOk returns a tuple with the Redactions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRedactions

`func (o *StreamingDefinition) SetRedactions(v []string)`

SetRedactions sets Redactions field to given value.

### HasRedactions

`func (o *StreamingDefinition) HasRedactions() bool`

HasRedactions returns a boolean if a field has been set.

### GetObservationOnly

`func (o *StreamingDefinition) GetObservationOnly() bool`

GetObservationOnly returns the ObservationOnly field if non-nil, zero value otherwise.

### GetObservationOnlyOk

`func (o *StreamingDefinition) GetObservationOnlyOk() (*bool, bool)`

GetObservationOnlyOk returns a tuple with the ObservationOnly field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObservationOnly

`func (o *StreamingDefinition) SetObservationOnly(v bool)`

SetObservationOnly sets ObservationOnly field to given value.

### HasObservationOnly

`func (o *StreamingDefinition) HasObservationOnly() bool`

HasObservationOnly returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


