# FlowStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StepId** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**OrderIndex** | **int32** |  |
**FlowName** | Pointer to **NullableString** |  | [optional]
**StepType** | **string** |  |
**SpecId** | Pointer to **NullableString** |  | [optional]
**SpecType** | Pointer to [**NullableSpecType**](SpecType.md) |  | [optional]
**SpecName** | Pointer to **NullableString** |  | [optional]
**UiMacroId** | Pointer to **NullableString** |  | [optional]
**UiMacroName** | Pointer to **NullableString** |  | [optional]
**BrowserActionType** | Pointer to [**NullableBrowserActionType**](BrowserActionType.md) |  | [optional]
**Selector** | Pointer to **NullableString** |  | [optional]
**SelectorCandidates** | Pointer to **[]string** |  | [optional]
**Value** | Pointer to **NullableString** |  | [optional]
**VariableName** | Pointer to **NullableString** |  | [optional]
**TabAlias** | Pointer to **NullableString** |  | [optional]
**FrameSelector** | Pointer to **NullableString** |  | [optional]
**Pattern** | Pointer to **NullableString** |  | [optional]
**ExtractionHint** | Pointer to **NullableString** |  | [optional]
**TextSource** | Pointer to **NullableString** |  | [optional]
**ExpectedPageUrl** | Pointer to **NullableString** |  | [optional]
**ExpectedPageUrlPolicy** | Pointer to **NullableString** |  | [optional]
**ExpectedPageTitle** | Pointer to **NullableString** |  | [optional]
**ExpectedPageTitlePolicy** | Pointer to **NullableString** |  | [optional]
**ExpectedNetworkPolicy** | Pointer to **NullableString** |  | [optional]
**VisualAssertion** | Pointer to [**NullableBrowserVisualAssertion**](BrowserVisualAssertion.md) |  | [optional]
**ExpectedNetworkCalls** | Pointer to [**[]BrowserNetworkExpectation**](BrowserNetworkExpectation.md) |  | [optional]
**StoreValues** | Pointer to **map[string]string** |  | [optional]
**OverrideValues** | Pointer to **map[string]interface{}** |  | [optional]

## Methods

### NewFlowStep

`func NewFlowStep(stepId string, orderIndex int32, stepType string, ) *FlowStep`

NewFlowStep instantiates a new FlowStep object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlowStepWithDefaults

`func NewFlowStepWithDefaults() *FlowStep`

NewFlowStepWithDefaults instantiates a new FlowStep object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStepId

`func (o *FlowStep) GetStepId() string`

GetStepId returns the StepId field if non-nil, zero value otherwise.

### GetStepIdOk

`func (o *FlowStep) GetStepIdOk() (*string, bool)`

GetStepIdOk returns a tuple with the StepId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepId

`func (o *FlowStep) SetStepId(v string)`

SetStepId sets StepId field to given value.


### GetOrderIndex

`func (o *FlowStep) GetOrderIndex() int32`

GetOrderIndex returns the OrderIndex field if non-nil, zero value otherwise.

### GetOrderIndexOk

`func (o *FlowStep) GetOrderIndexOk() (*int32, bool)`

GetOrderIndexOk returns a tuple with the OrderIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrderIndex

`func (o *FlowStep) SetOrderIndex(v int32)`

SetOrderIndex sets OrderIndex field to given value.


### GetFlowName

`func (o *FlowStep) GetFlowName() string`

GetFlowName returns the FlowName field if non-nil, zero value otherwise.

### GetFlowNameOk

`func (o *FlowStep) GetFlowNameOk() (*string, bool)`

GetFlowNameOk returns a tuple with the FlowName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlowName

`func (o *FlowStep) SetFlowName(v string)`

SetFlowName sets FlowName field to given value.

### HasFlowName

`func (o *FlowStep) HasFlowName() bool`

HasFlowName returns a boolean if a field has been set.

### SetFlowNameNil

