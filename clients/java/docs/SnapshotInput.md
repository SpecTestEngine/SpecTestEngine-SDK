

# SnapshotInput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**sprint** | **String** |  |  |
|**sourceBatchId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**parentSnapshotId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  [optional] |
|**selectionPolicy** | **SnapshotSelectionPolicy** |  |  [optional] |
|**batchItemIds** | **List&lt;UUID&gt;** |  |  [optional] |
|**environment** | **String** |  |  |
|**branchName** | **String** |  |  [optional] |
|**backendCommit** | **String** |  |  [optional] |
|**frontendCommit** | **String** |  |  [optional] |
|**createdBy** | **String** |  |  [optional] |
