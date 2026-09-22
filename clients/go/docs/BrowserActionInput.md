# BrowserActionInput

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

## Methods

### NewBrowserActionInput

`func NewBrowserActionInput(actionType BrowserActionType, ) *BrowserActionInput`

NewBrowserActionInput instantiates a new BrowserActionInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrowserActionInputWithDefaults

`func NewBrowserActionInputWithDefaults() *BrowserActionInput`

NewBrowserActionInputWithDefaults instantiates a new BrowserActionInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOrderIndex

`func (o *BrowserActionInput) GetOrderIndex() int32`

GetOrderIndex returns the OrderIndex field if non-nil, zero value otherwise.

### GetOrderIndexOk

`func (o *BrowserActionInput) GetOrderIndexOk() (*int32, bool)`

GetOrderIndexOk returns a tuple with the OrderIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrderIndex

`func (o *BrowserActionInput) SetOrderIndex(v int32)`

SetOrderIndex sets OrderIndex field to given value.

### HasOrderIndex

`func (o *BrowserActionInput) HasOrderIndex() bool`

HasOrderIndex returns a boolean if a field has been set.

### GetActionType

`func (o *BrowserActionInput) GetActionType() BrowserActionType`

GetActionType returns the ActionType field if non-nil, zero value otherwise.

### GetActionTypeOk

`func (o *BrowserActionInput) GetActionTypeOk() (*BrowserActionType, bool)`

GetActionTypeOk returns a tuple with the ActionType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActionType

`func (o *BrowserActionInput) SetActionType(v BrowserActionType)`

SetActionType sets ActionType field to given value.


### GetSelector

`func (o *BrowserActionInput) GetSelector() string`

GetSelector returns the Selector field if non-nil, zero value otherwise.

### GetSelectorOk

`func (o *BrowserActionInput) GetSelectorOk() (*string, bool)`

GetSelectorOk returns a tuple with the Selector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelector

`func (o *BrowserActionInput) SetSelector(v string)`

SetSelector sets Selector field to given value.

### HasSelector

`func (o *BrowserActionInput) HasSelector() bool`

HasSelector returns a boolean if a field has been set.

### GetSelectorCandidates

`func (o *BrowserActionInput) GetSelectorCandidates() []string`

GetSelectorCandidates returns the SelectorCandidates field if non-nil, zero value otherwise.

### GetSelectorCandidatesOk

`func (o *BrowserActionInput) GetSelectorCandidatesOk() (*[]string, bool)`

GetSelectorCandidatesOk returns a tuple with the SelectorCandidates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelectorCandidates

`func (o *BrowserActionInput) SetSelectorCandidates(v []string)`

SetSelectorCandidates sets SelectorCandidates field to given value.

### HasSelectorCandidates

`func (o *BrowserActionInput) HasSelectorCandidates() bool`

HasSelectorCandidates returns a boolean if a field has been set.

### GetValue

`func (o *BrowserActionInput) GetValue() string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *BrowserActionInput) GetValueOk() (*string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *BrowserActionInput) SetValue(v string)`

SetValue sets Value field to given value.

### HasValue

`func (o *BrowserActionInput) HasValue() bool`

HasValue returns a boolean if a field has been set.

### GetSensitive

`func (o *BrowserActionInput) GetSensitive() bool`

GetSensitive returns the Sensitive field if non-nil, zero value otherwise.

### GetSensitiveOk

`func (o *BrowserActionInput) GetSensitiveOk() (*bool, bool)`

GetSensitiveOk returns a tuple with the Sensitive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSensitive

`func (o *BrowserActionInput) SetSensitive(v bool)`

SetSensitive sets Sensitive field to given value.

### HasSensitive

`func (o *BrowserActionInput) HasSensitive() bool`

HasSensitive returns a boolean if a field has been set.

### GetTimeoutMs

`func (o *BrowserActionInput) GetTimeoutMs() int64`

GetTimeoutMs returns the TimeoutMs field if non-nil, zero value otherwise.

### GetTimeoutMsOk

`func (o *BrowserActionInput) GetTimeoutMsOk() (*int64, bool)`

GetTimeoutMsOk returns a tuple with the TimeoutMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimeoutMs

`func (o *BrowserActionInput) SetTimeoutMs(v int64)`

SetTimeoutMs sets TimeoutMs field to given value.

### HasTimeoutMs

`func (o *BrowserActionInput) HasTimeoutMs() bool`

HasTimeoutMs returns a boolean if a field has been set.

### GetTabAlias

`func (o *BrowserActionInput) GetTabAlias() string`

GetTabAlias returns the TabAlias field if non-nil, zero value otherwise.

### GetTabAliasOk

`func (o *BrowserActionInput) GetTabAliasOk() (*string, bool)`

