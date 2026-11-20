# PreparationSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  |
**StableKey** | **string** |  |
**Name** | **string** |  |
**Protocol** | **string** |  |
**Outputs** | [**map[string]PreparationOutput**](PreparationOutput.md) |  |

## Methods

### NewPreparationSummary

`func NewPreparationSummary(id string, stableKey string, name string, protocol string, outputs map[string]PreparationOutput, ) *PreparationSummary`

NewPreparationSummary instantiates a new PreparationSummary object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPreparationSummaryWithDefaults

`func NewPreparationSummaryWithDefaults() *PreparationSummary`

NewPreparationSummaryWithDefaults instantiates a new PreparationSummary object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *PreparationSummary) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PreparationSummary) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PreparationSummary) SetId(v string)`

SetId sets Id field to given value.


### GetStableKey

`func (o *PreparationSummary) GetStableKey() string`

GetStableKey returns the StableKey field if non-nil, zero value otherwise.

### GetStableKeyOk

`func (o *PreparationSummary) GetStableKeyOk() (*string, bool)`

GetStableKeyOk returns a tuple with the StableKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStableKey

`func (o *PreparationSummary) SetStableKey(v string)`

SetStableKey sets StableKey field to given value.


### GetName

`func (o *PreparationSummary) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PreparationSummary) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PreparationSummary) SetName(v string)`

SetName sets Name field to given value.


### GetProtocol

`func (o *PreparationSummary) GetProtocol() string`

GetProtocol returns the Protocol field if non-nil, zero value otherwise.

### GetProtocolOk

`func (o *PreparationSummary) GetProtocolOk() (*string, bool)`

GetProtocolOk returns a tuple with the Protocol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProtocol

`func (o *PreparationSummary) SetProtocol(v string)`

SetProtocol sets Protocol field to given value.


### GetOutputs

`func (o *PreparationSummary) GetOutputs() map[string]PreparationOutput`

GetOutputs returns the Outputs field if non-nil, zero value otherwise.

### GetOutputsOk

`func (o *PreparationSummary) GetOutputsOk() (*map[string]PreparationOutput, bool)`

GetOutputsOk returns a tuple with the Outputs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutputs

`func (o *PreparationSummary) SetOutputs(v map[string]PreparationOutput)`

SetOutputs sets Outputs field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
