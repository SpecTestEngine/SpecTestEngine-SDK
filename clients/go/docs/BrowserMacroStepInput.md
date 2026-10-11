# BrowserMacroStepInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OrderIndex** | Pointer to **int32** |  | [optional]
**ActionType** | [**BrowserActionType**](BrowserActionType.md) |  |
**Selector** | Pointer to **string** |  | [optional]
**SelectorCandidates** | Pointer to **[]string** |  | [optional]
**Value** | Pointer to **string** | Action value or explicit variable template. EXTRACT_TEXT captures a fresh value on every run; a later FILL uses that variable, never a recorded OTP sample. | [optional]
**Sensitive** | Pointer to **bool** | Explicit sensitive-action marker. Persist variable references, not secret literal values. | [optional]
**TimeoutMs** | Pointer to **int64** |  | [optional] [default to 20000]
**TabAlias** | Pointer to **string** |  | [optional]
**FrameSelector** | Pointer to **string** |  | [optional]
**VariableName** | Pointer to **string** |  | [optional]
**Pattern** | Pointer to **string** |  | [optional]
**ExtractionHint** | Pointer to **string** |  | [optional]
**TextSource** | Pointer to **string** |  | [optional]
**ExpectedPageUrl** | Pointer to **string** |  | [optional]
**ExpectedPageUrlPolicy** | Pointer to **string** |  | [optional]
**ExpectedPageTitle** | Pointer to **string** |  | [optional]
**ExpectedPageTitlePolicy** | Pointer to **string** |  | [optional]
**ExpectedNetworkPolicy** | Pointer to **string** |  | [optional]
**ExpectedNetworkCalls** | Pointer to [**[]BrowserNetworkExpectation**](BrowserNetworkExpectation.md) |  | [optional]
**VisualAssertion** | Pointer to [**NullableBrowserVisualAssertionInput**](BrowserVisualAssertionInput.md) |  | [optional]
**PageId** | Pointer to **string** |  | [optional]

## Methods

### NewBrowserMacroStepInput

`func NewBrowserMacroStepInput(actionType BrowserActionType, ) *BrowserMacroStepInput`

NewBrowserMacroStepInput instantiates a new BrowserMacroStepInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserMacroStepInputWithDefaults

`func NewBrowserMacroStepInputWithDefaults() *BrowserMacroStepInput`

NewBrowserMacroStepInputWithDefaults instantiates a new BrowserMacroStepInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOrderIndex

`func (o *BrowserMacroStepInput) GetOrderIndex() int32`

GetOrderIndex returns the OrderIndex field if non-nil, zero value otherwise.

### GetOrderIndexOk

`func (o *BrowserMacroStepInput) GetOrderIndexOk() (*int32, bool)`

GetOrderIndexOk returns a tuple with the OrderIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrderIndex

`func (o *BrowserMacroStepInput) SetOrderIndex(v int32)`

SetOrderIndex sets OrderIndex field to given value.

### HasOrderIndex

`func (o *BrowserMacroStepInput) HasOrderIndex() bool`

HasOrderIndex returns a boolean if a field has been set.

### GetActionType

`func (o *BrowserMacroStepInput) GetActionType() BrowserActionType`

GetActionType returns the ActionType field if non-nil, zero value otherwise.

### GetActionTypeOk

`func (o *BrowserMacroStepInput) GetActionTypeOk() (*BrowserActionType, bool)`

GetActionTypeOk returns a tuple with the ActionType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActionType

`func (o *BrowserMacroStepInput) SetActionType(v BrowserActionType)`

SetActionType sets ActionType field to given value.


### GetSelector

`func (o *BrowserMacroStepInput) GetSelector() string`

GetSelector returns the Selector field if non-nil, zero value otherwise.

### GetSelectorOk

`func (o *BrowserMacroStepInput) GetSelectorOk() (*string, bool)`

GetSelectorOk returns a tuple with the Selector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelector

`func (o *BrowserMacroStepInput) SetSelector(v string)`

SetSelector sets Selector field to given value.

### HasSelector

`func (o *BrowserMacroStepInput) HasSelector() bool`

HasSelector returns a boolean if a field has been set.

### GetSelectorCandidates

`func (o *BrowserMacroStepInput) GetSelectorCandidates() []string`

GetSelectorCandidates returns the SelectorCandidates field if non-nil, zero value otherwise.

