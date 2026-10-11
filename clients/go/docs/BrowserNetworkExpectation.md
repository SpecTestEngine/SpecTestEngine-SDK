# BrowserNetworkExpectation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | Pointer to **bool** |  | [optional]
**RecordedCallId** | Pointer to **int32** |  | [optional]
**RecordedUrl** | Pointer to **string** |  | [optional]
**Method** | Pointer to **string** |  | [optional]
**Url** | Pointer to **string** |  | [optional]
**ExpectedStatusCode** | Pointer to **int32** |  | [optional]
**CandidateStatusCode** | Pointer to **int32** |  | [optional]
**ExpectedContentType** | Pointer to **string** |  | [optional]
**CandidateContentType** | Pointer to **string** |  | [optional]
**ExpectedHeaders** | Pointer to **map[string]string** |  | [optional]
**CandidateHeaders** | Pointer to **map[string]string** |  | [optional]
**ExcludedHeaderFields** | Pointer to **[]string** |  | [optional]
**ExcludeAllOtherHeaderFields** | Pointer to **bool** |  | [optional]
**Body** | Pointer to **interface{}** |  | [optional]
**CandidateBody** | Pointer to **interface{}** |  | [optional]
**ExpectedBodyPaths** | Pointer to **[]map[string]interface{}** |  | [optional]
**CandidateBodyPaths** | Pointer to **map[string]interface{}** |  | [optional]
**ExcludedBodyFields** | Pointer to **[]string** |  | [optional]

## Methods

### NewBrowserNetworkExpectation

`func NewBrowserNetworkExpectation() *BrowserNetworkExpectation`

NewBrowserNetworkExpectation instantiates a new BrowserNetworkExpectation object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserNetworkExpectationWithDefaults

`func NewBrowserNetworkExpectationWithDefaults() *BrowserNetworkExpectation`

NewBrowserNetworkExpectationWithDefaults instantiates a new BrowserNetworkExpectation object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnabled

`func (o *BrowserNetworkExpectation) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *BrowserNetworkExpectation) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *BrowserNetworkExpectation) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *BrowserNetworkExpectation) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetRecordedCallId

`func (o *BrowserNetworkExpectation) GetRecordedCallId() int32`

GetRecordedCallId returns the RecordedCallId field if non-nil, zero value otherwise.

### GetRecordedCallIdOk

`func (o *BrowserNetworkExpectation) GetRecordedCallIdOk() (*int32, bool)`

GetRecordedCallIdOk returns a tuple with the RecordedCallId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecordedCallId

`func (o *BrowserNetworkExpectation) SetRecordedCallId(v int32)`

SetRecordedCallId sets RecordedCallId field to given value.

### HasRecordedCallId

`func (o *BrowserNetworkExpectation) HasRecordedCallId() bool`

HasRecordedCallId returns a boolean if a field has been set.

### GetRecordedUrl

`func (o *BrowserNetworkExpectation) GetRecordedUrl() string`

GetRecordedUrl returns the RecordedUrl field if non-nil, zero value otherwise.

### GetRecordedUrlOk

`func (o *BrowserNetworkExpectation) GetRecordedUrlOk() (*string, bool)`

GetRecordedUrlOk returns a tuple with the RecordedUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecordedUrl

`func (o *BrowserNetworkExpectation) SetRecordedUrl(v string)`

SetRecordedUrl sets RecordedUrl field to given value.

### HasRecordedUrl

`func (o *BrowserNetworkExpectation) HasRecordedUrl() bool`

HasRecordedUrl returns a boolean if a field has been set.

### GetMethod

`func (o *BrowserNetworkExpectation) GetMethod() string`

GetMethod returns the Method field if non-nil, zero value otherwise.

### GetMethodOk

`func (o *BrowserNetworkExpectation) GetMethodOk() (*string, bool)`

GetMethodOk returns a tuple with the Method field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMethod

`func (o *BrowserNetworkExpectation) SetMethod(v string)`

SetMethod sets Method field to given value.

### HasMethod

`func (o *BrowserNetworkExpectation) HasMethod() bool`

HasMethod returns a boolean if a field has been set.

### GetUrl

`func (o *BrowserNetworkExpectation) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *BrowserNetworkExpectation) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *BrowserNetworkExpectation) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *BrowserNetworkExpectation) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### GetExpectedStatusCode

`func (o *BrowserNetworkExpectation) GetExpectedStatusCode() int32`

GetExpectedStatusCode returns the ExpectedStatusCode field if non-nil, zero value otherwise.

### GetExpectedStatusCodeOk

`func (o *BrowserNetworkExpectation) GetExpectedStatusCodeOk() (*int32, bool)`

GetExpectedStatusCodeOk returns a tuple with the ExpectedStatusCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedStatusCode

`func (o *BrowserNetworkExpectation) SetExpectedStatusCode(v int32)`

SetExpectedStatusCode sets ExpectedStatusCode field to given value.

### HasExpectedStatusCode

`func (o *BrowserNetworkExpectation) HasExpectedStatusCode() bool`

HasExpectedStatusCode returns a boolean if a field has been set.

