# SpecTestEngine.Sdk.Model.BrowserPathExpectation
Exactly one of value or pattern is required. Values retain JSON types, including explicit null. Pattern is a whole-string glob with at most 32 stars; only a star or backslash can be escaped. Runtime templates are not accepted in patterns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Path** | **string** |  |
**Value** | **Object** | Exact JSON value, including null. Absence selects pattern matching instead. | [optional]
**Pattern** | **string** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
