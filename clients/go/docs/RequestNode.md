# RequestNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Type** | **string** |  |
**ParentNodeId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**OrderIndex** | Pointer to **int32** |  | [optional]
**Request** | Pointer to [**SavedRequestInput**](SavedRequestInput.md) |  | [optional]
**Id** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**CreatedAt** | **time.Time** |  |
**UpdatedAt** | **time.Time** |  |

## Methods

### NewRequestNode

`func NewRequestNode(name string, type_ string, id string, createdAt time.Time, updatedAt time.Time, ) *RequestNode`

NewRequestNode instantiates a new RequestNode object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRequestNodeWithDefaults

`func NewRequestNodeWithDefaults() *RequestNode`

NewRequestNodeWithDefaults instantiates a new RequestNode object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *RequestNode) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RequestNode) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *RequestNode) SetName(v string)`

SetName sets Name field to given value.


### GetType

`func (o *RequestNode) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *RequestNode) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *RequestNode) SetType(v string)`

SetType sets Type field to given value.


### GetParentNodeId

`func (o *RequestNode) GetParentNodeId() string`

GetParentNodeId returns the ParentNodeId field if non-nil, zero value otherwise.

### GetParentNodeIdOk

`func (o *RequestNode) GetParentNodeIdOk() (*string, bool)`

GetParentNodeIdOk returns a tuple with the ParentNodeId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentNodeId

`func (o *RequestNode) SetParentNodeId(v string)`

SetParentNodeId sets ParentNodeId field to given value.

### HasParentNodeId

`func (o *RequestNode) HasParentNodeId() bool`

HasParentNodeId returns a boolean if a field has been set.

### SetParentNodeIdNil

`func (o *RequestNode) SetParentNodeIdNil(b bool)`

 SetParentNodeIdNil sets the value for ParentNodeId to be an explicit nil

### UnsetParentNodeId
`func (o *RequestNode) UnsetParentNodeId()`

UnsetParentNodeId ensures that no value is present for ParentNodeId, not even an explicit nil
### GetOrderIndex

`func (o *RequestNode) GetOrderIndex() int32`

GetOrderIndex returns the OrderIndex field if non-nil, zero value otherwise.

### GetOrderIndexOk

`func (o *RequestNode) GetOrderIndexOk() (*int32, bool)`

GetOrderIndexOk returns a tuple with the OrderIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrderIndex

`func (o *RequestNode) SetOrderIndex(v int32)`

SetOrderIndex sets OrderIndex field to given value.

### HasOrderIndex

`func (o *RequestNode) HasOrderIndex() bool`

HasOrderIndex returns a boolean if a field has been set.

### GetRequest

`func (o *RequestNode) GetRequest() SavedRequestInput`

GetRequest returns the Request field if non-nil, zero value otherwise.

### GetRequestOk

`func (o *RequestNode) GetRequestOk() (*SavedRequestInput, bool)`

GetRequestOk returns a tuple with the Request field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequest

`func (o *RequestNode) SetRequest(v SavedRequestInput)`

SetRequest sets Request field to given value.

### HasRequest

`func (o *RequestNode) HasRequest() bool`

HasRequest returns a boolean if a field has been set.

### GetId

`func (o *RequestNode) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *RequestNode) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *RequestNode) SetId(v string)`

SetId sets Id field to given value.


### GetCreatedAt

`func (o *RequestNode) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *RequestNode) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *RequestNode) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *RequestNode) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *RequestNode) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *RequestNode) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
