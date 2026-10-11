
# SentinelCheck


## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`sourceName` | string
`environment` | string
`type` | string
`specType` | [SpecType](SpecType.md)
`format` | [ContentFormat](ContentFormat.md)
`definition` | string
`active` | boolean
`timeoutMs` | number
`failureStrategy` | string
`maxRetries` | number
`retryDelayMinMs` | number
`retryDelayMaxMs` | number
`circuitBreakerFailureThreshold` | number
`cooldownMs` | number
`id` | string
`definitionHash` | string
`consecutiveFailures` | number
`pausedUntil` | Date
`lastRunAt` | Date
`lastRunStatus` | [RunStatus](RunStatus.md)
`createdAt` | Date
`updatedAt` | Date

## Example

```typescript
import type { SentinelCheck } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "sourceName": null,
  "environment": null,
  "type": null,
  "specType": null,
  "format": null,
  "definition": null,
  "active": null,
  "timeoutMs": null,
  "failureStrategy": null,
  "maxRetries": null,
  "retryDelayMinMs": null,
  "retryDelayMaxMs": null,
  "circuitBreakerFailureThreshold": null,
  "cooldownMs": null,
  "id": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "definitionHash": null,
  "consecutiveFailures": null,
  "pausedUntil": null,
  "lastRunAt": null,
  "lastRunStatus": null,
  "createdAt": null,
  "updatedAt": null,
} satisfies SentinelCheck

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SentinelCheck
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
