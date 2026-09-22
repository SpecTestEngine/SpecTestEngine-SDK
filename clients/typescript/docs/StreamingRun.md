
# StreamingRun


## Properties

Name | Type
------------ | -------------
`id` | string
`specId` | string
`specName` | string
`specStableKey` | string
`specType` | string
`format` | string
`transport` | [StreamingTransport](StreamingTransport.md)
`definitionHash` | string
`state` | [StreamingRunState](StreamingRunState.md)
`outcome` | [StreamingRunOutcome](StreamingRunOutcome.md)
`terminationReason` | string
`eventCount` | number
`byteCount` | number
`assertionPassCount` | number
`assertionFailCount` | number
`evidenceSummary` | { [key: string]: any; }
`errorMessage` | string
`createdAt` | Date
`startedAt` | Date
`finishedAt` | Date

## Example

```typescript
import type { StreamingRun } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "specId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "specName": null,
  "specStableKey": null,
  "specType": null,
  "format": null,
  "transport": null,
  "definitionHash": null,
  "state": null,
  "outcome": null,
  "terminationReason": null,
  "eventCount": null,
  "byteCount": null,
  "assertionPassCount": null,
  "assertionFailCount": null,
  "evidenceSummary": null,
  "errorMessage": null,
  "createdAt": null,
  "startedAt": null,
  "finishedAt": null,
} satisfies StreamingRun

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StreamingRun
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


