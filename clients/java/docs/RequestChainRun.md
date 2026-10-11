

# RequestChainRun


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**workspaceId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**requestNodeId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**flowName** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**overallTestFlowStatus** | **String** |  |  |
|**steps** | **List&lt;Map&lt;String, Object&gt;&gt;** |  |  |
|**context** | **Map&lt;String, Object&gt;** | Values explicitly captured during this run. Workflow/global input values and secret sources are not echoed here. |  |
|**startedAt** | **OffsetDateTime** |  |  |
|**finishedAt** | **OffsetDateTime** |  |  |
