

# ArtifactSpecRef


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**specType** | [**SpecTypeEnum**](#SpecTypeEnum) | Selects the owning engine used to resolve this specification. Streaming specifications are not currently representable by the HTTP ATF runtime and must fail through the compatibility policy. |  |



## Enum: SpecTypeEnum

| Name | Value |
|---- | -----|
| REST | &quot;REST&quot; |
| SOAP | &quot;SOAP&quot; |
| GRAPHQL | &quot;GRAPHQL&quot; |
