# DocumentVisualDiff

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**VisualDiffId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**ViewerUrl** | **string** |  |
**SourceType** | **string** |  |
**SourceRunId** | Pointer to **NullableString** |  | [optional]
**SourceStepId** | Pointer to **NullableString** |  | [optional]
**AttachmentId** | **string** |  |
**ActualContentType** | **string** |  |
**ActualSha256** | **string** |  |
**ExpectedSha256** | Pointer to **NullableString** |  | [optional]
**Status** | [**DocumentVisualDiffStatus**](DocumentVisualDiffStatus.md) |  |
**Decision** | [**DocumentVisualDiffDecision**](DocumentVisualDiffDecision.md) |  |
**ActualPageCount** | **int32** |  |
**CreatedAt** | **time.Time** |  |
**ExpiresAt** | **time.Time** |  |
**ActualAvailable** | **bool** |  |
**ExpectedUploadRequired** | **bool** |  |
**RegenerateAvailable** | **bool** |  |
**Generations** | [**[]DocumentVisualDiffGeneration**](DocumentVisualDiffGeneration.md) |  |
**CurrentGeneration** | Pointer to [**NullableDocumentVisualDiffGeneration**](DocumentVisualDiffGeneration.md) |  | [optional]

## Methods

### NewDocumentVisualDiff

`func NewDocumentVisualDiff(visualDiffId string, viewerUrl string, sourceType string, attachmentId string, actualContentType string, actualSha256 string, status DocumentVisualDiffStatus, decision DocumentVisualDiffDecision, actualPageCount int32, createdAt time.Time, expiresAt time.Time, actualAvailable bool, expectedUploadRequired bool, regenerateAvailable bool, generations []DocumentVisualDiffGeneration, ) *DocumentVisualDiff`

NewDocumentVisualDiff instantiates a new DocumentVisualDiff object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDocumentVisualDiffWithDefaults

`func NewDocumentVisualDiffWithDefaults() *DocumentVisualDiff`

NewDocumentVisualDiffWithDefaults instantiates a new DocumentVisualDiff object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetVisualDiffId

`func (o *DocumentVisualDiff) GetVisualDiffId() string`

GetVisualDiffId returns the VisualDiffId field if non-nil, zero value otherwise.

### GetVisualDiffIdOk

`func (o *DocumentVisualDiff) GetVisualDiffIdOk() (*string, bool)`

GetVisualDiffIdOk returns a tuple with the VisualDiffId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVisualDiffId

`func (o *DocumentVisualDiff) SetVisualDiffId(v string)`

SetVisualDiffId sets VisualDiffId field to given value.


### GetViewerUrl

`func (o *DocumentVisualDiff) GetViewerUrl() string`

GetViewerUrl returns the ViewerUrl field if non-nil, zero value otherwise.

### GetViewerUrlOk

`func (o *DocumentVisualDiff) GetViewerUrlOk() (*string, bool)`

GetViewerUrlOk returns a tuple with the ViewerUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetViewerUrl

`func (o *DocumentVisualDiff) SetViewerUrl(v string)`

SetViewerUrl sets ViewerUrl field to given value.


### GetSourceType

`func (o *DocumentVisualDiff) GetSourceType() string`

GetSourceType returns the SourceType field if non-nil, zero value otherwise.

### GetSourceTypeOk

`func (o *DocumentVisualDiff) GetSourceTypeOk() (*string, bool)`

GetSourceTypeOk returns a tuple with the SourceType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceType

`func (o *DocumentVisualDiff) SetSourceType(v string)`

SetSourceType sets SourceType field to given value.


### GetSourceRunId

`func (o *DocumentVisualDiff) GetSourceRunId() string`

GetSourceRunId returns the SourceRunId field if non-nil, zero value otherwise.

### GetSourceRunIdOk

`func (o *DocumentVisualDiff) GetSourceRunIdOk() (*string, bool)`

GetSourceRunIdOk returns a tuple with the SourceRunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceRunId

`func (o *DocumentVisualDiff) SetSourceRunId(v string)`

SetSourceRunId sets SourceRunId field to given value.

### HasSourceRunId

`func (o *DocumentVisualDiff) HasSourceRunId() bool`

HasSourceRunId returns a boolean if a field has been set.

### SetSourceRunIdNil

`func (o *DocumentVisualDiff) SetSourceRunIdNil(b bool)`

 SetSourceRunIdNil sets the value for SourceRunId to be an explicit nil

### UnsetSourceRunId
`func (o *DocumentVisualDiff) UnsetSourceRunId()`