### GetCandidateStatusCode

`func (o *BrowserNetworkExpectation) GetCandidateStatusCode() int32`

GetCandidateStatusCode returns the CandidateStatusCode field if non-nil, zero value otherwise.

### GetCandidateStatusCodeOk

`func (o *BrowserNetworkExpectation) GetCandidateStatusCodeOk() (*int32, bool)`

GetCandidateStatusCodeOk returns a tuple with the CandidateStatusCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCandidateStatusCode

`func (o *BrowserNetworkExpectation) SetCandidateStatusCode(v int32)`

SetCandidateStatusCode sets CandidateStatusCode field to given value.

### HasCandidateStatusCode

`func (o *BrowserNetworkExpectation) HasCandidateStatusCode() bool`

HasCandidateStatusCode returns a boolean if a field has been set.

### GetExpectedContentType

`func (o *BrowserNetworkExpectation) GetExpectedContentType() string`

GetExpectedContentType returns the ExpectedContentType field if non-nil, zero value otherwise.

### GetExpectedContentTypeOk

`func (o *BrowserNetworkExpectation) GetExpectedContentTypeOk() (*string, bool)`

GetExpectedContentTypeOk returns a tuple with the ExpectedContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedContentType

`func (o *BrowserNetworkExpectation) SetExpectedContentType(v string)`

SetExpectedContentType sets ExpectedContentType field to given value.

### HasExpectedContentType

`func (o *BrowserNetworkExpectation) HasExpectedContentType() bool`

HasExpectedContentType returns a boolean if a field has been set.

### GetCandidateContentType

`func (o *BrowserNetworkExpectation) GetCandidateContentType() string`

GetCandidateContentType returns the CandidateContentType field if non-nil, zero value otherwise.

### GetCandidateContentTypeOk

`func (o *BrowserNetworkExpectation) GetCandidateContentTypeOk() (*string, bool)`

GetCandidateContentTypeOk returns a tuple with the CandidateContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCandidateContentType

`func (o *BrowserNetworkExpectation) SetCandidateContentType(v string)`

SetCandidateContentType sets CandidateContentType field to given value.

### HasCandidateContentType

`func (o *BrowserNetworkExpectation) HasCandidateContentType() bool`

HasCandidateContentType returns a boolean if a field has been set.

### GetExpectedHeaders

`func (o *BrowserNetworkExpectation) GetExpectedHeaders() map[string]string`

GetExpectedHeaders returns the ExpectedHeaders field if non-nil, zero value otherwise.

### GetExpectedHeadersOk

`func (o *BrowserNetworkExpectation) GetExpectedHeadersOk() (*map[string]string, bool)`

GetExpectedHeadersOk returns a tuple with the ExpectedHeaders field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedHeaders

`func (o *BrowserNetworkExpectation) SetExpectedHeaders(v map[string]string)`

SetExpectedHeaders sets ExpectedHeaders field to given value.

### HasExpectedHeaders

`func (o *BrowserNetworkExpectation) HasExpectedHeaders() bool`

HasExpectedHeaders returns a boolean if a field has been set.

### GetCandidateHeaders

`func (o *BrowserNetworkExpectation) GetCandidateHeaders() map[string]string`

GetCandidateHeaders returns the CandidateHeaders field if non-nil, zero value otherwise.

### GetCandidateHeadersOk

`func (o *BrowserNetworkExpectation) GetCandidateHeadersOk() (*map[string]string, bool)`

GetCandidateHeadersOk returns a tuple with the CandidateHeaders field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCandidateHeaders

`func (o *BrowserNetworkExpectation) SetCandidateHeaders(v map[string]string)`

SetCandidateHeaders sets CandidateHeaders field to given value.

### HasCandidateHeaders

`func (o *BrowserNetworkExpectation) HasCandidateHeaders() bool`

HasCandidateHeaders returns a boolean if a field has been set.

### GetExcludedHeaderFields

`func (o *BrowserNetworkExpectation) GetExcludedHeaderFields() []string`

GetExcludedHeaderFields returns the ExcludedHeaderFields field if non-nil, zero value otherwise.

### GetExcludedHeaderFieldsOk

`func (o *BrowserNetworkExpectation) GetExcludedHeaderFieldsOk() (*[]string, bool)`

GetExcludedHeaderFieldsOk returns a tuple with the ExcludedHeaderFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludedHeaderFields

`func (o *BrowserNetworkExpectation) SetExcludedHeaderFields(v []string)`

SetExcludedHeaderFields sets ExcludedHeaderFields field to given value.

### HasExcludedHeaderFields

`func (o *BrowserNetworkExpectation) HasExcludedHeaderFields() bool`

HasExcludedHeaderFields returns a boolean if a field has been set.

### GetExcludeAllOtherHeaderFields

`func (o *BrowserNetworkExpectation) GetExcludeAllOtherHeaderFields() bool`

GetExcludeAllOtherHeaderFields returns the ExcludeAllOtherHeaderFields field if non-nil, zero value otherwise.

### GetExcludeAllOtherHeaderFieldsOk

