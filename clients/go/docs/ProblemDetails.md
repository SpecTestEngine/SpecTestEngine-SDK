# ProblemDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Timestamp** | **time.Time** |  |
**Status** | **int32** |  |
**Error** | **string** |  |
**Message** | **string** |  |
**Path** | **string** |  |
**ErrorCode** | **string** |  |
**TranslationKey** | Pointer to **NullableString** |  | [optional]
**RequestId** | Pointer to **NullableString** |  | [optional]
**Violations** | Pointer to **[]map[string]interface{}** |  | [optional]

## Methods

### NewProblemDetails

`func NewProblemDetails(timestamp time.Time, status int32, error_ string, message string, path string, errorCode string, ) *ProblemDetails`

NewProblemDetails instantiates a new ProblemDetails object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProblemDetailsWithDefaults

`func NewProblemDetailsWithDefaults() *ProblemDetails`

NewProblemDetailsWithDefaults instantiates a new ProblemDetails object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTimestamp

`func (o *ProblemDetails) GetTimestamp() time.Time`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *ProblemDetails) GetTimestampOk() (*time.Time, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *ProblemDetails) SetTimestamp(v time.Time)`

SetTimestamp sets Timestamp field to given value.


### GetStatus

`func (o *ProblemDetails) GetStatus() int32`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ProblemDetails) GetStatusOk() (*int32, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ProblemDetails) SetStatus(v int32)`

SetStatus sets Status field to given value.


### GetError

`func (o *ProblemDetails) GetError() string`

GetError returns the Error field if non-nil, zero value otherwise.

### GetErrorOk

`func (o *ProblemDetails) GetErrorOk() (*string, bool)`

GetErrorOk returns a tuple with the Error field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetError

`func (o *ProblemDetails) SetError(v string)`

SetError sets Error field to given value.


### GetMessage

`func (o *ProblemDetails) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *ProblemDetails) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *ProblemDetails) SetMessage(v string)`

SetMessage sets Message field to given value.


### GetPath

`func (o *ProblemDetails) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *ProblemDetails) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *ProblemDetails) SetPath(v string)`

SetPath sets Path field to given value.


### GetErrorCode

`func (o *ProblemDetails) GetErrorCode() string`

GetErrorCode returns the ErrorCode field if non-nil, zero value otherwise.

### GetErrorCodeOk

`func (o *ProblemDetails) GetErrorCodeOk() (*string, bool)`

GetErrorCodeOk returns a tuple with the ErrorCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorCode

`func (o *ProblemDetails) SetErrorCode(v string)`

SetErrorCode sets ErrorCode field to given value.


### GetTranslationKey

`func (o *ProblemDetails) GetTranslationKey() string`

GetTranslationKey returns the TranslationKey field if non-nil, zero value otherwise.

### GetTranslationKeyOk

`func (o *ProblemDetails) GetTranslationKeyOk() (*string, bool)`

GetTranslationKeyOk returns a tuple with the TranslationKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTranslationKey

`func (o *ProblemDetails) SetTranslationKey(v string)`

SetTranslationKey sets TranslationKey field to given value.

### HasTranslationKey

`func (o *ProblemDetails) HasTranslationKey() bool`

HasTranslationKey returns a boolean if a field has been set.

### SetTranslationKeyNil

`func (o *ProblemDetails) SetTranslationKeyNil(b bool)`

 SetTranslationKeyNil sets the value for TranslationKey to be an explicit nil

### UnsetTranslationKey
`func (o *ProblemDetails) UnsetTranslationKey()`

UnsetTranslationKey ensures that no value is present for TranslationKey, not even an explicit nil
### GetRequestId

`func (o *ProblemDetails) GetRequestId() string`

GetRequestId returns the RequestId field if non-nil, zero value otherwise.

### GetRequestIdOk

`func (o *ProblemDetails) GetRequestIdOk() (*string, bool)`

GetRequestIdOk returns a tuple with the RequestId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestId

`func (o *ProblemDetails) SetRequestId(v string)`

SetRequestId sets RequestId field to given value.

### HasRequestId

`func (o *ProblemDetails) HasRequestId() bool`

HasRequestId returns a boolean if a field has been set.

### SetRequestIdNil

`func (o *ProblemDetails) SetRequestIdNil(b bool)`

 SetRequestIdNil sets the value for RequestId to be an explicit nil

### UnsetRequestId
`func (o *ProblemDetails) UnsetRequestId()`

UnsetRequestId ensures that no value is present for RequestId, not even an explicit nil
### GetViolations

`func (o *ProblemDetails) GetViolations() []map[string]interface{}`

GetViolations returns the Violations field if non-nil, zero value otherwise.

### GetViolationsOk

`func (o *ProblemDetails) GetViolationsOk() (*[]map[string]interface{}, bool)`

GetViolationsOk returns a tuple with the Violations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetViolations

`func (o *ProblemDetails) SetViolations(v []map[string]interface{})`

SetViolations sets Violations field to given value.

### HasViolations

`func (o *ProblemDetails) HasViolations() bool`

HasViolations returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