`func (o *FlowStep) SetFlowNameNil(b bool)`

 SetFlowNameNil sets the value for FlowName to be an explicit nil

### UnsetFlowName
`func (o *FlowStep) UnsetFlowName()`

UnsetFlowName ensures that no value is present for FlowName, not even an explicit nil
### GetStepType

`func (o *FlowStep) GetStepType() string`

GetStepType returns the StepType field if non-nil, zero value otherwise.

### GetStepTypeOk

`func (o *FlowStep) GetStepTypeOk() (*string, bool)`

GetStepTypeOk returns a tuple with the StepType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepType

`func (o *FlowStep) SetStepType(v string)`

SetStepType sets StepType field to given value.


### GetSpecId

`func (o *FlowStep) GetSpecId() string`

GetSpecId returns the SpecId field if non-nil, zero value otherwise.

### GetSpecIdOk

`func (o *FlowStep) GetSpecIdOk() (*string, bool)`

GetSpecIdOk returns a tuple with the SpecId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecId

`func (o *FlowStep) SetSpecId(v string)`

SetSpecId sets SpecId field to given value.

### HasSpecId

`func (o *FlowStep) HasSpecId() bool`

HasSpecId returns a boolean if a field has been set.

### SetSpecIdNil

`func (o *FlowStep) SetSpecIdNil(b bool)`

 SetSpecIdNil sets the value for SpecId to be an explicit nil

### UnsetSpecId
`func (o *FlowStep) UnsetSpecId()`

UnsetSpecId ensures that no value is present for SpecId, not even an explicit nil
### GetSpecType

