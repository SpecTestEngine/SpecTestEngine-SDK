# StreamingCapabilities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Engine** | **string** |  |
**Storage** | **string** |  |
**Formats** | **[]string** |  |
**Transports** | [**[]StreamingTransport**](StreamingTransport.md) |  |
**Schemes** | **map[string][]string** |  |
**Codecs** | **[]string** |  |
**Actions** | **[]string** |  |
**EventAssertionFields** | **[]string** |  |
**Limits** | [**StreamingLimits**](StreamingLimits.md) |  |

## Methods

### NewStreamingCapabilities

`func NewStreamingCapabilities(engine string, storage string, formats []string, transports []StreamingTransport, schemes map[string][]string, codecs []string, actions []string, eventAssertionFields []string, limits StreamingLimits, ) *StreamingCapabilities`

NewStreamingCapabilities instantiates a new StreamingCapabilities object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStreamingCapabilitiesWithDefaults

`func NewStreamingCapabilitiesWithDefaults() *StreamingCapabilities`

NewStreamingCapabilitiesWithDefaults instantiates a new StreamingCapabilities object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEngine

`func (o *StreamingCapabilities) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *StreamingCapabilities) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *StreamingCapabilities) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetStorage

`func (o *StreamingCapabilities) GetStorage() string`

GetStorage returns the Storage field if non-nil, zero value otherwise.

### GetStorageOk

`func (o *StreamingCapabilities) GetStorageOk() (*string, bool)`

GetStorageOk returns a tuple with the Storage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStorage

`func (o *StreamingCapabilities) SetStorage(v string)`

SetStorage sets Storage field to given value.


### GetFormats

`func (o *StreamingCapabilities) GetFormats() []string`

GetFormats returns the Formats field if non-nil, zero value otherwise.

### GetFormatsOk

`func (o *StreamingCapabilities) GetFormatsOk() (*[]string, bool)`

GetFormatsOk returns a tuple with the Formats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFormats

`func (o *StreamingCapabilities) SetFormats(v []string)`

SetFormats sets Formats field to given value.


### GetTransports

`func (o *StreamingCapabilities) GetTransports() []StreamingTransport`

GetTransports returns the Transports field if non-nil, zero value otherwise.

### GetTransportsOk

`func (o *StreamingCapabilities) GetTransportsOk() (*[]StreamingTransport, bool)`

GetTransportsOk returns a tuple with the Transports field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransports

`func (o *StreamingCapabilities) SetTransports(v []StreamingTransport)`

SetTransports sets Transports field to given value.


### GetSchemes

`func (o *StreamingCapabilities) GetSchemes() map[string][]string`

GetSchemes returns the Schemes field if non-nil, zero value otherwise.

### GetSchemesOk

`func (o *StreamingCapabilities) GetSchemesOk() (*map[string][]string, bool)`

GetSchemesOk returns a tuple with the Schemes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSchemes

`func (o *StreamingCapabilities) SetSchemes(v map[string][]string)`

SetSchemes sets Schemes field to given value.


### GetCodecs

`func (o *StreamingCapabilities) GetCodecs() []string`

GetCodecs returns the Codecs field if non-nil, zero value otherwise.

### GetCodecsOk

`func (o *StreamingCapabilities) GetCodecsOk() (*[]string, bool)`

GetCodecsOk returns a tuple with the Codecs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCodecs

`func (o *StreamingCapabilities) SetCodecs(v []string)`

SetCodecs sets Codecs field to given value.


### GetActions

`func (o *StreamingCapabilities) GetActions() []string`

GetActions returns the Actions field if non-nil, zero value otherwise.

### GetActionsOk

`func (o *StreamingCapabilities) GetActionsOk() (*[]string, bool)`

GetActionsOk returns a tuple with the Actions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActions

`func (o *StreamingCapabilities) SetActions(v []string)`

SetActions sets Actions field to given value.


### GetEventAssertionFields

`func (o *StreamingCapabilities) GetEventAssertionFields() []string`

GetEventAssertionFields returns the EventAssertionFields field if non-nil, zero value otherwise.

### GetEventAssertionFieldsOk

`func (o *StreamingCapabilities) GetEventAssertionFieldsOk() (*[]string, bool)`

GetEventAssertionFieldsOk returns a tuple with the EventAssertionFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEventAssertionFields

`func (o *StreamingCapabilities) SetEventAssertionFields(v []string)`

SetEventAssertionFields sets EventAssertionFields field to given value.


### GetLimits

`func (o *StreamingCapabilities) GetLimits() StreamingLimits`

GetLimits returns the Limits field if non-nil, zero value otherwise.

### GetLimitsOk

`func (o *StreamingCapabilities) GetLimitsOk() (*StreamingLimits, bool)`

GetLimitsOk returns a tuple with the Limits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimits

`func (o *StreamingCapabilities) SetLimits(v StreamingLimits)`

SetLimits sets Limits field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


