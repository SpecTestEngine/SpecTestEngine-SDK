
# FlowSummary


## Properties

Name | Type
------------ | -------------
`flowId` | string
`name` | string
`description` | string
`steps` | Array&lt;{ [key: string]: any; }&gt;
`createdAt` | Date
`updatedAt` | Date
`lastRunId` | string
`previousRunId` | string
`lastRunAt` | Date
`lastRunStatus` | string

## Example

```typescript
import type { FlowSummary } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "flowId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "name": null,
  "description": null,
  "steps": null,
  "createdAt": null,
  "updatedAt": null,
  "lastRunId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "previousRunId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "lastRunAt": null,
  "lastRunStatus": null,
} satisfies FlowSummary

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowSummary
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
