

# SavedRequestInput

HTTP-shaped fields are required for REST/SOAP/GraphQL; streamingSpec is required for STREAMING.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**specType** | [**SpecTypeEnum**](#SpecTypeEnum) |  |  |
|**method** | [**MethodEnum**](#MethodEnum) |  |  [optional] |
|**url** | **String** |  |  [optional] |
|**streamingSpec** | [**StreamingDefinition**](StreamingDefinition.md) |  |  [optional] |
|**headers** | **Map&lt;String, String&gt;** |  |  [optional] |
|**queryParams** | **Map&lt;String, String&gt;** |  |  [optional] |
|**body** | **String** |  |  [optional] |
|**auth** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**requestAuth** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**requestAttachments** | [**List&lt;DocumentAssetReference&gt;**](DocumentAssetReference.md) |  |  [optional] |
|**prerequisites** | **List&lt;Map&lt;String, Object&gt;&gt;** |  |  [optional] |



## Enum: SpecTypeEnum

| Name | Value |
|---- | -----|
| REST | &quot;REST&quot; |
| SOAP | &quot;SOAP&quot; |
| GRAPHQL | &quot;GRAPHQL&quot; |
| STREAMING | &quot;STREAMING&quot; |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PUT | &quot;PUT&quot; |
| PATCH | &quot;PATCH&quot; |
| DELETE | &quot;DELETE&quot; |
| HEAD | &quot;HEAD&quot; |
| OPTIONS | &quot;OPTIONS&quot; |