### GetSelectorCandidatesOk

`func (o *BrowserMacroStepInput) GetSelectorCandidatesOk() (*[]string, bool)`

GetSelectorCandidatesOk returns a tuple with the SelectorCandidates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelectorCandidates

`func (o *BrowserMacroStepInput) SetSelectorCandidates(v []string)`

SetSelectorCandidates sets SelectorCandidates field to given value.

### HasSelectorCandidates

`func (o *BrowserMacroStepInput) HasSelectorCandidates() bool`

HasSelectorCandidates returns a boolean if a field has been set.

### GetValue

`func (o *BrowserMacroStepInput) GetValue() string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *BrowserMacroStepInput) GetValueOk() (*string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *BrowserMacroStepInput) SetValue(v string)`

SetValue sets Value field to given value.

### HasValue

`func (o *BrowserMacroStepInput) HasValue() bool`

HasValue returns a boolean if a field has been set.

### GetSensitive

`func (o *BrowserMacroStepInput) GetSensitive() bool`

GetSensitive returns the Sensitive field if non-nil, zero value otherwise.

### GetSensitiveOk

`func (o *BrowserMacroStepInput) GetSensitiveOk() (*bool, bool)`

GetSensitiveOk returns a tuple with the Sensitive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSensitive

`func (o *BrowserMacroStepInput) SetSensitive(v bool)`

SetSensitive sets Sensitive field to given value.

### HasSensitive

`func (o *BrowserMacroStepInput) HasSensitive() bool`

HasSensitive returns a boolean if a field has been set.

### GetTimeoutMs

`func (o *BrowserMacroStepInput) GetTimeoutMs() int64`

GetTimeoutMs returns the TimeoutMs field if non-nil, zero value otherwise.

### GetTimeoutMsOk

`func (o *BrowserMacroStepInput) GetTimeoutMsOk() (*int64, bool)`

GetTimeoutMsOk returns a tuple with the TimeoutMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimeoutMs

`func (o *BrowserMacroStepInput) SetTimeoutMs(v int64)`

SetTimeoutMs sets TimeoutMs field to given value.

### HasTimeoutMs

`func (o *BrowserMacroStepInput) HasTimeoutMs() bool`

HasTimeoutMs returns a boolean if a field has been set.

### GetTabAlias

`func (o *BrowserMacroStepInput) GetTabAlias() string`

GetTabAlias returns the TabAlias field if non-nil, zero value otherwise.

### GetTabAliasOk

`func (o *BrowserMacroStepInput) GetTabAliasOk() (*string, bool)`

GetTabAliasOk returns a tuple with the TabAlias field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTabAlias

`func (o *BrowserMacroStepInput) SetTabAlias(v string)`

SetTabAlias sets TabAlias field to given value.

### HasTabAlias

`func (o *BrowserMacroStepInput) HasTabAlias() bool`

HasTabAlias returns a boolean if a field has been set.

### GetFrameSelector

`func (o *BrowserMacroStepInput) GetFrameSelector() string`

GetFrameSelector returns the FrameSelector field if non-nil, zero value otherwise.

### GetFrameSelectorOk

`func (o *BrowserMacroStepInput) GetFrameSelectorOk() (*string, bool)`

GetFrameSelectorOk returns a tuple with the FrameSelector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrameSelector

`func (o *BrowserMacroStepInput) SetFrameSelector(v string)`

SetFrameSelector sets FrameSelector field to given value.

### HasFrameSelector

`func (o *BrowserMacroStepInput) HasFrameSelector() bool`

HasFrameSelector returns a boolean if a field has been set.

### GetVariableName

`func (o *BrowserMacroStepInput) GetVariableName() string`

GetVariableName returns the VariableName field if non-nil, zero value otherwise.

### GetVariableNameOk

`func (o *BrowserMacroStepInput) GetVariableNameOk() (*string, bool)`

GetVariableNameOk returns a tuple with the VariableName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariableName

`func (o *BrowserMacroStepInput) SetVariableName(v string)`

SetVariableName sets VariableName field to given value.

### HasVariableName

`func (o *BrowserMacroStepInput) HasVariableName() bool`

HasVariableName returns a boolean if a field has been set.

### GetPattern

`func (o *BrowserMacroStepInput) GetPattern() string`

GetPattern returns the Pattern field if non-nil, zero value otherwise.

### GetPatternOk

