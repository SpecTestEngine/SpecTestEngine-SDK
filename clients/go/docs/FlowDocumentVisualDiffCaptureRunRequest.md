# FlowDocumentVisualDiffCaptureRunRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StepOrderIndex** | **int32** | Zero-based order index of the saved API specification step. |
**AttachmentId** | **string** | Attachment assertion identifier from that failed step. |

## Methods

### NewFlowDocumentVisualDiffCaptureRunRequest

`func NewFlowDocumentVisualDiffCaptureRunRequest(stepOrderIndex int32, attachmentId string, ) *FlowDocumentVisualDiffCaptureRunRequest`

NewFlowDocumentVisualDiffCaptureRunRequest instantiates a new FlowDocumentVisualDiffCaptureRunRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowDocumentVisualDiffCaptureRunRequestWithDefaults

`func NewFlowDocumentVisualDiffCaptureRunRequestWithDefaults() *FlowDocumentVisualDiffCaptureRunRequest`

NewFlowDocumentVisualDiffCaptureRunRequestWithDefaults instantiates a new FlowDocumentVisualDiffCaptureRunRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStepOrderIndex

`func (o *FlowDocumentVisualDiffCaptureRunRequest) GetStepOrderIndex() int32`

GetStepOrderIndex returns the StepOrderIndex field if non-nil, zero value otherwise.

### GetStepOrderIndexOk

`func (o *FlowDocumentVisualDiffCaptureRunRequest) GetStepOrderIndexOk() (*int32, bool)`

GetStepOrderIndexOk returns a tuple with the StepOrderIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepOrderIndex

`func (o *FlowDocumentVisualDiffCaptureRunRequest) SetStepOrderIndex(v int32)`

SetStepOrderIndex sets StepOrderIndex field to given value.


### GetAttachmentId

`func (o *FlowDocumentVisualDiffCaptureRunRequest) GetAttachmentId() string`

GetAttachmentId returns the AttachmentId field if non-nil, zero value otherwise.

### GetAttachmentIdOk

`func (o *FlowDocumentVisualDiffCaptureRunRequest) GetAttachmentIdOk() (*string, bool)`

GetAttachmentIdOk returns a tuple with the AttachmentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttachmentId

`func (o *FlowDocumentVisualDiffCaptureRunRequest) SetAttachmentId(v string)`

SetAttachmentId sets AttachmentId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
