# BrowserAuthSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Source** | **string** |  |
**Path** | **string** |  |
**ScopeOrigin** | **string** | Exact HTTP(S) origin without credentials, path, query or fragment. |
**UpdateFrom** | Pointer to [**NullableBrowserAuthGuard**](BrowserAuthGuard.md) |  | [optional]

## Methods

### NewBrowserAuthSource

`func NewBrowserAuthSource(name string, source string, path string, scopeOrigin string, ) *BrowserAuthSource`

NewBrowserAuthSource instantiates a new BrowserAuthSource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserAuthSourceWithDefaults

`func NewBrowserAuthSourceWithDefaults() *BrowserAuthSource`

NewBrowserAuthSourceWithDefaults instantiates a new BrowserAuthSource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *BrowserAuthSource) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *BrowserAuthSource) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *BrowserAuthSource) SetName(v string)`

SetName sets Name field to given value.


### GetSource

`func (o *BrowserAuthSource) GetSource() string`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *BrowserAuthSource) GetSourceOk() (*string, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *BrowserAuthSource) SetSource(v string)`

SetSource sets Source field to given value.


### GetPath

`func (o *BrowserAuthSource) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *BrowserAuthSource) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *BrowserAuthSource) SetPath(v string)`

SetPath sets Path field to given value.


### GetScopeOrigin

`func (o *BrowserAuthSource) GetScopeOrigin() string`

GetScopeOrigin returns the ScopeOrigin field if non-nil, zero value otherwise.

### GetScopeOriginOk

`func (o *BrowserAuthSource) GetScopeOriginOk() (*string, bool)`

GetScopeOriginOk returns a tuple with the ScopeOrigin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopeOrigin

`func (o *BrowserAuthSource) SetScopeOrigin(v string)`

SetScopeOrigin sets ScopeOrigin field to given value.


### GetUpdateFrom

`func (o *BrowserAuthSource) GetUpdateFrom() BrowserAuthGuard`

GetUpdateFrom returns the UpdateFrom field if non-nil, zero value otherwise.

### GetUpdateFromOk

`func (o *BrowserAuthSource) GetUpdateFromOk() (*BrowserAuthGuard, bool)`

GetUpdateFromOk returns a tuple with the UpdateFrom field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateFrom

`func (o *BrowserAuthSource) SetUpdateFrom(v BrowserAuthGuard)`

SetUpdateFrom sets UpdateFrom field to given value.

### HasUpdateFrom

`func (o *BrowserAuthSource) HasUpdateFrom() bool`

HasUpdateFrom returns a boolean if a field has been set.

### SetUpdateFromNil

`func (o *BrowserAuthSource) SetUpdateFromNil(b bool)`

 SetUpdateFromNil sets the value for UpdateFrom to be an explicit nil

### UnsetUpdateFrom
`func (o *BrowserAuthSource) UnsetUpdateFrom()`

UnsetUpdateFrom ensures that no value is present for UpdateFrom, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
