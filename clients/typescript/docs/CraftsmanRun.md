
# CraftsmanRun


## Properties

Name | Type
------------ | -------------
`runId` | string
`workspaceId` | string
`nodeId` | string
`state` | [CraftsmanRunState](CraftsmanRunState.md)
`result` | [RequestChainRun](RequestChainRun.md)
`transcript` | any
`errorMessage` | string
`createdAt` | Date
`startedAt` | Date
`finishedAt` | Date

## Example

```typescript
import type { CraftsmanRun } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "runId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "workspaceId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "nodeId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "state": null,
  "result": null,
  "transcript": null,
  "errorMessage": null,
  "createdAt": null,
  "startedAt": null,
  "finishedAt": null,
} satisfies CraftsmanRun

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CraftsmanRun
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


