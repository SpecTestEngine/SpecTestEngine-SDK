# FlowRunStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StepId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**OrderIndex** | **int32** |  |
**StepType** | **string** |  |
**SpecName** | Pointer to **NullableString** |  | [optional]
**UiMacroId** | Pointer to **NullableString** |  | [optional]
**UiMacroName** | Pointer to **NullableString** |  | [optional]
**UiMacroRunId** | Pointer to **NullableString** |  | [optional]
**BrowserActionType** | Pointer to [**NullableBrowserActionType**](BrowserActionType.md) |  | [optional]
**Selector** | Pointer to **NullableString** |  | [optional]
**Value** | Pointer to **NullableString** |  | [optional]
**VariableName** | Pointer to **NullableString** |  | [optional]
**BrowserPageUrl** | Pointer to **NullableString** |  | [optional]
**BrowserPageTitle** | Pointer to **NullableString** |  | [optional]
**BrowserFailureCode** | Pointer to **NullableString** |  | [optional]
**BrowserFailureMessage** | Pointer to **NullableString** |  | [optional]
**VisualComparison** | Pointer to [**NullableBrowserVisualComparisonSummary**](BrowserVisualComparisonSummary.md) |  | [optional]
**StepStatus** | **string** |  |
**UiMacroFailureCode** | Pointer to **NullableString** |  | [optional]
**UiMacroFailureMessage** | Pointer to **NullableString** |  | [optional]
**TestStepRun** | Pointer to **map[string]interface{}** | Engine-native specification result; Browser steps do not fabricate an API result. | [optional]

## Methods

### NewFlowRunStep

`func NewFlowRunStep(stepId string, orderIndex int32, stepType string, stepStatus string, ) *FlowRunStep`

NewFlowRunStep instantiates a new FlowRunStep object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowRunStepWithDefaults

`func NewFlowRunStepWithDefaults() *FlowRunStep`

NewFlowRunStepWithDefaults instantiates a new FlowRunStep object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStepId

`func (o *FlowRunStep) GetStepId() string`

GetStepId returns the StepId field if non-nil, zero value otherwise.

### GetStepIdOk

`func (o *FlowRunStep) GetStepIdOk() (*string, bool)`

GetStepIdOk returns a tuple with the StepId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepId

`func (o *FlowRunStep) SetStepId(v string)`

SetStepId sets StepId field to given value.


### GetOrderIndex

`func (o *FlowRunStep) GetOrderIndex() int32`

GetOrderIndex returns the OrderIndex field if non-nil, zero value otherwise.

### GetOrderIndexOk

`func (o *FlowRunStep) GetOrderIndexOk() (*int32, bool)`

GetOrderIndexOk returns a tuple with the OrderIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrderIndex

`func (o *FlowRunStep) SetOrderIndex(v int32)`

SetOrderIndex sets OrderIndex field to given value.


### GetStepType

`func (o *FlowRunStep) GetStepType() string`

GetStepType returns the StepType field if non-nil, zero value otherwise.

### GetStepTypeOk

`func (o *FlowRunStep) GetStepTypeOk() (*string, bool)`

GetStepTypeOk returns a tuple with the StepType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepType

`func (o *FlowRunStep) SetStepType(v string)`

SetStepType sets StepType field to given value.


### GetSpecName

`func (o *FlowRunStep) GetSpecName() string`

GetSpecName returns the SpecName field if non-nil, zero value otherwise.

### GetSpecNameOk

`func (o *FlowRunStep) GetSpecNameOk() (*string, bool)`

GetSpecNameOk returns a tuple with the SpecName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecName

`func (o *FlowRunStep) SetSpecName(v string)`

SetSpecName sets SpecName field to given value.

### HasSpecName

`func (o *FlowRunStep) HasSpecName() bool`

HasSpecName returns a boolean if a field has been set.

### SetSpecNameNil

`func (o *FlowRunStep) SetSpecNameNil(b bool)`

 SetSpecNameNil sets the value for SpecName to be an explicit nil

### UnsetSpecName
`func (o *FlowRunStep) UnsetSpecName()`

