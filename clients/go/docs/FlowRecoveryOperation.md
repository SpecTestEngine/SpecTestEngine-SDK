# FlowRecoveryOperation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OperationId** | **string** |  |
**State** | **string** |  |
**Mode** | Pointer to **string** |  | [optional]
**FlowId** | Pointer to **NullableString** |  | [optional]
**FailureCode** | Pointer to **NullableString** |  | [optional]
**IdempotencyKey** | **string** |  |
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**ManifestHash** | **string** |  |
**CopiedDependencies** | **int32** |  |
**TotalDependencies** | **int32** |  |

## Methods

### NewFlowRecoveryOperation

`func NewFlowRecoveryOperation(operationId string, state string, idempotencyKey string, name string, manifestHash string, copiedDependencies int32, totalDependencies int32, ) *FlowRecoveryOperation`

NewFlowRecoveryOperation instantiates a new FlowRecoveryOperation object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowRecoveryOperationWithDefaults

`func NewFlowRecoveryOperationWithDefaults() *FlowRecoveryOperation`

NewFlowRecoveryOperationWithDefaults instantiates a new FlowRecoveryOperation object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOperationId

`func (o *FlowRecoveryOperation) GetOperationId() string`

GetOperationId returns the OperationId field if non-nil, zero value otherwise.

### GetOperationIdOk

`func (o *FlowRecoveryOperation) GetOperationIdOk() (*string, bool)`

GetOperationIdOk returns a tuple with the OperationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOperationId

`func (o *FlowRecoveryOperation) SetOperationId(v string)`

SetOperationId sets OperationId field to given value.


### GetState

`func (o *FlowRecoveryOperation) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *FlowRecoveryOperation) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *FlowRecoveryOperation) SetState(v string)`

SetState sets State field to given value.


### GetMode

`func (o *FlowRecoveryOperation) GetMode() string`

GetMode returns the Mode field if non-nil, zero value otherwise.

### GetModeOk

`func (o *FlowRecoveryOperation) GetModeOk() (*string, bool)`

GetModeOk returns a tuple with the Mode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMode

`func (o *FlowRecoveryOperation) SetMode(v string)`

SetMode sets Mode field to given value.

### HasMode

`func (o *FlowRecoveryOperation) HasMode() bool`

HasMode returns a boolean if a field has been set.

### GetFlowId

`func (o *FlowRecoveryOperation) GetFlowId() string`

GetFlowId returns the FlowId field if non-nil, zero value otherwise.

### GetFlowIdOk

`func (o *FlowRecoveryOperation) GetFlowIdOk() (*string, bool)`

GetFlowIdOk returns a tuple with the FlowId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlowId

`func (o *FlowRecoveryOperation) SetFlowId(v string)`

SetFlowId sets FlowId field to given value.

### HasFlowId

`func (o *FlowRecoveryOperation) HasFlowId() bool`

HasFlowId returns a boolean if a field has been set.

### SetFlowIdNil

`func (o *FlowRecoveryOperation) SetFlowIdNil(b bool)`

 SetFlowIdNil sets the value for FlowId to be an explicit nil

### UnsetFlowId
`func (o *FlowRecoveryOperation) UnsetFlowId()`

UnsetFlowId ensures that no value is present for FlowId, not even an explicit nil
### GetFailureCode

`func (o *FlowRecoveryOperation) GetFailureCode() string`

GetFailureCode returns the FailureCode field if non-nil, zero value otherwise.

### GetFailureCodeOk

`func (o *FlowRecoveryOperation) GetFailureCodeOk() (*string, bool)`

GetFailureCodeOk returns a tuple with the FailureCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFailureCode

`func (o *FlowRecoveryOperation) SetFailureCode(v string)`

SetFailureCode sets FailureCode field to given value.

### HasFailureCode

`func (o *FlowRecoveryOperation) HasFailureCode() bool`

HasFailureCode returns a boolean if a field has been set.

### SetFailureCodeNil

`func (o *FlowRecoveryOperation) SetFailureCodeNil(b bool)`

 SetFailureCodeNil sets the value for FailureCode to be an explicit nil

### UnsetFailureCode
`func (o *FlowRecoveryOperation) UnsetFailureCode()`

UnsetFailureCode ensures that no value is present for FailureCode, not even an explicit nil
### GetIdempotencyKey

`func (o *FlowRecoveryOperation) GetIdempotencyKey() string`

GetIdempotencyKey returns the IdempotencyKey field if non-nil, zero value otherwise.

### GetIdempotencyKeyOk

`func (o *FlowRecoveryOperation) GetIdempotencyKeyOk() (*string, bool)`

GetIdempotencyKeyOk returns a tuple with the IdempotencyKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdempotencyKey

`func (o *FlowRecoveryOperation) SetIdempotencyKey(v string)`

SetIdempotencyKey sets IdempotencyKey field to given value.


### GetName

`func (o *FlowRecoveryOperation) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *FlowRecoveryOperation) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *FlowRecoveryOperation) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *FlowRecoveryOperation) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *FlowRecoveryOperation) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *FlowRecoveryOperation) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *FlowRecoveryOperation) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *FlowRecoveryOperation) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *FlowRecoveryOperation) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetManifestHash

`func (o *FlowRecoveryOperation) GetManifestHash() string`

GetManifestHash returns the ManifestHash field if non-nil, zero value otherwise.

### GetManifestHashOk

`func (o *FlowRecoveryOperation) GetManifestHashOk() (*string, bool)`

GetManifestHashOk returns a tuple with the ManifestHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManifestHash

`func (o *FlowRecoveryOperation) SetManifestHash(v string)`

SetManifestHash sets ManifestHash field to given value.


### GetCopiedDependencies

`func (o *FlowRecoveryOperation) GetCopiedDependencies() int32`

GetCopiedDependencies returns the CopiedDependencies field if non-nil, zero value otherwise.

### GetCopiedDependenciesOk

`func (o *FlowRecoveryOperation) GetCopiedDependenciesOk() (*int32, bool)`

GetCopiedDependenciesOk returns a tuple with the CopiedDependencies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCopiedDependencies

`func (o *FlowRecoveryOperation) SetCopiedDependencies(v int32)`

SetCopiedDependencies sets CopiedDependencies field to given value.


### GetTotalDependencies

`func (o *FlowRecoveryOperation) GetTotalDependencies() int32`

GetTotalDependencies returns the TotalDependencies field if non-nil, zero value otherwise.

### GetTotalDependenciesOk

`func (o *FlowRecoveryOperation) GetTotalDependenciesOk() (*int32, bool)`

GetTotalDependenciesOk returns a tuple with the TotalDependencies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalDependencies

`func (o *FlowRecoveryOperation) SetTotalDependencies(v int32)`

SetTotalDependencies sets TotalDependencies field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
