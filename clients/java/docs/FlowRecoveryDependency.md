

# FlowRecoveryDependency


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** |  |  |
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**sourceName** | **String** |  |  |
|**format** | [**FormatEnum**](#FormatEnum) |  |  |
|**definitionHash** | **String** |  |  |
|**roles** | [**List&lt;RolesEnum&gt;**](#List&lt;RolesEnum&gt;) |  |  |
|**bindingCount** | **Integer** |  |  |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| REST | &quot;REST&quot; |
| SOAP | &quot;SOAP&quot; |
| GRAPHQL | &quot;GRAPHQL&quot; |
| STREAMING | &quot;STREAMING&quot; |
| UI_MACRO | &quot;UI_MACRO&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| JSON | &quot;JSON&quot; |
| YAML | &quot;YAML&quot; |
| XML | &quot;XML&quot; |



## Enum: List&lt;RolesEnum&gt;

| Name | Value |
|---- | -----|
| EXECUTED | &quot;EXECUTED&quot; |
| PLANNED_NOT_EXECUTED | &quot;PLANNED_NOT_EXECUTED&quot; |
