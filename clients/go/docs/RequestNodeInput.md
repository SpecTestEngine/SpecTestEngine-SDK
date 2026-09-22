# RequestNodeInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Type** | **string** |  |
**ParentNodeId** | Pointer to **NullableString** | A UUIDv7 identifier. Treat identifiers as opaque values. | [optional]
**OrderIndex** | Pointer to **int32** |  | [optional]
**Request** | Pointer to [**SavedRequestInput**](SavedRequestInput.md) |  | [optional]

## Methods

### NewRequestNodeInput

`func NewRequestNodeInput(name string, type_ string, ) *RequestNodeInput`

NewRequestNodeInput instantiates a new RequestNodeInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRequestNodeInputWithDefaults

`func NewRequestNodeInputWithDefaults() *RequestNodeInput`

NewRequestNodeInputWithDefaults instantiates a new RequestNodeInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *RequestNodeInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RequestNodeInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *RequestNodeInput) SetName(v string)`

SetName sets Name field to given value.


### GetType

`func (o *RequestNodeInput) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *RequestNodeInput) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *RequestNodeInput) SetType(v string)`

SetType sets Type field to given value.


### GetParentNodeId

`func (o *RequestNodeInput) GetParentNodeId() string`

GetParentNodeId returns the ParentNodeId field if non-nil, zero value otherwise.

### GetParentNodeIdOk

`func (o *RequestNodeInput) GetParentNodeIdOk() (*string, bool)`

GetParentNodeIdOk returns a tuple with the ParentNodeId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentNodeId

`func (o *RequestNodeInput) SetParentNodeId(v string)`

SetParentNodeId sets ParentNodeId field to given value.

### HasParentNodeId

`func (o *RequestNodeInput) HasParentNodeId() bool`

HasParentNodeId returns a boolean if a field has been set.

### SetParentNodeIdNil

`func (o *RequestNodeInput) SetParentNodeIdNil(b bool)`

 SetParentNodeIdNil sets the value for ParentNodeId to be an explicit nil

### UnsetParentNodeId
`func (o *RequestNodeInput) UnsetParentNodeId()`

UnsetParentNodeId ensures that no value is present for ParentNodeId, not even an explicit nil
### GetOrderIndex

`func (o *RequestNodeInput) GetOrderIndex() int32`

GetOrderIndex returns the OrderIndex field if non-nil, zero value otherwise.

### GetOrderIndexOk

`func (o *RequestNodeInput) GetOrderIndexOk() (*int32, bool)`

GetOrderIndexOk returns a tuple with the OrderIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrderIndex

`func (o *RequestNodeInput) SetOrderIndex(v int32)`

SetOrderIndex sets OrderIndex field to given value.

### HasOrderIndex

`func (o *RequestNodeInput) HasOrderIndex() bool`

HasOrderIndex returns a boolean if a field has been set.

### GetRequest

`func (o *RequestNodeInput) GetRequest() SavedRequestInput`

GetRequest returns the Request field if non-nil, zero value otherwise.

### GetRequestOk

`func (o *RequestNodeInput) GetRequestOk() (*SavedRequestInput, bool)`

GetRequestOk returns a tuple with the Request field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequest

`func (o *RequestNodeInput) SetRequest(v SavedRequestInput)`

SetRequest sets Request field to given value.

### HasRequest

`func (o *RequestNodeInput) HasRequest() bool`

HasRequest returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


