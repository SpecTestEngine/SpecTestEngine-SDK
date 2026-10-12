# FlowRecoveryCurrentDependencySource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SourceId** | **string** |  |
**Revision** | **int64** |  |
**Name** | **string** |  |
**Format** | **string** |  |
**Definition** | Pointer to [**NullableFlowRecoveryProjection**](FlowRecoveryProjection.md) |  | [optional]

## Methods

### NewFlowRecoveryCurrentDependencySource

`func NewFlowRecoveryCurrentDependencySource(sourceId string, revision int64, name string, format string, ) *FlowRecoveryCurrentDependencySource`

NewFlowRecoveryCurrentDependencySource instantiates a new FlowRecoveryCurrentDependencySource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowRecoveryCurrentDependencySourceWithDefaults

`func NewFlowRecoveryCurrentDependencySourceWithDefaults() *FlowRecoveryCurrentDependencySource`

NewFlowRecoveryCurrentDependencySourceWithDefaults instantiates a new FlowRecoveryCurrentDependencySource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSourceId

`func (o *FlowRecoveryCurrentDependencySource) GetSourceId() string`

GetSourceId returns the SourceId field if non-nil, zero value otherwise.

### GetSourceIdOk

`func (o *FlowRecoveryCurrentDependencySource) GetSourceIdOk() (*string, bool)`

GetSourceIdOk returns a tuple with the SourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceId

`func (o *FlowRecoveryCurrentDependencySource) SetSourceId(v string)`

SetSourceId sets SourceId field to given value.


### GetRevision

`func (o *FlowRecoveryCurrentDependencySource) GetRevision() int64`

GetRevision returns the Revision field if non-nil, zero value otherwise.

### GetRevisionOk

`func (o *FlowRecoveryCurrentDependencySource) GetRevisionOk() (*int64, bool)`

GetRevisionOk returns a tuple with the Revision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevision

`func (o *FlowRecoveryCurrentDependencySource) SetRevision(v int64)`

SetRevision sets Revision field to given value.


### GetName

`func (o *FlowRecoveryCurrentDependencySource) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *FlowRecoveryCurrentDependencySource) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *FlowRecoveryCurrentDependencySource) SetName(v string)`

SetName sets Name field to given value.


### GetFormat

`func (o *FlowRecoveryCurrentDependencySource) GetFormat() string`

GetFormat returns the Format field if non-nil, zero value otherwise.

### GetFormatOk

`func (o *FlowRecoveryCurrentDependencySource) GetFormatOk() (*string, bool)`

GetFormatOk returns a tuple with the Format field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFormat

`func (o *FlowRecoveryCurrentDependencySource) SetFormat(v string)`

SetFormat sets Format field to given value.


### GetDefinition

`func (o *FlowRecoveryCurrentDependencySource) GetDefinition() FlowRecoveryProjection`

GetDefinition returns the Definition field if non-nil, zero value otherwise.

### GetDefinitionOk

`func (o *FlowRecoveryCurrentDependencySource) GetDefinitionOk() (*FlowRecoveryProjection, bool)`

GetDefinitionOk returns a tuple with the Definition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinition

`func (o *FlowRecoveryCurrentDependencySource) SetDefinition(v FlowRecoveryProjection)`

SetDefinition sets Definition field to given value.

### HasDefinition

`func (o *FlowRecoveryCurrentDependencySource) HasDefinition() bool`

HasDefinition returns a boolean if a field has been set.

### SetDefinitionNil

`func (o *FlowRecoveryCurrentDependencySource) SetDefinitionNil(b bool)`

 SetDefinitionNil sets the value for Definition to be an explicit nil

### UnsetDefinition
`func (o *FlowRecoveryCurrentDependencySource) UnsetDefinition()`

UnsetDefinition ensures that no value is present for Definition, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
