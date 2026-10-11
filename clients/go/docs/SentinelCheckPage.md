# SentinelCheckPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Page** | **int32** |  |
**Size** | **int32** |  |
**TotalElements** | **int64** |  |
**TotalPages** | **int32** |  |
**First** | **bool** |  |
**Last** | **bool** |  |
**Items** | [**[]SentinelCheck**](SentinelCheck.md) |  |

## Methods

### NewSentinelCheckPage

`func NewSentinelCheckPage(page int32, size int32, totalElements int64, totalPages int32, first bool, last bool, items []SentinelCheck, ) *SentinelCheckPage`

NewSentinelCheckPage instantiates a new SentinelCheckPage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSentinelCheckPageWithDefaults

`func NewSentinelCheckPageWithDefaults() *SentinelCheckPage`

NewSentinelCheckPageWithDefaults instantiates a new SentinelCheckPage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPage

`func (o *SentinelCheckPage) GetPage() int32`

GetPage returns the Page field if non-nil, zero value otherwise.

### GetPageOk

`func (o *SentinelCheckPage) GetPageOk() (*int32, bool)`

GetPageOk returns a tuple with the Page field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPage

`func (o *SentinelCheckPage) SetPage(v int32)`

SetPage sets Page field to given value.


### GetSize

`func (o *SentinelCheckPage) GetSize() int32`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *SentinelCheckPage) GetSizeOk() (*int32, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *SentinelCheckPage) SetSize(v int32)`

SetSize sets Size field to given value.


### GetTotalElements

`func (o *SentinelCheckPage) GetTotalElements() int64`

GetTotalElements returns the TotalElements field if non-nil, zero value otherwise.

### GetTotalElementsOk

`func (o *SentinelCheckPage) GetTotalElementsOk() (*int64, bool)`

GetTotalElementsOk returns a tuple with the TotalElements field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalElements

`func (o *SentinelCheckPage) SetTotalElements(v int64)`

SetTotalElements sets TotalElements field to given value.


### GetTotalPages

`func (o *SentinelCheckPage) GetTotalPages() int32`

GetTotalPages returns the TotalPages field if non-nil, zero value otherwise.

### GetTotalPagesOk

`func (o *SentinelCheckPage) GetTotalPagesOk() (*int32, bool)`

GetTotalPagesOk returns a tuple with the TotalPages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalPages

`func (o *SentinelCheckPage) SetTotalPages(v int32)`

SetTotalPages sets TotalPages field to given value.


### GetFirst

`func (o *SentinelCheckPage) GetFirst() bool`

GetFirst returns the First field if non-nil, zero value otherwise.

### GetFirstOk

`func (o *SentinelCheckPage) GetFirstOk() (*bool, bool)`

GetFirstOk returns a tuple with the First field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirst

`func (o *SentinelCheckPage) SetFirst(v bool)`

SetFirst sets First field to given value.


### GetLast

`func (o *SentinelCheckPage) GetLast() bool`

GetLast returns the Last field if non-nil, zero value otherwise.

### GetLastOk

`func (o *SentinelCheckPage) GetLastOk() (*bool, bool)`

GetLastOk returns a tuple with the Last field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLast

`func (o *SentinelCheckPage) SetLast(v bool)`

SetLast sets Last field to given value.


### GetItems

`func (o *SentinelCheckPage) GetItems() []SentinelCheck`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *SentinelCheckPage) GetItemsOk() (*[]SentinelCheck, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *SentinelCheckPage) SetItems(v []SentinelCheck)`

SetItems sets Items field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