GetTabAliasOk returns a tuple with the TabAlias field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTabAlias

`func (o *BrowserActionInput) SetTabAlias(v string)`

SetTabAlias sets TabAlias field to given value.

### HasTabAlias

`func (o *BrowserActionInput) HasTabAlias() bool`

HasTabAlias returns a boolean if a field has been set.

### GetFrameSelector

`func (o *BrowserActionInput) GetFrameSelector() string`

GetFrameSelector returns the FrameSelector field if non-nil, zero value otherwise.

### GetFrameSelectorOk

`func (o *BrowserActionInput) GetFrameSelectorOk() (*string, bool)`

GetFrameSelectorOk returns a tuple with the FrameSelector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrameSelector

`func (o *BrowserActionInput) SetFrameSelector(v string)`

SetFrameSelector sets FrameSelector field to given value.

### HasFrameSelector

`func (o *BrowserActionInput) HasFrameSelector() bool`

HasFrameSelector returns a boolean if a field has been set.

### GetVariableName

`func (o *BrowserActionInput) GetVariableName() string`

GetVariableName returns the VariableName field if non-nil, zero value otherwise.

### GetVariableNameOk

`func (o *BrowserActionInput) GetVariableNameOk() (*string, bool)`

GetVariableNameOk returns a tuple with the VariableName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariableName

`func (o *BrowserActionInput) SetVariableName(v string)`

SetVariableName sets VariableName field to given value.

### HasVariableName

`func (o *BrowserActionInput) HasVariableName() bool`

HasVariableName returns a boolean if a field has been set.

### GetPattern

`func (o *BrowserActionInput) GetPattern() string`

GetPattern returns the Pattern field if non-nil, zero value otherwise.

### GetPatternOk

`func (o *BrowserActionInput) GetPatternOk() (*string, bool)`

GetPatternOk returns a tuple with the Pattern field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPattern

`func (o *BrowserActionInput) SetPattern(v string)`

SetPattern sets Pattern field to given value.

### HasPattern

`func (o *BrowserActionInput) HasPattern() bool`

HasPattern returns a boolean if a field has been set.

### GetExtractionHint

`func (o *BrowserActionInput) GetExtractionHint() string`

GetExtractionHint returns the ExtractionHint field if non-nil, zero value otherwise.

### GetExtractionHintOk

`func (o *BrowserActionInput) GetExtractionHintOk() (*string, bool)`

GetExtractionHintOk returns a tuple with the ExtractionHint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtractionHint

`func (o *BrowserActionInput) SetExtractionHint(v string)`

SetExtractionHint sets ExtractionHint field to given value.

### HasExtractionHint

`func (o *BrowserActionInput) HasExtractionHint() bool`

HasExtractionHint returns a boolean if a field has been set.

### GetTextSource

`func (o *BrowserActionInput) GetTextSource() string`

GetTextSource returns the TextSource field if non-nil, zero value otherwise.

### GetTextSourceOk

`func (o *BrowserActionInput) GetTextSourceOk() (*string, bool)`

GetTextSourceOk returns a tuple with the TextSource field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTextSource

`func (o *BrowserActionInput) SetTextSource(v string)`

SetTextSource sets TextSource field to given value.

### HasTextSource

`func (o *BrowserActionInput) HasTextSource() bool`

HasTextSource returns a boolean if a field has been set.

### GetExpectedPageUrl

`func (o *BrowserActionInput) GetExpectedPageUrl() string`

GetExpectedPageUrl returns the ExpectedPageUrl field if non-nil, zero value otherwise.

### GetExpectedPageUrlOk

`func (o *BrowserActionInput) GetExpectedPageUrlOk() (*string, bool)`

GetExpectedPageUrlOk returns a tuple with the ExpectedPageUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedPageUrl

`func (o *BrowserActionInput) SetExpectedPageUrl(v string)`

SetExpectedPageUrl sets ExpectedPageUrl field to given value.

### HasExpectedPageUrl

`func (o *BrowserActionInput) HasExpectedPageUrl() bool`

HasExpectedPageUrl returns a boolean if a field has been set.

### GetExpectedPageUrlPolicy

`func (o *BrowserActionInput) GetExpectedPageUrlPolicy() string`

GetExpectedPageUrlPolicy returns the ExpectedPageUrlPolicy field if non-nil, zero value otherwise.

### GetExpectedPageUrlPolicyOk

`func (o *BrowserActionInput) GetExpectedPageUrlPolicyOk() (*string, bool)`

GetExpectedPageUrlPolicyOk returns a tuple with the ExpectedPageUrlPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedPageUrlPolicy

`func (o *BrowserActionInput) SetExpectedPageUrlPolicy(v string)`

SetExpectedPageUrlPolicy sets ExpectedPageUrlPolicy field to given value.