UnsetSourceRunId ensures that no value is present for SourceRunId, not even an explicit nil
### GetSourceStepId

`func (o *DocumentVisualDiff) GetSourceStepId() string`

GetSourceStepId returns the SourceStepId field if non-nil, zero value otherwise.

### GetSourceStepIdOk

`func (o *DocumentVisualDiff) GetSourceStepIdOk() (*string, bool)`

GetSourceStepIdOk returns a tuple with the SourceStepId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceStepId

`func (o *DocumentVisualDiff) SetSourceStepId(v string)`

SetSourceStepId sets SourceStepId field to given value.

### HasSourceStepId

`func (o *DocumentVisualDiff) HasSourceStepId() bool`

HasSourceStepId returns a boolean if a field has been set.

### SetSourceStepIdNil

`func (o *DocumentVisualDiff) SetSourceStepIdNil(b bool)`

 SetSourceStepIdNil sets the value for SourceStepId to be an explicit nil

### UnsetSourceStepId
`func (o *DocumentVisualDiff) UnsetSourceStepId()`

UnsetSourceStepId ensures that no value is present for SourceStepId, not even an explicit nil
### GetAttachmentId

`func (o *DocumentVisualDiff) GetAttachmentId() string`

GetAttachmentId returns the AttachmentId field if non-nil, zero value otherwise.

### GetAttachmentIdOk

`func (o *DocumentVisualDiff) GetAttachmentIdOk() (*string, bool)`

GetAttachmentIdOk returns a tuple with the AttachmentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttachmentId

`func (o *DocumentVisualDiff) SetAttachmentId(v string)`

SetAttachmentId sets AttachmentId field to given value.


### GetActualContentType

`func (o *DocumentVisualDiff) GetActualContentType() string`

GetActualContentType returns the ActualContentType field if non-nil, zero value otherwise.

### GetActualContentTypeOk

`func (o *DocumentVisualDiff) GetActualContentTypeOk() (*string, bool)`

GetActualContentTypeOk returns a tuple with the ActualContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActualContentType

`func (o *DocumentVisualDiff) SetActualContentType(v string)`

SetActualContentType sets ActualContentType field to given value.


### GetActualSha256

`func (o *DocumentVisualDiff) GetActualSha256() string`

GetActualSha256 returns the ActualSha256 field if non-nil, zero value otherwise.

### GetActualSha256Ok

`func (o *DocumentVisualDiff) GetActualSha256Ok() (*string, bool)`

GetActualSha256Ok returns a tuple with the ActualSha256 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActualSha256

`func (o *DocumentVisualDiff) SetActualSha256(v string)`

SetActualSha256 sets ActualSha256 field to given value.


### GetExpectedSha256

`func (o *DocumentVisualDiff) GetExpectedSha256() string`

GetExpectedSha256 returns the ExpectedSha256 field if non-nil, zero value otherwise.

### GetExpectedSha256Ok

`func (o *DocumentVisualDiff) GetExpectedSha256Ok() (*string, bool)`

GetExpectedSha256Ok returns a tuple with the ExpectedSha256 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedSha256

`func (o *DocumentVisualDiff) SetExpectedSha256(v string)`

SetExpectedSha256 sets ExpectedSha256 field to given value.

### HasExpectedSha256

`func (o *DocumentVisualDiff) HasExpectedSha256() bool`

HasExpectedSha256 returns a boolean if a field has been set.

### SetExpectedSha256Nil

`func (o *DocumentVisualDiff) SetExpectedSha256Nil(b bool)`

 SetExpectedSha256Nil sets the value for ExpectedSha256 to be an explicit nil

### UnsetExpectedSha256
`func (o *DocumentVisualDiff) UnsetExpectedSha256()`

UnsetExpectedSha256 ensures that no value is present for ExpectedSha256, not even an explicit nil
### GetStatus

`func (o *DocumentVisualDiff) GetStatus() DocumentVisualDiffStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *DocumentVisualDiff) GetStatusOk() (*DocumentVisualDiffStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *DocumentVisualDiff) SetStatus(v DocumentVisualDiffStatus)`

SetStatus sets Status field to given value.


### GetDecision

`func (o *DocumentVisualDiff) GetDecision() DocumentVisualDiffDecision`

GetDecision returns the Decision field if non-nil, zero value otherwise.

### GetDecisionOk

`func (o *DocumentVisualDiff) GetDecisionOk() (*DocumentVisualDiffDecision, bool)`

GetDecisionOk returns a tuple with the Decision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDecision

