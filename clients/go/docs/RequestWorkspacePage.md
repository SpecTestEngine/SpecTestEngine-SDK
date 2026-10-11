# RequestWorkspacePage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Page** | **int32** |  |
**Size** | **int32** |  |
**TotalElements** | **int64** |  |
**TotalPages** | **int32** |  |
**First** | **bool** |  |
**Last** | **bool** |  |
**Items** | [**[]RequestWorkspace**](RequestWorkspace.md) |  |

## Methods

### NewRequestWorkspacePage

`func NewRequestWorkspacePage(page int32, size int32, totalElements int64, totalPages int32, first bool, last bool, items []RequestWorkspace, ) *RequestWorkspacePage`

NewRequestWorkspacePage instantiates a new RequestWorkspacePage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRequestWorkspacePageWithDefaults

`func NewRequestWorkspacePageWithDefaults() *RequestWorkspacePage`

NewRequestWorkspacePageWithDefaults instantiates a new RequestWorkspacePage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPage

`func (o *RequestWorkspacePage) GetPage() int32`

GetPage returns the Page field if non-nil, zero value otherwise.

### GetPageOk

`func (o *RequestWorkspacePage) GetPageOk() (*int32, bool)`

GetPageOk returns a tuple with the Page field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPage

`func (o *RequestWorkspacePage) SetPage(v int32)`

SetPage sets Page field to given value.


### GetSize

`func (o *RequestWorkspacePage) GetSize() int32`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *RequestWorkspacePage) GetSizeOk() (*int32, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *RequestWorkspacePage) SetSize(v int32)`

SetSize sets Size field to given value.


### GetTotalElements

`func (o *RequestWorkspacePage) GetTotalElements() int64`

GetTotalElements returns the TotalElements field if non-nil, zero value otherwise.

### GetTotalElementsOk

`func (o *RequestWorkspacePage) GetTotalElementsOk() (*int64, bool)`

GetTotalElementsOk returns a tuple with the TotalElements field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalElements

`func (o *RequestWorkspacePage) SetTotalElements(v int64)`

SetTotalElements sets TotalElements field to given value.


### GetTotalPages

`func (o *RequestWorkspacePage) GetTotalPages() int32`

GetTotalPages returns the TotalPages field if non-nil, zero value otherwise.

### GetTotalPagesOk

`func (o *RequestWorkspacePage) GetTotalPagesOk() (*int32, bool)`

GetTotalPagesOk returns a tuple with the TotalPages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalPages

`func (o *RequestWorkspacePage) SetTotalPages(v int32)`

SetTotalPages sets TotalPages field to given value.


### GetFirst

`func (o *RequestWorkspacePage) GetFirst() bool`

GetFirst returns the First field if non-nil, zero value otherwise.

### GetFirstOk

`func (o *RequestWorkspacePage) GetFirstOk() (*bool, bool)`

GetFirstOk returns a tuple with the First field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirst

`func (o *RequestWorkspacePage) SetFirst(v bool)`

SetFirst sets First field to given value.


### GetLast

`func (o *RequestWorkspacePage) GetLast() bool`

GetLast returns the Last field if non-nil, zero value otherwise.

### GetLastOk

`func (o *RequestWorkspacePage) GetLastOk() (*bool, bool)`

GetLastOk returns a tuple with the Last field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLast

`func (o *RequestWorkspacePage) SetLast(v bool)`

SetLast sets Last field to given value.


### GetItems

`func (o *RequestWorkspacePage) GetItems() []RequestWorkspace`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *RequestWorkspacePage) GetItemsOk() (*[]RequestWorkspace, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *RequestWorkspacePage) SetItems(v []RequestWorkspace)`

SetItems sets Items field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
