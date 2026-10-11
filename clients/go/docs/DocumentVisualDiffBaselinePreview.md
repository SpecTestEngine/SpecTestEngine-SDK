# DocumentVisualDiffBaselinePreview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**VisualDiffId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**SourceType** | **string** |  |
**SourceRunId** | Pointer to **NullableString** |  | [optional]
**SourceStepId** | Pointer to **NullableString** |  | [optional]
**AttachmentId** | **string** |  |
**ExpectedAttachmentHash** | **string** |  |
**ExpectedAttachmentFingerprint** | Pointer to **NullableString** | Serialized deterministic fingerprint for a new specification revision. | [optional]
**Mode** | **string** |  |
**ProposedAssertion** | [**DocumentAttachmentAssertionBaseline**](DocumentAttachmentAssertionBaseline.md) |  |
**Confirmed** | **bool** |  |
**Status** | **string** |  |
**Message** | **string** |  |

## Methods

### NewDocumentVisualDiffBaselinePreview

`func NewDocumentVisualDiffBaselinePreview(visualDiffId string, sourceType string, attachmentId string, expectedAttachmentHash string, mode string, proposedAssertion DocumentAttachmentAssertionBaseline, confirmed bool, status string, message string, ) *DocumentVisualDiffBaselinePreview`

NewDocumentVisualDiffBaselinePreview instantiates a new DocumentVisualDiffBaselinePreview object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDocumentVisualDiffBaselinePreviewWithDefaults

`func NewDocumentVisualDiffBaselinePreviewWithDefaults() *DocumentVisualDiffBaselinePreview`

NewDocumentVisualDiffBaselinePreviewWithDefaults instantiates a new DocumentVisualDiffBaselinePreview object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetVisualDiffId

`func (o *DocumentVisualDiffBaselinePreview) GetVisualDiffId() string`

GetVisualDiffId returns the VisualDiffId field if non-nil, zero value otherwise.

### GetVisualDiffIdOk

`func (o *DocumentVisualDiffBaselinePreview) GetVisualDiffIdOk() (*string, bool)`

GetVisualDiffIdOk returns a tuple with the VisualDiffId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVisualDiffId

`func (o *DocumentVisualDiffBaselinePreview) SetVisualDiffId(v string)`

SetVisualDiffId sets VisualDiffId field to given value.


### GetSourceType

`func (o *DocumentVisualDiffBaselinePreview) GetSourceType() string`

GetSourceType returns the SourceType field if non-nil, zero value otherwise.

### GetSourceTypeOk

`func (o *DocumentVisualDiffBaselinePreview) GetSourceTypeOk() (*string, bool)`

GetSourceTypeOk returns a tuple with the SourceType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceType

`func (o *DocumentVisualDiffBaselinePreview) SetSourceType(v string)`

SetSourceType sets SourceType field to given value.


### GetSourceRunId

`func (o *DocumentVisualDiffBaselinePreview) GetSourceRunId() string`

GetSourceRunId returns the SourceRunId field if non-nil, zero value otherwise.

### GetSourceRunIdOk

`func (o *DocumentVisualDiffBaselinePreview) GetSourceRunIdOk() (*string, bool)`

GetSourceRunIdOk returns a tuple with the SourceRunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceRunId

`func (o *DocumentVisualDiffBaselinePreview) SetSourceRunId(v string)`

SetSourceRunId sets SourceRunId field to given value.

### HasSourceRunId

`func (o *DocumentVisualDiffBaselinePreview) HasSourceRunId() bool`

HasSourceRunId returns a boolean if a field has been set.

### SetSourceRunIdNil

`func (o *DocumentVisualDiffBaselinePreview) SetSourceRunIdNil(b bool)`

 SetSourceRunIdNil sets the value for SourceRunId to be an explicit nil

### UnsetSourceRunId
`func (o *DocumentVisualDiffBaselinePreview) UnsetSourceRunId()`

UnsetSourceRunId ensures that no value is present for SourceRunId, not even an explicit nil
### GetSourceStepId

`func (o *DocumentVisualDiffBaselinePreview) GetSourceStepId() string`

GetSourceStepId returns the SourceStepId field if non-nil, zero value otherwise.

### GetSourceStepIdOk

`func (o *DocumentVisualDiffBaselinePreview) GetSourceStepIdOk() (*string, bool)`

GetSourceStepIdOk returns a tuple with the SourceStepId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceStepId

`func (o *DocumentVisualDiffBaselinePreview) SetSourceStepId(v string)`

SetSourceStepId sets SourceStepId field to given value.

### HasSourceStepId

`func (o *DocumentVisualDiffBaselinePreview) HasSourceStepId() bool`

HasSourceStepId returns a boolean if a field has been set.

### SetSourceStepIdNil

`func (o *DocumentVisualDiffBaselinePreview) SetSourceStepIdNil(b bool)`

 SetSourceStepIdNil sets the value for SourceStepId to be an explicit nil

### UnsetSourceStepId
`func (o *DocumentVisualDiffBaselinePreview) UnsetSourceStepId()`

