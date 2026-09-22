# SpecTestEngine.Sdk.Model.DocumentVisualAssertion
Persistent masked-render assertion. Protocol engines contact Browser Engine only when excludedRegions is non-empty and the local attachment hash or fingerprint failed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**VarVersion** | **int** |  |
**Algorithm** | **string** |  |
**RenderProfile** | **string** |  |
**Pages** | [**List&lt;DocumentVisualAssertionPage&gt;**](DocumentVisualAssertionPage.md) |  |
**ExcludedRegions** | [**List&lt;DocumentVisualExcludedRegion&gt;**](DocumentVisualExcludedRegion.md) |  |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