### HasExpectedPageUrlPolicy

`func (o *BrowserActionInput) HasExpectedPageUrlPolicy() bool`

HasExpectedPageUrlPolicy returns a boolean if a field has been set.

### GetExpectedPageTitle

`func (o *BrowserActionInput) GetExpectedPageTitle() string`

GetExpectedPageTitle returns the ExpectedPageTitle field if non-nil, zero value otherwise.

### GetExpectedPageTitleOk

`func (o *BrowserActionInput) GetExpectedPageTitleOk() (*string, bool)`

GetExpectedPageTitleOk returns a tuple with the ExpectedPageTitle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedPageTitle

`func (o *BrowserActionInput) SetExpectedPageTitle(v string)`

SetExpectedPageTitle sets ExpectedPageTitle field to given value.

### HasExpectedPageTitle

`func (o *BrowserActionInput) HasExpectedPageTitle() bool`

HasExpectedPageTitle returns a boolean if a field has been set.

### GetExpectedPageTitlePolicy

`func (o *BrowserActionInput) GetExpectedPageTitlePolicy() string`

GetExpectedPageTitlePolicy returns the ExpectedPageTitlePolicy field if non-nil, zero value otherwise.

### GetExpectedPageTitlePolicyOk

`func (o *BrowserActionInput) GetExpectedPageTitlePolicyOk() (*string, bool)`

GetExpectedPageTitlePolicyOk returns a tuple with the ExpectedPageTitlePolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedPageTitlePolicy

`func (o *BrowserActionInput) SetExpectedPageTitlePolicy(v string)`

SetExpectedPageTitlePolicy sets ExpectedPageTitlePolicy field to given value.

### HasExpectedPageTitlePolicy

`func (o *BrowserActionInput) HasExpectedPageTitlePolicy() bool`

HasExpectedPageTitlePolicy returns a boolean if a field has been set.

### GetExpectedNetworkPolicy

`func (o *BrowserActionInput) GetExpectedNetworkPolicy() string`

GetExpectedNetworkPolicy returns the ExpectedNetworkPolicy field if non-nil, zero value otherwise.

### GetExpectedNetworkPolicyOk

`func (o *BrowserActionInput) GetExpectedNetworkPolicyOk() (*string, bool)`

GetExpectedNetworkPolicyOk returns a tuple with the ExpectedNetworkPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedNetworkPolicy

`func (o *BrowserActionInput) SetExpectedNetworkPolicy(v string)`

SetExpectedNetworkPolicy sets ExpectedNetworkPolicy field to given value.

### HasExpectedNetworkPolicy

`func (o *BrowserActionInput) HasExpectedNetworkPolicy() bool`

HasExpectedNetworkPolicy returns a boolean if a field has been set.

### GetExpectedNetworkCalls

`func (o *BrowserActionInput) GetExpectedNetworkCalls() []BrowserNetworkExpectation`

GetExpectedNetworkCalls returns the ExpectedNetworkCalls field if non-nil, zero value otherwise.

### GetExpectedNetworkCallsOk

`func (o *BrowserActionInput) GetExpectedNetworkCallsOk() (*[]BrowserNetworkExpectation, bool)`

GetExpectedNetworkCallsOk returns a tuple with the ExpectedNetworkCalls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedNetworkCalls

`func (o *BrowserActionInput) SetExpectedNetworkCalls(v []BrowserNetworkExpectation)`

SetExpectedNetworkCalls sets ExpectedNetworkCalls field to given value.

### HasExpectedNetworkCalls

`func (o *BrowserActionInput) HasExpectedNetworkCalls() bool`

HasExpectedNetworkCalls returns a boolean if a field has been set.

### GetVisualAssertion

`func (o *BrowserActionInput) GetVisualAssertion() BrowserVisualAssertionInput`

GetVisualAssertion returns the VisualAssertion field if non-nil, zero value otherwise.

### GetVisualAssertionOk

`func (o *BrowserActionInput) GetVisualAssertionOk() (*BrowserVisualAssertionInput, bool)`

GetVisualAssertionOk returns a tuple with the VisualAssertion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVisualAssertion

`func (o *BrowserActionInput) SetVisualAssertion(v BrowserVisualAssertionInput)`

SetVisualAssertion sets VisualAssertion field to given value.

### HasVisualAssertion

`func (o *BrowserActionInput) HasVisualAssertion() bool`

HasVisualAssertion returns a boolean if a field has been set.

### SetVisualAssertionNil

`func (o *BrowserActionInput) SetVisualAssertionNil(b bool)`

 SetVisualAssertionNil sets the value for VisualAssertion to be an explicit nil

### UnsetVisualAssertion
`func (o *BrowserActionInput) UnsetVisualAssertion()`

UnsetVisualAssertion ensures that no value is present for VisualAssertion, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


