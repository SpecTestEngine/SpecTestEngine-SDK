# DocumentAssetReference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssetId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**FileName** | **string** |  |
**ContentType** | **string** |  |
**SizeBytes** | **int64** |  |
**Sha256** | **string** |  |
**ObjectKey** | **string** |  |
**FieldName** | **string** |  |
**ContentId** | Pointer to **NullableString** |  | [optional]

## Methods

### NewDocumentAssetReference

`func NewDocumentAssetReference(assetId string, fileName string, contentType string, sizeBytes int64, sha256 string, objectKey string, fieldName string, ) *DocumentAssetReference`

NewDocumentAssetReference instantiates a new DocumentAssetReference object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDocumentAssetReferenceWithDefaults

`func NewDocumentAssetReferenceWithDefaults() *DocumentAssetReference`

NewDocumentAssetReferenceWithDefaults instantiates a new DocumentAssetReference object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssetId

`func (o *DocumentAssetReference) GetAssetId() string`

GetAssetId returns the AssetId field if non-nil, zero value otherwise.

### GetAssetIdOk

`func (o *DocumentAssetReference) GetAssetIdOk() (*string, bool)`

GetAssetIdOk returns a tuple with the AssetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssetId

`func (o *DocumentAssetReference) SetAssetId(v string)`

SetAssetId sets AssetId field to given value.


### GetFileName

`func (o *DocumentAssetReference) GetFileName() string`

GetFileName returns the FileName field if non-nil, zero value otherwise.

### GetFileNameOk

`func (o *DocumentAssetReference) GetFileNameOk() (*string, bool)`

GetFileNameOk returns a tuple with the FileName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFileName

`func (o *DocumentAssetReference) SetFileName(v string)`

SetFileName sets FileName field to given value.


### GetContentType

`func (o *DocumentAssetReference) GetContentType() string`

GetContentType returns the ContentType field if non-nil, zero value otherwise.

### GetContentTypeOk

`func (o *DocumentAssetReference) GetContentTypeOk() (*string, bool)`

GetContentTypeOk returns a tuple with the ContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentType

`func (o *DocumentAssetReference) SetContentType(v string)`

SetContentType sets ContentType field to given value.


### GetSizeBytes

`func (o *DocumentAssetReference) GetSizeBytes() int64`

GetSizeBytes returns the SizeBytes field if non-nil, zero value otherwise.

### GetSizeBytesOk

`func (o *DocumentAssetReference) GetSizeBytesOk() (*int64, bool)`

GetSizeBytesOk returns a tuple with the SizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSizeBytes

`func (o *DocumentAssetReference) SetSizeBytes(v int64)`

SetSizeBytes sets SizeBytes field to given value.


### GetSha256

`func (o *DocumentAssetReference) GetSha256() string`

GetSha256 returns the Sha256 field if non-nil, zero value otherwise.

### GetSha256Ok

`func (o *DocumentAssetReference) GetSha256Ok() (*string, bool)`

GetSha256Ok returns a tuple with the Sha256 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSha256

`func (o *DocumentAssetReference) SetSha256(v string)`

SetSha256 sets Sha256 field to given value.


### GetObjectKey

`func (o *DocumentAssetReference) GetObjectKey() string`

GetObjectKey returns the ObjectKey field if non-nil, zero value otherwise.

### GetObjectKeyOk

`func (o *DocumentAssetReference) GetObjectKeyOk() (*string, bool)`

GetObjectKeyOk returns a tuple with the ObjectKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectKey

`func (o *DocumentAssetReference) SetObjectKey(v string)`

SetObjectKey sets ObjectKey field to given value.


### GetFieldName

`func (o *DocumentAssetReference) GetFieldName() string`

GetFieldName returns the FieldName field if non-nil, zero value otherwise.

### GetFieldNameOk

`func (o *DocumentAssetReference) GetFieldNameOk() (*string, bool)`

GetFieldNameOk returns a tuple with the FieldName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFieldName

`func (o *DocumentAssetReference) SetFieldName(v string)`

SetFieldName sets FieldName field to given value.


### GetContentId

`func (o *DocumentAssetReference) GetContentId() string`

GetContentId returns the ContentId field if non-nil, zero value otherwise.

### GetContentIdOk

`func (o *DocumentAssetReference) GetContentIdOk() (*string, bool)`

GetContentIdOk returns a tuple with the ContentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentId

`func (o *DocumentAssetReference) SetContentId(v string)`

SetContentId sets ContentId field to given value.

### HasContentId

`func (o *DocumentAssetReference) HasContentId() bool`

HasContentId returns a boolean if a field has been set.

### SetContentIdNil

`func (o *DocumentAssetReference) SetContentIdNil(b bool)`

 SetContentIdNil sets the value for ContentId to be an explicit nil

### UnsetContentId
`func (o *DocumentAssetReference) UnsetContentId()`

UnsetContentId ensures that no value is present for ContentId, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


