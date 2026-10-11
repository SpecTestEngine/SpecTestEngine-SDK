
# SentinelRun


## Properties

Name | Type
------------ | -------------
`id` | string
`executionId` | string
`environment` | string
`checkId` | string
`checkName` | string
`checkType` | string
`definitionHash` | string
`behaviorHash` | string
`region` | string
`triggerType` | string
`status` | [RunStatus](RunStatus.md)
`errorType` | string
`finalStatusCode` | number
`latencyMs` | number
`responseSizeBytes` | number
`errorMessage` | string
`resultLog` | string
`queuedAt` | Date
`startedAt` | Date
`finishedAt` | Date
`attempts` | Array&lt;{ [key: string]: any; }&gt;
`baseline` | [SentinelRunBaseline](SentinelRunBaseline.md)

## Example

```typescript
import type { SentinelRun } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "executionId": null,
  "environment": null,
  "checkId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "checkName": null,
  "checkType": null,
  "definitionHash": null,
  "behaviorHash": null,
  "region": null,
  "triggerType": null,
  "status": null,
  "errorType": null,
  "finalStatusCode": null,
  "latencyMs": null,
  "responseSizeBytes": null,
  "errorMessage": null,
  "resultLog": null,
  "queuedAt": null,
  "startedAt": null,
  "finishedAt": null,
  "attempts": null,
  "baseline": null,
} satisfies SentinelRun

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SentinelRun
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
