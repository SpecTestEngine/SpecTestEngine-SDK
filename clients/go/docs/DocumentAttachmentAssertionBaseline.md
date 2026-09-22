# DocumentAttachmentAssertionBaseline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  |
**ExpectedAttachmentHash** | **string** |  |
**VisualAssertion** | Pointer to [**NullableDocumentVisualAssertion**](DocumentVisualAssertion.md) |  | [optional]

## Methods

### NewDocumentAttachmentAssertionBaseline

`func NewDocumentAttachmentAssertionBaseline(id string, expectedAttachmentHash string, ) *DocumentAttachmentAssertionBaseline`

NewDocumentAttachmentAssertionBaseline instantiates a new DocumentAttachmentAssertionBaseline object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDocumentAttachmentAssertionBaselineWithDefaults

`func NewDocumentAttachmentAssertionBaselineWithDefaults() *DocumentAttachmentAssertionBaseline`

NewDocumentAttachmentAssertionBaselineWithDefaults instantiates a new DocumentAttachmentAssertionBaseline object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *DocumentAttachmentAssertionBaseline) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DocumentAttachmentAssertionBaseline) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DocumentAttachmentAssertionBaseline) SetId(v string)`

SetId sets Id field to given value.


### GetExpectedAttachmentHash

`func (o *DocumentAttachmentAssertionBaseline) GetExpectedAttachmentHash() string`

GetExpectedAttachmentHash returns the ExpectedAttachmentHash field if non-nil, zero value otherwise.

### GetExpectedAttachmentHashOk

`func (o *DocumentAttachmentAssertionBaseline) GetExpectedAttachmentHashOk() (*string, bool)`

GetExpectedAttachmentHashOk returns a tuple with the ExpectedAttachmentHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedAttachmentHash

`func (o *DocumentAttachmentAssertionBaseline) SetExpectedAttachmentHash(v string)`

SetExpectedAttachmentHash sets ExpectedAttachmentHash field to given value.


### GetVisualAssertion

`func (o *DocumentAttachmentAssertionBaseline) GetVisualAssertion() DocumentVisualAssertion`

GetVisualAssertion returns the VisualAssertion field if non-nil, zero value otherwise.

### GetVisualAssertionOk

`func (o *DocumentAttachmentAssertionBaseline) GetVisualAssertionOk() (*DocumentVisualAssertion, bool)`

GetVisualAssertionOk returns a tuple with the VisualAssertion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVisualAssertion

`func (o *DocumentAttachmentAssertionBaseline) SetVisualAssertion(v DocumentVisualAssertion)`

SetVisualAssertion sets VisualAssertion field to given value.

### HasVisualAssertion

`func (o *DocumentAttachmentAssertionBaseline) HasVisualAssertion() bool`

HasVisualAssertion returns a boolean if a field has been set.

### SetVisualAssertionNil

`func (o *DocumentAttachmentAssertionBaseline) SetVisualAssertionNil(b bool)`

 SetVisualAssertionNil sets the value for VisualAssertion to be an explicit nil

### UnsetVisualAssertion
`func (o *DocumentAttachmentAssertionBaseline) UnsetVisualAssertion()`

UnsetVisualAssertion ensures that no value is present for VisualAssertion, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


