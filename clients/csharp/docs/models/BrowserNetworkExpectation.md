# SpecTestEngine.Sdk.Model.BrowserNetworkExpectation
Approved expectations and recorded candidates are separate. Body/path values remain typed JSON; exclusions affect network validation only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | **bool** |  | [optional]
**RecordedCallId** | **int** |  | [optional]
**RecordedUrl** | **string** |  | [optional]
**Method** | **string** |  | [optional]
**Url** | **string** |  | [optional]
**ExpectedStatusCode** | **int** |  | [optional]
**CandidateStatusCode** | **int** |  | [optional]
**ExpectedContentType** | **string** |  | [optional]
**CandidateContentType** | **string** |  | [optional]
**ExpectedHeaders** | **Dictionary&lt;string, string&gt;** |  | [optional]
**CandidateHeaders** | **Dictionary&lt;string, string&gt;** |  | [optional]
**ExcludedHeaderFields** | **List&lt;string&gt;** |  | [optional]
**ExcludeAllOtherHeaderFields** | **bool** |  | [optional]
**Body** | **Object** |  | [optional]
**CandidateBody** | **Object** |  | [optional]
**ExpectedBodyPaths** | **List&lt;Dictionary&lt;string, Object&gt;&gt;** |  | [optional]
**CandidateBodyPaths** | **Dictionary&lt;string, Object&gt;** |  | [optional]
**ExcludedBodyFields** | **List&lt;string&gt;** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
