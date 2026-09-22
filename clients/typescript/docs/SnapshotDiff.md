
# SnapshotDiff


## Properties

Name | Type
------------ | -------------
`leftSnapshotId` | string
`rightSnapshotId` | string
`batchId` | string
`entries` | [Array&lt;SnapshotDiffEntry&gt;](SnapshotDiffEntry.md)
`generatedAt` | Date

## Example

```typescript
import type { SnapshotDiff } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "leftSnapshotId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "rightSnapshotId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "batchId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "entries": null,
  "generatedAt": null,
} satisfies SnapshotDiff

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SnapshotDiff
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


