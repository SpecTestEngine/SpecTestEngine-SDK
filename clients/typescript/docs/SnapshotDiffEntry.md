
# SnapshotDiffEntry


## Properties

Name | Type
------------ | -------------
`subjectType` | [SnapshotSubjectType](SnapshotSubjectType.md)
`subjectKey` | string
`subjectName` | string
`changeType` | [SnapshotDiffChangeType](SnapshotDiffChangeType.md)
`leftStatus` | string
`rightStatus` | string
`leftDefinitionHash` | string
`rightDefinitionHash` | string
`leftBehaviorHash` | string
`rightBehaviorHash` | string
`details` | string

## Example

```typescript
import type { SnapshotDiffEntry } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "subjectType": null,
  "subjectKey": null,
  "subjectName": null,
  "changeType": null,
  "leftStatus": null,
  "rightStatus": null,
  "leftDefinitionHash": null,
  "rightDefinitionHash": null,
  "leftBehaviorHash": null,
  "rightBehaviorHash": null,
  "details": null,
} satisfies SnapshotDiffEntry

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SnapshotDiffEntry
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