UnsetSpecName ensures that no value is present for SpecName, not even an explicit nil
### GetUiMacroId

`func (o *FlowRunStep) GetUiMacroId() string`

GetUiMacroId returns the UiMacroId field if non-nil, zero value otherwise.

### GetUiMacroIdOk

`func (o *FlowRunStep) GetUiMacroIdOk() (*string, bool)`

GetUiMacroIdOk returns a tuple with the UiMacroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiMacroId

`func (o *FlowRunStep) SetUiMacroId(v string)`

SetUiMacroId sets UiMacroId field to given value.

### HasUiMacroId

`func (o *FlowRunStep) HasUiMacroId() bool`

HasUiMacroId returns a boolean if a field has been set.

### SetUiMacroIdNil

`func (o *FlowRunStep) SetUiMacroIdNil(b bool)`

 SetUiMacroIdNil sets the value for UiMacroId to be an explicit nil

### UnsetUiMacroId
`func (o *FlowRunStep) UnsetUiMacroId()`

UnsetUiMacroId ensures that no value is present for UiMacroId, not even an explicit nil
### GetUiMacroName

`func (o *FlowRunStep) GetUiMacroName() string`

GetUiMacroName returns the UiMacroName field if non-nil, zero value otherwise.

### GetUiMacroNameOk

`func (o *FlowRunStep) GetUiMacroNameOk() (*string, bool)`

GetUiMacroNameOk returns a tuple with the UiMacroName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiMacroName

`func (o *FlowRunStep) SetUiMacroName(v string)`

SetUiMacroName sets UiMacroName field to given value.

### HasUiMacroName

`func (o *FlowRunStep) HasUiMacroName() bool`

HasUiMacroName returns a boolean if a field has been set.

### SetUiMacroNameNil

`func (o *FlowRunStep) SetUiMacroNameNil(b bool)`

 SetUiMacroNameNil sets the value for UiMacroName to be an explicit nil

### UnsetUiMacroName
`func (o *FlowRunStep) UnsetUiMacroName()`

UnsetUiMacroName ensures that no value is present for UiMacroName, not even an explicit nil
### GetUiMacroRunId

`func (o *FlowRunStep) GetUiMacroRunId() string`

GetUiMacroRunId returns the UiMacroRunId field if non-nil, zero value otherwise.

### GetUiMacroRunIdOk

`func (o *FlowRunStep) GetUiMacroRunIdOk() (*string, bool)`

GetUiMacroRunIdOk returns a tuple with the UiMacroRunId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiMacroRunId

`func (o *FlowRunStep) SetUiMacroRunId(v string)`

SetUiMacroRunId sets UiMacroRunId field to given value.

### HasUiMacroRunId

`func (o *FlowRunStep) HasUiMacroRunId() bool`

HasUiMacroRunId returns a boolean if a field has been set.

### SetUiMacroRunIdNil

`func (o *FlowRunStep) SetUiMacroRunIdNil(b bool)`

 SetUiMacroRunIdNil sets the value for UiMacroRunId to be an explicit nil

### UnsetUiMacroRunId
`func (o *FlowRunStep) UnsetUiMacroRunId()`

UnsetUiMacroRunId ensures that no value is present for UiMacroRunId, not even an explicit nil
### GetBrowserActionType

`func (o *FlowRunStep) GetBrowserActionType() BrowserActionType`

GetBrowserActionType returns the BrowserActionType field if non-nil, zero value otherwise.

### GetBrowserActionTypeOk

`func (o *FlowRunStep) GetBrowserActionTypeOk() (*BrowserActionType, bool)`

GetBrowserActionTypeOk returns a tuple with the BrowserActionType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrowserActionType

`func (o *FlowRunStep) SetBrowserActionType(v BrowserActionType)`

SetBrowserActionType sets BrowserActionType field to given value.

### HasBrowserActionType

`func (o *FlowRunStep) HasBrowserActionType() bool`

HasBrowserActionType returns a boolean if a field has been set.

### SetBrowserActionTypeNil

`func (o *FlowRunStep) SetBrowserActionTypeNil(b bool)`

 SetBrowserActionTypeNil sets the value for BrowserActionType to be an explicit nil

