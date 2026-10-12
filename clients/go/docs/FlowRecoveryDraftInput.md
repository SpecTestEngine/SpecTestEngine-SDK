# FlowRecoveryDraftInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ManifestHash** | **string** |  |
**Mode** | **string** |  |
**Draft** | **map[string]interface{}** | Ordinary Flow create/update authoring shape, up to 16 MiB. Preserve retained visual references for owner validation. |
**ExpectedFlowRevision** | **int64** |  |
**SourceStepIds** | **[]string** | One original occurrence UUID per ordered draft step, or null for an added step. Identity does not grant authority. |
**DependencyRevisions** | **map[string]int64** |  |
**Bindings** | **map[string]interface{}** | Exactly required selected bindings. Preserve scalar types; never invent old literal inputs. Not retained in the journal. |

## Methods

### NewFlowRecoveryDraftInput

`func NewFlowRecoveryDraftInput(manifestHash string, mode string, draft map[string]interface{}, expectedFlowRevision int64, sourceStepIds []*string, dependencyRevisions map[string]int64, bindings map[string]interface{}, ) *FlowRecoveryDraftInput`

NewFlowRecoveryDraftInput instantiates a new FlowRecoveryDraftInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowRecoveryDraftInputWithDefaults

`func NewFlowRecoveryDraftInputWithDefaults() *FlowRecoveryDraftInput`

NewFlowRecoveryDraftInputWithDefaults instantiates a new FlowRecoveryDraftInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetManifestHash

`func (o *FlowRecoveryDraftInput) GetManifestHash() string`

GetManifestHash returns the ManifestHash field if non-nil, zero value otherwise.

### GetManifestHashOk

`func (o *FlowRecoveryDraftInput) GetManifestHashOk() (*string, bool)`

GetManifestHashOk returns a tuple with the ManifestHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManifestHash

`func (o *FlowRecoveryDraftInput) SetManifestHash(v string)`

SetManifestHash sets ManifestHash field to given value.


### GetMode

`func (o *FlowRecoveryDraftInput) GetMode() string`

GetMode returns the Mode field if non-nil, zero value otherwise.

### GetModeOk

`func (o *FlowRecoveryDraftInput) GetModeOk() (*string, bool)`

GetModeOk returns a tuple with the Mode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMode

`func (o *FlowRecoveryDraftInput) SetMode(v string)`

SetMode sets Mode field to given value.


### GetDraft

`func (o *FlowRecoveryDraftInput) GetDraft() map[string]interface{}`

GetDraft returns the Draft field if non-nil, zero value otherwise.

### GetDraftOk

`func (o *FlowRecoveryDraftInput) GetDraftOk() (*map[string]interface{}, bool)`

GetDraftOk returns a tuple with the Draft field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDraft

`func (o *FlowRecoveryDraftInput) SetDraft(v map[string]interface{})`

SetDraft sets Draft field to given value.


### GetExpectedFlowRevision

`func (o *FlowRecoveryDraftInput) GetExpectedFlowRevision() int64`

GetExpectedFlowRevision returns the ExpectedFlowRevision field if non-nil, zero value otherwise.

### GetExpectedFlowRevisionOk

`func (o *FlowRecoveryDraftInput) GetExpectedFlowRevisionOk() (*int64, bool)`

GetExpectedFlowRevisionOk returns a tuple with the ExpectedFlowRevision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedFlowRevision

`func (o *FlowRecoveryDraftInput) SetExpectedFlowRevision(v int64)`

SetExpectedFlowRevision sets ExpectedFlowRevision field to given value.


### GetSourceStepIds

`func (o *FlowRecoveryDraftInput) GetSourceStepIds() []*string`

GetSourceStepIds returns the SourceStepIds field if non-nil, zero value otherwise.

### GetSourceStepIdsOk

`func (o *FlowRecoveryDraftInput) GetSourceStepIdsOk() (*[]*string, bool)`

GetSourceStepIdsOk returns a tuple with the SourceStepIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceStepIds

`func (o *FlowRecoveryDraftInput) SetSourceStepIds(v []*string)`

SetSourceStepIds sets SourceStepIds field to given value.


### GetDependencyRevisions

`func (o *FlowRecoveryDraftInput) GetDependencyRevisions() map[string]int64`

GetDependencyRevisions returns the DependencyRevisions field if non-nil, zero value otherwise.

### GetDependencyRevisionsOk

`func (o *FlowRecoveryDraftInput) GetDependencyRevisionsOk() (*map[string]int64, bool)`

GetDependencyRevisionsOk returns a tuple with the DependencyRevisions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependencyRevisions

`func (o *FlowRecoveryDraftInput) SetDependencyRevisions(v map[string]int64)`

SetDependencyRevisions sets DependencyRevisions field to given value.


### GetBindings

`func (o *FlowRecoveryDraftInput) GetBindings() map[string]interface{}`

GetBindings returns the Bindings field if non-nil, zero value otherwise.

### GetBindingsOk

`func (o *FlowRecoveryDraftInput) GetBindingsOk() (*map[string]interface{}, bool)`

GetBindingsOk returns a tuple with the Bindings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBindings

`func (o *FlowRecoveryDraftInput) SetBindings(v map[string]interface{})`

SetBindings sets Bindings field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
