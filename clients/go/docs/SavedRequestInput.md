# SavedRequestInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SpecType** | **string** |  |
**Method** | Pointer to **string** |  | [optional]
**Url** | Pointer to **string** |  | [optional]
**StreamingSpec** | Pointer to [**NullableStreamingDefinition**](StreamingDefinition.md) |  | [optional]
**Headers** | Pointer to **map[string]string** |  | [optional]
**QueryParams** | Pointer to **map[string]string** |  | [optional]
**Body** | Pointer to **NullableString** |  | [optional]
**Auth** | Pointer to **map[string]interface{}** |  | [optional]
**RequestAuth** | Pointer to **map[string]interface{}** |  | [optional]
**RequestAttachments** | Pointer to [**[]DocumentAssetReference**](DocumentAssetReference.md) |  | [optional]
**Prerequisites** | Pointer to **[]map[string]interface{}** |  | [optional]

## Methods

### NewSavedRequestInput

`func NewSavedRequestInput(specType string, ) *SavedRequestInput`

NewSavedRequestInput instantiates a new SavedRequestInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSavedRequestInputWithDefaults

`func NewSavedRequestInputWithDefaults() *SavedRequestInput`

NewSavedRequestInputWithDefaults instantiates a new SavedRequestInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSpecType

`func (o *SavedRequestInput) GetSpecType() string`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *SavedRequestInput) GetSpecTypeOk() (*string, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *SavedRequestInput) SetSpecType(v string)`

SetSpecType sets SpecType field to given value.


### GetMethod

`func (o *SavedRequestInput) GetMethod() string`

GetMethod returns the Method field if non-nil, zero value otherwise.

### GetMethodOk

`func (o *SavedRequestInput) GetMethodOk() (*string, bool)`

GetMethodOk returns a tuple with the Method field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMethod

`func (o *SavedRequestInput) SetMethod(v string)`

SetMethod sets Method field to given value.

### HasMethod

`func (o *SavedRequestInput) HasMethod() bool`

HasMethod returns a boolean if a field has been set.

### GetUrl

`func (o *SavedRequestInput) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *SavedRequestInput) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *SavedRequestInput) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *SavedRequestInput) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### GetStreamingSpec

`func (o *SavedRequestInput) GetStreamingSpec() StreamingDefinition`

GetStreamingSpec returns the StreamingSpec field if non-nil, zero value otherwise.

### GetStreamingSpecOk

`func (o *SavedRequestInput) GetStreamingSpecOk() (*StreamingDefinition, bool)`

GetStreamingSpecOk returns a tuple with the StreamingSpec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreamingSpec

`func (o *SavedRequestInput) SetStreamingSpec(v StreamingDefinition)`

SetStreamingSpec sets StreamingSpec field to given value.

### HasStreamingSpec

`func (o *SavedRequestInput) HasStreamingSpec() bool`

HasStreamingSpec returns a boolean if a field has been set.

### SetStreamingSpecNil

`func (o *SavedRequestInput) SetStreamingSpecNil(b bool)`

 SetStreamingSpecNil sets the value for StreamingSpec to be an explicit nil

### UnsetStreamingSpec
`func (o *SavedRequestInput) UnsetStreamingSpec()`

UnsetStreamingSpec ensures that no value is present for StreamingSpec, not even an explicit nil
### GetHeaders

`func (o *SavedRequestInput) GetHeaders() map[string]string`

GetHeaders returns the Headers field if non-nil, zero value otherwise.

### GetHeadersOk

`func (o *SavedRequestInput) GetHeadersOk() (*map[string]string, bool)`

GetHeadersOk returns a tuple with the Headers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeaders

`func (o *SavedRequestInput) SetHeaders(v map[string]string)`

SetHeaders sets Headers field to given value.

### HasHeaders

`func (o *SavedRequestInput) HasHeaders() bool`

HasHeaders returns a boolean if a field has been set.

### GetQueryParams

`func (o *SavedRequestInput) GetQueryParams() map[string]string`

GetQueryParams returns the QueryParams field if non-nil, zero value otherwise.

### GetQueryParamsOk

`func (o *SavedRequestInput) GetQueryParamsOk() (*map[string]string, bool)`

