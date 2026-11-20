# SpecTestEngine.Sdk.Model.BrowserAuthTransfer
Metadata only. Initial sources are Action-bound; renewal sources are run-bound and require an exact current-run private input. No token values or public initial-variable seeds are accepted. Resolve Recorder ambiguity before saving.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Sources** | [**List&lt;BrowserAuthSource&gt;**](BrowserAuthSource.md) |  | [optional]
**AuthorizationVariable** | **string** |  | [optional]
**Candidates** | **List&lt;Object&gt;** |  | [optional]
**OptionalRefresh** | **bool** |  | [optional] [default to false]
**ChoiceId** | **string** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
