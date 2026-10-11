
# RequestChainRun


## Properties

Name | Type
------------ | -------------
`workspaceId` | string
`requestNodeId` | string
`flowName` | string
`description` | string
`overallTestFlowStatus` | string
`steps` | Array&lt;{ [key: string]: any; }&gt;
`context` | { [key: string]: any; }
`startedAt` | Date
`finishedAt` | Date

## Example

```typescript
import type { RequestChainRun } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "workspaceId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "requestNodeId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "flowName": null,
  "description": null,
  "overallTestFlowStatus": null,
  "steps": null,
  "context": null,
  "startedAt": null,
  "finishedAt": null,
} satisfies RequestChainRun

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RequestChainRun
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
