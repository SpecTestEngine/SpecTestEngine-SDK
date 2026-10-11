
# FlowRun


## Properties

Name | Type
------------ | -------------
`runId` | string
`flowId` | string
`flowName` | string
`description` | string
`overallTestFlowStatus` | string
`steps` | [Array&lt;FlowRunStep&gt;](FlowRunStep.md)
`startedAt` | Date
`finishedAt` | Date

## Example

```typescript
import type { FlowRun } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "runId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "flowId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "flowName": null,
  "description": null,
  "overallTestFlowStatus": null,
  "steps": null,
  "startedAt": null,
  "finishedAt": null,
} satisfies FlowRun

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowRun
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