`func (o *DocumentVisualDiff) SetDecision(v DocumentVisualDiffDecision)`

SetDecision sets Decision field to given value.


### GetActualPageCount

`func (o *DocumentVisualDiff) GetActualPageCount() int32`

GetActualPageCount returns the ActualPageCount field if non-nil, zero value otherwise.

### GetActualPageCountOk

`func (o *DocumentVisualDiff) GetActualPageCountOk() (*int32, bool)`

GetActualPageCountOk returns a tuple with the ActualPageCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActualPageCount

`func (o *DocumentVisualDiff) SetActualPageCount(v int32)`

SetActualPageCount sets ActualPageCount field to given value.


### GetCreatedAt

`func (o *DocumentVisualDiff) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *DocumentVisualDiff) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *DocumentVisualDiff) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetExpiresAt

`func (o *DocumentVisualDiff) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *DocumentVisualDiff) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *DocumentVisualDiff) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.


### GetActualAvailable

`func (o *DocumentVisualDiff) GetActualAvailable() bool`

GetActualAvailable returns the ActualAvailable field if non-nil, zero value otherwise.

### GetActualAvailableOk

`func (o *DocumentVisualDiff) GetActualAvailableOk() (*bool, bool)`

GetActualAvailableOk returns a tuple with the ActualAvailable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActualAvailable

`func (o *DocumentVisualDiff) SetActualAvailable(v bool)`

SetActualAvailable sets ActualAvailable field to given value.


### GetExpectedUploadRequired

`func (o *DocumentVisualDiff) GetExpectedUploadRequired() bool`

GetExpectedUploadRequired returns the ExpectedUploadRequired field if non-nil, zero value otherwise.

### GetExpectedUploadRequiredOk

`func (o *DocumentVisualDiff) GetExpectedUploadRequiredOk() (*bool, bool)`

GetExpectedUploadRequiredOk returns a tuple with the ExpectedUploadRequired field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedUploadRequired

`func (o *DocumentVisualDiff) SetExpectedUploadRequired(v bool)`

SetExpectedUploadRequired sets ExpectedUploadRequired field to given value.


### GetRegenerateAvailable

`func (o *DocumentVisualDiff) GetRegenerateAvailable() bool`

GetRegenerateAvailable returns the RegenerateAvailable field if non-nil, zero value otherwise.

### GetRegenerateAvailableOk

`func (o *DocumentVisualDiff) GetRegenerateAvailableOk() (*bool, bool)`

GetRegenerateAvailableOk returns a tuple with the RegenerateAvailable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegenerateAvailable

`func (o *DocumentVisualDiff) SetRegenerateAvailable(v bool)`

SetRegenerateAvailable sets RegenerateAvailable field to given value.


### GetGenerations

`func (o *DocumentVisualDiff) GetGenerations() []DocumentVisualDiffGeneration`

GetGenerations returns the Generations field if non-nil, zero value otherwise.

### GetGenerationsOk

`func (o *DocumentVisualDiff) GetGenerationsOk() (*[]DocumentVisualDiffGeneration, bool)`

GetGenerationsOk returns a tuple with the Generations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGenerations

`func (o *DocumentVisualDiff) SetGenerations(v []DocumentVisualDiffGeneration)`

SetGenerations sets Generations field to given value.


### GetCurrentGeneration

`func (o *DocumentVisualDiff) GetCurrentGeneration() DocumentVisualDiffGeneration`

GetCurrentGeneration returns the CurrentGeneration field if non-nil, zero value otherwise.

### GetCurrentGenerationOk

`func (o *DocumentVisualDiff) GetCurrentGenerationOk() (*DocumentVisualDiffGeneration, bool)`

GetCurrentGenerationOk returns a tuple with the CurrentGeneration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentGeneration

`func (o *DocumentVisualDiff) SetCurrentGeneration(v DocumentVisualDiffGeneration)`

SetCurrentGeneration sets CurrentGeneration field to given value.

### HasCurrentGeneration

`func (o *DocumentVisualDiff) HasCurrentGeneration() bool`

HasCurrentGeneration returns a boolean if a field has been set.

### SetCurrentGenerationNil

`func (o *DocumentVisualDiff) SetCurrentGenerationNil(b bool)`

 SetCurrentGenerationNil sets the value for CurrentGeneration to be an explicit nil

### UnsetCurrentGeneration
`func (o *DocumentVisualDiff) UnsetCurrentGeneration()`

UnsetCurrentGeneration ensures that no value is present for CurrentGeneration, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
