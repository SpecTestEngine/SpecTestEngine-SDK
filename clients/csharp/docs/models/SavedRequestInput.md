# SpecTestEngine.Sdk.Model.SavedRequestInput
HTTP-shaped fields are required for REST/SOAP/GraphQL; streamingSpec is required for STREAMING.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SpecType** | **string** |  |
**Method** | **string** |  | [optional]
**Url** | **string** |  | [optional]
**StreamingSpec** | [**StreamingDefinition**](StreamingDefinition.md) |  | [optional]
**Headers** | **Dictionary&lt;string, string&gt;** |  | [optional]
**QueryParams** | **Dictionary&lt;string, string&gt;** |  | [optional]
**Body** | **string** |  | [optional]
**Auth** | **Dictionary&lt;string, Object&gt;** |  | [optional]
**RequestAuth** | **Dictionary&lt;string, Object&gt;** |  | [optional]
**RequestAttachments** | [**List&lt;DocumentAssetReference&gt;**](DocumentAssetReference.md) |  | [optional]
**Prerequisites** | **List&lt;Dictionary&lt;string, Object&gt;&gt;** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
