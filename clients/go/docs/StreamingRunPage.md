# StreamingRunPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Page** | **int32** |  |
**Size** | **int32** |  |
**TotalElements** | **int64** |  |
**TotalPages** | **int32** |  |
**First** | **bool** |  |
**Last** | **bool** |  |
**Items** | [**[]StreamingRun**](StreamingRun.md) |  |

## Methods

### NewStreamingRunPage

`func NewStreamingRunPage(page int32, size int32, totalElements int64, totalPages int32, first bool, last bool, items []StreamingRun, ) *StreamingRunPage`

NewStreamingRunPage instantiates a new StreamingRunPage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStreamingRunPageWithDefaults

`func NewStreamingRunPageWithDefaults() *StreamingRunPage`

NewStreamingRunPageWithDefaults instantiates a new StreamingRunPage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPage

`func (o *StreamingRunPage) GetPage() int32`

GetPage returns the Page field if non-nil, zero value otherwise.

### GetPageOk

`func (o *StreamingRunPage) GetPageOk() (*int32, bool)`

GetPageOk returns a tuple with the Page field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPage

`func (o *StreamingRunPage) SetPage(v int32)`

SetPage sets Page field to given value.


### GetSize

`func (o *StreamingRunPage) GetSize() int32`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *StreamingRunPage) GetSizeOk() (*int32, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *StreamingRunPage) SetSize(v int32)`

SetSize sets Size field to given value.


### GetTotalElements

`func (o *StreamingRunPage) GetTotalElements() int64`

GetTotalElements returns the TotalElements field if non-nil, zero value otherwise.

### GetTotalElementsOk

`func (o *StreamingRunPage) GetTotalElementsOk() (*int64, bool)`

GetTotalElementsOk returns a tuple with the TotalElements field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalElements

`func (o *StreamingRunPage) SetTotalElements(v int64)`

SetTotalElements sets TotalElements field to given value.


### GetTotalPages

`func (o *StreamingRunPage) GetTotalPages() int32`

GetTotalPages returns the TotalPages field if non-nil, zero value otherwise.

### GetTotalPagesOk

`func (o *StreamingRunPage) GetTotalPagesOk() (*int32, bool)`

GetTotalPagesOk returns a tuple with the TotalPages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalPages

`func (o *StreamingRunPage) SetTotalPages(v int32)`

SetTotalPages sets TotalPages field to given value.


### GetFirst

`func (o *StreamingRunPage) GetFirst() bool`

GetFirst returns the First field if non-nil, zero value otherwise.

### GetFirstOk

`func (o *StreamingRunPage) GetFirstOk() (*bool, bool)`

GetFirstOk returns a tuple with the First field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirst

`func (o *StreamingRunPage) SetFirst(v bool)`

SetFirst sets First field to given value.


### GetLast

`func (o *StreamingRunPage) GetLast() bool`

GetLast returns the Last field if non-nil, zero value otherwise.

### GetLastOk

`func (o *StreamingRunPage) GetLastOk() (*bool, bool)`

GetLastOk returns a tuple with the Last field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLast

`func (o *StreamingRunPage) SetLast(v bool)`

SetLast sets Last field to given value.


### GetItems

`func (o *StreamingRunPage) GetItems() []StreamingRun`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *StreamingRunPage) GetItemsOk() (*[]StreamingRun, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *StreamingRunPage) SetItems(v []StreamingRun)`

SetItems sets Items field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
