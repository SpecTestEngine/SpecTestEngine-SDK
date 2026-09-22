# SpecificationRunPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Page** | **int32** |  |
**Size** | **int32** |  |
**TotalElements** | **int64** |  |
**TotalPages** | **int32** |  |
**First** | **bool** |  |
**Last** | **bool** |  |
**Items** | [**[]SpecificationRunSummary**](SpecificationRunSummary.md) |  |

## Methods

### NewSpecificationRunPage

`func NewSpecificationRunPage(page int32, size int32, totalElements int64, totalPages int32, first bool, last bool, items []SpecificationRunSummary, ) *SpecificationRunPage`

NewSpecificationRunPage instantiates a new SpecificationRunPage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSpecificationRunPageWithDefaults

`func NewSpecificationRunPageWithDefaults() *SpecificationRunPage`

NewSpecificationRunPageWithDefaults instantiates a new SpecificationRunPage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPage

`func (o *SpecificationRunPage) GetPage() int32`

GetPage returns the Page field if non-nil, zero value otherwise.

### GetPageOk

`func (o *SpecificationRunPage) GetPageOk() (*int32, bool)`

GetPageOk returns a tuple with the Page field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPage

`func (o *SpecificationRunPage) SetPage(v int32)`

SetPage sets Page field to given value.


### GetSize

`func (o *SpecificationRunPage) GetSize() int32`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *SpecificationRunPage) GetSizeOk() (*int32, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *SpecificationRunPage) SetSize(v int32)`

SetSize sets Size field to given value.


### GetTotalElements

`func (o *SpecificationRunPage) GetTotalElements() int64`

GetTotalElements returns the TotalElements field if non-nil, zero value otherwise.

### GetTotalElementsOk

`func (o *SpecificationRunPage) GetTotalElementsOk() (*int64, bool)`

GetTotalElementsOk returns a tuple with the TotalElements field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalElements

`func (o *SpecificationRunPage) SetTotalElements(v int64)`

SetTotalElements sets TotalElements field to given value.


### GetTotalPages

`func (o *SpecificationRunPage) GetTotalPages() int32`

GetTotalPages returns the TotalPages field if non-nil, zero value otherwise.

### GetTotalPagesOk

`func (o *SpecificationRunPage) GetTotalPagesOk() (*int32, bool)`

GetTotalPagesOk returns a tuple with the TotalPages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalPages

`func (o *SpecificationRunPage) SetTotalPages(v int32)`

SetTotalPages sets TotalPages field to given value.


### GetFirst

`func (o *SpecificationRunPage) GetFirst() bool`

GetFirst returns the First field if non-nil, zero value otherwise.

### GetFirstOk

`func (o *SpecificationRunPage) GetFirstOk() (*bool, bool)`

GetFirstOk returns a tuple with the First field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirst

`func (o *SpecificationRunPage) SetFirst(v bool)`

SetFirst sets First field to given value.


### GetLast

`func (o *SpecificationRunPage) GetLast() bool`

GetLast returns the Last field if non-nil, zero value otherwise.

### GetLastOk

`func (o *SpecificationRunPage) GetLastOk() (*bool, bool)`

GetLastOk returns a tuple with the Last field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLast

`func (o *SpecificationRunPage) SetLast(v bool)`

SetLast sets Last field to given value.


### GetItems

`func (o *SpecificationRunPage) GetItems() []SpecificationRunSummary`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *SpecificationRunPage) GetItemsOk() (*[]SpecificationRunSummary, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *SpecificationRunPage) SetItems(v []SpecificationRunSummary)`

SetItems sets Items field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


