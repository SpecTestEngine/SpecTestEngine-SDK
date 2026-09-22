
# SnapshotItem


## Properties

Name | Type
------------ | -------------
`snapshotFlowId` | string
`sourceBatchItemId` | string
`subjectType` | [SnapshotSubjectType](SnapshotSubjectType.md)
`subjectId` | string
`subjectKey` | string
`subjectName` | string
`sourceRunType` | [SnapshotSourceRunType](SnapshotSourceRunType.md)
`sourceRunId` | string
`status` | string
`definitionHash` | string
`behaviorHash` | string
`definitionPayload` | any
`behaviorPayload` | any
`createdAt` | Date

## Example

```typescript
import type { SnapshotItem } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "snapshotFlowId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "sourceBatchItemId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "subjectType": null,
  "subjectId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "subjectKey": null,
  "subjectName": null,
  "sourceRunType": null,
  "sourceRunId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "status": null,
  "definitionHash": null,
  "behaviorHash": null,
  "definitionPayload": null,
  "behaviorPayload": null,
  "createdAt": null,
} satisfies SnapshotItem

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SnapshotItem
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


