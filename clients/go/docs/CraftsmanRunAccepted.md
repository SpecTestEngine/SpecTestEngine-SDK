# CraftsmanRunAccepted

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RunId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**State** | [**CraftsmanRunState**](CraftsmanRunState.md) |  |

## Methods

### NewCraftsmanRunAccepted

`func NewCraftsmanRunAccepted(runId string, state CraftsmanRunState, ) *CraftsmanRunAccepted`

NewCraftsmanRunAccepted instantiates a new CraftsmanRunAccepted object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCraftsmanRunAcceptedWithDefaults

`func NewCraftsmanRunAcceptedWithDefaults() *CraftsmanRunAccepted`

NewCraftsmanRunAcceptedWithDefaults instantiates a new CraftsmanRunAccepted object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRunId

`func (o *CraftsmanRunAccepted) GetRunId() string`

GetRunId returns the RunId field if non-nil, zero value otherwise.

### GetRunIdOk

`func (o *CraftsmanRunAccepted) GetRunIdOk() (*string, bool)`

GetRunIdOk returns a tuple with the RunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRunId

`func (o *CraftsmanRunAccepted) SetRunId(v string)`

SetRunId sets RunId field to given value.


### GetState

`func (o *CraftsmanRunAccepted) GetState() CraftsmanRunState`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *CraftsmanRunAccepted) GetStateOk() (*CraftsmanRunState, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *CraftsmanRunAccepted) SetState(v CraftsmanRunState)`

SetState sets State field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


