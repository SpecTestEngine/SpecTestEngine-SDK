

# BrowserNetworkExpectation

Approved expectations and recorded candidates are separate. Body/path values remain typed JSON; exclusions affect network validation only.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** |  |  [optional] |
|**recordedCallId** | **Integer** |  |  [optional] |
|**recordedUrl** | **String** |  |  [optional] |
|**method** | **String** |  |  [optional] |
|**url** | **String** |  |  [optional] |
|**expectedStatusCode** | **Integer** |  |  [optional] |
|**candidateStatusCode** | **Integer** |  |  [optional] |
|**expectedContentType** | **String** |  |  [optional] |
|**candidateContentType** | **String** |  |  [optional] |
|**expectedHeaders** | **Map&lt;String, String&gt;** |  |  [optional] |
|**candidateHeaders** | **Map&lt;String, String&gt;** |  |  [optional] |
|**excludedHeaderFields** | **List&lt;String&gt;** |  |  [optional] |
|**excludeAllOtherHeaderFields** | **Boolean** |  |  [optional] |
|**body** | **Object** |  |  [optional] |
|**candidateBody** | **Object** |  |  [optional] |
|**expectedBodyPaths** | **List&lt;Map&lt;String, Object&gt;&gt;** |  |  [optional] |
|**candidateBodyPaths** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**excludedBodyFields** | **List&lt;String&gt;** |  |  [optional] |