`func (o *FlowStep) GetSpecType() SpecType`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *FlowStep) GetSpecTypeOk() (*SpecType, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *FlowStep) SetSpecType(v SpecType)`

SetSpecType sets SpecType field to given value.

### HasSpecType

`func (o *FlowStep) HasSpecType() bool`

HasSpecType returns a boolean if a field has been set.

### SetSpecTypeNil

`func (o *FlowStep) SetSpecTypeNil(b bool)`

 SetSpecTypeNil sets the value for SpecType to be an explicit nil

### UnsetSpecType
`func (o *FlowStep) UnsetSpecType()`

UnsetSpecType ensures that no value is present for SpecType, not even an explicit nil
### GetSpecName

`func (o *FlowStep) GetSpecName() string`

GetSpecName returns the SpecName field if non-nil, zero value otherwise.

### GetSpecNameOk

`func (o *FlowStep) GetSpecNameOk() (*string, bool)`

GetSpecNameOk returns a tuple with the SpecName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecName

`func (o *FlowStep) SetSpecName(v string)`

SetSpecName sets SpecName field to given value.

### HasSpecName

`func (o *FlowStep) HasSpecName() bool`

HasSpecName returns a boolean if a field has been set.

### SetSpecNameNil

`func (o *FlowStep) SetSpecNameNil(b bool)`

 SetSpecNameNil sets the value for SpecName to be an explicit nil

### UnsetSpecName
`func (o *FlowStep) UnsetSpecName()`

UnsetSpecName ensures that no value is present for SpecName, not even an explicit nil
### GetUiMacroId

`func (o *FlowStep) GetUiMacroId() string`

GetUiMacroId returns the UiMacroId field if non-nil, zero value otherwise.

### GetUiMacroIdOk

`func (o *FlowStep) GetUiMacroIdOk() (*string, bool)`

GetUiMacroIdOk returns a tuple with the UiMacroId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiMacroId

`func (o *FlowStep) SetUiMacroId(v string)`

SetUiMacroId sets UiMacroId field to given value.

### HasUiMacroId

`func (o *FlowStep) HasUiMacroId() bool`

HasUiMacroId returns a boolean if a field has been set.

### SetUiMacroIdNil

`func (o *FlowStep) SetUiMacroIdNil(b bool)`

 SetUiMacroIdNil sets the value for UiMacroId to be an explicit nil

### UnsetUiMacroId
`func (o *FlowStep) UnsetUiMacroId()`

UnsetUiMacroId ensures that no value is present for UiMacroId, not even an explicit nil
### GetUiMacroName

`func (o *FlowStep) GetUiMacroName() string`

GetUiMacroName returns the UiMacroName field if non-nil, zero value otherwise.

### GetUiMacroNameOk

`func (o *FlowStep) GetUiMacroNameOk() (*string, bool)`

GetUiMacroNameOk returns a tuple with the UiMacroName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiMacroName

`func (o *FlowStep) SetUiMacroName(v string)`

SetUiMacroName sets UiMacroName field to given value.

### HasUiMacroName

`func (o *FlowStep) HasUiMacroName() bool`

HasUiMacroName returns a boolean if a field has been set.

### SetUiMacroNameNil

`func (o *FlowStep) SetUiMacroNameNil(b bool)`

 SetUiMacroNameNil sets the value for UiMacroName to be an explicit nil

### UnsetUiMacroName
`func (o *FlowStep) UnsetUiMacroName()`

UnsetUiMacroName ensures that no value is present for UiMacroName, not even an explicit nil
### GetBrowserActionType

`func (o *FlowStep) GetBrowserActionType() BrowserActionType`

GetBrowserActionType returns the BrowserActionType field if non-nil, zero value otherwise.

### GetBrowserActionTypeOk

`func (o *FlowStep) GetBrowserActionTypeOk() (*BrowserActionType, bool)`

GetBrowserActionTypeOk returns a tuple with the BrowserActionType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrowserActionType

`func (o *FlowStep) SetBrowserActionType(v BrowserActionType)`

SetBrowserActionType sets BrowserActionType field to given value.

### HasBrowserActionType

`func (o *FlowStep) HasBrowserActionType() bool`

HasBrowserActionType returns a boolean if a field has been set.

### SetBrowserActionTypeNil

`func (o *FlowStep) SetBrowserActionTypeNil(b bool)`

 SetBrowserActionTypeNil sets the value for BrowserActionType to be an explicit nil

### UnsetBrowserActionType
`func (o *FlowStep) UnsetBrowserActionType()`

UnsetBrowserActionType ensures that no value is present for BrowserActionType, not even an explicit nil
### GetSelector

`func (o *FlowStep) GetSelector() string`

GetSelector returns the Selector field if non-nil, zero value otherwise.

### GetSelectorOk

`func (o *FlowStep) GetSelectorOk() (*string, bool)`

GetSelectorOk returns a tuple with the Selector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelector

`func (o *FlowStep) SetSelector(v string)`

SetSelector sets Selector field to given value.

### HasSelector

`func (o *FlowStep) HasSelector() bool`

HasSelector returns a boolean if a field has been set.

### SetSelectorNil

`func (o *FlowStep) SetSelectorNil(b bool)`

 SetSelectorNil sets the value for Selector to be an explicit nil

### UnsetSelector
`func (o *FlowStep) UnsetSelector()`

UnsetSelector ensures that no value is present for Selector, not even an explicit nil
### GetSelectorCandidates

`func (o *FlowStep) GetSelectorCandidates() []string`

GetSelectorCandidates returns the SelectorCandidates field if non-nil, zero value otherwise.

### GetSelectorCandidatesOk

`func (o *FlowStep) GetSelectorCandidatesOk() (*[]string, bool)`

GetSelectorCandidatesOk returns a tuple with the SelectorCandidates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelectorCandidates

`func (o *FlowStep) SetSelectorCandidates(v []string)`

SetSelectorCandidates sets SelectorCandidates field to given value.

### HasSelectorCandidates

`func (o *FlowStep) HasSelectorCandidates() bool`

HasSelectorCandidates returns a boolean if a field has been set.

### GetValue

`func (o *FlowStep) GetValue() string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *FlowStep) GetValueOk() (*string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *FlowStep) SetValue(v string)`

SetValue sets Value field to given value.

### HasValue

`func (o *FlowStep) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValueNil

