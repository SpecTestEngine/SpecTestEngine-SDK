# FragmentCatalogType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | [**FragmentType**](FragmentType.md) |  |
**AllowedFields** | **[]string** |  |
**Singleton** | **bool** |  |
**EditorMode** | **string** |  |
**CompatibleStreamingTransports** | Pointer to [**[]StreamingTransport**](StreamingTransport.md) |  | [optional]
**StarterTemplate** | **map[string]interface{}** |  |

## Methods

### NewFragmentCatalogType

`func NewFragmentCatalogType(type_ FragmentType, allowedFields []string, singleton bool, editorMode string, starterTemplate map[string]interface{}, ) *FragmentCatalogType`

NewFragmentCatalogType instantiates a new FragmentCatalogType object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFragmentCatalogTypeWithDefaults

`func NewFragmentCatalogTypeWithDefaults() *FragmentCatalogType`

NewFragmentCatalogTypeWithDefaults instantiates a new FragmentCatalogType object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *FragmentCatalogType) GetType() FragmentType`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *FragmentCatalogType) GetTypeOk() (*FragmentType, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *FragmentCatalogType) SetType(v FragmentType)`

SetType sets Type field to given value.


### GetAllowedFields

`func (o *FragmentCatalogType) GetAllowedFields() []string`

GetAllowedFields returns the AllowedFields field if non-nil, zero value otherwise.

### GetAllowedFieldsOk

`func (o *FragmentCatalogType) GetAllowedFieldsOk() (*[]string, bool)`

GetAllowedFieldsOk returns a tuple with the AllowedFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowedFields

`func (o *FragmentCatalogType) SetAllowedFields(v []string)`

SetAllowedFields sets AllowedFields field to given value.


### GetSingleton

`func (o *FragmentCatalogType) GetSingleton() bool`

GetSingleton returns the Singleton field if non-nil, zero value otherwise.

### GetSingletonOk

`func (o *FragmentCatalogType) GetSingletonOk() (*bool, bool)`

GetSingletonOk returns a tuple with the Singleton field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSingleton

`func (o *FragmentCatalogType) SetSingleton(v bool)`

SetSingleton sets Singleton field to given value.


### GetEditorMode

`func (o *FragmentCatalogType) GetEditorMode() string`

GetEditorMode returns the EditorMode field if non-nil, zero value otherwise.

### GetEditorModeOk

`func (o *FragmentCatalogType) GetEditorModeOk() (*string, bool)`

GetEditorModeOk returns a tuple with the EditorMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEditorMode

`func (o *FragmentCatalogType) SetEditorMode(v string)`

SetEditorMode sets EditorMode field to given value.


### GetCompatibleStreamingTransports

`func (o *FragmentCatalogType) GetCompatibleStreamingTransports() []StreamingTransport`

GetCompatibleStreamingTransports returns the CompatibleStreamingTransports field if non-nil, zero value otherwise.

### GetCompatibleStreamingTransportsOk

`func (o *FragmentCatalogType) GetCompatibleStreamingTransportsOk() (*[]StreamingTransport, bool)`

GetCompatibleStreamingTransportsOk returns a tuple with the CompatibleStreamingTransports field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompatibleStreamingTransports

`func (o *FragmentCatalogType) SetCompatibleStreamingTransports(v []StreamingTransport)`

SetCompatibleStreamingTransports sets CompatibleStreamingTransports field to given value.

### HasCompatibleStreamingTransports

`func (o *FragmentCatalogType) HasCompatibleStreamingTransports() bool`

HasCompatibleStreamingTransports returns a boolean if a field has been set.

### GetStarterTemplate

`func (o *FragmentCatalogType) GetStarterTemplate() map[string]interface{}`

GetStarterTemplate returns the StarterTemplate field if non-nil, zero value otherwise.

### GetStarterTemplateOk

`func (o *FragmentCatalogType) GetStarterTemplateOk() (*map[string]interface{}, bool)`

GetStarterTemplateOk returns a tuple with the StarterTemplate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStarterTemplate

`func (o *FragmentCatalogType) SetStarterTemplate(v map[string]interface{})`

SetStarterTemplate sets StarterTemplate field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


