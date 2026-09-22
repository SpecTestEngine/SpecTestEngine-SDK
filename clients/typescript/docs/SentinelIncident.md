
# SentinelIncident


## Properties

Name | Type
------------ | -------------
`id` | string
`environment` | string
`checkId` | string
`checkName` | string
`fingerprint` | string
`status` | string
`consecutiveFailures` | number
`lastRunId` | string
`summary` | string
`startedAt` | Date
`resolvedAt` | Date

## Example

```typescript
import type { SentinelIncident } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "environment": null,
  "checkId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "checkName": null,
  "fingerprint": null,
  "status": null,
  "consecutiveFailures": null,
  "lastRunId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "summary": null,
  "startedAt": null,
  "resolvedAt": null,
} satisfies SentinelIncident

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SentinelIncident
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