`func (o *FlowStep) SetValueNil(b bool)`

 SetValueNil sets the value for Value to be an explicit nil

### UnsetValue
`func (o *FlowStep) UnsetValue()`

UnsetValue ensures that no value is present for Value, not even an explicit nil
### GetVariableName

`func (o *FlowStep) GetVariableName() string`

GetVariableName returns the VariableName field if non-nil, zero value otherwise.

### GetVariableNameOk

`func (o *FlowStep) GetVariableNameOk() (*string, bool)`

GetVariableNameOk returns a tuple with the VariableName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariableName

`func (o *FlowStep) SetVariableName(v string)`

SetVariableName sets VariableName field to given value.

### HasVariableName

`func (o *FlowStep) HasVariableName() bool`

HasVariableName returns a boolean if a field has been set.

### SetVariableNameNil

`func (o *FlowStep) SetVariableNameNil(b bool)`

 SetVariableNameNil sets the value for VariableName to be an explicit nil

### UnsetVariableName
`func (o *FlowStep) UnsetVariableName()`

UnsetVariableName ensures that no value is present for VariableName, not even an explicit nil
### GetTabAlias

`func (o *FlowStep) GetTabAlias() string`

GetTabAlias returns the TabAlias field if non-nil, zero value otherwise.

### GetTabAliasOk

`func (o *FlowStep) GetTabAliasOk() (*string, bool)`

GetTabAliasOk returns a tuple with the TabAlias field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTabAlias

`func (o *FlowStep) SetTabAlias(v string)`

SetTabAlias sets TabAlias field to given value.

### HasTabAlias

`func (o *FlowStep) HasTabAlias() bool`

HasTabAlias returns a boolean if a field has been set.

### SetTabAliasNil

`func (o *FlowStep) SetTabAliasNil(b bool)`

 SetTabAliasNil sets the value for TabAlias to be an explicit nil

### UnsetTabAlias
`func (o *FlowStep) UnsetTabAlias()`

UnsetTabAlias ensures that no value is present for TabAlias, not even an explicit nil
### GetFrameSelector

`func (o *FlowStep) GetFrameSelector() string`

GetFrameSelector returns the FrameSelector field if non-nil, zero value otherwise.

### GetFrameSelectorOk

`func (o *FlowStep) GetFrameSelectorOk() (*string, bool)`

GetFrameSelectorOk returns a tuple with the FrameSelector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrameSelector

`func (o *FlowStep) SetFrameSelector(v string)`

SetFrameSelector sets FrameSelector field to given value.

### HasFrameSelector

`func (o *FlowStep) HasFrameSelector() bool`

HasFrameSelector returns a boolean if a field has been set.

### SetFrameSelectorNil

`func (o *FlowStep) SetFrameSelectorNil(b bool)`

 SetFrameSelectorNil sets the value for FrameSelector to be an explicit nil

### UnsetFrameSelector
`func (o *FlowStep) UnsetFrameSelector()`

UnsetFrameSelector ensures that no value is present for FrameSelector, not even an explicit nil
### GetPattern

`func (o *FlowStep) GetPattern() string`

GetPattern returns the Pattern field if non-nil, zero value otherwise.

### GetPatternOk

`func (o *FlowStep) GetPatternOk() (*string, bool)`

GetPatternOk returns a tuple with the Pattern field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPattern

`func (o *FlowStep) SetPattern(v string)`

SetPattern sets Pattern field to given value.

### HasPattern

`func (o *FlowStep) HasPattern() bool`

HasPattern returns a boolean if a field has been set.

### SetPatternNil

`func (o *FlowStep) SetPatternNil(b bool)`

 SetPatternNil sets the value for Pattern to be an explicit nil