### UnsetBrowserActionType
`func (o *FlowRunStep) UnsetBrowserActionType()`

UnsetBrowserActionType ensures that no value is present for BrowserActionType, not even an explicit nil
### GetSelector

`func (o *FlowRunStep) GetSelector() string`

GetSelector returns the Selector field if non-nil, zero value otherwise.

### GetSelectorOk

`func (o *FlowRunStep) GetSelectorOk() (*string, bool)`

GetSelectorOk returns a tuple with the Selector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelector

`func (o *FlowRunStep) SetSelector(v string)`

SetSelector sets Selector field to given value.

### HasSelector

`func (o *FlowRunStep) HasSelector() bool`

HasSelector returns a boolean if a field has been set.

### SetSelectorNil

`func (o *FlowRunStep) SetSelectorNil(b bool)`

 SetSelectorNil sets the value for Selector to be an explicit nil

### UnsetSelector
`func (o *FlowRunStep) UnsetSelector()`

UnsetSelector ensures that no value is present for Selector, not even an explicit nil
### GetValue

`func (o *FlowRunStep) GetValue() string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *FlowRunStep) GetValueOk() (*string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *FlowRunStep) SetValue(v string)`

SetValue sets Value field to given value.

### HasValue

`func (o *FlowRunStep) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValueNil

`func (o *FlowRunStep) SetValueNil(b bool)`

 SetValueNil sets the value for Value to be an explicit nil

### UnsetValue
`func (o *FlowRunStep) UnsetValue()`

UnsetValue ensures that no value is present for Value, not even an explicit nil
### GetVariableName

`func (o *FlowRunStep) GetVariableName() string`

GetVariableName returns the VariableName field if non-nil, zero value otherwise.

### GetVariableNameOk

`func (o *FlowRunStep) GetVariableNameOk() (*string, bool)`

GetVariableNameOk returns a tuple with the VariableName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariableName

`func (o *FlowRunStep) SetVariableName(v string)`

SetVariableName sets VariableName field to given value.

### HasVariableName

`func (o *FlowRunStep) HasVariableName() bool`

HasVariableName returns a boolean if a field has been set.

### SetVariableNameNil

`func (o *FlowRunStep) SetVariableNameNil(b bool)`

 SetVariableNameNil sets the value for VariableName to be an explicit nil

### UnsetVariableName
`func (o *FlowRunStep) UnsetVariableName()`

UnsetVariableName ensures that no value is present for VariableName, not even an explicit nil
### GetBrowserPageUrl

`func (o *FlowRunStep) GetBrowserPageUrl() string`

GetBrowserPageUrl returns the BrowserPageUrl field if non-nil, zero value otherwise.

### GetBrowserPageUrlOk

`func (o *FlowRunStep) GetBrowserPageUrlOk() (*string, bool)`

GetBrowserPageUrlOk returns a tuple with the BrowserPageUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrowserPageUrl

`func (o *FlowRunStep) SetBrowserPageUrl(v string)`

SetBrowserPageUrl sets BrowserPageUrl field to given value.

### HasBrowserPageUrl

`func (o *FlowRunStep) HasBrowserPageUrl() bool`

HasBrowserPageUrl returns a boolean if a field has been set.

### SetBrowserPageUrlNil

`func (o *FlowRunStep) SetBrowserPageUrlNil(b bool)`

 SetBrowserPageUrlNil sets the value for BrowserPageUrl to be an explicit nil

### UnsetBrowserPageUrl
`func (o *FlowRunStep) UnsetBrowserPageUrl()`

UnsetBrowserPageUrl ensures that no value is present for BrowserPageUrl, not even an explicit nil
### GetBrowserPageTitle

`func (o *FlowRunStep) GetBrowserPageTitle() string`

GetBrowserPageTitle returns the BrowserPageTitle field if non-nil, zero value otherwise.

### GetBrowserPageTitleOk

`func (o *FlowRunStep) GetBrowserPageTitleOk() (*string, bool)`

GetBrowserPageTitleOk returns a tuple with the BrowserPageTitle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrowserPageTitle

`func (o *FlowRunStep) SetBrowserPageTitle(v string)`

SetBrowserPageTitle sets BrowserPageTitle field to given value.

### HasBrowserPageTitle

`func (o *FlowRunStep) HasBrowserPageTitle() bool`

HasBrowserPageTitle returns a boolean if a field has been set.

### SetBrowserPageTitleNil

`func (o *FlowRunStep) SetBrowserPageTitleNil(b bool)`

 SetBrowserPageTitleNil sets the value for BrowserPageTitle to be an explicit nil

### UnsetBrowserPageTitle
`func (o *FlowRunStep) UnsetBrowserPageTitle()`

UnsetBrowserPageTitle ensures that no value is present for BrowserPageTitle, not even an explicit nil
### GetBrowserFailureCode

`func (o *FlowRunStep) GetBrowserFailureCode() string`

GetBrowserFailureCode returns the BrowserFailureCode field if non-nil, zero value otherwise.

### GetBrowserFailureCodeOk

`func (o *FlowRunStep) GetBrowserFailureCodeOk() (*string, bool)`

GetBrowserFailureCodeOk returns a tuple with the BrowserFailureCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrowserFailureCode

`func (o *FlowRunStep) SetBrowserFailureCode(v string)`

SetBrowserFailureCode sets BrowserFailureCode field to given value.

### HasBrowserFailureCode

`func (o *FlowRunStep) HasBrowserFailureCode() bool`

HasBrowserFailureCode returns a boolean if a field has been set.

### SetBrowserFailureCodeNil

`func (o *FlowRunStep) SetBrowserFailureCodeNil(b bool)`

 SetBrowserFailureCodeNil sets the value for BrowserFailureCode to be an explicit nil

### UnsetBrowserFailureCode
`func (o *FlowRunStep) UnsetBrowserFailureCode()`

UnsetBrowserFailureCode ensures that no value is present for BrowserFailureCode, not even an explicit nil
### GetBrowserFailureMessage

`func (o *FlowRunStep) GetBrowserFailureMessage() string`

GetBrowserFailureMessage returns the BrowserFailureMessage field if non-nil, zero value otherwise.

### GetBrowserFailureMessageOk

`func (o *FlowRunStep) GetBrowserFailureMessageOk() (*string, bool)`

GetBrowserFailureMessageOk returns a tuple with the BrowserFailureMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrowserFailureMessage

`func (o *FlowRunStep) SetBrowserFailureMessage(v string)`

SetBrowserFailureMessage sets BrowserFailureMessage field to given value.

### HasBrowserFailureMessage

`func (o *FlowRunStep) HasBrowserFailureMessage() bool`

HasBrowserFailureMessage returns a boolean if a field has been set.

### SetBrowserFailureMessageNil

`func (o *FlowRunStep) SetBrowserFailureMessageNil(b bool)`

 SetBrowserFailureMessageNil sets the value for BrowserFailureMessage to be an explicit nil

### UnsetBrowserFailureMessage
`func (o *FlowRunStep) UnsetBrowserFailureMessage()`

UnsetBrowserFailureMessage ensures that no value is present for BrowserFailureMessage, not even an explicit nil
### GetVisualComparison

`func (o *FlowRunStep) GetVisualComparison() BrowserVisualComparisonSummary`

GetVisualComparison returns the VisualComparison field if non-nil, zero value otherwise.

### GetVisualComparisonOk

`func (o *FlowRunStep) GetVisualComparisonOk() (*BrowserVisualComparisonSummary, bool)`

GetVisualComparisonOk returns a tuple with the VisualComparison field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVisualComparison

`func (o *FlowRunStep) SetVisualComparison(v BrowserVisualComparisonSummary)`

SetVisualComparison sets VisualComparison field to given value.

### HasVisualComparison

`func (o *FlowRunStep) HasVisualComparison() bool`

HasVisualComparison returns a boolean if a field has been set.

### SetVisualComparisonNil

`func (o *FlowRunStep) SetVisualComparisonNil(b bool)`

 SetVisualComparisonNil sets the value for VisualComparison to be an explicit nil

### UnsetVisualComparison
`func (o *FlowRunStep) UnsetVisualComparison()`

UnsetVisualComparison ensures that no value is present for VisualComparison, not even an explicit nil
### GetStepStatus

`func (o *FlowRunStep) GetStepStatus() string`

GetStepStatus returns the StepStatus field if non-nil, zero value otherwise.

### GetStepStatusOk

`func (o *FlowRunStep) GetStepStatusOk() (*string, bool)`

GetStepStatusOk returns a tuple with the StepStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepStatus

`func (o *FlowRunStep) SetStepStatus(v string)`

SetStepStatus sets StepStatus field to given value.


### GetUiMacroFailureCode

`func (o *FlowRunStep) GetUiMacroFailureCode() string`

GetUiMacroFailureCode returns the UiMacroFailureCode field if non-nil, zero value otherwise.

### GetUiMacroFailureCodeOk

`func (o *FlowRunStep) GetUiMacroFailureCodeOk() (*string, bool)`

GetUiMacroFailureCodeOk returns a tuple with the UiMacroFailureCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiMacroFailureCode

`func (o *FlowRunStep) SetUiMacroFailureCode(v string)`

SetUiMacroFailureCode sets UiMacroFailureCode field to given value.

### HasUiMacroFailureCode

`func (o *FlowRunStep) HasUiMacroFailureCode() bool`

HasUiMacroFailureCode returns a boolean if a field has been set.

### SetUiMacroFailureCodeNil

`func (o *FlowRunStep) SetUiMacroFailureCodeNil(b bool)`

 SetUiMacroFailureCodeNil sets the value for UiMacroFailureCode to be an explicit nil

### UnsetUiMacroFailureCode
`func (o *FlowRunStep) UnsetUiMacroFailureCode()`

UnsetUiMacroFailureCode ensures that no value is present for UiMacroFailureCode, not even an explicit nil
### GetUiMacroFailureMessage

`func (o *FlowRunStep) GetUiMacroFailureMessage() string`

GetUiMacroFailureMessage returns the UiMacroFailureMessage field if non-nil, zero value otherwise.

### GetUiMacroFailureMessageOk

`func (o *FlowRunStep) GetUiMacroFailureMessageOk() (*string, bool)`

GetUiMacroFailureMessageOk returns a tuple with the UiMacroFailureMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiMacroFailureMessage

`func (o *FlowRunStep) SetUiMacroFailureMessage(v string)`

SetUiMacroFailureMessage sets UiMacroFailureMessage field to given value.

### HasUiMacroFailureMessage

`func (o *FlowRunStep) HasUiMacroFailureMessage() bool`

HasUiMacroFailureMessage returns a boolean if a field has been set.

### SetUiMacroFailureMessageNil

`func (o *FlowRunStep) SetUiMacroFailureMessageNil(b bool)`

 SetUiMacroFailureMessageNil sets the value for UiMacroFailureMessage to be an explicit nil

### UnsetUiMacroFailureMessage
`func (o *FlowRunStep) UnsetUiMacroFailureMessage()`

UnsetUiMacroFailureMessage ensures that no value is present for UiMacroFailureMessage, not even an explicit nil
### GetTestStepRun

`func (o *FlowRunStep) GetTestStepRun() map[string]interface{}`

GetTestStepRun returns the TestStepRun field if non-nil, zero value otherwise.

### GetTestStepRunOk

`func (o *FlowRunStep) GetTestStepRunOk() (*map[string]interface{}, bool)`

GetTestStepRunOk returns a tuple with the TestStepRun field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTestStepRun

`func (o *FlowRunStep) SetTestStepRun(v map[string]interface{})`

SetTestStepRun sets TestStepRun field to given value.

### HasTestStepRun

`func (o *FlowRunStep) HasTestStepRun() bool`

HasTestStepRun returns a boolean if a field has been set.

### SetTestStepRunNil

`func (o *FlowRunStep) SetTestStepRunNil(b bool)`

 SetTestStepRunNil sets the value for TestStepRun to be an explicit nil

### UnsetTestStepRun
`func (o *FlowRunStep) UnsetTestStepRun()`

UnsetTestStepRun ensures that no value is present for TestStepRun, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


