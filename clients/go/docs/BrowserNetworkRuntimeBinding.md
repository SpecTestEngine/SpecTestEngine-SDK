# BrowserNetworkRuntimeBinding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Source** | **string** |  |
**Path** | **string** |  |
**ScopeOrigin** | Pointer to **string** | Optional explicit HTTP(S) origin for later matching calls; no credentials, path, query or fragment. Defaults to the source call origin. | [optional]

## Methods

### NewBrowserNetworkRuntimeBinding

`func NewBrowserNetworkRuntimeBinding(name string, source string, path string, ) *BrowserNetworkRuntimeBinding`

NewBrowserNetworkRuntimeBinding instantiates a new BrowserNetworkRuntimeBinding object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserNetworkRuntimeBindingWithDefaults

`func NewBrowserNetworkRuntimeBindingWithDefaults() *BrowserNetworkRuntimeBinding`

NewBrowserNetworkRuntimeBindingWithDefaults instantiates a new BrowserNetworkRuntimeBinding object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *BrowserNetworkRuntimeBinding) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *BrowserNetworkRuntimeBinding) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *BrowserNetworkRuntimeBinding) SetName(v string)`

SetName sets Name field to given value.


### GetSource

`func (o *BrowserNetworkRuntimeBinding) GetSource() string`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *BrowserNetworkRuntimeBinding) GetSourceOk() (*string, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *BrowserNetworkRuntimeBinding) SetSource(v string)`

SetSource sets Source field to given value.


### GetPath

`func (o *BrowserNetworkRuntimeBinding) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *BrowserNetworkRuntimeBinding) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *BrowserNetworkRuntimeBinding) SetPath(v string)`

SetPath sets Path field to given value.


### GetScopeOrigin

`func (o *BrowserNetworkRuntimeBinding) GetScopeOrigin() string`

GetScopeOrigin returns the ScopeOrigin field if non-nil, zero value otherwise.

### GetScopeOriginOk

`func (o *BrowserNetworkRuntimeBinding) GetScopeOriginOk() (*string, bool)`

GetScopeOriginOk returns a tuple with the ScopeOrigin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopeOrigin

`func (o *BrowserNetworkRuntimeBinding) SetScopeOrigin(v string)`

SetScopeOrigin sets ScopeOrigin field to given value.

### HasScopeOrigin

`func (o *BrowserNetworkRuntimeBinding) HasScopeOrigin() bool`

HasScopeOrigin returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