### UnsetPattern
`func (o *FlowStep) UnsetPattern()`

UnsetPattern ensures that no value is present for Pattern, not even an explicit nil
### GetExtractionHint

`func (o *FlowStep) GetExtractionHint() string`

GetExtractionHint returns the ExtractionHint field if non-nil, zero value otherwise.

### GetExtractionHintOk

`func (o *FlowStep) GetExtractionHintOk() (*string, bool)`

GetExtractionHintOk returns a tuple with the ExtractionHint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtractionHint

`func (o *FlowStep) SetExtractionHint(v string)`

SetExtractionHint sets ExtractionHint field to given value.

### HasExtractionHint

`func (o *FlowStep) HasExtractionHint() bool`

HasExtractionHint returns a boolean if a field has been set.

### SetExtractionHintNil

`func (o *FlowStep) SetExtractionHintNil(b bool)`

 SetExtractionHintNil sets the value for ExtractionHint to be an explicit nil

### UnsetExtractionHint
`func (o *FlowStep) UnsetExtractionHint()`

UnsetExtractionHint ensures that no value is present for ExtractionHint, not even an explicit nil
### GetTextSource

`func (o *FlowStep) GetTextSource() string`

GetTextSource returns the TextSource field if non-nil, zero value otherwise.

### GetTextSourceOk

`func (o *FlowStep) GetTextSourceOk() (*string, bool)`

GetTextSourceOk returns a tuple with the TextSource field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTextSource

`func (o *FlowStep) SetTextSource(v string)`

SetTextSource sets TextSource field to given value.

### HasTextSource

`func (o *FlowStep) HasTextSource() bool`

HasTextSource returns a boolean if a field has been set.

### SetTextSourceNil

`func (o *FlowStep) SetTextSourceNil(b bool)`

 SetTextSourceNil sets the value for TextSource to be an explicit nil

### UnsetTextSource
`func (o *FlowStep) UnsetTextSource()`

UnsetTextSource ensures that no value is present for TextSource, not even an explicit nil
### GetExpectedPageUrl

`func (o *FlowStep) GetExpectedPageUrl() string`

GetExpectedPageUrl returns the ExpectedPageUrl field if non-nil, zero value otherwise.

### GetExpectedPageUrlOk

`func (o *FlowStep) GetExpectedPageUrlOk() (*string, bool)`

GetExpectedPageUrlOk returns a tuple with the ExpectedPageUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedPageUrl

`func (o *FlowStep) SetExpectedPageUrl(v string)`

SetExpectedPageUrl sets ExpectedPageUrl field to given value.

### HasExpectedPageUrl

`func (o *FlowStep) HasExpectedPageUrl() bool`

HasExpectedPageUrl returns a boolean if a field has been set.

### SetExpectedPageUrlNil

`func (o *FlowStep) SetExpectedPageUrlNil(b bool)`

 SetExpectedPageUrlNil sets the value for ExpectedPageUrl to be an explicit nil

### UnsetExpectedPageUrl
`func (o *FlowStep) UnsetExpectedPageUrl()`

UnsetExpectedPageUrl ensures that no value is present for ExpectedPageUrl, not even an explicit nil
### GetExpectedPageUrlPolicy

`func (o *FlowStep) GetExpectedPageUrlPolicy() string`

GetExpectedPageUrlPolicy returns the ExpectedPageUrlPolicy field if non-nil, zero value otherwise.

### GetExpectedPageUrlPolicyOk

`func (o *FlowStep) GetExpectedPageUrlPolicyOk() (*string, bool)`

GetExpectedPageUrlPolicyOk returns a tuple with the ExpectedPageUrlPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedPageUrlPolicy

`func (o *FlowStep) SetExpectedPageUrlPolicy(v string)`

SetExpectedPageUrlPolicy sets ExpectedPageUrlPolicy field to given value.

### HasExpectedPageUrlPolicy

