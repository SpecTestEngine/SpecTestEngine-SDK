

# FragmentCatalogType


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **FragmentType** |  |  |
|**allowedFields** | **List&lt;String&gt;** |  |  |
|**singleton** | **Boolean** |  |  |
|**editorMode** | [**EditorModeEnum**](#EditorModeEnum) |  |  |
|**compatibleStreamingTransports** | **Set&lt;StreamingTransport&gt;** |  |  [optional] |
|**starterTemplate** | **Map&lt;String, Object&gt;** |  |  |



## Enum: EditorModeEnum

| Name | Value |
|---- | -----|
| REQUEST | &quot;request&quot; |
| HEADERS | &quot;headers&quot; |
| JSON | &quot;json&quot; |
| ATTACHMENTS | &quot;attachments&quot; |
| ASSERTIONS | &quot;assertions&quot; |
| SOAP | &quot;soap&quot; |
| GRAPHQL | &quot;graphql&quot; |
| STREAM_REQUEST | &quot;stream-request&quot; |
| PROTOBUF | &quot;protobuf&quot; |
| STREAM_EVENT | &quot;stream-event&quot; |
| STREAM_CONTROL | &quot;stream-control&quot; |
| STREAM_ASSERTIONS | &quot;stream-assertions&quot; |