GetQueryParamsOk returns a tuple with the QueryParams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryParams

`func (o *SavedRequestInput) SetQueryParams(v map[string]string)`

SetQueryParams sets QueryParams field to given value.

### HasQueryParams

`func (o *SavedRequestInput) HasQueryParams() bool`

HasQueryParams returns a boolean if a field has been set.

### GetBody

`func (o *SavedRequestInput) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *SavedRequestInput) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *SavedRequestInput) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *SavedRequestInput) HasBody() bool`

HasBody returns a boolean if a field has been set.

### SetBodyNil

`func (o *SavedRequestInput) SetBodyNil(b bool)`

 SetBodyNil sets the value for Body to be an explicit nil

### UnsetBody
`func (o *SavedRequestInput) UnsetBody()`

UnsetBody ensures that no value is present for Body, not even an explicit nil
### GetAuth

`func (o *SavedRequestInput) GetAuth() map[string]interface{}`

GetAuth returns the Auth field if non-nil, zero value otherwise.

### GetAuthOk

`func (o *SavedRequestInput) GetAuthOk() (*map[string]interface{}, bool)`

GetAuthOk returns a tuple with the Auth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuth

`func (o *SavedRequestInput) SetAuth(v map[string]interface{})`

SetAuth sets Auth field to given value.

### HasAuth

`func (o *SavedRequestInput) HasAuth() bool`

HasAuth returns a boolean if a field has been set.

### SetAuthNil

`func (o *SavedRequestInput) SetAuthNil(b bool)`

 SetAuthNil sets the value for Auth to be an explicit nil

### UnsetAuth
`func (o *SavedRequestInput) UnsetAuth()`

UnsetAuth ensures that no value is present for Auth, not even an explicit nil
### GetRequestAuth

`func (o *SavedRequestInput) GetRequestAuth() map[string]interface{}`

GetRequestAuth returns the RequestAuth field if non-nil, zero value otherwise.

### GetRequestAuthOk

`func (o *SavedRequestInput) GetRequestAuthOk() (*map[string]interface{}, bool)`

GetRequestAuthOk returns a tuple with the RequestAuth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestAuth

`func (o *SavedRequestInput) SetRequestAuth(v map[string]interface{})`

SetRequestAuth sets RequestAuth field to given value.

### HasRequestAuth

`func (o *SavedRequestInput) HasRequestAuth() bool`

HasRequestAuth returns a boolean if a field has been set.

### SetRequestAuthNil

`func (o *SavedRequestInput) SetRequestAuthNil(b bool)`

 SetRequestAuthNil sets the value for RequestAuth to be an explicit nil

### UnsetRequestAuth
`func (o *SavedRequestInput) UnsetRequestAuth()`

UnsetRequestAuth ensures that no value is present for RequestAuth, not even an explicit nil
### GetRequestAttachments

`func (o *SavedRequestInput) GetRequestAttachments() []DocumentAssetReference`

GetRequestAttachments returns the RequestAttachments field if non-nil, zero value otherwise.

### GetRequestAttachmentsOk

`func (o *SavedRequestInput) GetRequestAttachmentsOk() (*[]DocumentAssetReference, bool)`

GetRequestAttachmentsOk returns a tuple with the RequestAttachments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestAttachments

`func (o *SavedRequestInput) SetRequestAttachments(v []DocumentAssetReference)`

SetRequestAttachments sets RequestAttachments field to given value.

### HasRequestAttachments

`func (o *SavedRequestInput) HasRequestAttachments() bool`

HasRequestAttachments returns a boolean if a field has been set.

### GetPrerequisites

`func (o *SavedRequestInput) GetPrerequisites() []map[string]interface{}`

GetPrerequisites returns the Prerequisites field if non-nil, zero value otherwise.

### GetPrerequisitesOk

`func (o *SavedRequestInput) GetPrerequisitesOk() (*[]map[string]interface{}, bool)`

GetPrerequisitesOk returns a tuple with the Prerequisites field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrerequisites

`func (o *SavedRequestInput) SetPrerequisites(v []map[string]interface{})`

SetPrerequisites sets Prerequisites field to given value.

### HasPrerequisites

`func (o *SavedRequestInput) HasPrerequisites() bool`

HasPrerequisites returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