`func (o *FlowStep) HasExpectedPageUrlPolicy() bool`

HasExpectedPageUrlPolicy returns a boolean if a field has been set.

### SetExpectedPageUrlPolicyNil

`func (o *FlowStep) SetExpectedPageUrlPolicyNil(b bool)`

 SetExpectedPageUrlPolicyNil sets the value for ExpectedPageUrlPolicy to be an explicit nil

### UnsetExpectedPageUrlPolicy
`func (o *FlowStep) UnsetExpectedPageUrlPolicy()`

UnsetExpectedPageUrlPolicy ensures that no value is present for ExpectedPageUrlPolicy, not even an explicit nil
### GetExpectedPageTitle

`func (o *FlowStep) GetExpectedPageTitle() string`

GetExpectedPageTitle returns the ExpectedPageTitle field if non-nil, zero value otherwise.

### GetExpectedPageTitleOk

`func (o *FlowStep) GetExpectedPageTitleOk() (*string, bool)`

GetExpectedPageTitleOk returns a tuple with the ExpectedPageTitle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedPageTitle

`func (o *FlowStep) SetExpectedPageTitle(v string)`

SetExpectedPageTitle sets ExpectedPageTitle field to given value.

### HasExpectedPageTitle

`func (o *FlowStep) HasExpectedPageTitle() bool`

HasExpectedPageTitle returns a boolean if a field has been set.

### SetExpectedPageTitleNil

`func (o *FlowStep) SetExpectedPageTitleNil(b bool)`

 SetExpectedPageTitleNil sets the value for ExpectedPageTitle to be an explicit nil

### UnsetExpectedPageTitle
`func (o *FlowStep) UnsetExpectedPageTitle()`

UnsetExpectedPageTitle ensures that no value is present for ExpectedPageTitle, not even an explicit nil
### GetExpectedPageTitlePolicy

`func (o *FlowStep) GetExpectedPageTitlePolicy() string`

GetExpectedPageTitlePolicy returns the ExpectedPageTitlePolicy field if non-nil, zero value otherwise.

### GetExpectedPageTitlePolicyOk

`func (o *FlowStep) GetExpectedPageTitlePolicyOk() (*string, bool)`

GetExpectedPageTitlePolicyOk returns a tuple with the ExpectedPageTitlePolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedPageTitlePolicy

`func (o *FlowStep) SetExpectedPageTitlePolicy(v string)`

SetExpectedPageTitlePolicy sets ExpectedPageTitlePolicy field to given value.

### HasExpectedPageTitlePolicy

`func (o *FlowStep) HasExpectedPageTitlePolicy() bool`

HasExpectedPageTitlePolicy returns a boolean if a field has been set.

### SetExpectedPageTitlePolicyNil

`func (o *FlowStep) SetExpectedPageTitlePolicyNil(b bool)`

 SetExpectedPageTitlePolicyNil sets the value for ExpectedPageTitlePolicy to be an explicit nil

### UnsetExpectedPageTitlePolicy
`func (o *FlowStep) UnsetExpectedPageTitlePolicy()`

UnsetExpectedPageTitlePolicy ensures that no value is present for ExpectedPageTitlePolicy, not even an explicit nil
### GetExpectedNetworkPolicy

`func (o *FlowStep) GetExpectedNetworkPolicy() string`

GetExpectedNetworkPolicy returns the ExpectedNetworkPolicy field if non-nil, zero value otherwise.

### GetExpectedNetworkPolicyOk

`func (o *FlowStep) GetExpectedNetworkPolicyOk() (*string, bool)`

GetExpectedNetworkPolicyOk returns a tuple with the ExpectedNetworkPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedNetworkPolicy

`func (o *FlowStep) SetExpectedNetworkPolicy(v string)`

SetExpectedNetworkPolicy sets ExpectedNetworkPolicy field to given value.

### HasExpectedNetworkPolicy

