
# SpecificationRunSummary


## Properties

Name | Type
------------ | -------------
`runId` | string
`specId` | string
`specName` | string
`specStableKey` | string
`specType` | [SpecType](SpecType.md)
`overallTestStatus` | string
`startedAt` | Date
`finishedAt` | Date

## Example

```typescript
import type { SpecificationRunSummary } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "runId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "specId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "specName": null,
  "specStableKey": null,
  "specType": null,
  "overallTestStatus": null,
  "startedAt": null,
  "finishedAt": null,
} satisfies SpecificationRunSummary

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SpecificationRunSummary
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
