# FlowRecoveryPreview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RunId** | **string** |  |
**Available** | **bool** |  |
**Reason** | Pointer to **NullableString** |  | [optional]
**ManifestVersion** | **int32** |  |
**ManifestHash** | Pointer to **NullableString** |  | [optional]
**SuggestedName** | Pointer to **NullableString** |  | [optional]
**Flow** | Pointer to [**NullableFlowRecoveryHistoricalDefinition**](FlowRecoveryHistoricalDefinition.md) |  | [optional]
**StepCount** | **int32** |  |
**CopyCount** | **int32** |  |
**Bindings** | [**[]FlowRecoveryBinding**](FlowRecoveryBinding.md) |  |
**Dependencies** | [**FlowRecoveryDependencyPage**](FlowRecoveryDependencyPage.md) |  |
**ActiveOperation** | Pointer to [**NullableFlowRecoveryOperation**](FlowRecoveryOperation.md) |  | [optional]

## Methods

### NewFlowRecoveryPreview

`func NewFlowRecoveryPreview(runId string, available bool, manifestVersion int32, stepCount int32, copyCount int32, bindings []FlowRecoveryBinding, dependencies FlowRecoveryDependencyPage, ) *FlowRecoveryPreview`

NewFlowRecoveryPreview instantiates a new FlowRecoveryPreview object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowRecoveryPreviewWithDefaults

`func NewFlowRecoveryPreviewWithDefaults() *FlowRecoveryPreview`

NewFlowRecoveryPreviewWithDefaults instantiates a new FlowRecoveryPreview object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRunId

`func (o *FlowRecoveryPreview) GetRunId() string`

GetRunId returns the RunId field if non-nil, zero value otherwise.

### GetRunIdOk

`func (o *FlowRecoveryPreview) GetRunIdOk() (*string, bool)`

GetRunIdOk returns a tuple with the RunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRunId

`func (o *FlowRecoveryPreview) SetRunId(v string)`

SetRunId sets RunId field to given value.


### GetAvailable

`func (o *FlowRecoveryPreview) GetAvailable() bool`

GetAvailable returns the Available field if non-nil, zero value otherwise.

### GetAvailableOk

`func (o *FlowRecoveryPreview) GetAvailableOk() (*bool, bool)`

GetAvailableOk returns a tuple with the Available field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvailable

`func (o *FlowRecoveryPreview) SetAvailable(v bool)`

SetAvailable sets Available field to given value.


### GetReason

`func (o *FlowRecoveryPreview) GetReason() string`

GetReason returns the Reason field if non-nil, zero value otherwise.

### GetReasonOk

`func (o *FlowRecoveryPreview) GetReasonOk() (*string, bool)`

GetReasonOk returns a tuple with the Reason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReason

`func (o *FlowRecoveryPreview) SetReason(v string)`

SetReason sets Reason field to given value.

### HasReason

`func (o *FlowRecoveryPreview) HasReason() bool`

HasReason returns a boolean if a field has been set.

### SetReasonNil

`func (o *FlowRecoveryPreview) SetReasonNil(b bool)`

 SetReasonNil sets the value for Reason to be an explicit nil

### UnsetReason
`func (o *FlowRecoveryPreview) UnsetReason()`

UnsetReason ensures that no value is present for Reason, not even an explicit nil
### GetManifestVersion

`func (o *FlowRecoveryPreview) GetManifestVersion() int32`

GetManifestVersion returns the ManifestVersion field if non-nil, zero value otherwise.

### GetManifestVersionOk

`func (o *FlowRecoveryPreview) GetManifestVersionOk() (*int32, bool)`

GetManifestVersionOk returns a tuple with the ManifestVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManifestVersion

`func (o *FlowRecoveryPreview) SetManifestVersion(v int32)`

SetManifestVersion sets ManifestVersion field to given value.


### GetManifestHash

`func (o *FlowRecoveryPreview) GetManifestHash() string`

GetManifestHash returns the ManifestHash field if non-nil, zero value otherwise.

### GetManifestHashOk

`func (o *FlowRecoveryPreview) GetManifestHashOk() (*string, bool)`

GetManifestHashOk returns a tuple with the ManifestHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManifestHash

`func (o *FlowRecoveryPreview) SetManifestHash(v string)`

SetManifestHash sets ManifestHash field to given value.

### HasManifestHash

`func (o *FlowRecoveryPreview) HasManifestHash() bool`

HasManifestHash returns a boolean if a field has been set.

### SetManifestHashNil

`func (o *FlowRecoveryPreview) SetManifestHashNil(b bool)`

 SetManifestHashNil sets the value for ManifestHash to be an explicit nil

### UnsetManifestHash
`func (o *FlowRecoveryPreview) UnsetManifestHash()`

UnsetManifestHash ensures that no value is present for ManifestHash, not even an explicit nil
### GetSuggestedName

`func (o *FlowRecoveryPreview) GetSuggestedName() string`

GetSuggestedName returns the SuggestedName field if non-nil, zero value otherwise.

### GetSuggestedNameOk

