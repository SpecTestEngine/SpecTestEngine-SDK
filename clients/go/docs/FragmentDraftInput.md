# FragmentDraftInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** |  | [optional]
**Type** | [**FragmentType**](FragmentType.md) |  |
**Content** | **map[string]interface{}** |  |

## Methods

### NewFragmentDraftInput

`func NewFragmentDraftInput(type_ FragmentType, content map[string]interface{}, ) *FragmentDraftInput`

NewFragmentDraftInput instantiates a new FragmentDraftInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFragmentDraftInputWithDefaults

`func NewFragmentDraftInputWithDefaults() *FragmentDraftInput`

NewFragmentDraftInputWithDefaults instantiates a new FragmentDraftInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *FragmentDraftInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *FragmentDraftInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *FragmentDraftInput) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *FragmentDraftInput) HasName() bool`

HasName returns a boolean if a field has been set.

### GetType

`func (o *FragmentDraftInput) GetType() FragmentType`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *FragmentDraftInput) GetTypeOk() (*FragmentType, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *FragmentDraftInput) SetType(v FragmentType)`

SetType sets Type field to given value.


### GetContent

`func (o *FragmentDraftInput) GetContent() map[string]interface{}`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *FragmentDraftInput) GetContentOk() (*map[string]interface{}, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *FragmentDraftInput) SetContent(v map[string]interface{})`

SetContent sets Content field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
