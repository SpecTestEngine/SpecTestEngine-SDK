# SentinelRunBaseline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Status** | [**RunStatus**](RunStatus.md) |  |
**Label** | **string** |  |
**DefinitionHash** | **string** |  |
**BehaviorHash** | Pointer to **NullableString** | Assertion-relevant fingerprint; raw transport payloads and explicitly excluded evidence do not affect it. | [optional]
**ResponseHeadersJson** | Pointer to **NullableString** |  | [optional]
**ResponseBodyPreview** | Pointer to **NullableString** |  | [optional]
**ResultLog** | Pointer to **NullableString** |  | [optional]
**ErrorMessage** | Pointer to **NullableString** |  | [optional]
**FinishedAt** | Pointer to **NullableTime** |  | [optional]

## Methods

### NewSentinelRunBaseline

`func NewSentinelRunBaseline(id string, status RunStatus, label string, definitionHash string, ) *SentinelRunBaseline`

NewSentinelRunBaseline instantiates a new SentinelRunBaseline object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSentinelRunBaselineWithDefaults

`func NewSentinelRunBaselineWithDefaults() *SentinelRunBaseline`

NewSentinelRunBaselineWithDefaults instantiates a new SentinelRunBaseline object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SentinelRunBaseline) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SentinelRunBaseline) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SentinelRunBaseline) SetId(v string)`

SetId sets Id field to given value.


### GetStatus

`func (o *SentinelRunBaseline) GetStatus() RunStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SentinelRunBaseline) GetStatusOk() (*RunStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SentinelRunBaseline) SetStatus(v RunStatus)`

SetStatus sets Status field to given value.


### GetLabel

`func (o *SentinelRunBaseline) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *SentinelRunBaseline) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *SentinelRunBaseline) SetLabel(v string)`

SetLabel sets Label field to given value.


### GetDefinitionHash

`func (o *SentinelRunBaseline) GetDefinitionHash() string`

GetDefinitionHash returns the DefinitionHash field if non-nil, zero value otherwise.

### GetDefinitionHashOk

`func (o *SentinelRunBaseline) GetDefinitionHashOk() (*string, bool)`

GetDefinitionHashOk returns a tuple with the DefinitionHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinitionHash

`func (o *SentinelRunBaseline) SetDefinitionHash(v string)`

SetDefinitionHash sets DefinitionHash field to given value.


### GetBehaviorHash

`func (o *SentinelRunBaseline) GetBehaviorHash() string`

GetBehaviorHash returns the BehaviorHash field if non-nil, zero value otherwise.

### GetBehaviorHashOk

`func (o *SentinelRunBaseline) GetBehaviorHashOk() (*string, bool)`

GetBehaviorHashOk returns a tuple with the BehaviorHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBehaviorHash

`func (o *SentinelRunBaseline) SetBehaviorHash(v string)`

SetBehaviorHash sets BehaviorHash field to given value.

### HasBehaviorHash

`func (o *SentinelRunBaseline) HasBehaviorHash() bool`

HasBehaviorHash returns a boolean if a field has been set.

### SetBehaviorHashNil

`func (o *SentinelRunBaseline) SetBehaviorHashNil(b bool)`

 SetBehaviorHashNil sets the value for BehaviorHash to be an explicit nil

### UnsetBehaviorHash
`func (o *SentinelRunBaseline) UnsetBehaviorHash()`

UnsetBehaviorHash ensures that no value is present for BehaviorHash, not even an explicit nil
### GetResponseHeadersJson

`func (o *SentinelRunBaseline) GetResponseHeadersJson() string`

GetResponseHeadersJson returns the ResponseHeadersJson field if non-nil, zero value otherwise.

### GetResponseHeadersJsonOk

`func (o *SentinelRunBaseline) GetResponseHeadersJsonOk() (*string, bool)`

GetResponseHeadersJsonOk returns a tuple with the ResponseHeadersJson field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseHeadersJson

`func (o *SentinelRunBaseline) SetResponseHeadersJson(v string)`

SetResponseHeadersJson sets ResponseHeadersJson field to given value.

### HasResponseHeadersJson

`func (o *SentinelRunBaseline) HasResponseHeadersJson() bool`

HasResponseHeadersJson returns a boolean if a field has been set.

### SetResponseHeadersJsonNil

`func (o *SentinelRunBaseline) SetResponseHeadersJsonNil(b bool)`

 SetResponseHeadersJsonNil sets the value for ResponseHeadersJson to be an explicit nil

### UnsetResponseHeadersJson
`func (o *SentinelRunBaseline) UnsetResponseHeadersJson()`

UnsetResponseHeadersJson ensures that no value is present for ResponseHeadersJson, not even an explicit nil
### GetResponseBodyPreview

`func (o *SentinelRunBaseline) GetResponseBodyPreview() string`

GetResponseBodyPreview returns the ResponseBodyPreview field if non-nil, zero value otherwise.

### GetResponseBodyPreviewOk

`func (o *SentinelRunBaseline) GetResponseBodyPreviewOk() (*string, bool)`

GetResponseBodyPreviewOk returns a tuple with the ResponseBodyPreview field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseBodyPreview

`func (o *SentinelRunBaseline) SetResponseBodyPreview(v string)`

SetResponseBodyPreview sets ResponseBodyPreview field to given value.

### HasResponseBodyPreview

`func (o *SentinelRunBaseline) HasResponseBodyPreview() bool`

HasResponseBodyPreview returns a boolean if a field has been set.

### SetResponseBodyPreviewNil

`func (o *SentinelRunBaseline) SetResponseBodyPreviewNil(b bool)`

 SetResponseBodyPreviewNil sets the value for ResponseBodyPreview to be an explicit nil

### UnsetResponseBodyPreview
`func (o *SentinelRunBaseline) UnsetResponseBodyPreview()`

UnsetResponseBodyPreview ensures that no value is present for ResponseBodyPreview, not even an explicit nil
### GetResultLog

`func (o *SentinelRunBaseline) GetResultLog() string`

GetResultLog returns the ResultLog field if non-nil, zero value otherwise.

### GetResultLogOk

`func (o *SentinelRunBaseline) GetResultLogOk() (*string, bool)`

GetResultLogOk returns a tuple with the ResultLog field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResultLog

`func (o *SentinelRunBaseline) SetResultLog(v string)`

SetResultLog sets ResultLog field to given value.

### HasResultLog

`func (o *SentinelRunBaseline) HasResultLog() bool`

HasResultLog returns a boolean if a field has been set.

### SetResultLogNil

`func (o *SentinelRunBaseline) SetResultLogNil(b bool)`

 SetResultLogNil sets the value for ResultLog to be an explicit nil

### UnsetResultLog
`func (o *SentinelRunBaseline) UnsetResultLog()`

UnsetResultLog ensures that no value is present for ResultLog, not even an explicit nil
### GetErrorMessage

`func (o *SentinelRunBaseline) GetErrorMessage() string`

GetErrorMessage returns the ErrorMessage field if non-nil, zero value otherwise.

### GetErrorMessageOk

`func (o *SentinelRunBaseline) GetErrorMessageOk() (*string, bool)`

GetErrorMessageOk returns a tuple with the ErrorMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorMessage

`func (o *SentinelRunBaseline) SetErrorMessage(v string)`

SetErrorMessage sets ErrorMessage field to given value.

### HasErrorMessage

`func (o *SentinelRunBaseline) HasErrorMessage() bool`

HasErrorMessage returns a boolean if a field has been set.

### SetErrorMessageNil

`func (o *SentinelRunBaseline) SetErrorMessageNil(b bool)`

 SetErrorMessageNil sets the value for ErrorMessage to be an explicit nil

### UnsetErrorMessage
`func (o *SentinelRunBaseline) UnsetErrorMessage()`

UnsetErrorMessage ensures that no value is present for ErrorMessage, not even an explicit nil
### GetFinishedAt

`func (o *SentinelRunBaseline) GetFinishedAt() time.Time`

GetFinishedAt returns the FinishedAt field if non-nil, zero value otherwise.

### GetFinishedAtOk

`func (o *SentinelRunBaseline) GetFinishedAtOk() (*time.Time, bool)`

GetFinishedAtOk returns a tuple with the FinishedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinishedAt

`func (o *SentinelRunBaseline) SetFinishedAt(v time.Time)`

SetFinishedAt sets FinishedAt field to given value.

### HasFinishedAt

`func (o *SentinelRunBaseline) HasFinishedAt() bool`

HasFinishedAt returns a boolean if a field has been set.

### SetFinishedAtNil

`func (o *SentinelRunBaseline) SetFinishedAtNil(b bool)`

 SetFinishedAtNil sets the value for FinishedAt to be an explicit nil

### UnsetFinishedAt
`func (o *SentinelRunBaseline) UnsetFinishedAt()`

UnsetFinishedAt ensures that no value is present for FinishedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


