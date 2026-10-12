
# FlowRecoveryOperation


## Properties

Name | Type
------------ | -------------
`operationId` | string
`state` | string
`mode` | string
`flowId` | string
`failureCode` | string
`idempotencyKey` | string
`name` | string
`description` | string
`manifestHash` | string
`copiedDependencies` | number
`totalDependencies` | number

## Example

```typescript
import type { FlowRecoveryOperation } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "operationId": null,
  "state": null,
  "mode": null,
  "flowId": null,
  "failureCode": null,
  "idempotencyKey": null,
  "name": null,
  "description": null,
  "manifestHash": null,
  "copiedDependencies": null,
  "totalDependencies": null,
} satisfies FlowRecoveryOperation

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowRecoveryOperation
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
