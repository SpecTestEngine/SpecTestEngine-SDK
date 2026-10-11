# RequestWorkspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**Variables** | Pointer to **map[string]string** |  | [optional]
**GlobalVariableFallbacks** | Pointer to **map[string]string** |  | [optional]
**Id** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Nodes** | [**[]RequestNode**](RequestNode.md) |  |
**CreatedAt** | **time.Time** |  |
**UpdatedAt** | **time.Time** |  |

## Methods

### NewRequestWorkspace

`func NewRequestWorkspace(name string, id string, nodes []RequestNode, createdAt time.Time, updatedAt time.Time, ) *RequestWorkspace`

NewRequestWorkspace instantiates a new RequestWorkspace object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRequestWorkspaceWithDefaults

`func NewRequestWorkspaceWithDefaults() *RequestWorkspace`

NewRequestWorkspaceWithDefaults instantiates a new RequestWorkspace object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *RequestWorkspace) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RequestWorkspace) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *RequestWorkspace) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *RequestWorkspace) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *RequestWorkspace) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *RequestWorkspace) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *RequestWorkspace) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *RequestWorkspace) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *RequestWorkspace) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetVariables

`func (o *RequestWorkspace) GetVariables() map[string]string`

GetVariables returns the Variables field if non-nil, zero value otherwise.

### GetVariablesOk

`func (o *RequestWorkspace) GetVariablesOk() (*map[string]string, bool)`

GetVariablesOk returns a tuple with the Variables field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariables

`func (o *RequestWorkspace) SetVariables(v map[string]string)`

SetVariables sets Variables field to given value.

### HasVariables

`func (o *RequestWorkspace) HasVariables() bool`

HasVariables returns a boolean if a field has been set.

### GetGlobalVariableFallbacks

`func (o *RequestWorkspace) GetGlobalVariableFallbacks() map[string]string`

GetGlobalVariableFallbacks returns the GlobalVariableFallbacks field if non-nil, zero value otherwise.

### GetGlobalVariableFallbacksOk

`func (o *RequestWorkspace) GetGlobalVariableFallbacksOk() (*map[string]string, bool)`

GetGlobalVariableFallbacksOk returns a tuple with the GlobalVariableFallbacks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGlobalVariableFallbacks

`func (o *RequestWorkspace) SetGlobalVariableFallbacks(v map[string]string)`

SetGlobalVariableFallbacks sets GlobalVariableFallbacks field to given value.

### HasGlobalVariableFallbacks

`func (o *RequestWorkspace) HasGlobalVariableFallbacks() bool`

HasGlobalVariableFallbacks returns a boolean if a field has been set.

### GetId

`func (o *RequestWorkspace) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *RequestWorkspace) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *RequestWorkspace) SetId(v string)`

SetId sets Id field to given value.


### GetNodes

`func (o *RequestWorkspace) GetNodes() []RequestNode`

GetNodes returns the Nodes field if non-nil, zero value otherwise.

### GetNodesOk

`func (o *RequestWorkspace) GetNodesOk() (*[]RequestNode, bool)`

GetNodesOk returns a tuple with the Nodes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNodes

`func (o *RequestWorkspace) SetNodes(v []RequestNode)`

SetNodes sets Nodes field to given value.


### GetCreatedAt

`func (o *RequestWorkspace) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *RequestWorkspace) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *RequestWorkspace) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *RequestWorkspace) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *RequestWorkspace) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *RequestWorkspace) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
