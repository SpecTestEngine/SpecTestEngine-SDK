
# RunBatch


## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`environment` | string
`sprint` | string
`backendCommit` | string
`frontendCommit` | string
`branchName` | string
`triggeredBy` | string
`triggerType` | string
`notes` | string
`specRunIds` | Array&lt;string&gt;
`uiMacroRunIds` | Array&lt;string&gt;
`flowRunIds` | Array&lt;string&gt;
`batchId` | string
`items` | [Array&lt;RunBatchItem&gt;](RunBatchItem.md)
`createdAt` | Date
`finishedAt` | Date

## Example

```typescript
import type { RunBatch } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "name": release-candidate-smoke,
  "description": API, browser, and flow evidence collected before release.,
  "environment": staging,
  "sprint": 2026.09,
  "backendCommit": null,
  "frontendCommit": null,
  "branchName": null,
  "triggeredBy": null,
  "triggerType": manual,
  "notes": null,
  "specRunIds": null,
  "uiMacroRunIds": null,
  "flowRunIds": null,
  "batchId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "items": null,
  "createdAt": null,
  "finishedAt": null,
} satisfies RunBatch

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RunBatch
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