`func (o *BrowserMacroStepInput) GetPatternOk() (*string, bool)`

GetPatternOk returns a tuple with the Pattern field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPattern

`func (o *BrowserMacroStepInput) SetPattern(v string)`

SetPattern sets Pattern field to given value.

### HasPattern

`func (o *BrowserMacroStepInput) HasPattern() bool`

HasPattern returns a boolean if a field has been set.

### GetExtractionHint

`func (o *BrowserMacroStepInput) GetExtractionHint() string`

GetExtractionHint returns the ExtractionHint field if non-nil, zero value otherwise.

### GetExtractionHintOk

`func (o *BrowserMacroStepInput) GetExtractionHintOk() (*string, bool)`

GetExtractionHintOk returns a tuple with the ExtractionHint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtractionHint

`func (o *BrowserMacroStepInput) SetExtractionHint(v string)`

SetExtractionHint sets ExtractionHint field to given value.

### HasExtractionHint

`func (o *BrowserMacroStepInput) HasExtractionHint() bool`

HasExtractionHint returns a boolean if a field has been set.

### GetTextSource

`func (o *BrowserMacroStepInput) GetTextSource() string`

GetTextSource returns the TextSource field if non-nil, zero value otherwise.

### GetTextSourceOk

`func (o *BrowserMacroStepInput) GetTextSourceOk() (*string, bool)`

GetTextSourceOk returns a tuple with the TextSource field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTextSource

`func (o *BrowserMacroStepInput) SetTextSource(v string)`

SetTextSource sets TextSource field to given value.

### HasTextSource

`func (o *BrowserMacroStepInput) HasTextSource() bool`

HasTextSource returns a boolean if a field has been set.

### GetExpectedPageUrl

`func (o *BrowserMacroStepInput) GetExpectedPageUrl() string`

GetExpectedPageUrl returns the ExpectedPageUrl field if non-nil, zero value otherwise.

### GetExpectedPageUrlOk

`func (o *BrowserMacroStepInput) GetExpectedPageUrlOk() (*string, bool)`

GetExpectedPageUrlOk returns a tuple with the ExpectedPageUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedPageUrl

`func (o *BrowserMacroStepInput) SetExpectedPageUrl(v string)`

SetExpectedPageUrl sets ExpectedPageUrl field to given value.

### HasExpectedPageUrl

`func (o *BrowserMacroStepInput) HasExpectedPageUrl() bool`

HasExpectedPageUrl returns a boolean if a field has been set.

### GetExpectedPageUrlPolicy

`func (o *BrowserMacroStepInput) GetExpectedPageUrlPolicy() string`

GetExpectedPageUrlPolicy returns the ExpectedPageUrlPolicy field if non-nil, zero value otherwise.

### GetExpectedPageUrlPolicyOk

`func (o *BrowserMacroStepInput) GetExpectedPageUrlPolicyOk() (*string, bool)`

GetExpectedPageUrlPolicyOk returns a tuple with the ExpectedPageUrlPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedPageUrlPolicy

`func (o *BrowserMacroStepInput) SetExpectedPageUrlPolicy(v string)`

SetExpectedPageUrlPolicy sets ExpectedPageUrlPolicy field to given value.

### HasExpectedPageUrlPolicy

`func (o *BrowserMacroStepInput) HasExpectedPageUrlPolicy() bool`

HasExpectedPageUrlPolicy returns a boolean if a field has been set.

### GetExpectedPageTitle

`func (o *BrowserMacroStepInput) GetExpectedPageTitle() string`

GetExpectedPageTitle returns the ExpectedPageTitle field if non-nil, zero value otherwise.

### GetExpectedPageTitleOk

`func (o *BrowserMacroStepInput) GetExpectedPageTitleOk() (*string, bool)`

GetExpectedPageTitleOk returns a tuple with the ExpectedPageTitle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedPageTitle

`func (o *BrowserMacroStepInput) SetExpectedPageTitle(v string)`

SetExpectedPageTitle sets ExpectedPageTitle field to given value.

### HasExpectedPageTitle

`func (o *BrowserMacroStepInput) HasExpectedPageTitle() bool`

HasExpectedPageTitle returns a boolean if a field has been set.

### GetExpectedPageTitlePolicy

`func (o *BrowserMacroStepInput) GetExpectedPageTitlePolicy() string`

