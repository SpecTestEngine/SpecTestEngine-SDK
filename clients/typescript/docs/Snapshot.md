
# Snapshot


## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`sprint` | string
`sourceBatchId` | string
`parentSnapshotId` | string
`selectionPolicy` | [SnapshotSelectionPolicy](SnapshotSelectionPolicy.md)
`batchItemIds` | Array&lt;string&gt;
`environment` | string
`branchName` | string
`backendCommit` | string
`frontendCommit` | string
`createdBy` | string
`snapshotId` | string
`status` | [SnapshotStatus](SnapshotStatus.md)
`flows` | [Array&lt;SnapshotItem&gt;](SnapshotItem.md)
`createdAt` | Date
`approvedAt` | Date

## Example

```typescript
import type { Snapshot } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "name": staging-release-baseline,
  "description": null,
  "sprint": 2026.07,
  "sourceBatchId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "parentSnapshotId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "selectionPolicy": null,
  "batchItemIds": null,
  "environment": null,
  "branchName": null,
  "backendCommit": null,
  "frontendCommit": null,
  "createdBy": null,
  "snapshotId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "status": null,
  "flows": null,
  "createdAt": null,
  "approvedAt": null,
} satisfies Snapshot

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Snapshot
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