`func (o *FlowStep) HasExpectedNetworkPolicy() bool`

HasExpectedNetworkPolicy returns a boolean if a field has been set.

### SetExpectedNetworkPolicyNil

`func (o *FlowStep) SetExpectedNetworkPolicyNil(b bool)`

 SetExpectedNetworkPolicyNil sets the value for ExpectedNetworkPolicy to be an explicit nil

### UnsetExpectedNetworkPolicy
`func (o *FlowStep) UnsetExpectedNetworkPolicy()`

UnsetExpectedNetworkPolicy ensures that no value is present for ExpectedNetworkPolicy, not even an explicit nil
### GetVisualAssertion

`func (o *FlowStep) GetVisualAssertion() BrowserVisualAssertion`

GetVisualAssertion returns the VisualAssertion field if non-nil, zero value otherwise.

### GetVisualAssertionOk

`func (o *FlowStep) GetVisualAssertionOk() (*BrowserVisualAssertion, bool)`

GetVisualAssertionOk returns a tuple with the VisualAssertion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVisualAssertion

`func (o *FlowStep) SetVisualAssertion(v BrowserVisualAssertion)`

SetVisualAssertion sets VisualAssertion field to given value.

### HasVisualAssertion

`func (o *FlowStep) HasVisualAssertion() bool`

HasVisualAssertion returns a boolean if a field has been set.

### SetVisualAssertionNil

`func (o *FlowStep) SetVisualAssertionNil(b bool)`

 SetVisualAssertionNil sets the value for VisualAssertion to be an explicit nil

### UnsetVisualAssertion
`func (o *FlowStep) UnsetVisualAssertion()`

UnsetVisualAssertion ensures that no value is present for VisualAssertion, not even an explicit nil
### GetExpectedNetworkCalls

`func (o *FlowStep) GetExpectedNetworkCalls() []BrowserNetworkExpectation`

GetExpectedNetworkCalls returns the ExpectedNetworkCalls field if non-nil, zero value otherwise.

### GetExpectedNetworkCallsOk

`func (o *FlowStep) GetExpectedNetworkCallsOk() (*[]BrowserNetworkExpectation, bool)`

GetExpectedNetworkCallsOk returns a tuple with the ExpectedNetworkCalls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedNetworkCalls

`func (o *FlowStep) SetExpectedNetworkCalls(v []BrowserNetworkExpectation)`

SetExpectedNetworkCalls sets ExpectedNetworkCalls field to given value.

### HasExpectedNetworkCalls

`func (o *FlowStep) HasExpectedNetworkCalls() bool`

HasExpectedNetworkCalls returns a boolean if a field has been set.

### GetStoreValues

`func (o *FlowStep) GetStoreValues() map[string]string`

GetStoreValues returns the StoreValues field if non-nil, zero value otherwise.

### GetStoreValuesOk

`func (o *FlowStep) GetStoreValuesOk() (*map[string]string, bool)`

GetStoreValuesOk returns a tuple with the StoreValues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStoreValues

`func (o *FlowStep) SetStoreValues(v map[string]string)`

SetStoreValues sets StoreValues field to given value.

### HasStoreValues

`func (o *FlowStep) HasStoreValues() bool`

HasStoreValues returns a boolean if a field has been set.

### GetOverrideValues

`func (o *FlowStep) GetOverrideValues() map[string]interface{}`

GetOverrideValues returns the OverrideValues field if non-nil, zero value otherwise.

### GetOverrideValuesOk

`func (o *FlowStep) GetOverrideValuesOk() (*map[string]interface{}, bool)`

GetOverrideValuesOk returns a tuple with the OverrideValues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOverrideValues

`func (o *FlowStep) SetOverrideValues(v map[string]interface{})`

SetOverrideValues sets OverrideValues field to given value.

### HasOverrideValues

`func (o *FlowStep) HasOverrideValues() bool`

HasOverrideValues returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


