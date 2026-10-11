# RequestChainRunInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OverrideValues** | Pointer to **map[string]interface{}** |  | [optional]
**GlobalVariables** | Pointer to **map[string]string** |  | [optional]
**GlobalVariableFallbacks** | Pointer to **map[string]string** |  | [optional]
**DraftRequest** | Pointer to [**SavedRequestInput**](SavedRequestInput.md) |  | [optional]

## Methods

### NewRequestChainRunInput

`func NewRequestChainRunInput() *RequestChainRunInput`

NewRequestChainRunInput instantiates a new RequestChainRunInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRequestChainRunInputWithDefaults

`func NewRequestChainRunInputWithDefaults() *RequestChainRunInput`

NewRequestChainRunInputWithDefaults instantiates a new RequestChainRunInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOverrideValues

`func (o *RequestChainRunInput) GetOverrideValues() map[string]interface{}`

GetOverrideValues returns the OverrideValues field if non-nil, zero value otherwise.

### GetOverrideValuesOk

`func (o *RequestChainRunInput) GetOverrideValuesOk() (*map[string]interface{}, bool)`

GetOverrideValuesOk returns a tuple with the OverrideValues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOverrideValues

`func (o *RequestChainRunInput) SetOverrideValues(v map[string]interface{})`

SetOverrideValues sets OverrideValues field to given value.

### HasOverrideValues

`func (o *RequestChainRunInput) HasOverrideValues() bool`

HasOverrideValues returns a boolean if a field has been set.

### GetGlobalVariables

`func (o *RequestChainRunInput) GetGlobalVariables() map[string]string`

GetGlobalVariables returns the GlobalVariables field if non-nil, zero value otherwise.

### GetGlobalVariablesOk

`func (o *RequestChainRunInput) GetGlobalVariablesOk() (*map[string]string, bool)`

GetGlobalVariablesOk returns a tuple with the GlobalVariables field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGlobalVariables

`func (o *RequestChainRunInput) SetGlobalVariables(v map[string]string)`

SetGlobalVariables sets GlobalVariables field to given value.

### HasGlobalVariables

`func (o *RequestChainRunInput) HasGlobalVariables() bool`

HasGlobalVariables returns a boolean if a field has been set.

### GetGlobalVariableFallbacks

`func (o *RequestChainRunInput) GetGlobalVariableFallbacks() map[string]string`

GetGlobalVariableFallbacks returns the GlobalVariableFallbacks field if non-nil, zero value otherwise.

### GetGlobalVariableFallbacksOk

`func (o *RequestChainRunInput) GetGlobalVariableFallbacksOk() (*map[string]string, bool)`

GetGlobalVariableFallbacksOk returns a tuple with the GlobalVariableFallbacks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGlobalVariableFallbacks

`func (o *RequestChainRunInput) SetGlobalVariableFallbacks(v map[string]string)`

SetGlobalVariableFallbacks sets GlobalVariableFallbacks field to given value.

### HasGlobalVariableFallbacks

`func (o *RequestChainRunInput) HasGlobalVariableFallbacks() bool`

HasGlobalVariableFallbacks returns a boolean if a field has been set.

### GetDraftRequest

`func (o *RequestChainRunInput) GetDraftRequest() SavedRequestInput`

GetDraftRequest returns the DraftRequest field if non-nil, zero value otherwise.

### GetDraftRequestOk

`func (o *RequestChainRunInput) GetDraftRequestOk() (*SavedRequestInput, bool)`

GetDraftRequestOk returns a tuple with the DraftRequest field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDraftRequest

`func (o *RequestChainRunInput) SetDraftRequest(v SavedRequestInput)`

SetDraftRequest sets DraftRequest field to given value.

### HasDraftRequest

`func (o *RequestChainRunInput) HasDraftRequest() bool`

HasDraftRequest returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