`func (o *BrowserNetworkExpectation) GetExcludeAllOtherHeaderFieldsOk() (*bool, bool)`

GetExcludeAllOtherHeaderFieldsOk returns a tuple with the ExcludeAllOtherHeaderFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeAllOtherHeaderFields

`func (o *BrowserNetworkExpectation) SetExcludeAllOtherHeaderFields(v bool)`

SetExcludeAllOtherHeaderFields sets ExcludeAllOtherHeaderFields field to given value.

### HasExcludeAllOtherHeaderFields

`func (o *BrowserNetworkExpectation) HasExcludeAllOtherHeaderFields() bool`

HasExcludeAllOtherHeaderFields returns a boolean if a field has been set.

### GetBody

`func (o *BrowserNetworkExpectation) GetBody() interface{}`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *BrowserNetworkExpectation) GetBodyOk() (*interface{}, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *BrowserNetworkExpectation) SetBody(v interface{})`

SetBody sets Body field to given value.

### HasBody

`func (o *BrowserNetworkExpectation) HasBody() bool`

HasBody returns a boolean if a field has been set.

### SetBodyNil

`func (o *BrowserNetworkExpectation) SetBodyNil(b bool)`

 SetBodyNil sets the value for Body to be an explicit nil

### UnsetBody
`func (o *BrowserNetworkExpectation) UnsetBody()`

UnsetBody ensures that no value is present for Body, not even an explicit nil
### GetCandidateBody

`func (o *BrowserNetworkExpectation) GetCandidateBody() interface{}`

GetCandidateBody returns the CandidateBody field if non-nil, zero value otherwise.

### GetCandidateBodyOk

`func (o *BrowserNetworkExpectation) GetCandidateBodyOk() (*interface{}, bool)`

GetCandidateBodyOk returns a tuple with the CandidateBody field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCandidateBody

`func (o *BrowserNetworkExpectation) SetCandidateBody(v interface{})`

SetCandidateBody sets CandidateBody field to given value.

### HasCandidateBody

`func (o *BrowserNetworkExpectation) HasCandidateBody() bool`

HasCandidateBody returns a boolean if a field has been set.

### SetCandidateBodyNil

`func (o *BrowserNetworkExpectation) SetCandidateBodyNil(b bool)`

 SetCandidateBodyNil sets the value for CandidateBody to be an explicit nil

### UnsetCandidateBody
`func (o *BrowserNetworkExpectation) UnsetCandidateBody()`

UnsetCandidateBody ensures that no value is present for CandidateBody, not even an explicit nil
### GetExpectedBodyPaths

`func (o *BrowserNetworkExpectation) GetExpectedBodyPaths() []map[string]interface{}`

GetExpectedBodyPaths returns the ExpectedBodyPaths field if non-nil, zero value otherwise.

### GetExpectedBodyPathsOk

`func (o *BrowserNetworkExpectation) GetExpectedBodyPathsOk() (*[]map[string]interface{}, bool)`

GetExpectedBodyPathsOk returns a tuple with the ExpectedBodyPaths field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedBodyPaths

`func (o *BrowserNetworkExpectation) SetExpectedBodyPaths(v []map[string]interface{})`

SetExpectedBodyPaths sets ExpectedBodyPaths field to given value.

### HasExpectedBodyPaths

`func (o *BrowserNetworkExpectation) HasExpectedBodyPaths() bool`

HasExpectedBodyPaths returns a boolean if a field has been set.

### GetCandidateBodyPaths

`func (o *BrowserNetworkExpectation) GetCandidateBodyPaths() map[string]interface{}`

GetCandidateBodyPaths returns the CandidateBodyPaths field if non-nil, zero value otherwise.

### GetCandidateBodyPathsOk

`func (o *BrowserNetworkExpectation) GetCandidateBodyPathsOk() (*map[string]interface{}, bool)`

GetCandidateBodyPathsOk returns a tuple with the CandidateBodyPaths field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCandidateBodyPaths

`func (o *BrowserNetworkExpectation) SetCandidateBodyPaths(v map[string]interface{})`

SetCandidateBodyPaths sets CandidateBodyPaths field to given value.

### HasCandidateBodyPaths

`func (o *BrowserNetworkExpectation) HasCandidateBodyPaths() bool`

HasCandidateBodyPaths returns a boolean if a field has been set.

### GetExcludedBodyFields

`func (o *BrowserNetworkExpectation) GetExcludedBodyFields() []string`

GetExcludedBodyFields returns the ExcludedBodyFields field if non-nil, zero value otherwise.

### GetExcludedBodyFieldsOk

`func (o *BrowserNetworkExpectation) GetExcludedBodyFieldsOk() (*[]string, bool)`

GetExcludedBodyFieldsOk returns a tuple with the ExcludedBodyFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludedBodyFields

`func (o *BrowserNetworkExpectation) SetExcludedBodyFields(v []string)`

SetExcludedBodyFields sets ExcludedBodyFields field to given value.

### HasExcludedBodyFields

`func (o *BrowserNetworkExpectation) HasExcludedBodyFields() bool`

HasExcludedBodyFields returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