UnsetSourceStepId ensures that no value is present for SourceStepId, not even an explicit nil
### GetAttachmentId

`func (o *DocumentVisualDiffBaselinePreview) GetAttachmentId() string`

GetAttachmentId returns the AttachmentId field if non-nil, zero value otherwise.

### GetAttachmentIdOk

`func (o *DocumentVisualDiffBaselinePreview) GetAttachmentIdOk() (*string, bool)`

GetAttachmentIdOk returns a tuple with the AttachmentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttachmentId

`func (o *DocumentVisualDiffBaselinePreview) SetAttachmentId(v string)`

SetAttachmentId sets AttachmentId field to given value.


### GetExpectedAttachmentHash

`func (o *DocumentVisualDiffBaselinePreview) GetExpectedAttachmentHash() string`

GetExpectedAttachmentHash returns the ExpectedAttachmentHash field if non-nil, zero value otherwise.

### GetExpectedAttachmentHashOk

`func (o *DocumentVisualDiffBaselinePreview) GetExpectedAttachmentHashOk() (*string, bool)`

GetExpectedAttachmentHashOk returns a tuple with the ExpectedAttachmentHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedAttachmentHash

`func (o *DocumentVisualDiffBaselinePreview) SetExpectedAttachmentHash(v string)`

SetExpectedAttachmentHash sets ExpectedAttachmentHash field to given value.


### GetExpectedAttachmentFingerprint

`func (o *DocumentVisualDiffBaselinePreview) GetExpectedAttachmentFingerprint() string`

GetExpectedAttachmentFingerprint returns the ExpectedAttachmentFingerprint field if non-nil, zero value otherwise.

### GetExpectedAttachmentFingerprintOk

`func (o *DocumentVisualDiffBaselinePreview) GetExpectedAttachmentFingerprintOk() (*string, bool)`

GetExpectedAttachmentFingerprintOk returns a tuple with the ExpectedAttachmentFingerprint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedAttachmentFingerprint

`func (o *DocumentVisualDiffBaselinePreview) SetExpectedAttachmentFingerprint(v string)`

SetExpectedAttachmentFingerprint sets ExpectedAttachmentFingerprint field to given value.

### HasExpectedAttachmentFingerprint

`func (o *DocumentVisualDiffBaselinePreview) HasExpectedAttachmentFingerprint() bool`

HasExpectedAttachmentFingerprint returns a boolean if a field has been set.

### SetExpectedAttachmentFingerprintNil

`func (o *DocumentVisualDiffBaselinePreview) SetExpectedAttachmentFingerprintNil(b bool)`

 SetExpectedAttachmentFingerprintNil sets the value for ExpectedAttachmentFingerprint to be an explicit nil

### UnsetExpectedAttachmentFingerprint
`func (o *DocumentVisualDiffBaselinePreview) UnsetExpectedAttachmentFingerprint()`

UnsetExpectedAttachmentFingerprint ensures that no value is present for ExpectedAttachmentFingerprint, not even an explicit nil
### GetMode

`func (o *DocumentVisualDiffBaselinePreview) GetMode() string`

GetMode returns the Mode field if non-nil, zero value otherwise.

### GetModeOk

`func (o *DocumentVisualDiffBaselinePreview) GetModeOk() (*string, bool)`

GetModeOk returns a tuple with the Mode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMode

`func (o *DocumentVisualDiffBaselinePreview) SetMode(v string)`

SetMode sets Mode field to given value.


### GetProposedAssertion

`func (o *DocumentVisualDiffBaselinePreview) GetProposedAssertion() DocumentAttachmentAssertionBaseline`

GetProposedAssertion returns the ProposedAssertion field if non-nil, zero value otherwise.

### GetProposedAssertionOk

`func (o *DocumentVisualDiffBaselinePreview) GetProposedAssertionOk() (*DocumentAttachmentAssertionBaseline, bool)`

GetProposedAssertionOk returns a tuple with the ProposedAssertion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProposedAssertion

`func (o *DocumentVisualDiffBaselinePreview) SetProposedAssertion(v DocumentAttachmentAssertionBaseline)`

SetProposedAssertion sets ProposedAssertion field to given value.


### GetConfirmed

`func (o *DocumentVisualDiffBaselinePreview) GetConfirmed() bool`

GetConfirmed returns the Confirmed field if non-nil, zero value otherwise.

### GetConfirmedOk

`func (o *DocumentVisualDiffBaselinePreview) GetConfirmedOk() (*bool, bool)`

GetConfirmedOk returns a tuple with the Confirmed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConfirmed

`func (o *DocumentVisualDiffBaselinePreview) SetConfirmed(v bool)`

SetConfirmed sets Confirmed field to given value.


### GetStatus

`func (o *DocumentVisualDiffBaselinePreview) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *DocumentVisualDiffBaselinePreview) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *DocumentVisualDiffBaselinePreview) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetMessage

`func (o *DocumentVisualDiffBaselinePreview) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *DocumentVisualDiffBaselinePreview) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *DocumentVisualDiffBaselinePreview) SetMessage(v string)`

SetMessage sets Message field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
