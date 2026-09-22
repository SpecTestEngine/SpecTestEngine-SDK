# StreamingTranscriptPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RunId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Events** | **[]map[string]interface{}** |  |
**Page** | **int32** |  |
**Size** | **int32** |  |
**TotalElements** | **int64** |  |
**TotalPages** | **int32** |  |
**Complete** | **bool** |  |

## Methods

### NewStreamingTranscriptPage

`func NewStreamingTranscriptPage(runId string, events []map[string]interface{}, page int32, size int32, totalElements int64, totalPages int32, complete bool, ) *StreamingTranscriptPage`

NewStreamingTranscriptPage instantiates a new StreamingTranscriptPage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStreamingTranscriptPageWithDefaults

`func NewStreamingTranscriptPageWithDefaults() *StreamingTranscriptPage`

NewStreamingTranscriptPageWithDefaults instantiates a new StreamingTranscriptPage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRunId

`func (o *StreamingTranscriptPage) GetRunId() string`

GetRunId returns the RunId field if non-nil, zero value otherwise.

### GetRunIdOk

`func (o *StreamingTranscriptPage) GetRunIdOk() (*string, bool)`

GetRunIdOk returns a tuple with the RunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRunId

`func (o *StreamingTranscriptPage) SetRunId(v string)`

SetRunId sets RunId field to given value.


### GetEvents

`func (o *StreamingTranscriptPage) GetEvents() []map[string]interface{}`

GetEvents returns the Events field if non-nil, zero value otherwise.

### GetEventsOk

`func (o *StreamingTranscriptPage) GetEventsOk() (*[]map[string]interface{}, bool)`

GetEventsOk returns a tuple with the Events field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvents

`func (o *StreamingTranscriptPage) SetEvents(v []map[string]interface{})`

SetEvents sets Events field to given value.


### GetPage

`func (o *StreamingTranscriptPage) GetPage() int32`

GetPage returns the Page field if non-nil, zero value otherwise.

### GetPageOk

`func (o *StreamingTranscriptPage) GetPageOk() (*int32, bool)`

GetPageOk returns a tuple with the Page field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPage

`func (o *StreamingTranscriptPage) SetPage(v int32)`

SetPage sets Page field to given value.


### GetSize

`func (o *StreamingTranscriptPage) GetSize() int32`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *StreamingTranscriptPage) GetSizeOk() (*int32, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *StreamingTranscriptPage) SetSize(v int32)`

SetSize sets Size field to given value.


### GetTotalElements

`func (o *StreamingTranscriptPage) GetTotalElements() int64`

GetTotalElements returns the TotalElements field if non-nil, zero value otherwise.

### GetTotalElementsOk

`func (o *StreamingTranscriptPage) GetTotalElementsOk() (*int64, bool)`

GetTotalElementsOk returns a tuple with the TotalElements field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalElements

`func (o *StreamingTranscriptPage) SetTotalElements(v int64)`

SetTotalElements sets TotalElements field to given value.


### GetTotalPages

`func (o *StreamingTranscriptPage) GetTotalPages() int32`

GetTotalPages returns the TotalPages field if non-nil, zero value otherwise.

### GetTotalPagesOk

`func (o *StreamingTranscriptPage) GetTotalPagesOk() (*int32, bool)`

GetTotalPagesOk returns a tuple with the TotalPages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalPages

`func (o *StreamingTranscriptPage) SetTotalPages(v int32)`

SetTotalPages sets TotalPages field to given value.


### GetComplete

`func (o *StreamingTranscriptPage) GetComplete() bool`

GetComplete returns the Complete field if non-nil, zero value otherwise.

### GetCompleteOk

`func (o *StreamingTranscriptPage) GetCompleteOk() (*bool, bool)`

GetCompleteOk returns a tuple with the Complete field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComplete

`func (o *StreamingTranscriptPage) SetComplete(v bool)`

SetComplete sets Complete field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


