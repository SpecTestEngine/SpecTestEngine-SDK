# StreamingLimits

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MaxDuration** | **string** |  |
**MaxIdleTimeout** | **string** |  |
**MaxEvents** | **int32** |  |
**MaxBytes** | **int64** |  |
**MaxEventBytes** | **int64** |  |
**MaxConcurrentRunsPerCompany** | **int32** |  |

## Methods

### NewStreamingLimits

`func NewStreamingLimits(maxDuration string, maxIdleTimeout string, maxEvents int32, maxBytes int64, maxEventBytes int64, maxConcurrentRunsPerCompany int32, ) *StreamingLimits`

NewStreamingLimits instantiates a new StreamingLimits object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStreamingLimitsWithDefaults

`func NewStreamingLimitsWithDefaults() *StreamingLimits`

NewStreamingLimitsWithDefaults instantiates a new StreamingLimits object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMaxDuration

`func (o *StreamingLimits) GetMaxDuration() string`

GetMaxDuration returns the MaxDuration field if non-nil, zero value otherwise.

### GetMaxDurationOk

`func (o *StreamingLimits) GetMaxDurationOk() (*string, bool)`

GetMaxDurationOk returns a tuple with the MaxDuration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxDuration

`func (o *StreamingLimits) SetMaxDuration(v string)`

SetMaxDuration sets MaxDuration field to given value.


### GetMaxIdleTimeout

`func (o *StreamingLimits) GetMaxIdleTimeout() string`

GetMaxIdleTimeout returns the MaxIdleTimeout field if non-nil, zero value otherwise.

### GetMaxIdleTimeoutOk

`func (o *StreamingLimits) GetMaxIdleTimeoutOk() (*string, bool)`

GetMaxIdleTimeoutOk returns a tuple with the MaxIdleTimeout field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxIdleTimeout

`func (o *StreamingLimits) SetMaxIdleTimeout(v string)`

SetMaxIdleTimeout sets MaxIdleTimeout field to given value.


### GetMaxEvents

`func (o *StreamingLimits) GetMaxEvents() int32`

GetMaxEvents returns the MaxEvents field if non-nil, zero value otherwise.

### GetMaxEventsOk

`func (o *StreamingLimits) GetMaxEventsOk() (*int32, bool)`

GetMaxEventsOk returns a tuple with the MaxEvents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxEvents

`func (o *StreamingLimits) SetMaxEvents(v int32)`

SetMaxEvents sets MaxEvents field to given value.


### GetMaxBytes

`func (o *StreamingLimits) GetMaxBytes() int64`

GetMaxBytes returns the MaxBytes field if non-nil, zero value otherwise.

### GetMaxBytesOk

`func (o *StreamingLimits) GetMaxBytesOk() (*int64, bool)`

GetMaxBytesOk returns a tuple with the MaxBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxBytes

`func (o *StreamingLimits) SetMaxBytes(v int64)`

SetMaxBytes sets MaxBytes field to given value.


### GetMaxEventBytes

`func (o *StreamingLimits) GetMaxEventBytes() int64`

GetMaxEventBytes returns the MaxEventBytes field if non-nil, zero value otherwise.

### GetMaxEventBytesOk

`func (o *StreamingLimits) GetMaxEventBytesOk() (*int64, bool)`

GetMaxEventBytesOk returns a tuple with the MaxEventBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxEventBytes

`func (o *StreamingLimits) SetMaxEventBytes(v int64)`

SetMaxEventBytes sets MaxEventBytes field to given value.


### GetMaxConcurrentRunsPerCompany

`func (o *StreamingLimits) GetMaxConcurrentRunsPerCompany() int32`

GetMaxConcurrentRunsPerCompany returns the MaxConcurrentRunsPerCompany field if non-nil, zero value otherwise.

### GetMaxConcurrentRunsPerCompanyOk

`func (o *StreamingLimits) GetMaxConcurrentRunsPerCompanyOk() (*int32, bool)`

GetMaxConcurrentRunsPerCompanyOk returns a tuple with the MaxConcurrentRunsPerCompany field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxConcurrentRunsPerCompany

`func (o *StreamingLimits) SetMaxConcurrentRunsPerCompany(v int32)`

SetMaxConcurrentRunsPerCompany sets MaxConcurrentRunsPerCompany field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