`func (o *FlowRecoveryPreview) GetSuggestedNameOk() (*string, bool)`

GetSuggestedNameOk returns a tuple with the SuggestedName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuggestedName

`func (o *FlowRecoveryPreview) SetSuggestedName(v string)`

SetSuggestedName sets SuggestedName field to given value.

### HasSuggestedName

`func (o *FlowRecoveryPreview) HasSuggestedName() bool`

HasSuggestedName returns a boolean if a field has been set.

### SetSuggestedNameNil

`func (o *FlowRecoveryPreview) SetSuggestedNameNil(b bool)`

 SetSuggestedNameNil sets the value for SuggestedName to be an explicit nil

### UnsetSuggestedName
`func (o *FlowRecoveryPreview) UnsetSuggestedName()`

UnsetSuggestedName ensures that no value is present for SuggestedName, not even an explicit nil
### GetFlow

`func (o *FlowRecoveryPreview) GetFlow() FlowRecoveryHistoricalDefinition`

GetFlow returns the Flow field if non-nil, zero value otherwise.

### GetFlowOk

`func (o *FlowRecoveryPreview) GetFlowOk() (*FlowRecoveryHistoricalDefinition, bool)`

GetFlowOk returns a tuple with the Flow field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlow

`func (o *FlowRecoveryPreview) SetFlow(v FlowRecoveryHistoricalDefinition)`

SetFlow sets Flow field to given value.

### HasFlow

`func (o *FlowRecoveryPreview) HasFlow() bool`

HasFlow returns a boolean if a field has been set.

### SetFlowNil

`func (o *FlowRecoveryPreview) SetFlowNil(b bool)`

 SetFlowNil sets the value for Flow to be an explicit nil

### UnsetFlow
`func (o *FlowRecoveryPreview) UnsetFlow()`

UnsetFlow ensures that no value is present for Flow, not even an explicit nil
### GetStepCount

`func (o *FlowRecoveryPreview) GetStepCount() int32`

GetStepCount returns the StepCount field if non-nil, zero value otherwise.

### GetStepCountOk

`func (o *FlowRecoveryPreview) GetStepCountOk() (*int32, bool)`

GetStepCountOk returns a tuple with the StepCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepCount

`func (o *FlowRecoveryPreview) SetStepCount(v int32)`

SetStepCount sets StepCount field to given value.


### GetCopyCount

`func (o *FlowRecoveryPreview) GetCopyCount() int32`

GetCopyCount returns the CopyCount field if non-nil, zero value otherwise.

### GetCopyCountOk

`func (o *FlowRecoveryPreview) GetCopyCountOk() (*int32, bool)`

GetCopyCountOk returns a tuple with the CopyCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCopyCount

`func (o *FlowRecoveryPreview) SetCopyCount(v int32)`

SetCopyCount sets CopyCount field to given value.


### GetBindings

`func (o *FlowRecoveryPreview) GetBindings() []FlowRecoveryBinding`

GetBindings returns the Bindings field if non-nil, zero value otherwise.

### GetBindingsOk

`func (o *FlowRecoveryPreview) GetBindingsOk() (*[]FlowRecoveryBinding, bool)`

GetBindingsOk returns a tuple with the Bindings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBindings

`func (o *FlowRecoveryPreview) SetBindings(v []FlowRecoveryBinding)`

SetBindings sets Bindings field to given value.


### GetDependencies

`func (o *FlowRecoveryPreview) GetDependencies() FlowRecoveryDependencyPage`

GetDependencies returns the Dependencies field if non-nil, zero value otherwise.

### GetDependenciesOk

`func (o *FlowRecoveryPreview) GetDependenciesOk() (*FlowRecoveryDependencyPage, bool)`

GetDependenciesOk returns a tuple with the Dependencies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependencies

`func (o *FlowRecoveryPreview) SetDependencies(v FlowRecoveryDependencyPage)`

SetDependencies sets Dependencies field to given value.


### GetActiveOperation

`func (o *FlowRecoveryPreview) GetActiveOperation() FlowRecoveryOperation`

GetActiveOperation returns the ActiveOperation field if non-nil, zero value otherwise.

### GetActiveOperationOk

`func (o *FlowRecoveryPreview) GetActiveOperationOk() (*FlowRecoveryOperation, bool)`

GetActiveOperationOk returns a tuple with the ActiveOperation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActiveOperation

`func (o *FlowRecoveryPreview) SetActiveOperation(v FlowRecoveryOperation)`

SetActiveOperation sets ActiveOperation field to given value.

### HasActiveOperation

`func (o *FlowRecoveryPreview) HasActiveOperation() bool`

HasActiveOperation returns a boolean if a field has been set.

### SetActiveOperationNil

`func (o *FlowRecoveryPreview) SetActiveOperationNil(b bool)`

 SetActiveOperationNil sets the value for ActiveOperation to be an explicit nil

### UnsetActiveOperation
`func (o *FlowRecoveryPreview) UnsetActiveOperation()`

UnsetActiveOperation ensures that no value is present for ActiveOperation, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
