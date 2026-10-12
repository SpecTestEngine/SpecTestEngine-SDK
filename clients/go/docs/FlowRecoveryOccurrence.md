# FlowRecoveryOccurrence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SourceStepId** | **string** |  |
**OrderIndex** | **int32** |  |
**DependencyKey** | Pointer to **NullableString** |  | [optional]
**Role** | **string** |  |

## Methods

### NewFlowRecoveryOccurrence

`func NewFlowRecoveryOccurrence(sourceStepId string, orderIndex int32, role string, ) *FlowRecoveryOccurrence`

NewFlowRecoveryOccurrence instantiates a new FlowRecoveryOccurrence object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowRecoveryOccurrenceWithDefaults

`func NewFlowRecoveryOccurrenceWithDefaults() *FlowRecoveryOccurrence`

NewFlowRecoveryOccurrenceWithDefaults instantiates a new FlowRecoveryOccurrence object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSourceStepId

`func (o *FlowRecoveryOccurrence) GetSourceStepId() string`

GetSourceStepId returns the SourceStepId field if non-nil, zero value otherwise.

### GetSourceStepIdOk

`func (o *FlowRecoveryOccurrence) GetSourceStepIdOk() (*string, bool)`

GetSourceStepIdOk returns a tuple with the SourceStepId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceStepId

`func (o *FlowRecoveryOccurrence) SetSourceStepId(v string)`

SetSourceStepId sets SourceStepId field to given value.


### GetOrderIndex

`func (o *FlowRecoveryOccurrence) GetOrderIndex() int32`

GetOrderIndex returns the OrderIndex field if non-nil, zero value otherwise.

### GetOrderIndexOk

`func (o *FlowRecoveryOccurrence) GetOrderIndexOk() (*int32, bool)`

GetOrderIndexOk returns a tuple with the OrderIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrderIndex

`func (o *FlowRecoveryOccurrence) SetOrderIndex(v int32)`

SetOrderIndex sets OrderIndex field to given value.


### GetDependencyKey

`func (o *FlowRecoveryOccurrence) GetDependencyKey() string`

GetDependencyKey returns the DependencyKey field if non-nil, zero value otherwise.

### GetDependencyKeyOk

`func (o *FlowRecoveryOccurrence) GetDependencyKeyOk() (*string, bool)`

GetDependencyKeyOk returns a tuple with the DependencyKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependencyKey

`func (o *FlowRecoveryOccurrence) SetDependencyKey(v string)`

SetDependencyKey sets DependencyKey field to given value.

### HasDependencyKey

`func (o *FlowRecoveryOccurrence) HasDependencyKey() bool`

HasDependencyKey returns a boolean if a field has been set.

### SetDependencyKeyNil

`func (o *FlowRecoveryOccurrence) SetDependencyKeyNil(b bool)`

 SetDependencyKeyNil sets the value for DependencyKey to be an explicit nil

### UnsetDependencyKey
`func (o *FlowRecoveryOccurrence) UnsetDependencyKey()`

UnsetDependencyKey ensures that no value is present for DependencyKey, not even an explicit nil
### GetRole

`func (o *FlowRecoveryOccurrence) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *FlowRecoveryOccurrence) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *FlowRecoveryOccurrence) SetRole(v string)`

SetRole sets Role field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
