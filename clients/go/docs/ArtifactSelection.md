# ArtifactSelection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Specs** | [**[]ArtifactSpecRef**](ArtifactSpecRef.md) |  |
**FlowIds** | **[]string** |  |
**UiMacroIds** | **[]string** |  |

## Methods

### NewArtifactSelection

`func NewArtifactSelection(specs []ArtifactSpecRef, flowIds []string, uiMacroIds []string, ) *ArtifactSelection`

NewArtifactSelection instantiates a new ArtifactSelection object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactSelectionWithDefaults

`func NewArtifactSelectionWithDefaults() *ArtifactSelection`

NewArtifactSelectionWithDefaults instantiates a new ArtifactSelection object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSpecs

`func (o *ArtifactSelection) GetSpecs() []ArtifactSpecRef`

GetSpecs returns the Specs field if non-nil, zero value otherwise.

### GetSpecsOk

`func (o *ArtifactSelection) GetSpecsOk() (*[]ArtifactSpecRef, bool)`

GetSpecsOk returns a tuple with the Specs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecs

`func (o *ArtifactSelection) SetSpecs(v []ArtifactSpecRef)`

SetSpecs sets Specs field to given value.


### GetFlowIds

`func (o *ArtifactSelection) GetFlowIds() []string`

GetFlowIds returns the FlowIds field if non-nil, zero value otherwise.

### GetFlowIdsOk

`func (o *ArtifactSelection) GetFlowIdsOk() (*[]string, bool)`

GetFlowIdsOk returns a tuple with the FlowIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlowIds

`func (o *ArtifactSelection) SetFlowIds(v []string)`

SetFlowIds sets FlowIds field to given value.


### GetUiMacroIds

`func (o *ArtifactSelection) GetUiMacroIds() []string`

GetUiMacroIds returns the UiMacroIds field if non-nil, zero value otherwise.

### GetUiMacroIdsOk

`func (o *ArtifactSelection) GetUiMacroIdsOk() (*[]string, bool)`

GetUiMacroIdsOk returns a tuple with the UiMacroIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiMacroIds

`func (o *ArtifactSelection) SetUiMacroIds(v []string)`

SetUiMacroIds sets UiMacroIds field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
