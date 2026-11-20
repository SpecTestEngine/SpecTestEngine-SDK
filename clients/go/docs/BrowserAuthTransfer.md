# BrowserAuthTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Sources** | Pointer to [**[]BrowserAuthSource**](BrowserAuthSource.md) |  | [optional]
**AuthorizationVariable** | Pointer to **NullableString** |  | [optional]
**Candidates** | Pointer to **[]interface{}** |  | [optional]
**OptionalRefresh** | Pointer to **bool** |  | [optional] [default to false]
**ChoiceId** | Pointer to **NullableString** |  | [optional]

## Methods

### NewBrowserAuthTransfer

`func NewBrowserAuthTransfer() *BrowserAuthTransfer`

NewBrowserAuthTransfer instantiates a new BrowserAuthTransfer object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserAuthTransferWithDefaults

`func NewBrowserAuthTransferWithDefaults() *BrowserAuthTransfer`

NewBrowserAuthTransferWithDefaults instantiates a new BrowserAuthTransfer object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSources

`func (o *BrowserAuthTransfer) GetSources() []BrowserAuthSource`

GetSources returns the Sources field if non-nil, zero value otherwise.

### GetSourcesOk

`func (o *BrowserAuthTransfer) GetSourcesOk() (*[]BrowserAuthSource, bool)`

GetSourcesOk returns a tuple with the Sources field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSources

`func (o *BrowserAuthTransfer) SetSources(v []BrowserAuthSource)`

SetSources sets Sources field to given value.

### HasSources

`func (o *BrowserAuthTransfer) HasSources() bool`

HasSources returns a boolean if a field has been set.

### GetAuthorizationVariable

`func (o *BrowserAuthTransfer) GetAuthorizationVariable() string`

GetAuthorizationVariable returns the AuthorizationVariable field if non-nil, zero value otherwise.

### GetAuthorizationVariableOk

`func (o *BrowserAuthTransfer) GetAuthorizationVariableOk() (*string, bool)`

GetAuthorizationVariableOk returns a tuple with the AuthorizationVariable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationVariable

`func (o *BrowserAuthTransfer) SetAuthorizationVariable(v string)`

SetAuthorizationVariable sets AuthorizationVariable field to given value.

### HasAuthorizationVariable

`func (o *BrowserAuthTransfer) HasAuthorizationVariable() bool`

HasAuthorizationVariable returns a boolean if a field has been set.

### SetAuthorizationVariableNil

`func (o *BrowserAuthTransfer) SetAuthorizationVariableNil(b bool)`

 SetAuthorizationVariableNil sets the value for AuthorizationVariable to be an explicit nil

### UnsetAuthorizationVariable
`func (o *BrowserAuthTransfer) UnsetAuthorizationVariable()`

UnsetAuthorizationVariable ensures that no value is present for AuthorizationVariable, not even an explicit nil
### GetCandidates

`func (o *BrowserAuthTransfer) GetCandidates() []interface{}`

GetCandidates returns the Candidates field if non-nil, zero value otherwise.

### GetCandidatesOk

`func (o *BrowserAuthTransfer) GetCandidatesOk() (*[]interface{}, bool)`

GetCandidatesOk returns a tuple with the Candidates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCandidates

`func (o *BrowserAuthTransfer) SetCandidates(v []interface{})`

SetCandidates sets Candidates field to given value.

### HasCandidates

`func (o *BrowserAuthTransfer) HasCandidates() bool`

HasCandidates returns a boolean if a field has been set.

### GetOptionalRefresh

`func (o *BrowserAuthTransfer) GetOptionalRefresh() bool`

GetOptionalRefresh returns the OptionalRefresh field if non-nil, zero value otherwise.

### GetOptionalRefreshOk

`func (o *BrowserAuthTransfer) GetOptionalRefreshOk() (*bool, bool)`

GetOptionalRefreshOk returns a tuple with the OptionalRefresh field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOptionalRefresh

`func (o *BrowserAuthTransfer) SetOptionalRefresh(v bool)`

SetOptionalRefresh sets OptionalRefresh field to given value.

### HasOptionalRefresh

`func (o *BrowserAuthTransfer) HasOptionalRefresh() bool`

HasOptionalRefresh returns a boolean if a field has been set.

### GetChoiceId

`func (o *BrowserAuthTransfer) GetChoiceId() string`

GetChoiceId returns the ChoiceId field if non-nil, zero value otherwise.

### GetChoiceIdOk

`func (o *BrowserAuthTransfer) GetChoiceIdOk() (*string, bool)`

GetChoiceIdOk returns a tuple with the ChoiceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChoiceId

`func (o *BrowserAuthTransfer) SetChoiceId(v string)`

SetChoiceId sets ChoiceId field to given value.

### HasChoiceId

`func (o *BrowserAuthTransfer) HasChoiceId() bool`

HasChoiceId returns a boolean if a field has been set.

### SetChoiceIdNil

`func (o *BrowserAuthTransfer) SetChoiceIdNil(b bool)`

 SetChoiceIdNil sets the value for ChoiceId to be an explicit nil

### UnsetChoiceId
`func (o *BrowserAuthTransfer) UnsetChoiceId()`

UnsetChoiceId ensures that no value is present for ChoiceId, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