GetExpectedPageTitlePolicy returns the ExpectedPageTitlePolicy field if non-nil, zero value otherwise.

### GetExpectedPageTitlePolicyOk

`func (o *BrowserMacroStepInput) GetExpectedPageTitlePolicyOk() (*string, bool)`

GetExpectedPageTitlePolicyOk returns a tuple with the ExpectedPageTitlePolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedPageTitlePolicy

`func (o *BrowserMacroStepInput) SetExpectedPageTitlePolicy(v string)`

SetExpectedPageTitlePolicy sets ExpectedPageTitlePolicy field to given value.

### HasExpectedPageTitlePolicy

`func (o *BrowserMacroStepInput) HasExpectedPageTitlePolicy() bool`

HasExpectedPageTitlePolicy returns a boolean if a field has been set.

### GetExpectedNetworkPolicy

`func (o *BrowserMacroStepInput) GetExpectedNetworkPolicy() string`

GetExpectedNetworkPolicy returns the ExpectedNetworkPolicy field if non-nil, zero value otherwise.

### GetExpectedNetworkPolicyOk

`func (o *BrowserMacroStepInput) GetExpectedNetworkPolicyOk() (*string, bool)`

GetExpectedNetworkPolicyOk returns a tuple with the ExpectedNetworkPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedNetworkPolicy

`func (o *BrowserMacroStepInput) SetExpectedNetworkPolicy(v string)`

SetExpectedNetworkPolicy sets ExpectedNetworkPolicy field to given value.

### HasExpectedNetworkPolicy

`func (o *BrowserMacroStepInput) HasExpectedNetworkPolicy() bool`

HasExpectedNetworkPolicy returns a boolean if a field has been set.

### GetExpectedNetworkCalls

`func (o *BrowserMacroStepInput) GetExpectedNetworkCalls() []BrowserNetworkExpectation`

GetExpectedNetworkCalls returns the ExpectedNetworkCalls field if non-nil, zero value otherwise.

### GetExpectedNetworkCallsOk

`func (o *BrowserMacroStepInput) GetExpectedNetworkCallsOk() (*[]BrowserNetworkExpectation, bool)`

GetExpectedNetworkCallsOk returns a tuple with the ExpectedNetworkCalls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedNetworkCalls

`func (o *BrowserMacroStepInput) SetExpectedNetworkCalls(v []BrowserNetworkExpectation)`

SetExpectedNetworkCalls sets ExpectedNetworkCalls field to given value.

### HasExpectedNetworkCalls

`func (o *BrowserMacroStepInput) HasExpectedNetworkCalls() bool`

HasExpectedNetworkCalls returns a boolean if a field has been set.

### GetVisualAssertion

`func (o *BrowserMacroStepInput) GetVisualAssertion() BrowserVisualAssertionInput`

GetVisualAssertion returns the VisualAssertion field if non-nil, zero value otherwise.

### GetVisualAssertionOk

`func (o *BrowserMacroStepInput) GetVisualAssertionOk() (*BrowserVisualAssertionInput, bool)`

GetVisualAssertionOk returns a tuple with the VisualAssertion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVisualAssertion

`func (o *BrowserMacroStepInput) SetVisualAssertion(v BrowserVisualAssertionInput)`

SetVisualAssertion sets VisualAssertion field to given value.

### HasVisualAssertion

`func (o *BrowserMacroStepInput) HasVisualAssertion() bool`

HasVisualAssertion returns a boolean if a field has been set.

### SetVisualAssertionNil

`func (o *BrowserMacroStepInput) SetVisualAssertionNil(b bool)`

 SetVisualAssertionNil sets the value for VisualAssertion to be an explicit nil

### UnsetVisualAssertion
`func (o *BrowserMacroStepInput) UnsetVisualAssertion()`

UnsetVisualAssertion ensures that no value is present for VisualAssertion, not even an explicit nil
### GetPageId

`func (o *BrowserMacroStepInput) GetPageId() string`

GetPageId returns the PageId field if non-nil, zero value otherwise.

### GetPageIdOk

`func (o *BrowserMacroStepInput) GetPageIdOk() (*string, bool)`

GetPageIdOk returns a tuple with the PageId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPageId

`func (o *BrowserMacroStepInput) SetPageId(v string)`

SetPageId sets PageId field to given value.

### HasPageId

`func (o *BrowserMacroStepInput) HasPageId() bool`

HasPageId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
