# DocumentVisualDiffPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PageNumber** | **int32** |  |
**ActualArtifactId** | Pointer to **string** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**ExpectedArtifactId** | Pointer to **string** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**DiffArtifactId** | Pointer to **string** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**Width** | **int32** |  |
**Height** | **int32** |  |

## Methods

### NewDocumentVisualDiffPage

`func NewDocumentVisualDiffPage(pageNumber int32, width int32, height int32, ) *DocumentVisualDiffPage`

NewDocumentVisualDiffPage instantiates a new DocumentVisualDiffPage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDocumentVisualDiffPageWithDefaults

`func NewDocumentVisualDiffPageWithDefaults() *DocumentVisualDiffPage`

NewDocumentVisualDiffPageWithDefaults instantiates a new DocumentVisualDiffPage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPageNumber

`func (o *DocumentVisualDiffPage) GetPageNumber() int32`

GetPageNumber returns the PageNumber field if non-nil, zero value otherwise.

### GetPageNumberOk

`func (o *DocumentVisualDiffPage) GetPageNumberOk() (*int32, bool)`

GetPageNumberOk returns a tuple with the PageNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPageNumber

`func (o *DocumentVisualDiffPage) SetPageNumber(v int32)`

SetPageNumber sets PageNumber field to given value.


### GetActualArtifactId

`func (o *DocumentVisualDiffPage) GetActualArtifactId() string`

GetActualArtifactId returns the ActualArtifactId field if non-nil, zero value otherwise.

### GetActualArtifactIdOk

`func (o *DocumentVisualDiffPage) GetActualArtifactIdOk() (*string, bool)`

GetActualArtifactIdOk returns a tuple with the ActualArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActualArtifactId

`func (o *DocumentVisualDiffPage) SetActualArtifactId(v string)`

SetActualArtifactId sets ActualArtifactId field to given value.

### HasActualArtifactId

`func (o *DocumentVisualDiffPage) HasActualArtifactId() bool`

HasActualArtifactId returns a boolean if a field has been set.

### GetExpectedArtifactId

`func (o *DocumentVisualDiffPage) GetExpectedArtifactId() string`

GetExpectedArtifactId returns the ExpectedArtifactId field if non-nil, zero value otherwise.

### GetExpectedArtifactIdOk

`func (o *DocumentVisualDiffPage) GetExpectedArtifactIdOk() (*string, bool)`

GetExpectedArtifactIdOk returns a tuple with the ExpectedArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedArtifactId

`func (o *DocumentVisualDiffPage) SetExpectedArtifactId(v string)`

SetExpectedArtifactId sets ExpectedArtifactId field to given value.

### HasExpectedArtifactId

`func (o *DocumentVisualDiffPage) HasExpectedArtifactId() bool`

HasExpectedArtifactId returns a boolean if a field has been set.

### GetDiffArtifactId

`func (o *DocumentVisualDiffPage) GetDiffArtifactId() string`

GetDiffArtifactId returns the DiffArtifactId field if non-nil, zero value otherwise.

### GetDiffArtifactIdOk

`func (o *DocumentVisualDiffPage) GetDiffArtifactIdOk() (*string, bool)`

GetDiffArtifactIdOk returns a tuple with the DiffArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiffArtifactId

`func (o *DocumentVisualDiffPage) SetDiffArtifactId(v string)`

SetDiffArtifactId sets DiffArtifactId field to given value.

### HasDiffArtifactId

`func (o *DocumentVisualDiffPage) HasDiffArtifactId() bool`

HasDiffArtifactId returns a boolean if a field has been set.

### GetWidth

`func (o *DocumentVisualDiffPage) GetWidth() int32`

GetWidth returns the Width field if non-nil, zero value otherwise.

### GetWidthOk

`func (o *DocumentVisualDiffPage) GetWidthOk() (*int32, bool)`

GetWidthOk returns a tuple with the Width field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWidth

`func (o *DocumentVisualDiffPage) SetWidth(v int32)`

SetWidth sets Width field to given value.


### GetHeight

`func (o *DocumentVisualDiffPage) GetHeight() int32`

GetHeight returns the Height field if non-nil, zero value otherwise.

### GetHeightOk

`func (o *DocumentVisualDiffPage) GetHeightOk() (*int32, bool)`

GetHeightOk returns a tuple with the Height field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeight

`func (o *DocumentVisualDiffPage) SetHeight(v int32)`

SetHeight sets Height field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


